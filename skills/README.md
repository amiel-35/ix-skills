# skills/

Source canonique des skills ix-skills.

Ce dossier contient un fichier Markdown par skill, plus un fichier optionnel
`<id>.mystaffy.json` pour les paramètres et l'UI mystaffy.

Le catalogue complet est documenté dans :

- [`../README.md`](../README.md) — version anglaise
- [`../README-fr.md`](../README-fr.md) — version française

---

## Règle de structure

Pour chaque skill :

```text
skills/<id>.md
skills/<id>.mystaffy.json
```

`<id>` doit être en kebab-case, sans accent, et doit correspondre exactement
au champ `id` du frontmatter.

Exemple :

```text
skills/problem-framing.md
skills/problem-framing.mystaffy.json
```

---

## Format canonique

Chaque fichier `skills/<id>.md` commence par un frontmatter YAML.

Champs requis :

```yaml
---
id: problem-framing
label: Problématiser
version: 0.2.0
description_fr: "..."
description_en: "..."
icon: ⊙
domain: cognitif
category: atome
input_types: [brief, markdown, reference]
output_types: [problematisation]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---
```

Règles :

- `id` : anglais ou slug métier stable, kebab-case, identique au nom de fichier
- `label` : nom affiché, généralement en français
- `description_fr` / `description_en` : déclencheurs, rôle et limites du skill
- corps Markdown : instructions du skill, en anglais
- pas de logique, pas d'appel API, pas d'effet de bord dans un skill

---

## Overrides mystaffy

Le fichier `skills/<id>.mystaffy.json` complète le manifest généré depuis le
frontmatter.

Il sert surtout à définir :

- `category`
- `aliases`
- `params`
- `ui`
- `execution`

Pour les paramètres enum, utiliser `values` :

```json
{
  "params": {
    "mode": {
      "label": "Mode",
      "type": "enum",
      "required": false,
      "values": ["defensive", "offensive"]
    }
  }
}
```

---

## Build et validation

Depuis la racine du repo :

```bash
python3 build.py --validate
python3 build.py <id> --validate
python3 build.py <id> --target mystaffy --validate
python3 build.py <id> --target codex --validate
```

Les dossiers générés sont ignorés par git :

- `dist/`
- `mystaffy-dist/`
- `codex-dist/`

---

## Renommage d'un skill

Quand un skill est renommé :

1. Renommer `skills/<old-id>.md` en `skills/<new-id>.md`
2. Renommer `skills/<old-id>.mystaffy.json` en `skills/<new-id>.mystaffy.json`
3. Mettre à jour `id` dans le frontmatter
4. Ajouter l'ancien id dans `aliases` si la compatibilité de déclenchement est utile
5. Mettre à jour `.claude-plugin/plugin.json`
6. Mettre à jour `README.md` et `README-fr.md`
7. Lancer `python3 build.py --validate`

Exemples récents :

| Ancien id | Nouvel id |
|---|---|
| `prioriser` | `prioritize` |
| `problematiser` | `problem-framing` |
| `questionner` | `questioning` |
| `argumenter` | `argumentation` |
