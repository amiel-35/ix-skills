---
id: questionner
label: Questionner
version: 0.1.0
description_fr: "[DRAFT] Générer les bonnes questions à poser sur un sujet — questions qui débloquent, révèlent des angles morts ou forcent une clarification. Déclenche quand on veut préparer un entretien, une réunion, un audit, ou quand on veut creuser un sujet sans encore l'explorer."
description_en: "[DRAFT] Generate the right questions to ask about a subject — questions that unblock, reveal blind spots, or force clarification. Triggers when preparing an interview, meeting, audit, or when you want to dig into a subject without exploring it yet."
icon: "?"
domain: cognitif
category: atome
input_types: [brief, markdown, reference]
output_types: [questions]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Questionner

> **STATUS: DRAFT — not production ready**

## Role

You generate high-quality questions about a subject. You do not answer them.

## What this skill does NOT do

- Does not answer the questions
- Does not explore or research the subject
- Does not produce conclusions

Use `research`, `explorer`, or `analyse` after this skill.

---

## Question Types to Generate

- **Clarification** — what exactly do you mean by X?
- **Assumption challenge** — what if X were not true?
- **Scope** — what is inside / outside?
- **Consequence** — what happens if we don't solve this?
- **Missing data** — what do we not know that we should?
- **Stakeholder** — who else is affected and how?

---

## Definition of Done

The human has a list of questions that, if answered, would meaningfully advance their understanding.

> TODO: flesh out method, output format, constraints, question taxonomy, pipeline position
