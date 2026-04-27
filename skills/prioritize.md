---
id: prioritize
label: Prioriser
version: 1.1.0
description_fr: Ordonne une liste d'éléments par ordre d'attaque avec critères explicites et score visible. Déclenche quand l'utilisateur a plusieurs éléments à séquencer — features, tâches, initiatives, risques, idées, chantiers. Déclenche sur "dans quel ordre", "qu'est-ce qu'on fait en premier", "priorise ces items", "range ces tâches", "classe ces features". Produit toujours un classement numéroté avec rationale. Ne choisit pas entre options exclusives — utiliser `decision` pour ça. Ne décompose pas un problème — utiliser `decomposer` pour ça.
description_en: Ranks a list of items by attack order with explicit criteria and visible scores. Triggers when the user has multiple items to sequence — features, tasks, initiatives, risks, ideas, workstreams. Triggers on "in what order", "what do we do first", "prioritize these items", "rank these tasks", "sort these features". Always produces a numbered ranking with rationale. Does not choose between mutually exclusive options — use `decision` for that. Does not decompose a problem — use `decomposer` for that.
aliases: [prioriser]
icon: ↑↓
domain: cognitif
category: atome
input_types: [brief, markdown, reference, decomposition, options, critique]
output_types: [prioritized_list]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Prioritize

## Role

You take a list of items and produce a numbered ranking ordered by attack priority, with explicit criteria and visible scores.

## Absolute Rule

You must produce a ranked list.
No "it depends on your context" without a committed order.
Every item must appear in the output — either ranked or explicitly parked.
Trade-offs and scoring must be visible, not hidden.

---

## Context Gate

Before scoring, assess whether you have enough context to produce meaningful scores.

**Gate check — ask yourself:**
1. Do I know the goal driving this prioritization? (what success looks like, for whom)
2. Do I have at least one signal per item (description, size, risk, dependency)?

**If goal is completely absent:**
Ask exactly one question before proceeding:
> "What's the goal driving this prioritization?" *(e.g. ship faster, reduce risk, maximize revenue, clear backlog)*

Do not ask multiple questions. Do not ask for data you can infer or assume.

**If goal is thin but inferable** (items are self-describing, domain is clear):
Proceed in degraded mode — see below.

---

## Degraded Mode (low context)

Activate when: goal is absent or vague AND no criteria are provided.

Rules in degraded mode:
1. Fall back to **Value vs Effort** (2×2) — the framework least dependent on external data.
2. Score using only signals observable in the item descriptions themselves (complexity keywords, dependency language, risk language).
3. Mark every score as `[assumed]`.
4. Add a `## Degraded Mode` block in the output listing all assumptions made.
5. Set `confidence_level: low` in the output frontmatter.
6. End with: *"Provide the goal driving this prioritization to get a higher-confidence ranking."*

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
In degraded mode, always use **Value vs Effort**.

| Framework | When to use | Axes |
|---|---|---|
| **ICE** | General-purpose — tasks, features, initiatives | Impact · Confidence · Ease |
| **RICE** | Product roadmap with user reach data | Reach · Impact · Confidence · Effort |
| **MoSCoW** | Scope negotiation, delivery constraints | Must · Should · Could · Won't |
| **Eisenhower** | Personal or team task management | Urgent × Important matrix |
| **Value vs Effort** | Quick backlog sort or degraded mode | Value · Effort (2×2) |
| **Custom** | User provides explicit criteria | Use stated criteria directly |

---

## Method

1. Run the **context gate** — ask one question if goal is completely absent.
2. If goal is thin, activate **degraded mode**.
3. Identify the goal and time horizon from the brief.
4. Select the framework (or apply user-defined criteria).
5. Score each item on each axis (1–10 or H/M/L depending on framework).
6. Compute the composite score or place in matrix.
7. Apply hard constraints (regulatory, dependency, blocking).
8. Produce the ranked list.
9. Flag items that are deprioritized and make the reasoning explicit.
10. Surface assumptions that, if wrong, would change the order.

---

## Constraints

- Do not eliminate items silently — every item must be placed or explicitly parked.
- Do not default to "it depends" without committing to an order.
- Do not invent scores from thin air — if you assume, mark it `[assumed]` and explain why.
- Do not let recency bias or effort inflation distort scores — check for it.
- Never ask more than one clarifying question.

---

## Output Format

```markdown
---
status: draft
skill: prioritize
framework: [ice | rice | moscow | eisenhower | value-vs-effort | custom]
horizon: [sprint | quarter | year | unspecified]
confidence_level: [high | medium | low]
---

# Priority Order — {subject}

## Ranking

| # | Item | Score | Rationale |
|---|---|---|---|
| 1 | ... | ... | ... |
| 2 | ... | ... | ... |
| … | | | |

## Detailed Scores

| Item | {Axe 1} | {Axe 2} | {Axe 3} | Score composé |
|---|---|---|---|---|
| ... | | | | |

## Deprioritized Items

| Item | Reason |
|---|---|
| ... | ... |

## Key Assumptions
- [assumption] → [impact if false]

## What Would Change the Ranking
- [condition] → [impact on ranking]

<!-- Include only in degraded mode -->
## Degraded Mode
No goal was provided. Ranking produced with Value vs Effort using assumptions observable in the items.
Scores marked [assumed]. Provide the goal to get a more reliable ranking.
```

---

## Definition of Done

- Every item is placed in the ranked list or explicitly parked with a reason.
- The scoring method is visible and reproducible.
- Key assumptions that could invert the order are named.
- The human can act on the list immediately.
