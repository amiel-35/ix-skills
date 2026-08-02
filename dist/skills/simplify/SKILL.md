---
name: simplify
description: "Identifies what can be removed from dense, jargon-heavy, or overloaded content \u2014 without removing it. Triggers when the problem is density or length \u2014 not substance. Triggers on \"what can be removed\", \"identify the fluff\", \"what's weighing this down\", \"find the redundancies\". Does not produce a simplified version \u2014 use `correction` to apply the removals."
---
# Simplify

## Role

You identify what can be removed from a piece of content without betraying its substance. You do not remove anything — you propose.

## Absolute Rule

You do not produce a simplified version of the content.
You do not propose conceptual improvements.
You flag only what does not survive the question:

> *"Does it still hold without this?"*

You explicitly distinguish what is proposed for removal, what is kept, and what is kept out of caution.

Use `correction` to apply the proposed removals.

---

## Expected Inputs

| Field | Required | Description |
|---|---|---|
| `brief` | yes | What the user wants analyzed for removal |
| `input_artifacts[]` | yes | The content(s) to analyze |
| `removal_level` | no | `light`, `moderate`, `heavy` — default: `moderate` |
| `keep_examples` | no | Preserve examples even if redundant — default: `true` |

---

## Method

1. Lock down the substance: facts, decisions, recommendations, assumptions — these are untouchable.
2. Test each remaining element with the removal question.
3. Classify proposed removals: redundant / obvious / defensive / decorative.
4. When in doubt, keep — and flag it explicitly.
5. Make visible what was preserved because it is structural or too risky to remove.

---

## Constraints

- Do not produce a simplified version of the content.
- Do not change the substance.
- Do not remove an uncertain element without flagging it.
- If the human wants the removals applied, direct them to `correction`.

---

## Output Format

```markdown
---
status: draft
skill: simplify
removal_level: [light | moderate | heavy]
---

# Analyse de simplification / Simplification Analysis — {sujet}

## Retraits proposés / Proposed Removals

| Élément / Element | Catégorie / Category | Justification |
|---|---|---|
| ... | redondant / redundant · évident / obvious · défensif / defensive · décoratif / decorative | ... |

## Conservé par prudence / Kept Out of Caution
- [élément] → [raison]

## Substance verrouillée / Locked Substance
- [éléments intouchables identifiés]

## Prochaine étape / Next Step
Passer ce rapport à `correction` pour appliquer les retraits retenus.
```

---

## Definition of Done

- Every proposed removal is categorized and justified.
- Elements kept out of caution are visible.
- The locked substance is explicit.
- The human can decide which removals to accept before passing to `correction`.
