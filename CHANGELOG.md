# Changelog

Notable changes to the ix-skills corpus. Skills are versioned individually
(semver in each skill's frontmatter); entries are grouped by date. Format
inspired by [Keep a Changelog](https://keepachangelog.com).

## 2026-10-19 — goal-writing 1.1.0: hard length limit and split signal

- `goal-writing` 1.1.0: the goal holds in 1,200 words at most — a hard limit.
  Details that the core only points to (interfaces, contracts, long lists of
  paths, detailed conduct) go into an annex of the goal, a separate document the
  goal names and the agent reads. The writer measures the core; above the limit
  it does not compress but returns « to split », with the word count and a
  proposed split of the closed scoping by groups of deliverables, which goes
  back to the scoping. A correction after review goes into the annex unless it
  changes what the agent must do. Learnt from a passage where the goal grew to
  9,000 words and the subject should have been split.

## 2026-10-17 — plugin 4.3.0: cadrage `close` mode, goal-writing

- `cadrage` 1.3.0: a second mode, `close`, chosen by the message. It takes a
  submitted scoping and the answers given at the pause and returns a closed
  scoping — intent, audience and situation of use, decisions with their source,
  constraints with their rationale, scope and out of scope, stakeholders,
  deliverables with their reader and documentation (a specification and an
  architecture when the subject builds a system), remaining assumptions as
  accepted risks, splitting tests replayed, ready for the next step, retained
  readings, residual question. Three closing rules are written in the body: an
  answer from the pause prevails over the default and is cited as the source of
  the decision; a default accepted without an answer is marked and recalled; a
  blocking question left without an answer becomes the residual question.
  Without that mode in the message, the method and the output format are those
  of 1.2.2, unchanged. `cadrage.mystaffy.json` gains an optional `mode` param.
- `cadrage` 1.3.1: in mode `close`, remaining assumptions carry exactly one of
  three marks — accepted risk (only what the decision-maker accepted, with its
  origin), accepted by default and not raised at the pause (to confirm), or
  proposed by the writer (to confirm) — the last two being recalled to the
  decision-maker and not accepted risks. A default rejected at the pause is
  never cited as the source of a decision. The closed scoping no longer draws up
  a list of authorisations: what the subject allows or forbids stays under scope
  and constraints. Default mode unchanged.
- `cadrage` 1.3.2: in mode `close`, a constraint without rationale stays in the
  constraints table as « imposed by <who>, no other reason given » with the
  decision cited; the scope carries what the subject allows as in-scope items,
  with no permits and forbids sub-list; a default that settles a decision does
  not accept the assumption behind it; a true splitting test splits unless the
  decision-maker decided otherwise, cited; validators and readers are described
  by what they do, when and with which means.
- `cadrage` 1.3.3: in mode `close`, every constraint, wherever filed
  (decisions and prohibitions included), has a rationale given for it; one
  without becomes a residual question that asks why, never « imposed by <who> ».
  A closed scoping holds no assumption « to confirm »: assumptions the submitted
  scoping carried with their risk are accepted risks with their origin, those
  raised while closing go to a closing reminder and the scoping is not closed
  until it is answered. A true splitting test splits, without exception. Every
  reader, validator or checker named anywhere is described in the audience
  section; deliverables carry their part. Rule 3 no longer contradicts itself
  (a blocking question is declared blocking, for the part that starts now). A
  statement about how the solution is built is never an assumption raised at
  closing; a rationale covers a constraint only as far as it goes; the
  splitting verdicts must agree with the stakeholders, assumptions and
  residual questions. Default mode unchanged.
- `goal-writing` 1.0.0 (new): writes the goal of an autonomous agent from a
  closed scoping and settings — intent, deliverables each with its format skill
  received as an input, constraints and prohibitions, authorisations, a stopping
  condition that points to an acceptance script without knowing its content, a
  turn ceiling, named slots for values fixed later. Describes the content of a
  goal, not any tool's command.

## 2026-10-16 — plugin 4.2.0: calc-check

- `calc-check` 1.0.0 (new): recomputes every derived figure of a text
  (variance, rate, ratio, total, NRR, ROI, projection) from the source's values,
  operations written out, one verdict per figure — exact, discrepancy, not
  recomputable, inconsistent — with the cause of each discrepancy and the
  figures it contaminates. A value missing from the source is never guessed.
  Specified in ix-recipes `docs/atome-verification-calcul.md`.
- `fact-check` 1.0.1: a figure derived from source values is marked « derived —
  recompute with `calc-check` » instead of passing for an invented one.
- `quality-check` 1.1.1: description points to `calc-check` for calculations.
- `build.py` (shared with ix-recipes): `ix-skills:calc-check` joins
  `VERIFICATION_SKILLS`, the steps allowed to reread the source.

## 2026-10-14 — build.py: workflow validation

`build.py` (shared with ix-recipes) now checks the `workflow` block of workflow
recipes: required skills exist (here or in the sibling repo), only the first
step receives the raw input, every received field is transmitted by an earlier
step. No skill changed.

## 2026-10-14 — plugin 4.1.0: references read on demand

`build.py` copies the files a skill lists in `references` from `partials/`
into `dist/skills/<id>/references/`; the skill reads only the one it needs.

- `prioritize` 1.2.0: one reference per framework — ICE, RICE, WSJF (new),
  MoSCoW, Kano (new), Eisenhower, Value vs Effort, weighted scoring (replaces
  "custom") — with scales, exact formula, procedure, pitfalls and output
  columns. The skill picks the framework, then reads only its file. Tested
  headless: a WSJF request read `framework_wsjf.md` and nothing else.
- `deliver` 1.2.0: the HTML guidance and the recipient profiles lost in the
  migration from ix-memory come back as references (`deliver_html`,
  `deliver_html_dashboard`, `deliver_recipient_profiles`), read only when the
  target format is HTML or a recipient is given.
- `critique` 2.1.0: the content-type → lens table comes back as
  `critique_lenses`.

## 2026-10-14 — third-party credits

`THIRD_PARTY.md` added from a skill-by-skill provenance check: Ole Lehmann's
"LLM Council" (after Andrej Karpathy's llm-council) for `contrarian`,
`firstprinciples`, `expansionist`, `outsider`, `executor`, `chairman`;
obra/superpowers (MIT) for `cadrage` and `revue-feedback`; Anthropic
knowledge-work-plugins for `prioritize`. README: Credits section, and the
advisory category now names where its roles come from. No skill changed.

`build.py` and `scripts/install-codex.sh` gain the `references` mechanism
added in ix-recipes (partials copied next to SKILL.md, read on demand);
unused in ix-skills today, kept identical across both copies.

## 2026-10-14 — plugin 4.0.0

### Removed — domain skills moved to ix-recipes (breaking)

48 skills now live in [ix-recipes](https://github.com/amiel-35/ix-recipes), with
their git history: HR, legal, finance and pricing, sales and procurement,
product, tech, data, plus `note-strategique` and `offer-comparison`, which
ix-recipes will rewrite as workflows chaining ix-skills atoms. To keep them:

```bash
claude plugin marketplace add amiel-35/ix-recipes
claude plugin install ix-recipes@ix-recipes
```

Placement rule: a skill that applies a reasoning move to any content stays in
ix-skills; a skill that relies on domain knowledge that can go stale, or
produces an artefact a profession defines, goes to ix-recipes. ix-recipes
depends on ix-skills, never the other way round.

### Removed — three skills dropped

- `stakeholder-comms`: `deliver` already adapts a deliverable to its `recipient`.
- `data-storytelling`: nothing referenced it; its one specific rule (answer
  « RAS » when the data supports no insight) is the corpus null output.
- `retrospective`: a generic five-step method; finding the root cause is
  better done with `ach`, then `correction` for the actions.

### Changed

- `analysis` 1.1.1, `brief` 1.2.2, `cadrage` 1.2.2: `domain` moves from `ops`
  to `cognitif` (same mystaffy métier, `transverse`); pointers to
  `product-spec` and `note-strategique` removed.
- `indicateurs` 1.2.1, `outside-in` 1.1.1, `research` 1.1.1: pointers to
  `tableau-de-bord-kpi` and `analyse-concurrentielle` removed — an ix-skills
  atom never points to a skill the user may not have installed.
- README: 35 skills in 4 categories; new « Cadrage & production » category
  (`cadrage`, `brief`, `analysis`, `compte-rendu`); sibling projects section.

## 2026-10-06

### Added — `fact-check` 1.0.0: a text against evidence, claim by claim

One verdict per atomic claim — `confirmed`, `contradicted`, `not in the
source`, `not checkable` — each confirmed or contradicted verdict backed by a
verbatim quote a script can find in the source. The source is an input:
`closed` mode (default) ignores what the model knows, `open` mode admits
external sources only with a quotable passage and its URL. A claim of absence
is checked by searching the whole source and is proved by the search itself
(terms, sections, closest passage), not by a quote. Ids of the input text are
kept (F3 → F3.1, F3.2 when one item carries several claims). Optional final
JSON block. A claim that the source *gives* X is confirmed only if X itself is
there: a mention without content (« aux horaires d'ouverture ») contradicts
it. A quote is one continuous passage of the source as provided — markup,
apostrophes and quotation marks kept, never two passages joined (same rule for
`controle-qualite` passages). Born from the crawler-conseil-mononcle chain, where a critique
claimed to have observed things a page did not contain and corrections added
facts the page did not state.

### Added — `controle-qualite` 1.0.0: a deliverable against a set of rules, sweep or verdict

One verdict per finding, with the rule and the exact passage. The reference
is provided; a rule it names applies in full, a rule it does not name is at
most a remark set apart. `sweep` finds every breach and lists the rules
passed; `verdict` rules on a suspected list — `breach`, `compliant`,
`doubtful`, `not found`, `outside reference` — keeping its ids, so a cheap
detector and a judge can run on the same reference. Optional final JSON
block. Same origin: the spelling bench of the project and the report checked
against its template and forbidden vocabulary before it goes to the client.

Both validated on the CD56 bench (page « Les aides financières après 20
ans » and « Aide ménagère à domicile », collected 2026-10-05): with Sonnet,
false and added claims caught, true ones confirmed, every quote found by
script; 11/14 against the judged spelling reference, no false breach. Haiku
gets the verdicts mostly right but still rewrites apostrophes and joins
passages: usable only behind a quote check.

### Changed — plugin manifest 3.3.0

Two new skills consumers are meant to receive. `quality-check` keeps its name
for now; its rename to `fiabilite-sources` and the cross-references from
`critique`, `revue-feedback` and `quality-check` to the two new skills come
separately.

## 2026-09-21 — patch 2

### Fixed — `questioning` 1.0.1: a stated goal is not a rationale, an obligation is a constraint

Same two rules as `brief` and `cadrage` 1.2.0, for consistency across the
corpus: a rationale justifies a named term only when it says why this term
rather than another way to reach the goal, and a deadline, budget, mandated
vehicle or required deliverable stated as an obligation is a constraint,
asked about if useful, never `[blocking]`. Control on the pension brief
without the electoral sentence, sonnet: « ramener l'âge légal » and its
sizing « 62 ans » `[blocking]`, financing levers questioned without it, the
six-week deadline and the bill no longer listed as named solutions.

### Changed — plugin manifest 3.2.2

## 2026-09-21 — patch

### Fixed — `brief` 1.2.1, `cadrage` 1.2.1: the vehicle a consultation names is never a constraint on the need

On the FN Safer N1 RFP, `cadrage` had classified « formation » as a
justified constraint because it is the object of the consultation, and the
whole chain downstream produced four ways of running a training. What a
consultation or a mandate imposes on the response — pieces to include,
deliverables, format, deadline — is now listed apart as constraints on the
response. It never justifies the named vehicle as the answer to the need:
that vehicle stays a hypothesis, even when the answer has to be written
inside it. Same RFP, after: « formation » is a hypothesis with its open
question (weighed against mentoring, coaching, templates, a community of
practice?), the RFP's deliverables are constraints on the response.

### Changed — `explorer` 1.1.1: `breadth` decides what happens to the named vehicle

`focused` and `standard` keep the vehicle named in the input as a
constraint of the response — the base answer to an RFP. `broad` takes it
as the default answer to set aside and carries one positive constraint per
execution; the deliverables listed as constraints on the response stay
covered. A `cadrage` or `brief` can be passed as is: its hypotheses are the
named solutions. Tested on the N1 RFP, sonnet: `standard` gives four
training designs, `broad` with « practices change on the seven people's
real projects, while they run them » gives a case clinic, a threaded
mentoring, an instrumentation sprint and a periodic intervision circle —
the « mission » the fnsafer project kept as a light opening.

### Changed — plugin manifest 3.2.1

## 2026-09-21

### Changed — `brief` 1.2.0 and `cadrage` 1.2.0: a named solution is never promoted to the intent

The « named solution » guard of `questioning` 1.0.0, adapted to the two
skills that write a framing. The intent (`brief`) or the reformulated need
(`cadrage`) states the goal as the request states it. Every term that names
an artefact, implementation, format, figure or reference — umbrella term
first, then sizing parameters, then sub-artefacts — goes to constraints with
its quoted rationale when the input says why this means rather than another,
or to hypotheses « taken as the chosen answer to <its own purpose> — to
validate » when it does not. A sentence that states the goal or the
injustice the term answers is not a rationale for the term. A deadline, a
budget, a mandated vehicle or a required deliverable stated as an obligation
is a constraint. The term is kept in the user's words, never stripped, no
alternative proposed. `cadrage` adds one open question per such hypothesis.

Before: on « ramener l'âge de la retraite à 62 ans parce que la réforme est
injuste pour les carrières longues », `brief` wrote « 62 ans » as the intent.
After: the intent is the injustice to correct, « 62 ans » is a hypothesis —
and becomes a constraint only when the request adds « c'est l'engagement
numéro un de notre programme », which does justify the figure itself.
Validated on call center, listed-building retrofit and pension briefs, and
on the FN Safer N1 RFP chained `cadrage` → `questioning` → `explorer`.

### Changed — plugin manifest 3.2.0

Two skill releases consumers are meant to receive.

### Added — TODO.md

Design-thinking method chains as pipeline prompts, to build after this.

## 2026-09-20

### Added — `questioning` 1.0.0 out of DRAFT: the « Named solution » category

A request that names its artefact (« a compass rose », « an ITE », « a
training », « AI ») has already taken a decision without noticing. The skill
now scans the input in a fixed order — the umbrella term that frames the
whole request, then its sizing parameters (duration, quantity, format,
deadline), then the sub-artefacts — and asks, for each, what it is meant to
achieve and whether it was chosen against something or was the first thing
to come to mind. Flag-and-ask, never a filter: the term is kept as the
user's own word, a rationale found anywhere in the input is quoted and
withholds `[blocking]`, no alternative is ever named (that is `explorer`'s
job), the problem is never reformulated (that is `firstprinciples`'s job).
`[blocking]` is reserved for the umbrella and for parameters whose change
would alter the shape of the response, three items at most.

Validated on eleven briefs (design, energy retrofit, vaccination, call
center, municipal security, pension reform, two real training RFPs) across
haiku, sonnet, opus, GPT-6 and Gemini 3.1 Pro, twenty-six runs, two opus
juries. Every model found the umbrella; the six text corrections came from
the juries, not from switching models. Source of the mechanism:
Bike-routing/docs/briefer_une_ia_pour_du_design.md.

### Changed — `explorer` 1.1.0: write the default answer, then set it aside

Before generating options, the skill writes the first, obvious answer it
would give and excludes it from the set — visibly, in its own output block,
so the absolute rule « never eliminate an option without mentioning it »
still holds. A usage note states that when `nb_options` is high or
distinctness matters, each option is better produced as a separate
execution with one positive constraint of its own, rather than a one-pass
enumeration that anchors on the first idea; prohibitions redirect, they do
not free. On the pension-funding brief, the whole « time of life » axis was
absent from a one-pass run of eight options and came out entire from a
constrained execution.

### Changed — plugin manifest 3.1.0

Two skill releases consumers are meant to receive.

## 2026-09-15

### Fixed — plugin manifest version had never been bumped

`dist/.claude-plugin/plugin.json` still declared 2.1.0, written once on
2026-08-02 and never touched since. Plugin updates are resolved by that
version, not by content — so `claude plugin marketplace update` followed by
`claude plugin update` reported "already at the latest version" and installed
nothing. Three releases had shipped invisibly this way: the 2026-08-27
null-output batch, `okr` 2.0.0, and the description pass below. Manifest
bumped to **3.0.0** — the bundle now carries two narrowed invocation
contracts since 2.1.0 (`okr` and `critique`), which is breaking for anyone
relying on the old routing. The manifest is hand-maintained (`build.py`
validates it but never writes it), so it has to be bumped deliberately
alongside any release consumers are meant to receive.

### Changed — corpus-wide description pass (74 skills)

The `okr` 2.0.0 diagnosis, generalized. A skill's description is the only
surface an agent matches against when deciding whether to invoke it: a
description with no explicit trigger phrase never fires, and a description
that claims another skill's trigger phrases silently cannibalizes it. Both
defects were present across most of the corpus.

- **72 of 84 skills had no quoted trigger phrase.** All of them now follow
  the pattern already proven by `decision`, `explorer` and `prioritize` —
  role in one sentence, then « Déclenche sur … » with 3 to 5 real user
  phrasings in quotes, then an explicit negation of what the skill does not
  do, with a backtick pointer to the sibling that does. Both languages.
  Bodies are untouched: behaviour is identical, only the invocation surface
  changed. Minor bump for each.
- **The `critique` family was cannibalizing itself.** `critique` listed
  « joue l'avocat du diable », « dixième homme » and « red team » among its
  own triggers — the proper trigger phrases of three sibling skills, which
  therefore had no realistic path to being invoked. Scope removed from
  `critique` (major bump, 2.0.0: an invocation contract narrowed, not a
  description enriched); `dixieme-homme`, `red-team` and `contrarian` each
  given a distinct, explicitly bounded territory — the full opposing thesis,
  the adversary's perspective, and the single breaking point with its
  unverified assumptions.
- **Two further overlaps caught by an independent cross-corpus audit**, one
  of them introduced during this very pass: `contrarian` had taken over
  `key-assumptions`' characteristic phrasing, and `compliance-checklist`
  claimed GDPR as its own trigger against `conformite-rgpd`. Both corrected,
  with reciprocal pointers.
- **Eight skills assumed to be fine were not.** `analysis`, `decomposer`,
  `research`, `compliance-checklist`, `negotiation-brief`, `offer-comparison`,
  `strategie-prix` and `tech-debt` carried no trigger phrase at all; the
  `analysis` / `decomposer` pair additionally overlapped head-on. Fixed in
  the same pass.
- `okr` 2.1.0 — trigger phrases were described but never quoted; four added,
  nothing removed.

### Fixed — README contradictions surfaced by the pass

Nine statements in `README.md` / `README-fr.md` contradicted the skill they
described. All pre-existing, all corrected: `simplify` (documented as
performing removals it explicitly does not perform), `research` (`flash` mode
contradicts "sources required"), `decomposer` ("no shared dependencies" — the
skill identifies them), `legal-risk-flag` (severity scale), `code-review`
("only reports high-priority issues" — it ranks and surfaces both tiers),
`prd` / `product-spec` (two mutually exclusive hierarchies in one file),
`negotiation-brief` (scope broader in the doc than in the skill), and the
`contrarian` section, which attributed the *advocatus diaboli* request
phrasing to itself rather than to `dixieme-homme`.

### Verification

Trigger discrimination tested on six boundaries judged most at risk, each by
an independent agent with a clean context, given the 84 final descriptions
and two near-miss phrasings without being told which skill was under test:
12/12 routed to the intended skill, all at high confidence — including the
original bug (« joue l'avocat du diable » now reaching `dixieme-homme`, not
`critique`) and the audit's two catches.

### Changed — `okr` 2.0.0 (breaking: behaviour, not a fix)

Rewritten from a version validated in real use, not in review only: a
trigger test run by independent agents (4/4 on phrases that had to fire it,
2/2 on near-miss phrases that had to not — including "critique this action
plan", which belongs to `critique`), and a contre-check on an OKR already
written for a client, where the skill caught a KR that reproduced the
deadline/budget/scope triptych the client explicitly ruled out as a measure
of success — independently confirmed by a second run started from scratch
on the same need, which named the same trap without seeing the drafted OKR.

- **Major bump, not minor.** 1.0.2 produced a finished OKR from a brief in
  one pass. 2.0.0 never does, in either mode: the Objective is given or
  chosen by the person, the Key Results are discussed — never drafted by an
  agent then submitted for approval after the fact.
- **Two distinct modes.** *Template* reviews O/KR lines already written,
  line by line (formula conformity, task disguised as a KR, outcome or
  output, baseline sourced or missing, calibration profile) and never
  rewrites in the author's place. *Material to discuss* starts from a vague
  brief and produces candidate Objectives — each with what it excludes —
  plus families of Key Results with baseline, stretch, acceptable minimum,
  forcing mechanism and classic trap. The modes never merge.
- **Doctrine written into the body**, not referenced: the formula (O =
  action verb + what + intended impact, never a number; KR = measurement
  verb + what + from X to Y + deadline), the three calibration profiles
  (sandbagged / aspirational / stretch), and outcome > output — but a
  realistic sourced output over an invented or embellished outcome.
- **Absolute rule on baselines.** A missing X is declared « baseline
  missing — to be measured », never replaced by a plausible number.
- **Pushy description with explicit triggers** in both languages (objectif,
  résultat clé, KR, OKR, outcome/output, baseline manquante, sandbagged,
  aspirationnel, tâche déguisée en KR). 1.0.2 carried no trigger phrase at
  all and was never invoked automatically in a real session — the reason for
  this rewrite as much as the method was.
- `okr.mystaffy.json`: `mode` param added (auto / gabarit / materiau);
  `nb_kr_max` and `inclure_stretch` removed — both assumed a single finished
  output, and stretch calibration is now baseline doctrine rather than an
  option. `horizon` kept.

## 2026-08-27

### Corpus convention

- **Null output (« RAS — »)** documented in `README.md` and `README-fr.md`:
  a skill that has nothing to produce opens its response with the literal
  token « RAS — » followed by the reason, and stops. Greppable and testable
  across the whole corpus.

### Changed — null-output convention (audit correction #1, all minor bumps)

Skills phrased as searches always find something; three even mandated a
finding quota in their Definition of Done. Each skill below now names a
cheap null output bounded by its own scale, and search steps are reworded
as per-element tests where possible.

- `critique` 1.1.0 — per-lens test only: a lens with no flaw is reported
  as passed, never padded. Deliberately **no** document-level RAS:
  "resists every lens" is the reader's global judgment, not the critic's
  (validated by a before/after test on clean and defective control inputs).
- `legal-risk-flag` 1.1.0 — « RAS » when no signal reaches medium risk;
  clauses and absences tested one by one.
- `cgv-checker` 1.1.0 — « RAS » when no clause is unbalanced for the
  reading position; per-clause test.
- `key-assumptions` 1.1.0 — quota removed ("Critical assumptions are
  mandatory. Gaps are mandatory."); zero is a valid count, stated as « RAS ».
- `expansionist` 1.1.0 — "at least three opportunities" quota removed;
  as many as the subject carries, or « RAS ».
- `simplify` 2.1.0 — an empty removals table is a valid result (« RAS »
  names the level tested).
- `tech-debt` 1.1.0 — healthy verdict « RAS » when no item reaches the
  quarter threshold (score ≥ 15).
- `code-review` 1.1.0 — zero critical findings stated as « RAS —
  suggestions only », never inflated.
- `outsider` 1.1.0 — « RAS — this brief is self-contained » when nothing
  requires implicit context (perspective mode).
- `red-team` 1.1.0 — « RAS » when no credible opposing plan exists at
  these stakes; weak-signal and vindication sections now conditional on a
  plan being produced.
- `data-storytelling` 1.1.0 — « RAS » plus factual reading only when the
  data supports no robust narrative.
- `ach` 1.1.0 — explicit tie outcome when the available information does
  not discriminate between hypotheses.
- `indicateurs` 1.1.0 — "eight to twelve indicators" quota becomes "as
  many as the plan warrants, up to twelve" (no RAS: a monitoring request
  always warrants indicators).

`contrarian` deliberately untouched: forced dissent is the archetype's
contract, already fenced by the charitable reading, the confidence level,
and the self-invalidation section.

### Changed

- `dixieme-homme` 1.1.0 — recuses assignments that embed the consensus:
  names the trap in one line, then inverts the command's premise instead
  of obeying it.

## Earlier

Pre-changelog history: see `git log`.
