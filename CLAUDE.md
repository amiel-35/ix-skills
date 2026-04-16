# Guide de contribution — ix-skills

## 1. Structure du repo

| Chemin | Rôle |
|---|---|
| `skills/` | Source canonique : un fichier `.md` par skill + fichiers `.mystaffy.json` d'override |
| `dist/` | Artefacts `.skill` pour claude.ai — gitignore, généré par `build.py` |
| `mystaffy-dist/` | Artefacts mystaffy — gitignore, généré par `build.py` |
| `.claude-plugin/plugin.json` | Manifest pour Claude Code / Cowork |
| `build.py` | Seul point d'entrée pour packager les skills |
| `requirements.txt` | Dépendances Python (`jsonschema`, `pyyaml`) |

---

## 2. Format canonique d'un skill

Chaque fichier `skills/<id>.md` commence par un bloc frontmatter YAML.

### Champs obligatoires

| Champ | Type | Description |
|---|---|---|
| `id` | string | kebab-case, correspond exactement au nom du fichier |
| `label` | string | Nom affiché (en français) |
| `version` | string | semver (`x.y.z`) |
| `description_fr` | string | Déclencheurs + ce que le skill fait / ne fait pas (en français) |
| `description_en` | string | Même chose en anglais |
| `icon` | string | Emoji ou caractère unicode |
| `domain` | string | Tag métier — voir section 6 |
| `input_types` | string[] | Types d'entrée acceptés |
| `output_types` | string[] | Types de sortie produits |
| `compatible` | string[] | Toujours `[claude-ai, claude-code, cowork, gpt, gemini, mystaffy]` |

### Champs optionnels

| Champ | Type | Description |
|---|---|---|
| `category` | string | Type d'atome mystaffy : `atome`, `research`, `critique`, `decision`, `production`, … |
| `aliases` | string[] | Noms alternatifs pour le skill |

### Body

Le body (tout ce qui suit le frontmatter) est rédigé **entièrement en anglais**. Il décrit le rôle, les règles, la méthode, les contraintes et le format de sortie du skill.

---

## 3. Règles de nommage

- `id` : minuscules, kebab-case, correspond **exactement** au nom du fichier `.md`
- Pas d'espaces, pas d'accents dans les ids
- Breaking change → bump de version **majeure**
- Ajout de feature → bump de version **mineure**
- Correction → bump de version **patch**

---

## 4. Checklist — ajouter un nouveau skill

1. Créer `skills/<id>.md` avec le frontmatter canonique complet
2. Écrire le body en anglais
3. Créer `skills/<id>.mystaffy.json` avec `category`, `params`, `ui` (minimum)
4. Tester : `python3 build.py <id> --validate`
5. Builder : `python3 build.py <id>`
6. Vérifier que le skill apparaît dans `.claude-plugin/plugin.json` (mettre à jour si nécessaire)

---

## 5. Checklist — ajouter un nouveau domaine

1. Choisir un slug `domain` (minuscules, parmi la liste de la section 6)
2. Ajouter le mapping dans la table `DOMAIN_TO_METIER` de `build.py`
3. Documenter le domaine dans la section 6 de ce fichier

---

## 6. Domaines disponibles

| domain | metier[] mystaffy | statut |
|---|---|---|
| cognitif | transverse | actif |
| rh | rh | prévu |
| sales | commercial | prévu |
| finance | finance | prévu |
| legal | juridique | prévu |
| ops | transverse | prévu |
| data | analyste_data | prévu |
| strategy | intelligence_strategique | prévu |
| fondateur | fondateur_ceo | prévu |

---

## 7. Cibles de packaging

```bash
python3 build.py                              # tous les targets, tous les skills
python3 build.py <id>                         # un skill spécifique, tous targets
python3 build.py --target claude-ai           # dist/*.skill pour claude.ai
python3 build.py --target cowork              # valide .claude-plugin/plugin.json
python3 build.py --target mystaffy            # mystaffy-dist/<id>/
python3 build.py --target mystaffy --domain cognitif
python3 build.py --validate                   # valide sans écrire
```

### Étendre build.py pour une nouvelle cible

1. Ajouter la valeur dans le `choices` du `--target` argument
2. Créer une fonction `build_<target>(skill_id, ...)` dans `build.py`
3. L'appeler depuis `main()` selon le target sélectionné

---

## 8. Règles de contribution

- Le body des skills est **en anglais**
- `label`, `description_fr`, `description_en` et tout `README.md` sont **en français** (ou bilingues)
- Un skill = un fichier source dans `skills/`
- Pas de logique métier dans les skills — les skills sont des prompts, pas du code
- Pas de dépendances externes dans `build.py` sauf `jsonschema` et `pyyaml`
- `mystaffy-dist/` et `dist/` sont gitignorés — ne jamais les committer

---

## 9. Ce qu'on ne fait PAS

- Pas de logique conditionnelle, d'API calls, ou de side-effects dans les skills
- Pas de dépendances externes dans `build.py` (sauf `jsonschema` et `pyyaml`)
- Pas de fichiers générés dans le repo (`dist/`, `mystaffy-dist/` sont gitignorés)
- Pas de noms de skills avec accents ou majuscules dans l'`id`
