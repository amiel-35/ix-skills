---
id: simplify
label: Simplifier
version: 2.1.1
description_fr: Identifie ce qui peut être retiré d'un contenu dense, jargonneux ou surchargé — sans le retirer. Déclenche quand le problème est la densité ou la longueur — pas le fond. Déclenche sur "qu'est-ce qui peut être retiré", "identifie le superflu", "qu'est-ce qui alourdit ça", "trouve ce qui est redondant". Ne produit pas de version simplifiée — l'utilisateur applique lui-même les retraits qu'il retient (aucun autre skill ne le fait ; `correction` consolide une critique, il ne réécrit pas le texte).
description_en: Identifies what can be removed from dense, jargon-heavy, or overloaded content — without removing it. Triggers when the problem is density or length — not substance. Triggers on "what can be removed", "identify the fluff", "what's weighing this down", "find the redundancies". Does not produce a simplified version — the user applies the removals they accept (no other skill does it; `correction` consolidates a critique, it does not rewrite the text).
icon: △
domain: cognitif
category: atome
input_types: [brief, markdown, reference, critique]
output_types: [rapport_retraits]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
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
An empty removals table is a valid result: you output « RAS — nothing to remove at level {removal_level}. » and stop.

The user applies the removals they accept. No skill does it for them: `correction` consolidates a critique into directives, it does not rewrite the source text.

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
- If the human wants the removals applied, tell them they apply the accepted ones themselves (or edit the text directly outside this skill); do not send them to `correction`, which does not rewrite text.

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
Choisir les retraits à accepter, puis les appliquer soi-même au texte source.
```

---

## Definition of Done

- Every proposed removal is categorized and justified.
- Elements kept out of caution are visible.
- The locked substance is explicit.
- The human can decide which removals to accept before applying them to the source text.
- An empty removals report names the level tested — « RAS » ends the exercise.
