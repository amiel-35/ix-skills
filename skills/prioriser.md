---
id: prioriser
label: Prioriser
version: 1.0.0
description_fr: Ordonne une liste d'éléments par ordre d'attaque avec critères explicites et score visible. Déclenche quand l'utilisateur a plusieurs éléments à séquencer — features, tâches, initiatives, risques, idées, chantiers. Déclenche sur "dans quel ordre", "qu'est-ce qu'on fait en premier", "priorise ces items", "range ces tâches", "classe ces features". Produit toujours un classement numéroté avec rationale. Ne choisit pas entre options exclusives — utiliser `decision` pour ça. Ne décompose pas un problème — utiliser `decomposer` pour ça.
description_en: Ranks a list of items by attack order with explicit criteria and visible scores. Triggers when the user has multiple items to sequence — features, tasks, initiatives, risks, ideas, workstreams. Triggers on "in what order", "what do we do first", "prioritize these items", "rank these tasks", "sort these features". Always produces a numbered ranking with rationale. Does not choose between mutually exclusive options — use `decision` for that. Does not decompose a problem — use `decomposer` for that.
icon: ↑↓
domain: cognitif
category: atome
input_types: [brief, markdown, reference, decomposition, options, critique]
output_types: [prioritized_list]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Prioriser

## Role

You take a list of items and produce a numbered ranking ordered by attack priority, with explicit criteria and visible scores.

## Absolute Rule

You must produce a ranked list.
No "it depends on your context" without a committed order.
Every item must appear in the output — either ranked or explicitly parked.
Trade-offs and scoring must be visible, not hidden.

---

## Expected Inputs

| Field | Required | Description |
|---|---|---|
| `brief` | yes | The subject to prioritize and the goal driving it |
| `input_artifacts[]` | yes | The list of items to rank |
| `framework` | no | Scoring framework — default: ICE |
| `criteria` | no | Custom criteria overriding the framework |
| `constraints` | no | Hard constraints that force certain items up or down |
| `horizon` | no | Time horizon — sprint, quarter, year |

---

## Frameworks

Choose based on what the user provides. Default to **ICE** unless the brief suggests otherwise.

| Framework | When to use | Axes |
|---|---|---|
| **ICE** | General-purpose — tasks, features, initiatives | Impact · Confidence · Ease |
| **RICE** | Product roadmap with user reach data | Reach · Impact · Confidence · Effort |
| **MoSCoW** | Scope negotiation, delivery constraints | Must · Should · Could · Won't |
| **Eisenhower** | Personal or team task management | Urgent × Important matrix |
| **Value vs Effort** | Quick backlog sort, no data available | Value · Effort (2×2) |
| **Custom** | User provides explicit criteria | Use stated criteria directly |

---

## Method

1. Identify the goal and time horizon from the brief.
2. Select the framework (or apply user-defined criteria).
3. Score each item on each axis (1–10 or H/M/L depending on framework).
4. Compute the composite score or place in matrix.
5. Apply hard constraints (regulatory, dependency, blocking).
6. Produce the ranked list.
7. Flag items that are deprioritized and make the reasoning explicit.
8. Surface assumptions that, if wrong, would change the order.

---

## Constraints

- Do not eliminate items silently — every item must be placed or explicitly parked.
- Do not default to "it depends" without committing to an order.
- Do not let recency bias or effort inflation distort scores — check for it.
- If critical information is missing (e.g. reach data for RICE), acknowledge it and proceed with stated assumptions.

---

## Output Format

```markdown
---
status: draft
skill: prioriser
framework: [ice | rice | moscow | eisenhower | value-vs-effort | custom]
horizon: [sprint | quarter | year | unspecified]
---

# Priorité — {sujet}

## Classement / Ranking

| # | Item | Score | Rationale |
|---|---|---|---|
| 1 | ... | ... | ... |
| 2 | ... | ... | ... |
| … | | | |

## Scores détaillés / Detailed Scores

| Item | {Axe 1} | {Axe 2} | {Axe 3} | Score composé |
|---|---|---|---|---|
| ... | | | | |

## Items déprioritisés / Deprioritized Items

| Item | Raison |
|---|---|
| ... | ... |

## Hypothèses clés / Key Assumptions
- [hypothèse] → [impact si fausse]

## Ce qui changerait l'ordre / What Would Change the Ranking
- [condition] → [impact sur le classement]
```

---

## Definition of Done

- Every item is placed in the ranked list or explicitly parked with a reason.
- The scoring method is visible and reproducible.
- Key assumptions that could invert the order are named.
- The human can act on the list immediately.
