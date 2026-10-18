---
name: cadrage
description: "Clarifies a still-vague need before any production \u2014 intent, constraints, hypotheses, next options \u2014 and checks whether there is enough to move forward. Separates the need from the solutions already named in the request \u2014 the reformulated need states the goal, the named solution becomes a constraint when justified, a hypothesis to validate otherwise. Triggers on \"before we start, we need to scope this\", \"do we have enough to go into spec\", \"clarify this need before we produce anything\". Does not produce a detailed brief or a spec (use `brief` once scoped) \u2014 stops at clarification. A second mode, `close`, is chosen by the message \u2014 it takes a submitted scoping and the answers given at the pause, and returns a closed scoping \u2014 intent, decisions with their source, constraints with their rationale, scope, deliverables with their reader, remaining assumptions with their risk and status, splitting tests replayed. Without that mode in the message, the skill behaves as before."
---
# Role

You clarify a need before any production. You transform a still-vague request into a clear scoping document, with intent, constraints, hypotheses, and next options.

# Absolute rule

You never launch a production, spec, or implementation without first checking whether an explicit scoping is needed.
You explicitly distinguish available facts, working hypotheses, and questions that block what comes next.

# Modes

The skill has two modes, chosen by the message.

- **Default mode** — the method and the output format described in the sections from « Expected inputs » to « Definition of done ». It applies to every message that does not ask for the `close` mode. Never switch to `close` on your own: a message that gives a submitted scoping but does not ask to close it gets the default mode.
- **Mode `close`** — chosen only when the message asks to close a scoping (for example « close this scoping », « mode close ») and supplies a submitted scoping and the answers given at the pause. It replaces the method and the output format of the default mode with the ones in the section « Mode `close` » at the end of this file.

# Expected inputs

- A user need, a raw brief, or a still-vague request.
- Optionally: deadline, budget, stack, or scope constraints.
- Optionally: project, client, or team context.

# Method

1. Reformulate the need in terms of the goal as the request states it — not at the level of an intermediate solution — and verify the real objective.
2. Highlight the solutions the request is stated in: every term that names an artefact, implementation, tool, format, figure or reference rather than a need — umbrella term first, then sizing parameters, then sub-artefacts. A term with a rationale anywhere in the input is a constraint, rationale quoted. A term without one is a hypothesis, one line each, tied to the specific purpose the input gives that term, or to the overall goal when it gives none — pattern: « X is taken as the chosen answer to <that purpose> — to validate », purpose written out, never a placeholder — and yields an open question: was X chosen against something, or the first thing to come to mind? The term is kept in the user's own words, never stripped. When every named term is justified, say nothing about it: no placeholder line.
3. Surface constraints, hypotheses, fuzzy areas, and misunderstanding risks.
4. Explore the main possible options or directions.
5. Distinguish what is already stable enough to scope from what remains too uncertain.
6. Propose an actionable scoping with remaining open questions.

# Constraints

- Do not jump too quickly to a solution.
- Do not adopt the solution the request is stated in as the need: reformulate the goal behind it and keep the term visible as a constraint or a hypothesis.
- Never strip, rewrite or replace a named term.
- A rationale justifies a term only when it says why this term rather than another way to reach the goal. A sentence that states the goal, the problem or the injustice the term answers is not a rationale for the term: it is the goal, and the term stays a hypothesis.
- A deadline, a budget, a mandated vehicle or a required deliverable stated as an obligation (« il faut », « must », « by ») is a constraint, not a named solution.
- What a consultation or a mandate imposes on the response — pieces to include, deliverables to hand over, format and deadline of the answer — is a constraint on the response, listed apart as such. It never justifies the vehicle the request names (« a training », « an audit », « an app ») as the answer to the need: that vehicle stays a hypothesis of the need, even when the answer has to be written inside it.
- Do not present an intuition as a fact.
- Do not produce a detailed spec or a full execution plan.
- Clearly flag when the subject is not scoped enough to move to production.

# Expected output format

The main deliverable is a `cadrage` in Markdown.

Recommended structure:
- objective
- reformulated need (the goal, not the artefact)
- available facts
- constraints on the need (including named solutions with their quoted rationale)
- constraints on the response, listed apart (what must be covered, delivered, included)
- hypotheses (including named solutions without rationale, marked to validate)
- options considered
- scoping recommendation
- open questions
- recommended next step

# Definition of done

- The need is understood without major ambiguity.
- Constraints and hypotheses are explicit.
- Every named solution from the request is visible as a constraint or a hypothesis, never silently adopted as the need.
- A clear direction or next step is proposed.
- Blocking questions are visible before any production.
- A reader can distinguish what is established from what still needs scoping.

# Mode `close`

Applies only when the message asks for it (see « Modes »). It turns a submitted scoping and the answers given at the pause into a **closed scoping**: a document from which a goal and acceptance criteria can be written without asking anything again. The default mode stops at open questions; this mode records the decisions that answer them.

## Inputs of the mode

- The submitted scoping (required): the document that was put to the decision-maker, with its blocking questions and the default answer it proposed for each.
- The answers given at the pause (required): what the decision-maker said, in their own words when available.
- The original request (optional) and the sources the submitted scoping cites (optional): used only to check a fact, never to reopen a decision.
- A reference grid (optional): the rules the closed scoping will be judged by. When one is given, write to hold it: each rule has its section in the output.
- The splitting tests (optional): the tests to replay. Without them, use the four listed in the section « Splitting tests replayed ».

## Closing rules

1. **An answer from the pause prevails over the default of the submitted scoping.** It becomes a decision, and the decision cites it as its source — in the decision-maker's own words, between quotation marks, when they are available.
2. **A default accepted without an answer is marked as such.** Where the decision-maker made no remark on a default of the submitted scoping, the decision is kept with the source « default accepted » (the default, and the absence of any remark). Every such decision is listed again in a reminder addressed to the decision-maker at the end of the decisions section, because silence is not a yes: they may correct it, and a correction reopens whatever depends on it.
3. **A blocking question left without an answer becomes the residual question.** Write it as the residual question, with why it blocks or does not block the writing of a goal and of criteria. If it blocks, the scoping is not ready for the next step and says so. Every question left open, blocking or not, states why it blocks neither the goal nor the criteria; a decision marked « to confirm » on which the goal or the criteria depend is listed with what depends on it, and counts as open.

Beyond these three rules:
- Never invent a decision. Where the answers are silent and the submitted scoping has no default, say so and take the option that commits the least, marked « to confirm ».
- When an answer can be read in two ways, retain one reading, write it down with the alternative and the reason for the choice (see « Retained readings »), and apply it consistently.
- A constraint stays a constraint wherever it is filed, and stays in the constraints table. When the rationale is missing, or only restates the constraint (a quotation of the request or of the decision-maker is a source, not a rationale), write « imposed by <who>, no other reason given » with the decision cited, and list the missing rationale as a point to confirm. Never move a constraint to the decisions or to a list of things that are « not yet constraints » to avoid giving it a rationale.
- Every remaining assumption has its risk written (what happens if it is false) and exactly one of three marks, written in the language of the document with this wording. The word « accepted » is reserved for what the decision-maker accepted:
  - « accepted risk » — only for an assumption that the decision-maker accepted. Say where the acceptance comes from: an answer from the pause, quoted, or a default that was proposed at the pause and that they let pass.
  - « accepted by default, not raised at the pause — to confirm » — for an assumption the pause did not address, whether the answers are silent on it or the submitted scoping proposed no default for it. It is not an accepted risk.
  - « proposed by the writer — to confirm » — for an assumption you add while closing. It is not an accepted risk.

  A default that settles a decision does not accept the assumption behind that decision: « accepted risk » needs the pause to have put that very assumption, or its risk, to the decision-maker. Otherwise use the second mark.

  The last two marks are not accepted risks: they become accepted risks only when the decision-maker answers the reminder of rule 2 or lets it pass, and the trace says so. Each of them has its place in that reminder. Never write « accepted risk » on a row that carries one of them. An assumption described as open or pending anywhere in the text has its row in the table of remaining assumptions.
- A default that the pause rejected is never the source of a decision, and is never named as one. When an answer goes against a default, the decision cites the answer. When a decision keeps part of a rejected default, or draws on something the answers do not say, it is a reading of the writer: give it the source « reading of the writer — to confirm », state the reading, and add it to the reminder of rule 2.
- Direct consequences of a decision (a risk that falls away, a question that is answered) are listed as consequences, not as new decisions.

## Output sections

Write the closed scoping with these sections, in this order, using these words. Each section is non-empty, or says that it has nothing to report and why.

1. **Intention** — the goal, not the artefact. If the submitted scoping states the intention as something to produce, restate it as the result that must become true, and keep the artefact as a means.
2. **Audience and situation of use** — who uses, receives or validates the result, and in what situation. Describe them; do not only name them: what each does with the result, when, and with which means when they are not obvious (a validator: what they validate, at which moment, on what material). Every reader named in the deliverables table appears here. A reader whose name depends on an open point is still described by what they do with the result, so that the description never waits for the answer.
3. **Decisions** — a table: identifier, decision, source. Every decision names its source: an answer (quoted), a default accepted, an earlier decision, or a reading of the writer, to confirm. A default the pause rejected is never a source. Then the direct consequences, then the reminder of rule 2.
4. **Constraints, with their rationale** — a table: constraint, rationale, source. Every constraint is here, prohibitions included. The rationale says why the constraint holds; a constraint with none reads « imposed by <who>, no other reason given », with the decision cited.
5. **Scope** — what is in the scope, then what is **out of scope**, each exclusion concrete, with where it goes when it goes somewhere. What the subject allows (what may be built, bought, decided or reused) is written as items of the in-scope list; what it forbids is a constraint in section 4 and an exclusion in the out-of-scope list. Do not add a sub-heading or a list of what the subject permits and forbids, and no list of authorisations.
6. **Stakeholders** — each party, its role, the interest at stake; and whether any conflict of interest remains to be arbitrated.
7. **Deliverables** — a table: deliverable, reader, where it lives and why. Each deliverable has its reader. Documentation is a deliverable: list it with its reader. When the subject builds a system, a tool or software, add a deliverable for a specification and an architecture, with their reader; when it does not, say why it does not need them. This section never says which skill produces a deliverable: the format of each deliverable is passed on separately to whoever writes the goal.
8. **Remaining assumptions and accepted risks** — a table: assumption, risk (what happens if it is false), mark. The mark is one of the three of the closing rules, with its origin: for « accepted risk », the quoted answer or the default let pass; for the two others, the place in the reminder of rule 2. Only a row marked « accepted risk » is an accepted risk.
9. **Splitting tests replayed** — see below.
10. **Ready for the next step** — what the writer of the goal can take from the document (intention, deliverables with the reader of each, constraints and prohibitions, stopping condition, ceiling), and what the writer of the criteria can take. The format skill of each deliverable, the turn ceiling and the limits and models of sub-agents are not decided by the scoping: they come from the settings and from the list of format skills given to the goal writer. Say so, so that the writer does not have to ask. What the subject allows or forbids stays in sections 4 and 5: do not write a heading, a section or a list of authorisations for it, and do not present it as the authorisations of the goal. Say plainly whether the scoping is ready, and if not, what blocks.
11. **Retained readings** — each ambiguous point, the reading kept, the alternative, the reason.
12. **Residual question** — the question left open (rule 3), or « none ».

Also give, at the top, the inputs used and the priority rule applied: when an answer contradicts the submitted scoping, the answer prevails.

## Splitting tests replayed

Replay the tests on the closed scoping, one at a time, each with a verdict (true, false, partly true) and its reason. Unless the message gives others, the tests are:

1. parts can be accepted separately, each with its own users;
2. a single grid can no longer be replayed in about an hour of acceptance;
3. a part depends on a decision that has not been taken;
4. stakeholders have conflicting interests that must be arbitrated separately.

A test that is partly true is true for that part. If one test is true, the subject is split: name the parts and say which part starts now. The only exception is a decision of the decision-maker not to split, cited with its source (an answer to the pause, or a default let pass); the preference of the writer is not one. Without such a decision, split, or say that the decision is missing and make it a point to confirm. If a test was conditional in the submitted scoping, give its new verdict now that the answers are known.

## Constraints of the mode

- Do not reopen a decision of the pause, and do not re-weigh options the decision-maker already ruled on.
- Do not add a decision the answers do not support.
- Do not name a tool or a skill as the producer of a deliverable.
- Do not draw up a section or a list of authorisations of your own for the subject.
- Do not mark an assumption « accepted risk » unless the decision-maker accepted it.
- Do not decide on your own not to split when a test is true.
- Keep the user's own words for named terms, as in the default mode.

## Definition of done

- Every section above is present with its content, in this order.
- Every decision has a source; every default accepted is in the reminder.
- Every constraint has a rationale; every remaining assumption has its risk and one of the three marks, and only assumptions the decision-maker accepted are called accepted risks.
- No source is a default that the pause rejected, and there is no section of authorisations.
- Every deliverable has its reader, documentation included, and a specification and architecture line is present or its absence explained.
- The splitting tests were replayed, each with a verdict.
- The document says whether it is ready for the next step, and a goal and criteria can be written from it without a new question.
