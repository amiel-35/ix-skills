# Changelog

Notable changes to the ix-skills corpus. Skills are versioned individually
(semver in each skill's frontmatter); entries are grouped by date. Format
inspired by [Keep a Changelog](https://keepachangelog.com).

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
