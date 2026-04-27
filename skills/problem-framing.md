---
id: problem-framing
label: Problématiser
version: 0.2.0
description_fr: "[DRAFT] Reformule un sujet flou en problème actionnable avec une question centrale, des tensions sous-jacentes et des conditions de résolution. Déclenche quand la situation est décrite mais le vrai problème n'est pas encore formulé. Formule la question centrale — ne la résout pas."
description_en: "[DRAFT] Frames a vague subject as an actionable problem with a central question, underlying tensions, and resolution conditions. Triggers when the situation is described but the real problem is not yet formulated. Formulates the central question — does not solve it."
aliases: [problematiser]
icon: ⊙
domain: cognitif
category: atome
input_types: [brief, markdown, reference]
output_types: [problematisation]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Problem Framing

> **STATUS: DRAFT — not production ready**

## Role

You take a vague or ill-defined situation and reformulate it as a sharp, actionable problem.

## What this skill does NOT do

- Does not solve the problem
- Does not explore solutions
- Does not produce a plan

Use `explorer` or `decision` after this skill.

---

## Method

1. Extract the stated situation in one neutral sentence.
2. Separate symptoms, causes, constraints, stakeholders, and desired outcome.
3. Identify the main tension that makes the subject hard to resolve.
4. Remove false problems: issues that are symptoms, preferences, or implementation details.
5. Formulate one central question that is answerable and decision-useful.
6. Name the conditions that would make the problem resolved.

---

## Constraints

- Do not solve the problem.
- Do not recommend options.
- Do not produce an execution plan.
- Do not turn the problem into a vague theme or slogan.
- Prefer one sharp central question over multiple competing framings.

---

## Output Format

```markdown
---
status: draft
skill: problem-framing
confidence_level: [high | medium | low]
---

# Problem Framing — {subject}

## Situation
[One neutral sentence describing the situation.]

## Central Question
[One actionable question.]

## Underlying Tensions
- [tension] → [why it matters]

## What Is Not The Problem
- [false problem] → [why it is not central]

## Resolution Conditions
- [condition that would make the problem solved]

## Assumptions
- [assumption] → [impact if false]
```

---

## Core Output

1. **Central question** — the single sentence that frames the problem
2. **Underlying tensions** — what is in conflict (speed vs quality, autonomy vs control, etc.)
3. **What is not the problem** — false problems eliminated explicitly
4. **Resolution conditions** — what "solved" would look like

---

## Definition of Done

The human can answer: *"What exactly are we trying to solve?"* in one sentence.
