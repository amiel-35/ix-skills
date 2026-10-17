---
id: cadrage
label: Cadrage
version: 1.3.0
description_fr: Clarifie un besoin encore flou avant toute production — intention, contraintes, hypothèses, options de suite — et vérifie qu'on a assez d'éléments pour avancer. Sépare le besoin des solutions déjà nommées dans la demande — le besoin reformulé dit le but, la solution nommée devient contrainte si justifiée, hypothèse à valider sinon. Déclenche sur "avant de se lancer, on doit cadrer ce sujet", "est-ce qu'on a assez d'infos pour partir en spec", "cadre ce besoin avant qu'on produise quoi que ce soit". Ne produit ni brief détaillé ni spec (utiliser `brief` une fois le cadrage fait) — s'arrête à la clarification. Un second mode, `close` (« clore »), se choisit par le message — il prend un cadrage soumis et les réponses données à la pause, et rend un cadrage clos — intention, décisions avec leur source, contraintes avec leur raison, périmètre, livrables avec leur lecteur, risques acceptés, tests de découpage rejoués. Sans mention de ce mode, le skill se comporte comme avant.
description_en: Clarifies a still-vague need before any production — intent, constraints, hypotheses, next options — and checks whether there is enough to move forward. Separates the need from the solutions already named in the request — the reformulated need states the goal, the named solution becomes a constraint when justified, a hypothesis to validate otherwise. Triggers on "before we start, we need to scope this", "do we have enough to go into spec", "clarify this need before we produce anything". Does not produce a detailed brief or a spec (use `brief` once scoped) — stops at clarification. A second mode, `close`, is chosen by the message — it takes a submitted scoping and the answers given at the pause, and returns a closed scoping — intent, decisions with their source, constraints with their rationale, scope, deliverables with their reader, accepted risks, splitting tests replayed. Without that mode in the message, the skill behaves as before.
icon: ◇
domain: cognitif
category: decision
input_types:
- brief
- markdown
- reference
- ticket
output_types:
- cadrage
- cadrage_clos
- questions_ouvertes
- options
compatible:
- claude-ai
- claude-code
- cowork
- gpt
- gemini
- mystaffy
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
- A constraint whose rationale is missing, or only restates the constraint, is not written in the constraints table: record it as a decision with its source, and list the missing rationale as a point to confirm.
- An assumption the pause did not raise is not accepted on the decision-maker's behalf in silence: mark it « accepted by default, not raised at the pause » and add it to the reminder of rule 2. An assumption added by the writer is marked « added by the writer, to confirm » and added to the same reminder.
- Direct consequences of a decision (a risk that falls away, a question that is answered) are listed as consequences, not as new decisions.

## Output sections

Write the closed scoping with these sections, in this order, using these words. Each section is non-empty, or says that it has nothing to report and why.

1. **Intention** — the goal, not the artefact. If the submitted scoping states the intention as something to produce, restate it as the result that must become true, and keep the artefact as a means.
2. **Audience and situation of use** — who uses, receives or validates the result, and in what situation. Describe them; do not only name them. Every reader named in the deliverables table appears here.
3. **Decisions** — a table: identifier, decision, source. Every decision names its source: an answer (quoted), a default accepted, or an earlier decision. Then the direct consequences, then the reminder of rule 2.
4. **Constraints, with their rationale** — a table: constraint, rationale. A constraint without a rationale is not a constraint yet: say what is missing.
5. **Scope** — what is in the scope, then what is **out of scope**, each exclusion concrete, with where it goes when it goes somewhere.
6. **Stakeholders** — each party, its role, the interest at stake; and whether any conflict of interest remains to be arbitrated.
7. **Deliverables** — a table: deliverable, reader, where it lives and why. Each deliverable has its reader. Documentation is a deliverable: list it with its reader. When the subject builds a system, a tool or software, add a deliverable for a specification and an architecture, with their reader; when it does not, say why it does not need them. This section never says which skill produces a deliverable: the format of each deliverable is passed on separately to whoever writes the goal.
8. **Remaining assumptions, as accepted risks** — a table: assumption, accepted risk (what happens if it is false, and that the risk is accepted).
9. **Splitting tests replayed** — see below.
10. **Ready for the next step** — what the writer of the goal can take from the document (intention, deliverables with the reader of each, constraints and prohibitions, authorisations, stopping condition, ceiling), and what the writer of the criteria can take. The format skill of each deliverable and the turn ceiling are not decided by the scoping: they come from the settings and from the list of format skills given to the goal writer. Say so, so that the writer does not have to ask. Say plainly whether the scoping is ready, and if not, what blocks.
11. **Retained readings** — each ambiguous point, the reading kept, the alternative, the reason.
12. **Residual question** — the question left open (rule 3), or « none ».

Also give, at the top, the inputs used and the priority rule applied: when an answer contradicts the submitted scoping, the answer prevails.

## Splitting tests replayed

Replay the tests on the closed scoping, one at a time, each with a verdict (true, false, partly true) and its reason. Unless the message gives others, the tests are:

1. parts can be accepted separately, each with its own users;
2. a single grid can no longer be replayed in about an hour of acceptance;
3. a part depends on a decision that has not been taken;
4. stakeholders have conflicting interests that must be arbitrated separately.

If one test is true, say whether the subject is split, into what, and which part starts now. If a test was conditional in the submitted scoping, give its new verdict now that the answers are known.

## Constraints of the mode

- Do not reopen a decision of the pause, and do not re-weigh options the decision-maker already ruled on.
- Do not add a decision the answers do not support.
- Do not name a tool or a skill as the producer of a deliverable.
- Keep the user's own words for named terms, as in the default mode.

## Definition of done

- Every section above is present with its content, in this order.
- Every decision has a source; every default accepted is in the reminder.
- Every constraint has a rationale; every remaining assumption is an accepted risk.
- Every deliverable has its reader, documentation included, and a specification and architecture line is present or its absence explained.
- The splitting tests were replayed, each with a verdict.
- The document says whether it is ready for the next step, and a goal and criteria can be written from it without a new question.
