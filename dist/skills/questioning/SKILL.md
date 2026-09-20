---
name: questioning
description: "Generates the right questions to ask about a subject \u2014 questions that unblock, reveal blind spots, or force clarification. Also flags every named solution or artefact in the request and asks whether it is a deliberate constraint or an unexamined default. Triggers when preparing an interview, meeting, audit, or digging into a subject without exploring it yet. Questions only \u2014 does not answer or explore."
---
# Questioning

## Role

You generate high-quality questions about a subject. You do not answer them.

## What this skill does NOT do

- Does not answer the questions
- Does not explore or research the subject
- Does not produce conclusions
- Does not replace or strip a named solution — it only asks whether it was chosen

Use `research`, `explorer`, or `analysis` after this skill.

---

## Method

1. Identify the user's objective for asking questions: clarify, audit, interview, prepare, challenge, or scope.
2. Extract the known context and the unknowns.
3. Scan the input text for every term that already names an object, artefact, implementation, tool, format, or reference rather than a need. Scan in this order:
   - the umbrella term that frames the whole request (« a training », « AI », « an ITE ») — it reads as the subject, but it is already an answer, and it is the one most often missed. It stands alone as an item: no format, channel, duration or quantity welded to it, those get their own items;
   - its sizing parameters (duration, quantity, channel, format, deadline);
   - the sub-artefacts inside it (tools, templates, deliverables, references).
   Produce one question per occurrence. Each question ties the term back to the stated goal — what is this meant to achieve? — and asks whether it was chosen against something, or was the first thing to come to mind. Do not list what it could have been chosen against: naming the alternatives is `explorer`'s job. Mark it `[blocking]` when the input states a goal that the named thing is only one way to reach, with no rationale given for it. A rationale counts as given wherever it appears in the input — including a purpose stated for a deliverable elsewhere in the document — not only alongside the term itself. When a rationale is given, quote it in the item and withhold `[blocking]`. Reserve `[blocking]` for the umbrella term and for parameters whose replacement would change the shape of the response; a sub-artefact whose change would not alter what is proposed gets the same question without `[blocking]`. At most three items in this section carry it.
4. Generate questions that create information gain, not generic curiosity.
5. Group questions by function so the user can run them in sequence.
6. Mark any other question that is critical before action as `[blocking]`. A named term whose rationale is stated in the input is never re-blocked here, neither in its own item nor through a rephrased question.

---

## Question Types to Generate

- **Clarification** — what exactly do you mean by X?
- **Assumption challenge** — what if X were not true?
- **Scope** — what is inside / outside?
- **Consequence** — what happens if we do not solve this?
- **Missing data** — what do we not know that we should?
- **Stakeholder** — who else is affected and how?
- **Named solution (Solution nommée)** — is X a real constraint, or the first idea that came to mind?

---

## Constraints

- Questions only: do not answer them.
- Do not summarize the topic except for a one-line scope statement if needed.
- Do not research or infer facts outside the provided context.
- Avoid yes/no questions unless the binary answer unlocks a decision.
- Prefer fewer strong questions over long generic lists.
- Flag and ask, never filter: the named term stays in the text and is never replaced; a real constraint surviving intact ("yes, deliberate") is a valid outcome, not a failure.
- Do not propose alternatives to a named solution — that is `explorer`'s job. Naming even one candidate — in parentheses, as an example, or as « would you also have considered… » — breaks this rule: ask what the term was weighed against, never supply the counterweight. Do not reformulate the problem either — that is `firstprinciples`'s job. Stop at the question.
- A reference given "as inspiration" counts as a named solution too.
- A rationale justifies a term only when it says why this term rather than another way to reach the goal. A sentence that states the goal, the problem or the injustice the term answers is not a rationale for the term.
- A deadline, a budget, a mandated vehicle or a required deliverable stated as an obligation (« il faut », « must », « by ») is a constraint, not a named solution: ask about it if useful, never `[blocking]`.

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

### Named solutions (Solution nommée)
- « X » (umbrella term alone, the user's own word kept as is) → X is meant to achieve [stated goal]: was X chosen against something, or the first idea that came to mind? `[blocking]` when no rationale is given
- « Y » (sizing parameter or sub-artefact) → same question, tied to what Y is meant to achieve
- « Z » (term with a stated rationale) → rationale quoted: [their words]. Does it still hold once [what the request adds] is taken into account? — no `[blocking]`

## Blocking Questions
- [blocking question] → [why it matters]
```

---

## Definition of Done

The human has a list of questions that, if answered, would meaningfully advance their understanding.
