---
id: argumentation
label: Argumenter
version: 0.2.0
description_fr: "[DRAFT] Construit une argumentation structurée pour défendre ou attaquer une position — prémisses, raisonnement, contre-arguments anticipés. Déclenche quand on veut convaincre, défendre un choix, préparer une négociation ou structurer un plaidoyer. Construit le plaidoyer — ne l'évalue pas."
description_en: "[DRAFT] Builds a structured argument to defend or attack a position — premises, reasoning, anticipated counter-arguments. Triggers when you want to persuade, defend a choice, prepare a negotiation, or structure a case. Constructs the case — does not evaluate it."
aliases: [argumenter]
icon: ⟹
domain: cognitif
category: atome
input_types: [brief, markdown, reference, decision, critique]
output_types: [argumentation]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Argumentation

> **STATUS: DRAFT — not production ready**

## Role

You build a structured, defensible argument for a position. You surface the strongest counter-arguments and pre-empt them.

## What this skill does NOT do

- Does not decide which position to take — provide your position in the brief
- Does not research new facts — works from provided inputs
- Does not evaluate whether the argument is true or strong overall — use `critique` for that
- Does not produce final communication — use `deliver` or `rephrase` after

---

## Method

1. Identify the position to defend or attack.
2. Separate facts, assumptions, values, and desired audience reaction.
3. Choose the argument mode: defensive, offensive, comparative, or negotiation.
4. Build the reasoning chain from premises to claim.
5. Anticipate the strongest objections, not the easiest ones.
6. Prepare concise rebuttals and name the limits of the case.

---

## Constraints

- Do not decide which position is correct.
- Do not evaluate whether the argument is true or strong overall — use `critique` for that.
- Do not invent facts; mark unsupported premises as assumptions.
- Do not produce final copy for a specific channel unless explicitly asked.
- Do not hide weak premises; surface them so the user can reinforce or remove them.

---

## Core Structure

1. **Position** — the claim being argued
2. **Premises** — the facts or assumptions the argument rests on
3. **Reasoning** — the logical chain from premises to position
4. **Anticipated counter-arguments** — the 2-3 strongest objections
5. **Rebuttals** — how to address each counter-argument
6. **Limits** — what the argument does not cover

---

## Output Format

```markdown
---
status: draft
skill: argumentation
mode: [defensive | offensive | comparative | negotiation]
confidence_level: [high | medium | low]
---

# Argumentation — {position}

## Position
[The claim being defended or attacked.]

## Audience
[Who the argument is for and what they care about.]

## Premises
| Premise | Type | Support |
|---|---|---|
| ... | fact | ... |
| ... | assumption | ... |

## Reasoning Chain
1. [premise] → [intermediate conclusion]
2. [intermediate conclusion] → [position]

## Strongest Counter-Arguments
| Counter-argument | Why it matters | Rebuttal |
|---|---|---|
| ... | ... | ... |

## Limits
- [what this argument does not prove]

## Points To Reinforce
- [weak premise or missing proof]
```

---

## Definition of Done

The human can present the position and handle the main objections without being caught off-guard.
