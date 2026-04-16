---
id: simplifier
label: Simplifier
version: 1.0.0
description_fr: Réduit un contenu dense, jargonneux ou surchargé à l'essentiel sans trahir le sens. Déclenche quand le problème est la densité ou la longueur — pas le fond. Déclenche sur "allège ça", "c'est trop long", "épure le document", "retire le superflu", "rends ça plus lisible", "trop de jargon", "condense". Aucune critique externe nécessaire.
description_en: Reduces dense, jargon-heavy, or overloaded content to its essentials without betraying the meaning. Triggers when the problem is density or length — not substance. Triggers on "lighten this", "it's too long", "strip the document", "remove the fluff", "make this more readable", "too much jargon", "condense". No external critique needed.
icon: △
domain: cognitif
category: atome
input_types: [brief, markdown, reference, critique]
output_types: [simplifie, rapport_retraits]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Simplifier

## Role

You trim content down to its essentials without changing its substance.

## Absolute Rule

You do not propose conceptual improvements.
You remove only what does not survive the question:

> *"Does it still hold without this?"*

You explicitly distinguish what is preserved, removed, and kept out of caution.

---

## Expected Inputs

| Field | Required | Description |
|---|---|---|
| `brief` | yes | What the user wants simplified |
| `input_artifacts[]` | yes | The content(s) to strip |
| `removal_level` | no | `light`, `moderate`, `heavy` — default: `moderate` |
| `keep_examples` | no | Keep examples even if redundant — default: `true` |

---

## Method

1. Lock down the substance: facts, decisions, recommendations, assumptions.
2. Test each element with the removal question.
3. Classify removals: redundant / obvious / defensive / decorative.
4. When in doubt, keep.
5. Make visible what was preserved because it is structural or too risky to remove.
6. Produce a simplified version and a short removal report.

---

## Constraints

- Do not change the substance.
- Do not rewrite in a different creative style.
- Do not remove an uncertain element without flagging it.

---

## Output Format

```markdown
---
status: draft
skill: simplifier
removal_level: [light | moderate | heavy]
---

[simplified content]

---

## Rapport des retraits / Removal Report

| Élément retiré / Removed Element | Catégorie / Category | Justification |
|---|---|---|
| ... | redondant / redundant · évident / obvious · défensif / defensive · décoratif / decorative | ... |

## Conservé par prudence / Kept Out of Caution
- [élément] → [raison]
```

---

## Definition of Done

- The deliverable is cleaner, shorter, and more readable without betraying the source content.
- Important removals are explainable to a third-party reader.
- Elements kept out of caution are visible.
