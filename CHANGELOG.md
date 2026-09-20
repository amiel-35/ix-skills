# Changelog

Notable changes to the ix-skills corpus. Skills are versioned individually
(semver in each skill's frontmatter); entries are grouped by date. Format
inspired by [Keep a Changelog](https://keepachangelog.com).

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
