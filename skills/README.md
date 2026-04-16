# ix-skills

Atomic knowledge-work skills for structured pipelines.

7 skills composables, portables sur Claude, GPT, Gemini, et [mystaffy](https://mystaffy.io).

---

## Skills disponibles

| Skill | Rôle | Pipeline |
|---|---|---|
| `critique` | Trouver les failles sans proposer de solution | → correction |
| `correction` | Transformer une critique en directives actionnables | critique → |
| `simplifier` | Épurer un contenu sans changer le fond | standalone |
| `reformuler` | Transposer le sens dans un autre registre | standalone |
| `explorer` | Générer un espace d'options sans trancher | → décision |
| `décision` | Arbitrer avec trade-offs visibles et recommandation nette | explorer → |
| `livraison` | Transformer un artifact en livrable partageable | → fin de pipeline |

---

## Installation

### Claude Code / Cowork

```bash
# Ajouter le marketplace
claude plugin marketplace add amiel-35/ix-skills

# Installer tous les skills
claude plugin install ix-skills@ix-skills

# Ou skill par skill
claude plugin install critique@ix-skills
claude plugin install correction@ix-skills
```

### Claude.ai

1. Cloner le repo et builder les `.skill` :
```bash
git clone https://github.com/amiel-35/ix-skills
cd ix-skills
python build.py
```
2. Glisser les fichiers `dist/*.skill` dans **Settings → Skills** de Claude.ai.

### GPT / Gemini / autre LLM

Copier-coller le contenu de `skills/<skill>.md` directement comme system prompt. Le frontmatter YAML est ignoré par les LLMs qui ne le supportent pas — aucun impact.

### mystaffy

Les fichiers `skills/*.md` sont le format natif mystaffy. Copier dans ton catalogue de skills.

---

## Structure

```
ix-skills/
├── skills/              ← source canonique (un fichier par skill)
│   ├── critique.md
│   ├── correction.md
│   ├── simplifier.md
│   ├── reformuler.md
│   ├── explorer.md
│   ├── decision.md
│   └── livraison.md
├── dist/                ← .skill générés pour claude.ai (git-ignoré)
├── .claude-plugin/
│   └── plugin.json      ← manifest pour Claude Code / Cowork
├── build.py             ← compile skills/*.md → dist/*.skill
└── README.md
```

### Format canonique

Chaque `skill.md` contient un frontmatter YAML (métadonnées) suivi des instructions Markdown :

```markdown
---
id: critique
label: Critique
version: 1.0.0
description: ...
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Critique
...
```

Le frontmatter est utilisé par `build.py` et le runtime mystaffy. Il est ignoré sans effet de bord par les autres LLMs.

---

## Pipelines typiques

```
critique → correction → livraison
explorer → décision  → livraison
           simplifier (standalone)
           reformuler (standalone)
```

---

## Contribuer

Les skills sont du Markdown. Fork, modifie, PR.

---

## Licence

MIT
