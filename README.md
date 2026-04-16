# ix-skills

Skills de knowledge-work atomiques pour pipelines structurés.

---

## Skills disponibles

| Skill | Rôle | Pipeline |
|---|---|---|
| `critique` | Identifier les failles d'un contenu sans proposer de solution | → correction |
| `correction` | Transformer une critique en directives actionnables | critique → |
| `simplifier` | Épurer un contenu sans changer le fond | standalone |
| `reformuler` | Transposer le sens dans un autre registre | standalone |
| `explorer` | Générer un espace d'options sans trancher | → décision |
| `décision` | Arbitrer avec trade-offs visibles et recommandation nette | explorer → |
| `livraison` | Transformer un artifact en livrable partageable | → fin de pipeline |

---

## Pipelines typiques

```
critique → correction → livraison
explorer → décision   → livraison
           simplifier (standalone)
           reformuler (standalone)
```

---

## Installation

### Claude Code / Cowork

```bash
claude plugin install ix-skills
```

Le repo est le plugin. Les skills sont dans `skills/`.

### Claude.ai

```bash
git clone https://github.com/amiel-35/ix-skills
cd ix-skills
pip install -r requirements.txt
python3 build.py --target claude-ai
```

Glisser les fichiers `dist/*.skill` dans **Settings → Skills**.

### mystaffy

```bash
python3 build.py --target mystaffy
```

Les artefacts sont dans `mystaffy-dist/<id>/`.

### GPT / Gemini / autre LLM

Copier-coller le contenu de `skills/<id>.md` comme system prompt. Le frontmatter YAML est ignoré sans effet de bord.

---

## Structure

```
ix-skills/
├── skills/                 ← source canonique (un fichier par skill)
│   ├── critique.md
│   ├── critique.mystaffy.json
│   ├── correction.md
│   ├── ...
├── dist/                   ← .skill pour claude.ai (gitignore)
├── mystaffy-dist/          ← artefacts mystaffy (gitignore)
├── .claude-plugin/
│   └── plugin.json         ← manifest Claude Code / Cowork
├── build.py                ← packager multi-cibles
├── requirements.txt
└── CLAUDE.md               ← guide de contribution
```

---

## Packager

```bash
python3 build.py --validate          # valider sans écrire
python3 build.py                     # tous les targets
python3 build.py critique            # un skill spécifique
python3 build.py --target mystaffy --domain cognitif
```

---

## Contribuer

Fork, modifie, PR. Lire `CLAUDE.md` pour les conventions.

---

## Licence

MIT
