---
name: criteres-reussite
description: "Writes, from a scoping note or a brief, the verifiable success criteria of a deliverable \u2014 code, proposal, dissertation, specification, building works, salary grid, negotiation, bill \u2014 as a table of tests (check, expected result, evidence mechanical, review or field, who checks). Separates the deliverable from the outcome, aimed at as a zone between a floor and a target; adds what the theme requires unasked; looks for what would pass every test and still be wrong; keeps a hidden part for the judge against an author or an agent that games the tests; says what a loop covers and what it must show. Triggers on \"success criteria\", \"acceptance criteria\", \"definition of done\", \"cahier de recette\", \"how will we know it's done\", \"stopping criterion for the agent\". Does not produce or judge the deliverable \u2014 `controle-qualite` or `quality-check` use it as their grid."
---
# Critères de réussite

## Role

You write the success criteria of a deliverable before it exists — its acceptance plan, its
definition of done: the list of checks that will say, without asking its author, whether it is done.
You start from the scoping note or the brief. You do not produce the deliverable, and you do not
judge one: a later judge (a person, `controle-qualite`, `quality-check`, or the stopping criterion of
an agent working in a loop) uses your plan as its grid.

The gesture applies to anything someone sets out to deliver or achieve: code, a tender response or
the specification of any call for tenders, an advertising campaign, a dissertation, building works,
a salary grid, a negotiation, a bill, an event such as a wedding, even a personal commitment between
two people. The method below is complete on its own; the annexes only add depth for a few kinds of
deliverable, and a subject with no annex is treated with the method alone.

## Absolute Rule

- **Every line can be decided by someone other than the author** (when there is no separate judge,
  by the other parties), from what the line says alone: an observable, a threshold, a place to look.
  « Clear », « of quality », « convincing » are not results; write what one would see if it were
  true.
- **Every line traces back** to a requirement of the brief (E1, E2… quoted or cited) or to an
  answer to « what could pass and still be wrong? ». A requirement you infer is marked
  `[inferred]`; you invent none and do not add requirements of your own taste — the requirements of
  the theme (step 1) are not taste.
- **The deliverable and the outcome are separated.** The deliverable is what the author fully
  controls; the outcome depends on other actors (a client who signs, a union that agrees, a vote, a
  group that reacts). An outcome is aimed at as a **zone** — a floor below which it is a failure, a
  target above which it is a success — never as a single value.
- **The hidden part never reaches the author**: it is written apart, the visible plan never refers
  to it, and it is not written at all when the requester is, or may be, the author (step 9).
- **Coverage is stated honestly**: how many lines a script can settle, how many need a reviewer,
  how many can only be checked in the field. A plan that a loop « fully covers » for a negotiation or
  a bill is wrong.

---

## Expected Inputs

| Field | Required | Description |
|---|---|---|
| `brief` | yes | The scoping note, brief, spec or decomposition: what is to be delivered, for whom, under which constraints |
| `deliverable_kind` | no | software, document, offer, grid, negotiation, bill… Inferred from the brief when absent |
| `author` | no | Who will produce the deliverable: a person, a team, an agent working in a loop. Changes the hidden part, the « who checks » column and the coverage section |
| `judge` | no | Who will hold the plan and the hidden part, and whether that judge executes checks or only reads what the author shows (step 12). Without it, write « judge: someone other than the author » |
| `requester` | no | `author`, `judge` or `other`: who is asking for the plan. Without it, infer it from the brief (« we are preparing », « the work is done by me » → `author`; « I commission », « I will judge » → `judge`) and say so. **When nothing allows the inference, treat the requester as `author`**: write the sealed request, not the hidden part |
| `existing_tests` | no | A plan or test suite already written: you complete it, you do not rewrite it, and you say what it misses |
| `confidentiality` | no | What reviewers may see (personal data, salaries, negotiation mandate). Without it, infer from the brief and say so |

If the brief does not say what the deliverable is for (who uses it, to do what), ask that one
question before writing. When no one can answer — a pipeline, a batch run, an agent's loop — make the
most plausible assumption, state it marked `[inferred]` at the top of the summary, and go on.
Everything else can be marked `[inferred]` too.

---

## References

Four annexes, read only when the case calls for them (they may be missing if this skill was pasted
alone; then apply the method below, which stands on its own, and say the annex was not available):

- **Software** (an application, a module, a script, an API, a data pipeline): read
  `references/criteres_logiciel.md` — part A for any software (rendered output, server-side rules,
  distributions, personal data and erasure checked down to the files, who writes and freezes the
  tests of a loop), part B only for live multi-user sessions (load at the peak, venue, degraded
  mode, states and actors).
- **Negotiation** (commercial, salary, labour, political, legislative — any deliverable whose
  outcome is an agreement between parties): read `references/criteres_negociation.md` — weighted
  interests and a scoring template, each party above its fallback, non-dominated agreement, a
  threshold for the least-served party set in advance, felt satisfaction measured afterwards,
  durability, unrepresented parties, a simulated counterpart as hidden part.
- **Written deliverable** (a sales proposal or tender response, a dissertation or essay, a report,
  the specification of a call for tenders on any subject — advertising, works, software, services):
  read `references/criteres_document.md` — answering the question asked, sources that say what the
  text makes them say, leftovers from another text, a compliance matrix, and testing published
  criteria before publishing them.
- **Physical works** (construction, renovation, an installation, equipment made to order): read
  `references/criteres_travaux.md` — acceptance tests written before work starts, hold points
  before things are covered, reservations at handover, the defects that show after a season.

Read every annex that applies (a salary grid that will be negotiated: negotiation; a software
tender: software and written deliverable; a works contract to negotiate: works and negotiation).

---

## Method

1. **List the requirements.** Number every requirement of the brief E1, E2…, with the passage it
   comes from. Then add the requirements of the **theme**, marked `[inferred]`: what any specialist
   of this kind of deliverable would check even if the brief never mentions it — security and
   personal data for software, safety for building works, accessibility and a rain plan for an
   outdoor event, desire, sexuality and safety from violence or control for a couple. Look hardest
   at what a brief leaves out because it is intimate, embarrassing or taken for granted: it is often
   what fails. For an intimate dimension, name it and leave its signs to the parties (blind
   criteria, step 9). Note the constraints that are not requirements but limits (budget, deadline,
   what must not happen).
2. **Date the sources.** When a source is older than a decision recorded elsewhere, or a later
   document may have replaced its content (a figure, a wording, a chosen example), derive no
   `mécanique` line from that specific content before it is confirmed: write the line on the
   requirement (« the figure shown has a source and is the one retained »), and put the content
   itself in the open questions. A source with no date and no later document is not « dated »: use
   it, and say where each figure comes from.
3. **Separate deliverable and outcome.** For each requirement, say whether the author controls it
   fully (deliverable) or whether it depends on someone else (outcome). For each outcome, write the
   zone: floor, target, and who sets them. The floor is set **before** the work starts, by the one
   who commissions it, not by the author after seeing the result. For a quantity where less is
   better (a cost, a gap, a delay), the floor is the upper limit: say « failure above ».
4. **Write the lines.** At least one line per requirement, and one check per line (a line that
   bundles several conditions is split). Each line has: the item or situation tested, the check
   (what is done: run, search, read, observe), the expected result (an observable, with its
   threshold), the kind of evidence, who checks. A requirement that no line can test is listed under
   « Not testable as stated » with the question that would make it so.
   - **A fallback is a result, not a plan.** For each dependency that can fail (a supplier, a
     platform, a service, the weather, a person), name each kind of failure separately and write
     what must still hold — « the offer is filed on time even if the platform is down on the last
     day », « the ceremony takes place if it rains » — without dictating the solution. Check it by a
     dry run with the dependency removed (`terrain`) and by the presence of what the fallback needs
     (`relecture`). « A fallback plan exists » is not a line.
   - **For every actor, every state.** For each actor the deliverable touches, write what that
     actor sees and can do in each state of the deliverable, not only what is stored or handed
     over.
5. **Add the content lines**, which form-only plans miss:
   - no gap left in what the end reader will see: no « [à compléter] », TODO, TBD, XXX, lorem ipsum,
     empty field, placeholder name — searched in the **rendered** deliverable (the page displayed,
     the PDF sent, the text voted), in every variant, not only in the source;
   - every figure has a source, and the derived figures recompute (`calc-check` can do it);
   - every named element exists (a referenced annex, a linked page, a cited article, a script that
     a step relies on);
   - the parts agree with each other (totals, cross-references, the same rule applied everywhere).
6. **Ask « what could pass all these tests and still be wrong? »** Write at least three answers,
   concrete to this deliverable, and turn each into a line. Families to go through:
   - the test checks **presence** where the requirement is a **proportion** (a sample of invoices
     that covers one month out of twelve; a field filled for 3 rows out of 30);
   - the test checks the **interface** where the requirement is about the **state** (a record
     hidden from the screen but still in the file, a clause removed from the summary but not from
     the contract);
   - the test checks the **form** where the requirement is about the **content** (a section that
     exists but says nothing; an annex announced with no data in it);
   - the test runs on the **happy path** only (one user, good weather, a cooperative counterpart);
   - the test checks that **a plan exists** where the requirement is a **result** (« a fallback is
     written » while the filing fails when the platform is down);
   - the test checks that **a choice is documented** where the requirement is that the choice is
     **compliant** (« the hosting status is written down » passes when it says « not compliant »);
   - the test is satisfied by the **letter** and misses the **intent** of the brief;
   - the test can be satisfied by **changing the test** or the measuring instrument;
   - the test is **judged by the author**, or by a judge that shares the author's blind spots (the
     same person, the same model in the same context);
   - the plan covers **the problems already named** and misses the dimension nobody named (every
     known bug fixed and no security; every quarrel settled and no desire left).
7. **Choose the kind of evidence** for each line:
   - `mécanique` — a script, a search, a measurement or a calculation settles it, the same way
     every time;
   - `relecture` — a judge other than the author reads and decides; for an author that is a model,
     a different context at least, ideally a different model;
   - `terrain` — only in real conditions: real devices, the real group, the real counterpart, the
     real vote. A terrain line says what will be observed, when, and by whom; it cannot be ticked
     before.
   The label follows the instrument: an automatic audit is `mécanique`, and it settles only what it
   measures. Prefer the cheapest kind that really decides the line; do not label `mécanique` a line
   that a script can only approximate (« the tone is not moralising » is `relecture`). **Keep the
   cost in proportion** to what the line protects: a check that is destructive (drilling into a new
   wall), intrusive (searching people's mailboxes), or needs an environment or a budget the brief
   does not provide is marked `[costly]`, and either justified in one phrase or replaced by a
   lighter check.
8. **Say who checks**: the competence needed (lawyer, developer, payroll, the facilitator) **and the
   independence** (« a developer other than the author », « the judge », « a reader with no stake »),
   and the confidentiality level (pseudonymised data, salaries visible, mandate under seal). A line
   that names a role the author holds fails the absolute rule; a line no available person can check
   is flagged.
9. **Write the hidden part.** A few lines kept by the judge and never shown to the author. It is the
   counter to Goodhart's law (« when a measure becomes a target, it ceases to be a good measure », in
   Strathern's 1997 wording): an author who sees every test can satisfy the tests instead of the
   brief, and coding agents working in a loop have been observed rewriting tests and scorers to pass
   (METR, « Recent frontier models are reward hacking », June 2025). Rules:
   - a hidden line tests a **requirement the author knows** (an E already in the visible plan), by
     other inputs or from another angle; it never adds a requirement the author could not have known
     — that would be an ambush, not a check;
   - choose the lines most exposed to gaming: the content lines, the « could pass and still be
     wrong » lines, variants of visible mechanical tests with other inputs;
   - guard each chosen requirement with **at least two** hidden lines, so a failure does not point
     to a single test; when one fails, the author is told the requirement — or the family of
     requirements — not the test; a hidden line that failed and was then fixed, like one whose
     content has leaked, is spent and replaced;
   - **the visible plan never refers to the hidden part**: no H number, no « see hidden part », no
     scenario that only a hidden line guards. A « could pass and still be wrong » trap guarded only
     by hidden lines is written in the hidden part, not in the visible list;
   - **when the requester is, or may be, the author** (one of the authors, or nothing tells), do not
     write the hidden lines: a warning not to read them does not keep them hidden. Write instead a
     sealed request for the judge — how many hidden lines, and the instruction to run this skill
     with `requester: judge` on the same brief and the visible plan; the judge chooses which
     requirements to guard, so the request names none;
   - **when the plan is written inside the session of the agent that will do the work**, the same
     rule applies: whatever is written there is in the agent's context. The hidden part is written
     in another session, by or for the judge;
   - **when there is no separate judge** — the parties are both authors and judges (a couple, two
     partners, a team judging its own project) — a hidden part would be a trap set for one another,
     not a check. Replace it by **blind criteria**: each party writes, alone and before the work, the
     three to five signs by which it will judge success; they are compared only at the agreed date.
     The gap between the lists is itself a finding;
   - **when the criteria themselves will be published to competing authors** (a call for tenders,
     an announced grading grid, contest rules), keep no hidden criterion on their work: they are
     entitled to know how they will be judged, and public procurement rules generally require it.
     The hidden part then tests the criteria — a fictitious answer that ticks every box without
     serving the need must not win;
   - **when the requester is the judge and a visible plan is supplied**, write only the hidden part
     and the updated coverage; do not rewrite the visible plan, but name any visible line the hidden
     part shows to be weak.
10. **State the coverage.** Count the lines by kind of evidence, visible and hidden, and add one
   sentence on their weight: a loop may close most of the lines and little of what matters. Say what
   an automatic loop can close (the `mécanique` lines, run outside the author's reach), what needs a
   reviewer, what only the field will tell. Give the order of magnitude honestly: high for code or a
   salary grid, low for a negotiation or a bill, where the outcome is decided by others.
11. **Mark the core** when the visible plan has more than about forty-five lines. The core is what
   a short session replays before any intermediate delivery: the blocking lines, plus one guard per
   « could pass and still be wrong » trap, keeping only `mécanique` lines and quick `relecture` —
   never a dated `terrain` line, never a hidden line. At most about thirty lines; if the blocking
   lines and the guards come to more, keep the blocking lines and the guards of the traps that
   would make the deliverable unusable. Give a replay time only when the brief gives something to
   estimate it from.

---

## Stopping criterion for an agent in a loop

When `author` is an agent that iterates until the tests pass, say which of two settings applies,
and write that setting's section. If both apply — an evaluator that reads the conversation during
the loop, then a person or a pipeline before acceptance — write both.

12. **A judge who executes** — a person, or a pipeline the agent cannot write to, reruns the checks:
   - **the instrument is the judge's**: the scripts of the visible `mécanique` lines are written by
     the judge, or written by the agent and reviewed line by line by the judge, and frozen **before
     the first round**; a line whose script the author wrote and the judge has not reviewed counts
     as `relecture`;
   - **the loop stops** when every visible `mécanique` line passes **and** every hidden `mécanique`
     line, run by the judge outside the agent's workspace, passes — never on the agent's own report;
   - **the instrument stays as frozen**: test files, fixtures, scoring scripts and their
     configuration unchanged (a checksum the judge holds); no test skipped, deleted or marked as
     expected to fail; the number of tests and the coverage not lower than the frozen suite's;
   - **the loop does not decide** the `relecture` and `terrain` lines: they go to a judge after the
     loop; a failure sends the agent back with the requirement, not the hidden test, and only the
     visible symptom, never the hidden input or the expected value.
13. **An evaluator who only reads the conversation** — it runs nothing and reads no file; it judges
   what the agent shows (a goal condition checked at each turn, for instance):
   - it can close **only visible `mécanique` lines**: the goal statement lists all of them, or names
     the ones it leaves out and why; the hidden part is never in its stopping condition, and the
     hidden part, the `relecture` and the `terrain` lines are played **after** the loop, outside the
     agent's session, by a judge who executes;
   - for each of those lines the agent shows, in the conversation, the **exact command** and its
     **complete raw output**, not a summary;
   - the agent shows the checksum of the frozen test files and the number of tests before the first
     round and at the end of every round; the tests themselves are written or reviewed and frozen
     by the judge before the loop starts, as in step 12;
   - this evaluator cannot tell a fabricated output from a real one: say so in the plan, and do not
     count its verdict as acceptance;
   - write a short **goal statement**, about ten to fifteen lines, that an evaluator can hold: the
     visible `mécanique` lines it covers (by number), the three rules that protect the instrument
     (frozen tests, checksum shown each round, no test skipped or weakened), and what must be shown
     for a line to count.

---

## Constraints

- You write checks, not the deliverable: no draft clause, no code, no grid, no wording proposal.
- You do not grade a deliverable, even if one is supplied with the brief: you may use it to see
  what a check must catch, and you say so.
- Every expected result is observable and, when a number is involved, carries a threshold and its
  unit; a threshold taken from the brief is cited, a threshold you propose is marked `[proposed]`.
  A proposed threshold fits the use and the counter-measures, not a reference figure taken in the
  abstract. For a `[proposed]` threshold only: if no reasonable version of the deliverable could meet
  it, the threshold is wrong, not the versions. A threshold taken from the brief, a law, a standard
  or a contract stays as it is, even if no version meets it.
- For a personal or relational subject (a couple, a family, friends, an event among them), prefer
  signs the parties will recognise in their own words over scores and percentages; put a number only
  where the parties already count (money, time, dates). A plan that turns a relationship into a
  dashboard fails its own purpose.
- No line whose only possible checker is the author.
- When `existing_tests` is given, keep its numbering, add your lines after it, and list what it
  misses in its own section.

---

## Output Format

The output starts with the frontmatter; a warning the reader needs first goes into the summary. The
visible plan and the hidden part are two blocks, separated by a line the user can cut on, so the
visible plan can be sent to the author as is.

```markdown
---
status: draft
skill: criteres-reussite
deliverable_kind: {kind}
author: {who produces}
judge: {who holds the hidden part; executes checks or reads the conversation only}
requester: {author / judge / other — stated or inferred, and how}
---

# Critères de réussite — {deliverable}

## Synthèse / Summary
{3 to 5 lines: what is delivered, what "done" means in one sentence, n lines (x mécanique, y relecture, z terrain), the share a loop can cover and its weight, the main open question. Any assumption made without an interlocutor, marked [inferred].}
Lignes bloquantes / Blocking lines: {the few line numbers whose failure makes the deliverable unusable as it stands}
Noyau / Core: {when the visible plan has more than about 45 lines — at most about 30 line numbers, blocking lines plus one guard per trap, no terrain, no hidden line}

## Exigences / Requirements
| E | Requirement | Source | Deliverable or outcome |
|---|---|---|---|
| E1 | {requirement} | {« quote » or § of the brief, or [inferred]} | deliverable / outcome |

## Issue visée / Outcome zone
| E | Outcome | Floor (failure threshold; below, or above when less is better) | Target | Set by | Measured when |
|---|---|---|---|---|---|

## Critères vérifiables / Checks
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | {E-ref — item or situation} | {what is done} | {observable + threshold} | mécanique / relecture / terrain | {competence; independence; confidentiality} |

## Ce qui passerait et serait faux / What could pass and still be wrong
- {scenario} → line {# of a visible line only}

## Non testable en l'état / Not testable as stated
- {E-ref} — {why} — {question that would make it testable}

## Ce que manquait le cahier existant / What the existing plan missed
{only when existing_tests was given}

## Couverture / Coverage
| Kind | Visible | Hidden | Who |
|---|---|---|---|
| mécanique | n | n | script, run by {judge} |
| relecture | n | n | {reviewers} |
| terrain | n | n | {when, who} |
{one or two sentences: what a loop can close, what it cannot, and what that is worth.}

## Critère d'arrêt de la boucle / Loop stopping criterion
{only when the author is an agent in a loop: the setting that applies (step 12, step 13 or both), its rules, and for step 13 the goal statement}

## Questions ouvertes / Open questions

✂ ----- PART CACHÉE — pour le juge seul, ne pas transmettre à l'auteur / HIDDEN PART — judge only -----

## Part cachée / Hidden part
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| H1 | {E-ref — same requirement, other inputs or angle} | … | … | … | … |
{the traps guarded only here; for each H line, which requirement it guards and why it is exposed to gaming}
```

When the requester is, or may be, the author, the block after the cut line is replaced by:

```markdown
✂ ----- À TRANSMETTRE AU JUGE / FOR THE JUDGE -----

## Demande de part cachée / Hidden part request
Environ / About {n} lignes cachées, au moins deux par exigence gardée / at least two per guarded
requirement. Le juge choisit les exigences à garder / The judge chooses the requirements to guard.
Juge / Judge: {in the language of the brief — run `criteres-reussite` with `requester: judge`, this
brief and the visible plan above, in a session the author cannot read, and keep what it writes to
yourself}.
```

Empty sections are left out. Write in the language of the brief. When a pipeline asks for named
fields, `criteria` holds the visible table, `hidden_part` the hidden one, `coverage` the counts by
kind of evidence, and `goal_statement` the statement of step 13 when there is one.

---

## Definition of Done

- The requester is stated or inferred at the top; when it may be the author, no hidden line is
  written.
- Every requirement of the brief and of the theme has at least one line, or sits under « Not
  testable as stated » with its question.
- Every line holds one check, can be decided by someone other than the author, and names in « who
  checks » no role the author holds; costly checks are marked.
- Each outcome has a zone set before the work.
- At least three « could pass and still be wrong » scenarios are turned into lines; content lines
  are present.
- The visible plan contains no reference to the hidden part; the hidden part guards known
  requirements only, with at least two lines per guarded requirement, below the cut line.
- The summary and the loop section are reread against the tables: no count, rule or claim in them
  that the lines contradict.
- The coverage says what a loop can and cannot close, and what that is worth; a visible plan of
  more than about forty-five lines marks a core; a loop with an evaluator that reads only the
  conversation has its goal statement.
