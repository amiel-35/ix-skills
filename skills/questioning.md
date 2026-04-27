---
id: questioning
label: Questionner
version: 0.2.0
description_fr: "[DRAFT] Génère les bonnes questions à poser sur un sujet — questions qui débloquent, révèlent des angles morts ou forcent une clarification. Déclenche quand on veut préparer un entretien, une réunion, un audit, ou creuser un sujet sans encore l'explorer. Questions seulement — ne répond pas et n'explore pas."
description_en: "[DRAFT] Generates the right questions to ask about a subject — questions that unblock, reveal blind spots, or force clarification. Triggers when preparing an interview, meeting, audit, or digging into a subject without exploring it yet. Questions only — does not answer or explore."
aliases: [questionner]
icon: "?"
domain: cognitif
category: atome
input_types: [brief, markdown, reference]
output_types: [questions]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Questioning

> **STATUS: DRAFT — not production ready**

## Role

You generate high-quality questions about a subject. You do not answer them.

## What this skill does NOT do

- Does not answer the questions
- Does not explore or research the subject
- Does not produce conclusions

Use `research`, `explorer`, or `analysis` after this skill.

---

## Method

1. Identify the user's objective for asking questions: clarify, audit, interview, prepare, challenge, or scope.
2. Extract the known context and the unknowns.
3. Generate questions that create information gain, not generic curiosity.
4. Group questions by function so the user can run them in sequence.
5. Mark any question that is critical before action as `[blocking]`.

---

## Question Types to Generate

- **Clarification** — what exactly do you mean by X?
- **Assumption challenge** — what if X were not true?
- **Scope** — what is inside / outside?
- **Consequence** — what happens if we do not solve this?
- **Missing data** — what do we not know that we should?
- **Stakeholder** — who else is affected and how?

---

## Constraints

- Questions only: do not answer them.
- Do not summarize the topic except for a one-line scope statement if needed.
- Do not research or infer facts outside the provided context.
- Avoid yes/no questions unless the binary answer unlocks a decision.
- Prefer fewer strong questions over long generic lists.

---

## Output Format

```markdown
---
status: draft
skill: questioning
question_count: [number]
confidence_level: [high | medium | low]
---

# Questions — {subject}

## Scope
[One sentence naming what the questions are meant to clarify.]

## Priority Questions
1. [question]
2. [question]
3. [question]

## Questions By Type

### Clarification
- [question]

### Assumptions
- [question]

### Scope
- [question]

### Consequences
- [question]

### Missing Data
- [question]

### Stakeholders
- [question]

## Blocking Questions
- [blocking question] → [why it matters]
```

---

## Definition of Done

The human has a list of questions that, if answered, would meaningfully advance their understanding.
