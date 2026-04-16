import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.migrate_from_ix_memory import (
    build_frontmatter,
    build_mystaffy_json,
    metier_to_domain,
)

CONTRARIAN_MANIFEST = {
    "id": "contrarian",
    "label": "Contradicteur",
    "aliases": ["contradictor"],
    "version": "1.0.0",
    "description": "Cherche le point de defaillance.",
    "icon": "⚔️",
    "color": "#C0392B",
    "enabled": True,
    "visibility": "public",
    "kind": "llm",
    "category": "critique",
    "launch_mode": "run",
    "transport": "json",
    "input_types": ["brief", "markdown", "decision"],
    "output_type": "critique_contradictoire",
    "output_format": "markdown",
    "uses_partials": ["conseil-review"],
    "params": {
        "mode": {
            "label": "Mode",
            "type": "enum",
            "required": False,
            "default": "perspective",
            "values": ["perspective", "review"],
        }
    },
    "ui": {"simple_fields": ["mode"], "advanced_fields": []},
    "execution": {"supports_async": False, "max_estimated_tokens": 18000},
    "metier": ["intelligence_strategique"],
}

BRIEF_MANIFEST = {
    "id": "brief",
    "label": "Brief",
    "version": "1.0.2",
    "description": "Transformer un besoin flou en brief.",
    "icon": "◫",
    "kind": "llm",
    "category": "production",
    "input_types": ["brief", "markdown"],
    "output_types": ["brief", "questions_ouvertes"],
    "output_format": "markdown",
    "params": {},
    "ui": {"simple_fields": [], "advanced_fields": []},
    "metier": ["it_projet", "fondateur_ceo"],
}


def test_metier_to_domain_intelligence_strategique():
    assert metier_to_domain(["intelligence_strategique"]) == "strategy"


def test_metier_to_domain_fondateur():
    assert metier_to_domain(["it_projet", "fondateur_ceo"]) == "ops"


def test_metier_to_domain_fallback():
    assert metier_to_domain([]) == "cognitif"


def test_build_frontmatter_contrarian():
    fm = build_frontmatter(CONTRARIAN_MANIFEST)
    assert fm["id"] == "contrarian"
    assert fm["label"] == "Contradicteur"
    assert fm["version"] == "1.0.0"
    assert fm["domain"] == "strategy"
    assert fm["output_types"] == ["critique_contradictoire"]
    assert fm["compatible"] == ["claude-ai", "claude-code", "cowork", "gpt", "gemini", "mystaffy"]
    assert fm["aliases"] == ["contradictor"]


def test_build_frontmatter_output_types_list():
    fm = build_frontmatter(BRIEF_MANIFEST)
    assert fm["output_types"] == ["brief", "questions_ouvertes"]


def test_build_frontmatter_defaults():
    minimal = {"id": "x", "label": "X", "input_types": ["brief"], "output_type": "y", "metier": []}
    fm = build_frontmatter(minimal)
    assert fm["version"] == "1.0.0"
    assert fm["icon"] == "○"
    assert fm["domain"] == "cognitif"
    assert "description_fr" in fm


def test_build_mystaffy_json_preserves_partials():
    mj = build_mystaffy_json(CONTRARIAN_MANIFEST)
    assert mj["uses_partials"] == ["conseil-review"]
    assert mj["metier"] == ["intelligence_strategique"]


def test_build_mystaffy_json_preserves_execution():
    mj = build_mystaffy_json(CONTRARIAN_MANIFEST)
    assert mj["execution"]["max_estimated_tokens"] == 18000


def test_build_mystaffy_json_preserves_platform_fields():
    mj = build_mystaffy_json(CONTRARIAN_MANIFEST)
    assert mj["color"] == "#C0392B"
    assert mj["kind"] == "llm"
    assert mj["output_format"] == "markdown"


def test_build_mystaffy_json_no_uses_partials_when_absent():
    mj = build_mystaffy_json(BRIEF_MANIFEST)
    assert "uses_partials" not in mj


from scripts.migrate_from_ix_memory import process_partials, build_skill_md
import yaml


def test_process_partials_skips_deck():
    body = "# My Skill\nContent here."
    result = process_partials(body, ["deck-viewport"])
    assert "deck-viewport" not in result
    assert "Content here." in result


def test_process_partials_metier_hint():
    body = "# Skill"
    result = process_partials(body, ["metier_rh"])
    assert "Domain calibration: rh" in result


def test_process_partials_unknown_appends_todo():
    body = "# Skill"
    result = process_partials(body, ["unknown-partial"])
    assert "TODO: partial not handled: unknown-partial" in result


def test_build_skill_md_has_frontmatter_and_todo():
    fm = {"id": "test", "label": "Test", "version": "1.0.0",
          "description_fr": "desc", "description_en": "",
          "icon": "○", "domain": "cognitif", "category": "atome",
          "input_types": ["brief"], "output_types": ["result"],
          "compatible": ["claude-ai"]}
    result = build_skill_md(fm, "# Body\nContent.")
    assert result.startswith("---\n")
    assert "TODO: translate body to English" in result
    assert "# Body" in result
    # frontmatter must be valid YAML
    fm_text = result.split("---\n")[1]
    parsed = yaml.safe_load(fm_text)
    assert parsed["id"] == "test"


import tempfile
import os
from scripts.migrate_from_ix_memory import migrate_skill


def test_migrate_skill_dry_run(capsys):
    result = migrate_skill("contrarian", dry_run=True)
    assert result is True
    captured = capsys.readouterr()
    assert "dry-run" in captured.out
    assert "contrarian" in captured.out


def test_migrate_skill_writes_files(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "skills").mkdir()
    result = migrate_skill("contrarian", dry_run=False)
    assert result is True
    assert (tmp_path / "skills" / "contrarian.md").exists()
    assert (tmp_path / "skills" / "contrarian.mystaffy.json").exists()
    # frontmatter must parse
    content = (tmp_path / "skills" / "contrarian.md").read_text()
    assert content.startswith("---\n")
    assert "id: contrarian" in content
    # .mystaffy.json must be valid JSON with uses_partials
    mj = json.loads((tmp_path / "skills" / "contrarian.mystaffy.json").read_text())
    assert mj["uses_partials"] == ["conseil-review"]
    assert mj["metier"] == ["intelligence_strategique"]


import importlib.util as _ilu


def _load_build():
    spec = _ilu.spec_from_file_location("build", "build.py")
    mod = _ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_build_ixmemory_roundtrip(tmp_path, monkeypatch):
    build = _load_build()
    monkeypatch.chdir(tmp_path)
    (tmp_path / "skills").mkdir()
    (tmp_path / "mystaffy-dist").mkdir()

    # Write a canonical skill + .mystaffy.json
    skill_md = """---
id: contrarian
label: Contradicteur
version: 1.0.0
description_fr: desc fr
description_en: desc en
icon: "\u2694\ufe0f"
domain: strategy
category: critique
input_types: [brief, markdown]
output_types: [critique_contradictoire]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Contrarian
Body content.
"""
    (tmp_path / "skills" / "contrarian.md").write_text(skill_md)
    mystaffy_json = json.dumps({
        "metier": ["intelligence_strategique"],
        "uses_partials": ["conseil-review"],
        "category": "critique",
        "params": {"mode": {"label": "Mode", "type": "enum", "required": False, "values": ["perspective", "review"]}},
        "ui": {"simple_fields": ["mode"], "advanced_fields": []},
        "output_format": "markdown",
        "kind": "llm",
    })
    (tmp_path / "skills" / "contrarian.mystaffy.json").write_text(mystaffy_json)

    skills, _errors = build.load_skills(None, None)
    build.build_ix_memory(skills, dry_run=False)

    manifest_path = tmp_path / "mystaffy-dist" / "contrarian" / "manifest.json"
    assert manifest_path.exists()
    manifest = json.loads(manifest_path.read_text())
    assert manifest["id"] == "contrarian"
    assert manifest["metier"] == ["intelligence_strategique"]
    assert manifest["uses_partials"] == ["conseil-review"]
    assert "output_type" in manifest or "output_types" in manifest

    skill_md_out = tmp_path / "mystaffy-dist" / "contrarian" / "skill.md"
    assert skill_md_out.exists()
    assert "Body content." in skill_md_out.read_text()
