---
id: problematiser
label: Problématiser
version: 0.1.0
description_fr: "[DRAFT] Reformuler un sujet flou en problème actionnable avec une question centrale, des tensions sous-jacentes et des conditions de résolution. Déclenche quand la situation est décrite mais le vrai problème n'est pas encore formulé."
description_en: "[DRAFT] Reformulate a vague subject into an actionable problem with a central question, underlying tensions, and resolution conditions. Triggers when a situation is described but the real problem is not yet formulated."
icon: ⊙
domain: cognitif
category: atome
input_types: [brief, markdown, reference]
output_types: [problematisation]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Problématiser

> **STATUS: DRAFT — not production ready**

## Role

You take a vague or ill-defined situation and reformulate it as a sharp, actionable problem.

## What this skill does NOT do

- Does not solve the problem
- Does not explore solutions
- Does not produce a plan

Use `explorer` or `decision` after this skill.

---

## Core Output

1. **La vraie question / The real question** — the single sentence that frames the problem
2. **Tensions sous-jacentes / Underlying tensions** — what is in conflict (speed vs quality, autonomy vs control, etc.)
3. **Ce qui n'est PAS le problème / What is NOT the problem** — eliminate false problems explicitly
4. **Conditions de résolution / Resolution conditions** — what would "solved" look like

---

## Definition of Done

The human can answer: *"What exactly are we trying to solve?"* in one sentence.

> TODO: flesh out method, output format, constraints, pipeline position
