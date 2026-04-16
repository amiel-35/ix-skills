#!/usr/bin/env python3
"""
migrate_from_ix_memory.py — Migrate skills from ix-memory to ix-skills canonical format.

Usage:
    python3 scripts/migrate_from_ix_memory.py                  # all confirmed skills
    python3 scripts/migrate_from_ix_memory.py contrarian       # specific skill
    python3 scripts/migrate_from_ix_memory.py --dry-run        # validate without writing
    python3 scripts/migrate_from_ix_memory.py --list           # print confirmed skills
"""

import argparse
import json
import sys
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
IX_MEMORY_SKILLS = Path("/Users/amiellavon/Sites/IX_project/ix-memory/memory/_context/skills")
IX_MEMORY_PARTIALS = IX_MEMORY_SKILLS / "_partials"
SKILLS_DIR = Path("skills")

# ---------------------------------------------------------------------------
# Metier → domain reverse mapping
# ---------------------------------------------------------------------------
METIER_TO_DOMAIN = {
    "transverse":               "cognitif",
    "achats":                   "ops",
    "commercial":               "sales",
    "intelligence_strategique": "strategy",
    "finance":                  "finance",
    "juridique":                "legal",
    "it_projet":                "ops",
    "fondateur_ceo":            "fondateur",
    "rh":                       "rh",
    "analyste_data":            "data",
}

# ---------------------------------------------------------------------------
# Partial handling strategy
# ---------------------------------------------------------------------------
INLINE_PARTIALS = {"conseil-review", "recherche-sources", "transverse_anti_biais", "transverse_debrief"}
METIER_PARTIAL_PREFIX = "metier_"
SKIP_PARTIALS = {
    "deck-vibe-calm", "deck-vibe-excited", "deck-vibe-impressed",
    "deck-vibe-inspired", "deck-viewport",
    "livraison-html-dashboard", "livraison-html", "livraison-profils",
    "critique-lentilles",
}

# ---------------------------------------------------------------------------
# Confirmed skills list
# ---------------------------------------------------------------------------
CONFIRMED_SKILLS = [
    # Lot 1 — Conseil archetype (conseil-review partial)
    "contrarian", "executor", "expansionist", "firstprinciples", "outsider",
    # Lot 2 — Strategy / decision
    "outside-in", "dixieme-homme", "chairman", "red-team", "futurs-alternatifs",
    "key-assumptions", "note-strategique", "strategie-prix",
    # Lot 3 — Research
    "research", "analyse-concurrentielle", "analyse-cdc", "business-case-draft",
    "tam-sam-som", "system-design", "tech-debt",
    # Lot 4 — Production / output
    "brief", "synthese", "data-storytelling", "financial-narrative",
    "stakeholder-comms", "negotiation-brief", "compte-rendu",
    # Lot 5 — Decision / analysis
    "offer-comparison", "vendor-scorecard", "budget-variance-analysis",
    "total-cost-analysis", "metriques-saas", "indicateurs", "okr",
    "tableau-de-bord-kpi", "compliance-checklist", "quality-check", "analysis",
    # Lot 6 — Legal / contracts
    "cgv-checker", "contract-review", "conformite-rgpd", "legal-risk-flag",
    "nda-draft", "contrat-emploi", "contrat-fournisseur",
    # Lot 7 — HR
    "fiche-poste", "entretien-professionnel", "interview-guide-recruteur",
    "interview-loop-planner", "onboarding-plan", "offboarding-structure",
    "people-review", "performance-review-helper", "plan-developpement-competences",
    "grille-remuneration", "lettre-cadrage-disciplinaire",
    # Lot 8 — Product / tech
    "prd", "feature-spec", "spec", "decomposer", "cadrage", "ticket-triage",
    "code-review", "mockup", "reformulation-us", "journey-map",
    # Lot 9 — Business / sales
    "offre-commerciale", "rfp-draft", "org-design-brief", "persona",
    "lettre-motivation", "retrospective", "revue-feedback",
]

# 'spec' is renamed to 'product-spec' on output
ID_RENAMES = {"spec": "product-spec"}


def inline_partial(partial_name: str) -> str:
    partial_file = IX_MEMORY_PARTIALS / f"{partial_name}.md"
    if not partial_file.exists():
        return f"<!-- PARTIAL NOT FOUND: {partial_name} -->"
    return partial_file.read_text().strip()


def process_partials(body: str, uses_partials: list) -> str:
    sections = [body.strip()]
    for partial in uses_partials:
        if partial in SKIP_PARTIALS:
            continue
        elif partial in INLINE_PARTIALS:
            content = inline_partial(partial)
            sections.append(f"\n\n<!-- inlined from partial: {partial} -->\n\n{content}")
        elif partial.startswith(METIER_PARTIAL_PREFIX):
            metier = partial[len(METIER_PARTIAL_PREFIX):]
            sections.append(
                f"\n\n> Domain calibration: {metier}. Adapt lens and output format accordingly."
            )
        else:
            sections.append(f"\n\n<!-- TODO: partial not handled: {partial} -->")
    return "".join(sections)


def build_skill_md(frontmatter: dict, body: str) -> str:
    yaml_str = yaml.dump(
        frontmatter, allow_unicode=True, default_flow_style=False, sort_keys=False
    )
    return f"---\n{yaml_str}---\n\n<!-- TODO: translate body to English -->\n\n{body}\n"


def metier_to_domain(metier_list: list) -> str:
    for m in metier_list:
        if m in METIER_TO_DOMAIN:
            return METIER_TO_DOMAIN[m]
    return "cognitif"


def build_frontmatter(manifest: dict) -> dict:
    metier = manifest.get("metier", [])

    # Normalize output_type vs output_types
    if "output_types" in manifest:
        output_types = manifest["output_types"]
    elif "output_type" in manifest:
        output_types = [manifest["output_type"]]
    else:
        output_types = []

    fm = {
        "id": manifest["id"],
        "label": manifest["label"],
        "version": manifest.get("version", "1.0.0"),
        "description_fr": manifest.get("description_fr", manifest.get("description", "")),
        "description_en": manifest.get("description_en", ""),
        "icon": manifest.get("icon", "○"),
        "domain": metier_to_domain(metier),
        "category": manifest.get("category", "atome"),
        "input_types": manifest.get("input_types", []),
        "output_types": output_types,
        "compatible": ["claude-ai", "claude-code", "cowork", "gpt", "gemini", "mystaffy"],
    }
    if manifest.get("aliases"):
        fm["aliases"] = manifest["aliases"]
    return fm


def build_mystaffy_json(manifest: dict) -> dict:
    data: dict = {}

    # Preserve round-trip fields
    if manifest.get("metier"):
        data["metier"] = manifest["metier"]
    if manifest.get("uses_partials"):
        data["uses_partials"] = manifest["uses_partials"]

    data["category"] = manifest.get("category", "atome")
    data["params"] = manifest.get("params", {})
    data["ui"] = manifest.get("ui", {"simple_fields": [], "advanced_fields": []})

    # Preserve mystaffy platform fields
    for field in ["execution", "color", "kind", "launch_mode", "transport", "output_format",
                  "enabled", "visibility"]:
        if field in manifest:
            data[field] = manifest[field]

    return data
