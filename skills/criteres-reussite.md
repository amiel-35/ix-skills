---
id: criteres-reussite
label: Critères de réussite
version: 1.0.0
description_fr: Écrit, depuis un cadrage ou un brief, les critères de réussite vérifiables d'un livrable — code, offre, dissertation, cahier des charges, travaux, grille de salaires, négociation, texte de loi — en tableau de tests (élément, vérification, attendu, preuve mécanique, relecture ou terrain, qui vérifie). Sépare le livrable de l'issue, qui dépend d'autres acteurs et se vise par une zone entre un plancher et un objectif, avec la satisfaction de chaque partie en négociation ; cherche ce qui passerait tous les tests en restant faux ; teste le contenu, pas seulement la forme ; garde une part cachée pour le juge contre l'auteur ou l'agent qui optimise les tests ; dit ce qu'une boucle automatique couvre. Déclenche sur "critères de réussite", "cahier de recette", "critères d'acceptation", "définition de fini", "comment saura-t-on que c'est fini", "critère d'arrêt pour l'agent", "qu'est-ce qu'un bon accord". Ne produit ni ne juge le livrable — `controle-qualite` ou `quality-check` s'en servent ensuite comme grille.
description_en: Writes, from a scoping note or a brief, the verifiable success criteria of any deliverable — code, proposal, dissertation, specification, building works, salary grid, negotiation, bill — as a table of tests (item, check, expected result, evidence mechanical, review or field, who checks). Separates the deliverable from the outcome, which depends on other actors and is aimed at as a zone between a floor and a target, each party's satisfaction included for a negotiation; looks for what would pass every test and still be wrong; tests content, not only form; keeps a hidden part for the judge against an author or an agent that games the tests; says how much an automatic loop covers. Triggers on "success criteria", "acceptance criteria", "acceptance plan", "definition of done", "cahier de recette", "how will we know it's done", "stopping criterion for the agent", "what is a good deal here". Does not produce the deliverable and does not judge it — `controle-qualite` or `quality-check` then use it as their grid.
aliases: [success-criteria, acceptance-criteria, definition-of-done, cahier-de-recette]
icon: ☑
domain: cognitif
category: production
input_types: [brief, cadrage, markdown, spec, decomposition, reference]
output_types: [criteres_reussite]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
references: [criteres_logiciel, criteres_negociation, criteres_document, criteres_travaux]
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
  by the other parties), from what the line says alone:
  an observable, a threshold, a place to look. « Clear », « of quality », « convincing » are not
  results; write what one would see if it were true.
- **Every line traces back** to a requirement of the brief (E1, E2… quoted or cited) or to an
  answer to « what could pass and still be wrong? ». A requirement you infer is marked
  `[inferred]`; you invent none and do not add requirements of your own taste — the requirements of
  the theme (step 1) are not taste.
- **The deliverable and the outcome are separated.** The deliverable is what the author fully
  controls; the outcome depends on other actors (a client who signs, a union that agrees, a vote, a
  group that reacts). An outcome is aimed at as a **zone** — a floor below which it is a failure, a
  target above which it is a success — never as a single value.
- **The hidden part is written apart** and marked as such: it never goes to the author — not even
  when the author is the one asking (see step 8).
- **Coverage is stated honestly**: how many lines a script can settle, how many need a reviewer,
  how many can only be checked in the field. A plan that a loop « fully covers » for a negotiation or
  a bill is wrong.

---

## Expected Inputs

| Field | Required | Description |
|---|---|---|
| `brief` | yes | The scoping note, brief, spec or decomposition: what is to be delivered, for whom, under which constraints |
| `deliverable_kind` | no | software, document, offer, grid, negotiation, bill… Inferred from the brief when absent |
| `author` | no | Who will produce the deliverable: a person, a team, an agent working in a loop. Changes the hidden part and the coverage section |
| `judge` | no | Who will hold the plan and the hidden part. Without it, write « judge: someone other than the author » |
| `requester` | no | `author`, `judge` or `other`: who is asking for the plan. Without it, infer from the brief (« we are preparing », « the work is done by me » → `author`) and say so |
| `existing_tests` | no | A plan or test suite already written: you complete it, you do not rewrite it, and you say what it misses |
| `confidentiality` | no | What reviewers may see (personal data, salaries, negotiation mandate). Without it, infer from the brief and say so |

If the brief does not say what the deliverable is for (who uses it, to do what), ask that one
question before writing; everything else can be marked `[inferred]`.

---

## References

Four annexes, read only when the case calls for them (they may be missing if this skill was pasted
alone; then apply the method below, which stands on its own, and say the annex was not available):

- **Software** (an application, a module, a script, a data pipeline): read
  `references/criteres_logiciel.md` — automatable tests, load, real devices, anonymity and erasure
  checked down to the files, and how to keep an agent in a loop from passing by gaming the tests.
- **Negotiation** (commercial, salary, labour, political, legislative — any deliverable whose
  outcome is an agreement between parties): read `references/criteres_negociation.md` — weighted
  interests and a scoring template, each party above its fallback, non-dominated agreement, a
  threshold for the least-served party set in advance, felt satisfaction measured afterwards,
  durability, unrepresented parties, a simulated counterpart as hidden part.
- **Written deliverable** (a sales proposal or tender response, a dissertation or essay, a report,
  the specification of a call for tenders on any subject — advertising, works, software, services): read `references/criteres_document.md` —
  answering the question asked, sources that say what the text makes them say, leftovers from
  another text, a compliance matrix, and testing published criteria before publishing them.
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
   criteria, step 8) rather than writing them yourself. Note the constraints that are not
   requirements but limits (budget, deadline, what must not happen).
2. **Separate deliverable and outcome.** For each requirement, say whether the author controls it
   fully (deliverable) or whether it depends on someone else (outcome). For each outcome, write the
   zone: floor, target, and who sets them. The floor is set **before** the work starts, by the one
   who commissions it, not by the author after seeing the result.
3. **Write the lines.** At least one line per requirement. Each line has: the item or situation
   tested, the check (what is done: run, search, read, observe), the expected result (an
   observable, with its threshold), the kind of evidence, who checks. A requirement that no line
   can test is listed under « Not testable as stated » with the question that would make it so.
4. **Add the content lines**, which form-only plans miss:
   - no gap left in what the end user will see: no « [à compléter] », TODO, TBD, XXX, lorem ipsum,
     empty field, placeholder name — searched in the **rendered** deliverable (the page displayed,
     the PDF sent, the text voted), in every variant, not only in the source;
   - every figure has a source, and the derived figures recompute (`calc-check` can do it);
   - every named element exists (a referenced annex, a linked page, a cited article, a script that
     a step relies on);
   - the parts agree with each other (totals, cross-references, the same rule applied everywhere).
5. **Ask « what could pass all these tests and still be wrong? »** Write at least three answers,
   concrete to this deliverable, and turn each into a line. Families to go through:
   - the test checks **presence** where the requirement is a **proportion** (a random draw that
     exists but is unbalanced; a field filled for 3 rows out of 30);
   - the test checks the **interface** where the requirement is about the **state** (a record
     hidden from the screen but still in the file, a clause removed from the summary but not from
     the contract);
   - the test checks the **form** where the requirement is about the **content** (a section that
     exists but says nothing; a debrief screen with no debrief text);
   - the test runs on the **happy path** only (one user, a good network, a cooperative counterpart);
   - the test is satisfied by the **letter** and misses the **intent** of the brief;
   - the test can be satisfied by **changing the test** or the measuring instrument;
   - the test is **judged by the author**, or by a judge that shares the author's blind spots (the
     same person, the same model in the same context);
   - the plan covers **the problems already named** and misses the dimension nobody named (every
     known bug fixed and no security; every quarrel settled and no desire left).
6. **Choose the kind of evidence** for each line:
   - `mécanique` — a script, a search or a calculation settles it, the same way every time;
   - `relecture` — a judge other than the author reads and decides; for an author that is a model,
     a different context at least, ideally a different model;
   - `terrain` — only in real conditions: real devices, the real group, the real counterpart, the
     real vote. A terrain line says what will be observed, when, and by whom; it cannot be ticked
     before.
   Prefer the cheapest kind that really decides the line; do not label `mécanique` a line that a
   script can only approximate (« the tone is not moralising » is `relecture`).
7. **Say who checks**: the competence needed (lawyer, developer, payroll, the facilitator) and the confidentiality level (pseudonymised data, salaries visible, mandate under
   seal). A line no available person can check is flagged.
8. **Write the hidden part.** A few lines — about one in five, at least three — kept by the judge
   and never shown to the author. It is the counter to Goodhart's law (« when a measure becomes a
   target, it ceases to be a good measure », in Strathern's 1997 wording): an author who sees every
   test can satisfy the tests instead of the brief, and coding agents working in a loop have been
   observed rewriting tests and scorers to pass (METR, « Recent frontier models are reward
   hacking », June 2025). Rules:
   - a hidden line tests a **requirement the author knows** (an E already in the visible plan), by
     other inputs or from another angle; it never adds a requirement the author could not have known
     — that would be an ambush, not a check;
   - choose the lines most exposed to gaming: the content lines, the « could pass and still be
     wrong » lines, variants of visible mechanical tests with other inputs;
   - when a hidden line fails, the author is told **which requirement** failed, not the test
     itself; a hidden test whose content has leaked is spent and must be replaced;
   - **when the requester is the author** (or one of the authors), do not write the hidden lines:
     a warning not to read them does not keep them hidden. Write instead a sealed request for the
     judge — the requirements to guard (E numbers only), how many lines, and the instruction to run
     this skill with `requester: judge` on the same brief and the visible plan. The judge then writes
     the hidden part alone;
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
9. **State the coverage.** Count the lines by kind of evidence, visible and hidden. Say what an
   automatic loop can close (the `mécanique` lines, run outside the author's reach), what needs a
   reviewer, what only the field will tell. Give the order of magnitude honestly: high for code or a
   salary grid, low for a negotiation or a bill, where the outcome is decided by others.

---

## Stopping criterion for an agent in a loop

When `author` is an agent that iterates until the tests pass, add a section that says:

- **the loop stops** when every visible `mécanique` line passes **and** every hidden `mécanique`
  line, run by the judge outside the agent's workspace, passes — never on the agent's own report;
- **the loop does not decide** the `relecture` and `terrain` lines: they go to a judge after the
  loop, and a failure sends the agent back with the requirement, not the hidden test;
- **the measuring instrument is protected**: the test files, fixtures, scoring scripts and their
  configuration are checked unchanged (a checksum the judge holds), no test is skipped or marked as
  expected to fail, coverage is not lowered;
- **what the agent gets on failure**: the requirement number and the visible symptom, never the
  hidden input or the expected value.

---

## Constraints

- You write checks, not the deliverable: no draft clause, no code, no grid, no wording proposal.
- You do not grade a deliverable, even if one is supplied with the brief: you may use it to see
  what a check must catch, and you say so.
- One line, one check: a line that bundles three conditions is split.
- Every expected result is observable and, when a number is involved, carries a threshold and its
  unit; a threshold taken from the brief is cited, a threshold you propose is marked `[proposed]`.
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
judge: {who holds the hidden part}
---

# Critères de réussite — {deliverable}

## Synthèse / Summary
{3 to 5 lines: what is delivered, what "done" means in one sentence, n lines (x mécanique, y relecture, z terrain), the share a loop can cover, the main open question.}
Lignes bloquantes / Blocking lines: {the few line numbers whose failure makes the deliverable unusable as it stands}

## Exigences / Requirements
| E | Requirement | Source | Deliverable or outcome |
|---|---|---|---|
| E1 | {requirement} | {« quote » or § of the brief, or [inferred]} | deliverable / outcome |

## Issue visée / Outcome zone
| E | Outcome | Floor (failure below) | Target (success above) | Set by | Measured when |
|---|---|---|---|---|---|

## Critères vérifiables / Checks
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | {E-ref — item or situation} | {what is done} | {observable + threshold} | mécanique / relecture / terrain | {competence; confidentiality} |

## Ce qui passerait et serait faux / What could pass and still be wrong
- {scenario} → line {#}

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
{one or two sentences: what a loop can close, what it cannot.}

## Critère d'arrêt de la boucle / Loop stopping criterion
{only when the author is an agent in a loop}

## Questions ouvertes / Open questions

✂ ----- PART CACHÉE — pour le juge seul, ne pas transmettre à l'auteur / HIDDEN PART — judge only -----

## Part cachée / Hidden part
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| H1 | {E-ref — same requirement, other inputs or angle} | … | … | … | … |
{for each H line: which visible line or requirement it guards, and why it is exposed to gaming}
```

When the requester is the author, the block after the cut line is replaced by:

```markdown
✂ ----- À TRANSMETTRE AU JUGE / FOR THE JUDGE -----

## Demande de part cachée / Hidden part request
Exigences à garder / Requirements to guard: {E numbers}. Environ / About {n} lignes, au moins une par
exigence / at least one per requirement.
Juge / Judge: {in the language of the brief — run `criteres-reussite` with `requester: judge`, this
brief and the visible plan above, and keep what it writes to yourself}.
```

Empty sections are left out. Write in the language of the brief. When a pipeline asks for named
fields, `criteria` holds the visible table, `hidden_part` the hidden one, and `coverage` the
counts by kind of evidence.

---

## Definition of Done

Every requirement of the brief has at least one line, or sits under « Not testable as stated » with
its question. Every line can be decided by someone other than the author. Each outcome has a zone
set before the work. At least three « could pass and still be wrong » scenarios are turned into
lines. Content lines are present. The hidden part guards known requirements only, is cut off from
the visible plan, and is never written for a requester who is the author. The coverage says what a loop can and cannot close.
