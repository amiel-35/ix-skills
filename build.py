#!/usr/bin/env python3
"""
build.py — Multi-target skill builder for ix-skills.

Usage:
    python build.py                              # all targets, all skills
    python build.py <id>                         # specific skill id, all targets
    python build.py --target claude-ai           # all skills, claude-ai only
    python build.py --target cowork              # cowork validation only
    python build.py --target mystaffy            # all skills, mystaffy only
    python build.py --target mystaffy --domain cognitif  # filter by domain
    python build.py <id> --target mystaffy       # specific skill, mystaffy only
    python build.py --validate                   # validate without writing files
"""

import argparse
import json
import sys
import zipfile
from pathlib import Path

import yaml
import jsonschema

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SKILLS_DIR = Path("skills")
DIST_DIR = Path("dist")
MYSTAFFY_DIST_DIR = Path("mystaffy-dist")
PLUGIN_JSON = Path(".claude-plugin/plugin.json")

# ---------------------------------------------------------------------------
# Domain → métier mapping
# ---------------------------------------------------------------------------
DOMAIN_TO_METIER = {
    "cognitif":  ["transverse"],
    "rh":        ["rh"],
    "sales":     ["commercial"],
    "finance":   ["finance"],
    "legal":     ["juridique"],
    "ops":       ["transverse"],
    "data":      ["analyste_data"],
    "strategy":  ["intelligence_strategique"],
    "fondateur": ["fondateur_ceo"],
}

# ---------------------------------------------------------------------------
# Mystaffy JSON Schema
# ---------------------------------------------------------------------------
MYSTAFFY_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "IX Skill Manifest",
    "type": "object",
    "additionalProperties": False,
    "required": ["id", "label", "version", "description", "kind", "category",
                 "input_types", "output_format", "params", "ui"],
    "properties": {
        "artifact_kind": {"type": "string", "enum": ["skill", "workflow"]},
        "id": {"type": "string", "pattern": "^[a-z0-9_\\-]+$"},
        "label": {"type": "string", "minLength": 1},
        "aliases": {"type": "array", "items": {"type": "string"}, "uniqueItems": True},
        "version": {"type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$"},
        "description": {"type": "string", "minLength": 1},
        "icon": {"type": "string"},
        "color": {"type": "string"},
        "enabled": {"type": "boolean"},
        "visibility": {"type": "string", "enum": ["public", "internal"]},
        "metier": {
            "type": "array",
            "items": {"type": "string", "enum": [
                "transverse", "achats", "commercial", "intelligence_strategique",
                "finance", "juridique", "it_projet", "fondateur_ceo", "rh", "analyste_data"
            ]}
        },
        "kind": {"type": "string", "enum": ["local", "llm", "hybrid"]},
        "category": {"type": "string", "enum": [
            "atome", "research", "critique", "decision", "production",
            "import", "pipeline", "internal", "workflow"
        ]},
        "input_types": {"type": "array", "items": {"type": "string"}, "minItems": 1, "uniqueItems": True},
        "output_type": {"type": "string"},
        "output_types": {"type": "array", "items": {"type": "string"}, "minItems": 1, "uniqueItems": True},
        "output_format": {"type": "string", "enum": ["markdown", "json", "html", "pdf", "docx", "pptx", "mixed"]},
        "output_format_dynamic": {
            "type": "object",
            "required": ["param", "map"],
            "properties": {
                "param": {"type": "string"},
                "map": {"type": "object"}
            }
        },
        "params": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "required": ["label", "type", "required"],
                "properties": {
                    "label": {"type": "string"},
                    "type": {"type": "string", "enum": ["string", "text", "boolean", "number", "enum", "multiselect", "file"]},
                    "required": {"type": "boolean"},
                    "default": {},
                    "help": {"type": "string"},
                    "values": {"type": "array", "items": {"type": "string"}, "uniqueItems": True},
                    "placeholder": {"type": "string"},
                    "min": {"type": "number"},
                    "max": {"type": "number"}
                }
            }
        },
        "ui": {
            "type": "object",
            "required": ["simple_fields", "advanced_fields"],
            "properties": {
                "simple_fields": {"type": "array", "items": {"type": "string"}, "uniqueItems": True},
                "advanced_fields": {"type": "array", "items": {"type": "string"}, "uniqueItems": True}
            }
        },
        "execution": {
            "type": "object",
            "properties": {
                "supports_async": {"type": "boolean"},
                "supports_review_gate": {"type": "boolean"},
                "max_input_artifacts": {"type": "integer"},
                "max_estimated_tokens": {"type": "integer"}
            }
        },
        "launch_mode": {"type": "string", "enum": ["run", "direct_api"]},
        "transport": {"type": "string", "enum": ["json", "multipart"]},
        "endpoint": {"type": "string", "pattern": "^/"},
        "uses_partials": {"type": "array", "items": {"type": "string"}, "uniqueItems": True},
        "tools": {"type": "array", "items": {"type": "string"}, "uniqueItems": True}
    },
    "allOf": [
        {
            "oneOf": [
                {"required": ["output_type"], "not": {"required": ["output_types"]}},
                {"required": ["output_types"], "not": {"required": ["output_type"]}}
            ]
        },
        {
            "if": {"properties": {"launch_mode": {"const": "direct_api"}}, "required": ["launch_mode"]},
            "then": {"required": ["endpoint"]}
        }
    ]
}

# ---------------------------------------------------------------------------
# Skill parsing
# ---------------------------------------------------------------------------

def parse_skill(path: Path):
    """Parse a skill .md file, returning (frontmatter_dict, body_str).
    Raises ValueError on parse errors.
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"No YAML frontmatter found in {path}")
    # Find closing ---
    end = text.find("\n---\n", 3)
    if end == -1:
        raise ValueError(f"Unclosed frontmatter in {path}")
    fm_text = text[3:end]
    body = text[end + 5:]  # skip \n---\n
    body = body.lstrip("\n")
    fm = yaml.safe_load(fm_text)
    if not isinstance(fm, dict):
        raise ValueError(f"Frontmatter is not a mapping in {path}")
    return fm, body


def load_skills(skill_id=None, domain=None):
    """Return list of (path, frontmatter, body) for selected skills.
    Returns (skills_list, errors_count).
    """
    if skill_id:
        paths = [SKILLS_DIR / f"{skill_id}.md"]
    else:
        paths = sorted(p for p in SKILLS_DIR.glob("*.md") if p.name != "README.md")

    skills = []
    errors = 0
    for path in paths:
        if not path.exists():
            print(f"  Error: skill '{path.stem}' not found at {path}")
            errors += 1
            continue
        if path.name == "README.md":
            continue
        try:
            fm, body = parse_skill(path)
        except Exception as e:
            print(f"  Error parsing {path}: {e}")
            errors += 1
            continue
        if domain and fm.get("domain") != domain:
            continue
        skills.append((path, fm, body))
    return skills, errors


# ---------------------------------------------------------------------------
# Target: claude-ai
# ---------------------------------------------------------------------------

def build_claude_ai(skills, dry_run=False):
    print(f"\nTarget: claude-ai ({len(skills)} skill(s))")
    errors = 0
    for path, fm, body in skills:
        skill_id = fm["id"]
        out_path = DIST_DIR / f"{skill_id}.skill"
        try:
            if not dry_run:
                DIST_DIR.mkdir(exist_ok=True)
                with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
                    zf.write(path, f"{skill_id}/SKILL.md")
            dry_tag = " [dry-run]" if dry_run else ""
            print(f"  \u2713 claude-ai  {skill_id:<12} \u2192 dist/{skill_id}.skill{dry_tag}")
        except Exception as e:
            print(f"  \u2717 claude-ai  {skill_id:<12} \u2192 {e}")
            errors += 1
    return errors


# ---------------------------------------------------------------------------
# Target: cowork
# ---------------------------------------------------------------------------

def build_cowork(dry_run=False):
    print("\nTarget: cowork")
    errors = 0
    dry_tag = " [dry-run]" if dry_run else ""
    if not PLUGIN_JSON.exists():
        print(f"  \u2717 cowork: {PLUGIN_JSON} not found{dry_tag}")
        return 1
    try:
        data = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"  \u2717 cowork: {PLUGIN_JSON} invalid JSON — {e}{dry_tag}")
        return 1
    missing = [f for f in ("name", "version") if f not in data]
    has_skills = "skills" in data or (
        isinstance(data.get("components"), dict) and "skills" in data["components"]
    )
    if not has_skills:
        missing.append("components.skills")
    if missing:
        print(f"  \u2717 cowork: {PLUGIN_JSON} missing fields: {', '.join(missing)}{dry_tag}")
        errors += 1
    else:
        print(f"  \u2713 cowork: {PLUGIN_JSON} valid{dry_tag}")
    return errors


# ---------------------------------------------------------------------------
# Target: mystaffy
# ---------------------------------------------------------------------------

def build_mystaffy_manifest(fm):
    """Build a mystaffy manifest dict from frontmatter (steps 1–3)."""
    manifest = {
        "enabled": True,
        "visibility": "public",
        "launch_mode": "run",
        "transport": "json",
        "kind": "llm",
        "output_format": "markdown",
        "params": {},
        "ui": {"simple_fields": [], "advanced_fields": []},
    }

    # Step 2: map from frontmatter
    manifest["id"] = fm["id"]
    manifest["label"] = fm["label"]
    manifest["version"] = fm["version"]
    manifest["description"] = fm["description_fr"]
    if "icon" in fm:
        manifest["icon"] = fm["icon"]
    manifest["metier"] = DOMAIN_TO_METIER.get(fm.get("domain", ""), ["transverse"])
    manifest["input_types"] = fm["input_types"]
    output_types = fm.get("output_types", [])
    if len(output_types) == 1:
        manifest["output_type"] = output_types[0]
    else:
        manifest["output_types"] = output_types
    if "category" in fm:
        manifest["category"] = fm["category"]

    # Step 3: override from skills/<id>.mystaffy.json if present
    override_path = SKILLS_DIR / f"{fm['id']}.mystaffy.json"
    if override_path.exists():
        override = json.loads(override_path.read_text(encoding="utf-8"))
        manifest.update(override)

    return manifest


def build_mystaffy(skills, dry_run=False):
    print(f"\nTarget: mystaffy ({len(skills)} skill(s))")
    errors = 0
    for path, fm, body in skills:
        skill_id = fm["id"]
        out_dir = MYSTAFFY_DIST_DIR / skill_id
        dry_tag = " [dry-run]" if dry_run else ""
        try:
            manifest = build_mystaffy_manifest(fm)
            # Validate
            jsonschema.validate(manifest, MYSTAFFY_SCHEMA)
            if not dry_run:
                MYSTAFFY_DIST_DIR.mkdir(exist_ok=True)
                out_dir.mkdir(exist_ok=True)
                (out_dir / "manifest.json").write_text(
                    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8"
                )
                (out_dir / "skill.md").write_text(body, encoding="utf-8")
            print(f"  \u2713 mystaffy   {skill_id:<12} \u2192 mystaffy-dist/{skill_id}/{dry_tag}")
        except jsonschema.ValidationError as e:
            print(f"  \u2717 mystaffy   {skill_id:<12} \u2192 schema error: {e.message}")
            errors += 1
        except Exception as e:
            print(f"  \u2717 mystaffy   {skill_id:<12} \u2192 {e}")
            errors += 1
    return errors


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="Multi-target skill builder for ix-skills.",
        add_help=True,
    )
    parser.add_argument(
        "skill_id",
        nargs="?",
        default=None,
        help="Specific skill id to build (optional)",
    )
    parser.add_argument(
        "--target",
        choices=["claude-ai", "cowork", "mystaffy"],
        default=None,
        help="Build target (default: all)",
    )
    parser.add_argument(
        "--domain",
        default=None,
        help="Filter skills by domain (mystaffy only)",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate without writing files (dry-run)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    dry_run = args.validate
    total_errors = 0

    targets = [args.target] if args.target else ["cowork", "claude-ai", "mystaffy"]

    # --- cowork (repo-level, not per-skill) ---
    if "cowork" in targets:
        total_errors += build_cowork(dry_run=dry_run)

    # --- skill-based targets ---
    skill_targets = [t for t in targets if t != "cowork"]
    if skill_targets:
        # If skill_id given and not found, exit 1
        if args.skill_id:
            skill_path = SKILLS_DIR / f"{args.skill_id}.md"
            if not skill_path.exists():
                print(f"Error: skill '{args.skill_id}' not found at {skill_path}")
                sys.exit(1)

        skills, parse_errors = load_skills(skill_id=args.skill_id, domain=args.domain)
        total_errors += parse_errors

        if "claude-ai" in skill_targets:
            total_errors += build_claude_ai(skills, dry_run=dry_run)

        if "mystaffy" in skill_targets:
            total_errors += build_mystaffy(skills, dry_run=dry_run)

    print()
    if total_errors > 0:
        print(f"{total_errors} error(s) found.")
        sys.exit(1)
    else:
        if dry_run:
            print("Validation passed.")
        else:
            print("Done.")


if __name__ == "__main__":
    main()
