#!/usr/bin/env python3
"""
build.py — Compile skills/*.md → dist/*.skill (claude.ai format)

Usage:
    python build.py              # compile tous les skills
    python build.py critique     # compile un skill spécifique
"""

import sys
import zipfile
from pathlib import Path

SKILLS_DIR = Path("skills")
DIST_DIR = Path("dist")


def build_skill(skill_path: Path) -> Path:
    skill_id = skill_path.stem
    output_path = DIST_DIR / f"{skill_id}.skill"

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(skill_path, f"{skill_id}/SKILL.md")

    print(f"  ✓ {skill_id}.skill")
    return output_path


def main():
    DIST_DIR.mkdir(exist_ok=True)

    if len(sys.argv) > 1:
        # Skill spécifique
        targets = [SKILLS_DIR / f"{sys.argv[1]}.md"]
    else:
        # Tous les skills
        targets = sorted(SKILLS_DIR.glob("*.md"))

    if not targets:
        print("Aucun skill trouvé.")
        sys.exit(1)

    print(f"Building {len(targets)} skill(s) → dist/\n")
    for skill_path in targets:
        if skill_path.exists():
            build_skill(skill_path)
        else:
            print(f"  ✗ {skill_path} introuvable")

    print(f"\nDone. Fichiers dans dist/")


if __name__ == "__main__":
    main()
