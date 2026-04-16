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
