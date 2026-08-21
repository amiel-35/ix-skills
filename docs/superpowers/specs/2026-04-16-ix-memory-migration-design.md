# Design — Migration ix-memory → ix-skills

**Date:** 2026-04-16
**Statut:** Approuvé

---

## Objectif

Migrer ~65 skills portables depuis `/Users/amiellavon/Sites/IX_project/ix-memory/memory/_context/skills` vers ix-skills (format canonique), en conservant la capacité de re-packager vers ix-memory via `build.py --target ix-memory`.

ix-skills devient la source canonique. ix-memory ne conserve que les skills trop spécifiques à la plateforme.

---

## Approche retenue

**Option B — Script pour la structure, manuel pour la traduction du body.**

- Le script gère : mapping de champs, inline des partials, extraction `.mystaffy.json`, scaffold du body avec `<!-- TODO: translate -->`
- Le manuel gère : traduction en anglais, ajout du template de sortie bilingue

---

## Section 1 — Migration script

### Fichier

`scripts/migrate_from_ix_memory.py`

### Usage

```bash
python3 scripts/migrate_from_ix_memory.py                  # tous les skills confirmés
python3 scripts/migrate_from_ix_memory.py contrarian       # un skill spécifique
python3 scripts/migrate_from_ix_memory.py --dry-run        # valide sans écrire
```

### Ce que le script fait

1. Lit `<skill>/manifest.json` + `<skill>/skill.md` depuis ix-memory
2. Mappe les champs → frontmatter canonique ix-skills
3. Inline les partials selon la stratégie définie (voir section Partials)
4. Génère `skills/<id>.md` avec le body original en français préfixé `<!-- TODO: translate to English -->`
5. Génère `skills/<id>.mystaffy.json` depuis `params`, `ui`, `metier`, `uses_partials`

### Contrainte de round-trip

`build.py --target ix-memory` doit pouvoir reconstituer le format ix-memory depuis ix-skills. Pour cela :

- `uses_partials` est conservé dans `.mystaffy.json` (même si le body ix-skills a le contenu inliné)
- `metier[]` est conservé dans `.mystaffy.json`
- `build --target ix-memory` lit frontmatter + `.mystaffy.json` → reconstruit `manifest.json` + `skill.md`

---

## Section 2 — Field mapping

### `skills/<id>.md` frontmatter

| ix-memory `manifest.json` | ix-skills frontmatter | Règle |
|---|---|---|
| `id` | `id` | direct |
| `label` | `label` | direct |
| `version` | `version` | direct, défaut `1.0.0` si absent |
| `description_fr` | `description_fr` | direct si présent, sinon dérivé de `description` |
| `description_en` | `description_en` | direct si présent, sinon `""` + TODO |
| `icon` | `icon` | direct, défaut `○` si absent |
| `metier[]` | `domain` | reverse lookup `METIER_TO_DOMAIN` (premier élément) |
| `category` | `category` | direct |
| `input_types` | `input_types` | direct |
| `output_types` | `output_types` | direct |
| — | `compatible` | toujours `[claude-ai, claude-code, cowork, gpt, gemini, mystaffy]` |

### `METIER_TO_DOMAIN` (reverse de `DOMAIN_TO_METIER`)

| metier | domain |
|---|---|
| transverse | cognitif |
| rh | rh |
| commercial | sales |
| finance | finance |
| juridique | legal |
| analyste_data | data |
| intelligence_strategique | strategy |
| fondateur_ceo | fondateur |
| marketing | sales |
| tech | data |
| direction | fondateur |

### `skills/<id>.mystaffy.json`

```json
{
  "metier": ["..."],
  "uses_partials": ["..."],
  "category": "...",
  "params": [...],
  "ui": {
    "simple_fields": [...],
    "advanced_fields": [...]
  }
}
```

Champs absents dans le manifest source → omis (pas de valeur par défaut inventée).

---

## Section 3 — Stratégie partials

| Partial | Stratégie |
|---|---|
| `conseil-review.md` | Inline verbatim dans les skills conseil archetype |
| `recherche-sources.md` | Inline verbatim dans les skills research |
| `transverse_anti_biais.md` | Inline verbatim où référencé |
| `transverse_debrief.md` | Inline verbatim où référencé |
| `metier_*.md` | Remplacé par hint : `> Domain calibration: [metier]. Adapt lens and output format accordingly.` |
| `deck-*.md` | Skip — contenu deck-creator uniquement. Note: deck-planner comme futur skill indépendant |
| `livraison-*.md` | Déjà géré dans `deliver.md` |
| `critique-lentilles.md` | Déjà géré dans `critique.md` |

Le champ `uses_partials` est conservé dans `.mystaffy.json` pour le round-trip, même si le contenu est inliné dans le body.

---

## Section 4 — Exécution par lot

| Lot | Skills | Raison |
|---|---|---|
| 1 | Conseil archetype (contrarian, outsider, expansionist, firstprinciples, executor) | Valider inline `conseil-review` |
| 2 | Domain skills (9 skills métier RH, finance, etc.) | Valider hint `metier_*` |
| 3 | Research cluster (investigateur, veille, benchmark, etc.) | Valider inline `recherche-sources` |
| 4 | Production/output (brief, synthesizer, etc.) | |
| 5 | Decision/analysis | |
| 6 | Transverse (reste) | |

**Étapes manuelles par skill après script :**

1. Traduire le body en anglais (remplacer `<!-- TODO: translate to English -->`)
2. Ajouter le template de sortie bilingue (`## Synthèse / Summary`, etc.)
3. Valider : `python3 build.py <id> --validate`

---

## Section 5 — Modifications `build.py`

1. Ajouter `--target ix-memory` dans les `choices`
2. Créer `build_ix_memory(skills, dry_run)` :
   - Lit frontmatter + `.mystaffy.json`
   - Reconstruit `manifest.json` (champs ix-memory + `uses_partials` + `metier` depuis `.mystaffy.json`)
   - Écrit `mystaffy-dist/<id>/manifest.json` + `mystaffy-dist/<id>/skill.md`
3. Ajouter `METIER_TO_DOMAIN` comme table inverse de `DOMAIN_TO_METIER`

---

## Skills exclus (ne pas migrer)

| Skill | Raison |
|---|---|
| `init` | Infrastructure interne ix-memory, pas un skill cognitif |
| `deck-creator` | Trop dépendant des partials deck-* et du runtime mystaffy |
| `achats-indicateurs-a-prioriser` | Origine incertaine (probablement pas de l'auteur) |
| `priorisation` | On hold — réévaluer après migration principale |

---

## Contraintes

- Bodies traduits en anglais (même règle que les 7 skills existants)
- Output templates bilingues hardcodés (pas de traduction dynamique)
- `id` : minuscules, kebab-case — renommer si nécessaire
- `mystaffy-dist/` et `dist/` restent gitignorés
- Le script ne modifie jamais ix-memory — lecture seule

---

## Definition of Done

- ~65 skills dans `skills/` avec frontmatter canonique valide
- `build.py --validate` passe pour tous
- `build.py --target ix-memory` reconstruit un manifest.json valide
- CLAUDE.md mis à jour avec le target `ix-memory`
- `.claude-plugin/plugin.json` mis à jour avec tous les nouveaux skills
