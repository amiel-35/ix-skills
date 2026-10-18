---
name: cadrage
description: "Clarifies a still-vague need before any production \u2014 intent, constraints, hypotheses, next options \u2014 and checks whether there is enough to move forward. Separates the need from the solutions already named in the request \u2014 the reformulated need states the goal, the named solution becomes a constraint when justified, a hypothesis to validate otherwise. Triggers on \"before we start, we need to scope this\", \"do we have enough to go into spec\", \"clarify this need before we produce anything\". Does not produce a detailed brief or a spec (use `brief` once scoped) \u2014 stops at clarification. A second mode, `close`, is chosen by the message \u2014 it takes a submitted scoping and the answers given at the pause, and returns a closed scoping \u2014 intent, decisions with their source, constraints with their rationale, scope, deliverables with their reader, remaining assumptions with their risk (accepted risk and its origin, or closing reminder), splitting tests replayed. Without that mode in the message, the skill behaves as before."
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
3. **A question left without an answer becomes a residual question.** Write it as a residual question, and say whether it blocks the writing of a goal and of criteria.
   - If it blocks the goal or the criteria of the part that starts now (the whole subject when it is not split), the scoping is not ready for the next step and says so; it does not claim that the question blocks nothing. A question that blocks only a part that does not start now says exactly that, names the part, and says that the goal and the criteria of the part that starts now are written without it.
   - If it blocks neither, say why it blocks neither, and check that no decision on which the goal or the criteria depend rests on it.
   - A decision on which the goal or the criteria depend never stays on an unanswered point: it is a blocking residual question, not a decision. Take the option that commits the least only for a point on which neither depends, and say so.

Beyond these three rules:
- Never invent a decision. Where the answers are silent and the submitted scoping has no default, say so, and apply rule 3.
- When an answer can be read in two ways, retain one reading, write it down with the alternative and the reason for the choice (see « Retained readings »), and apply it consistently.
- A constraint stays a constraint wherever it is filed (constraints, decisions, scope, prohibitions passed on to the goal), and every constraint has a rationale. Before writing section 4, go through every decision, every exclusion and every prohibition, and pick out each one that limits the answer (what must be done, not done or respected, including a default accepted); each is a row of the constraints table. A rationale says why the constraint holds, and it is one only if the request, the submitted scoping or the answers give it for this very constraint. A quotation that restates the constraint is a source, not a rationale. A reason you infer yourself is not a rationale either: offer it to the decision-maker inside the question, never write it as the rationale. A rationale covers the constraint only as far as it goes: when the reason given covers one part of what the constraint forbids or requires (some of the people, some of the places, some of the cases), the other part has no rationale. Do not apply a constraint more widely than the answers say; when you must, write the extension as a separate row whose rationale is missing, with its residual question. When no rationale is given, the constraint stays in the table, still applied as stated, its rationale cell says that none was given and points to a residual question, and that question asks the decision-maker why. It blocks neither the goal nor the criteria, since the constraint is written as stated and the answer would only add its reason; say so in the question. Never move a constraint to the decisions or to a list of things that are « not yet constraints » to avoid giving it a rationale, and never write « imposed by <who> » as if it were a rationale.
- Every remaining assumption has its risk written (what happens if it is false). A closed scoping holds no assumption « to confirm ». An assumption is in one of two cases:
  - **Accepted risk**: the assumption was put to the decision-maker at the pause. The row says so and gives its origin, one of: an answer of the decision-maker, quoted; a default proposed at the pause that they let pass; an assumption that the submitted scoping carried with its risk, that was before the decision-maker at the pause, and on which the answers record no objection (say which section of the submitted scoping, and what the answers say about it, silence or « not discussed » included, in their words). The mark is « accepted risk » (« accepted risks »), which may agree in gender and number with the word it qualifies.
  - **Raised at closing**: the assumption appeared while closing, and the pause could not see it (an assumption you add, or one that follows from an answer or from a reading). The decision-maker has not accepted it, and you do not accept it for them. Add one only if the goal or the criteria of the part that starts now cannot be written at all without it. A statement about how the solution will be built or run (a technique, a moment, a place, who does it) is never indispensable: it belongs to the specification and the architecture, and a criterion can be written on the behaviour expected, whatever the way it is obtained. Leave such a statement out, or put it as a residual question that blocks nothing. It has its row in the table, marked « pending the closing reminder — not an accepted risk », and its place in the **closing reminder** addressed to the decision-maker. The scoping states, in its title, at its top and under « Ready for the next step », that it is **not closed** as long as the closing reminder has no answer or has not been let pass; a scoping titled « closed » never holds a pending reminder. When there is no such assumption, say that the closing reminder is empty and that the scoping is closed. It becomes closed when the reminder is answered or let pass, and the trace says so.

  A default that settles a decision does not accept the assumption behind that decision: the assumption is an accepted risk only if the pause put that very assumption, or its risk, to the decision-maker. Otherwise it is raised at closing. Never write « accepted risk » on a row without its origin. An assumption described as open or pending anywhere in the text has its row in the table of remaining assumptions.
- A default that the pause rejected is never the source of a decision, and is never named as one. When an answer goes against a default, the decision cites the answer. When a decision keeps part of a rejected default, or draws on something the answers do not say, it is a reading of the writer: give it the source « reading of the writer, see Retained readings », state the reading there, and add it to the reminder of rule 2.
- Direct consequences of a decision (a risk that falls away, a question that is answered) are listed as consequences, not as new decisions.

## Output sections

Write the closed scoping with these sections, in this order, using these words. Each section is non-empty, or says that it has nothing to report and why.

1. **Intention** — the goal, not the artefact. If the submitted scoping states the intention as something to produce, restate it as the result that must become true, and keep the artefact as a means.
2. **Audience and situation of use** — who uses, receives or validates the result, and in what situation. Describe them; do not only name them: what each does with the result, when, and with which means when they are not obvious (a validator: what they validate, at which moment, on what material). Every person or group named anywhere in the document as a reader, a validator, someone who checks, hands over or takes over (deliverables, decisions, constraints, scope, stakeholders) appears here. Each validation or check has its own line: what is validated or checked, at which moment, on what material. A reader whose name depends on an open point is still described by what they do with the result, so that the description never waits for the answer.
3. **Decisions** — a table: identifier, decision, source. Every decision names its source: an answer (quoted), a default accepted, an earlier decision, or a reading of the writer. A default the pause rejected is never a source. Then the direct consequences, then the reminder of rule 2.
4. **Constraints, with their rationale** — a table: constraint, rationale, source. Every constraint is here, prohibitions included. The rationale says why the constraint holds (see the bullet on constraints above). A constraint whose rationale was not given reads « no rationale given — see residual question Q<n> », and the question exists in section 12.
5. **Scope** — what is in the scope, then what is **out of scope**, each exclusion concrete, with where it goes when it goes somewhere. What the subject allows (what may be built, bought, decided or reused) is written as items of the in-scope list; what it forbids is a constraint in section 4 and an exclusion in the out-of-scope list. Do not add a sub-heading or a list of what the subject permits and forbids, and no list of authorisations.
6. **Stakeholders** — each party, its role, the interest at stake; and whether any conflict of interest remains to be arbitrated.
7. **Deliverables** — a table: deliverable, reader, part (the part of the split it belongs to, or « whole » when the subject is not split), where it lives and why. Each deliverable has its reader. Documentation is a deliverable: list it with its reader. When the subject builds a system, a tool or software, add a deliverable for a specification and an architecture, with their reader; when it does not, say why it does not need them. This section never says which skill produces a deliverable: the format of each deliverable is passed on separately to whoever writes the goal.
8. **Remaining assumptions and accepted risks** — a table: assumption, risk (what happens if it is false), mark and origin. The mark is « accepted risk » with its origin (the quoted answer, the default let pass, or the section of the submitted scoping and what the answers say about it), or, for an assumption raised at closing, « pending the closing reminder — not an accepted risk » with its place in that reminder. Then the closing reminder itself, or the statement that it is empty.
9. **Splitting tests replayed** — see below.
10. **Ready for the next step** — what the writer of the goal can take from the document (intention, deliverables with the reader of each, constraints and prohibitions, stopping condition, ceiling), and what the writer of the criteria can take. The format skill of each deliverable, the turn ceiling and the limits and models of sub-agents are not decided by the scoping: they come from the settings and from the list of format skills given to the goal writer. Say so, so that the writer does not have to ask. What the subject allows or forbids stays in sections 4 and 5: do not write a heading, a section or a list of authorisations for it, and do not present it as the authorisations of the goal. When the subject is split, say which deliverables, constraints and prohibitions belong to the part that starts now, so that the goal of that part does not have to guess; the other parts are named and left out of it. Say plainly whether the scoping is ready, whether it is closed (see rule on assumptions raised at closing), and if not, what blocks.
11. **Retained readings** — each ambiguous point, the reading kept, the alternative, the reason.
12. **Residual question** — each question left open (rule 3), one entry each, numbered Q1, Q2…, with whether it blocks and why or why not; or « none ».

Also give, at the top, the inputs used, the priority rule applied (when an answer contradicts the submitted scoping, the answer prevails), and the status of the scoping: closed, or not closed because the closing reminder is pending.

## Splitting tests replayed

Replay the tests on the closed scoping, one at a time, each with a verdict (true, false, partly true) and its reason. Unless the message gives others, the tests are:

1. parts can be accepted separately, each with its own users;
2. a single grid can no longer be replayed in about an hour of acceptance;
3. a part depends on a decision that has not been taken;
4. stakeholders have conflicting interests that must be arbitrated separately.

A test that is partly true is true for that part. If one test is true, the subject is split, without exception: name the parts and say which part starts now. A preference of the decision-maker not to split, or a clause of the submitted scoping that lets the split fall away, does not lift this: split, and record the preference as a residual question. If a test was conditional in the submitted scoping, give its new verdict now that the answers are known, and replay it on the answers, not on the condition. The verdicts must agree with the rest of the document: a conflict of interest that section 6 leaves unarbitrated makes test 4 true for that conflict; test 3 is true for every part whose goal or criteria wait on a question of section 12.

## Constraints of the mode

- Do not reopen a decision of the pause, and do not re-weigh options the decision-maker already ruled on.
- Do not add a decision the answers do not support.
- Do not name a tool or a skill as the producer of a deliverable.
- Do not draw up a section or a list of authorisations of your own for the subject.
- Do not mark an assumption « accepted risk » unless it was put to the decision-maker at the pause, and give its origin.
- Do not leave an assumption « to confirm » in a scoping that declares itself closed.
- Do not write a constraint without its rationale, and do not write « imposed by <who> » in its place.
- Do not decline to split when a test is true.
- Keep the user's own words for named terms, as in the default mode.

## Definition of done

- Every section above is present with its content, in this order.
- Every decision has a source; every default accepted is in the reminder.
- Every constraint, wherever it was filed, has a rationale given for it, or points to a residual question that asks for it.
- Every remaining assumption has its risk and either the mark « accepted risk » with its origin or its place in the closing reminder; a scoping that declares itself closed holds no assumption « to confirm » and no unanswered reminder.
- No source is a default that the pause rejected, and there is no section of authorisations.
- Every person named as a reader, validator or checker is described in section 2.
- Every deliverable has its reader and its part, documentation included, and a specification and architecture line is present or its absence explained.
- The splitting tests were replayed, each with a verdict, every true test split the subject, and the verdicts agree with sections 6, 8 and 12.
- Final check, done by going through the document, not from memory: each reader, validator or checker named in sections 3 to 7 has its line in section 2, each validation with its own object, moment and material; each decision or prohibition that limits the answer has its row in section 4; the title, the top and section 10 give the same status.
- The document says whether it is ready for the next step, and a goal and criteria can be written from it without a new question.
