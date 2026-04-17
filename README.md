# ix-skills

Atomic knowledge-work skills — portable across Claude, GPT, Gemini, and mystaffy.

78 skills in 10 categories. Each skill encodes a **cognitive process**, not domain expertise.

[🇫🇷 Version française](README-fr.md)

---

## Available skills

### 🧠 Cognitive — core process atoms

Primitive operations on content, problems, and decisions. Each encodes a single cognitive move — they are designed to chain, not to replace each other.

| id | Role | Key constraint |
|---|---|---|
| `critique` | Identify flaws in content without proposing solutions | Analysis only — **does not fix** |
| `correction` | Turn a critique into actionable directives | Transforms a critique — **does not re-analyze** |
| `simplify` | Strip content to essentials without changing the meaning | Preserves all information — removes friction only |
| `rephrase` | Restate the real meaning of dense or ambiguous content | Reinterprets — meaning may shift, not just trimmed |
| `explorer` | Generate an option space without committing to a choice | Breadth — **does not choose** |
| `decision` | Arbitrate with visible trade-offs and a clear recommendation | Chooses among existing options — **does not generate** |
| `deliver` | Transform an artifact into a shareable deliverable | Formatting and audience calibration |
| `research` | Build a sourced factual foundation before any decision | Sources required — no unsupported claims |
| `synthese` | Condense long content into an actionable summary | Lossy compression — detail is intentionally discarded |
| `decomposer` | Break a complex problem into independent sub-problems | Sub-problems must be independent — no shared dependencies |
| `revue-feedback` | Evaluate feedback rigorously before accepting or rejecting it | Evaluates incoming critique — not your own artifact |

#### Key distinctions

**`critique` vs `revue-feedback`**
`critique` analyzes *your own artifact* (a document, a plan, a proposal) to find its flaws. `revue-feedback` processes *feedback someone else gave you* — evaluating whether to accept, nuance, or reject it before responding. One is editorial, the other is diplomatic.

**`simplify` vs `rephrase` vs `synthese`**
- `simplify` removes noise while keeping all the information — the result is shorter but complete.
- `rephrase` rewrites dense or ambiguous content to make the actual meaning legible — it reinterprets, not just trims.
- `synthese` deliberately loses detail to extract the essential — lossy compression that produces an actionable summary.

**`explorer` vs `decision`**
Designed to run in sequence. `explorer` maps the option space without committing (breadth first). `decision` arbitrates among existing options with explicit trade-offs and a recommendation (depth). Running `decision` without `explorer` risks locking in too early from an incomplete set.

**`critique` vs Advisory archetypes (e.g. `dixieme-homme`, `contrarian`)**
`critique` is a quality check on *your own artifact* — editorial, finding flaws in what you produced. Advisory archetypes challenge *a belief, plan, or decision* from a specific perspective — they operate at the level of reasoning and conviction, not text quality. Use `critique` to improve a document; use Advisory to stress-test a conclusion.

---

### ⚔️ Advisory — perspective archetypes

Each skill forces a specific cognitive stance. They are not interchangeable — pick based on what you need to stress-test. Run `chairman` after several to synthesize.

---

#### `contrarian` — Failure points & unverified assumptions

**Origin:** The *advocatus diaboli* (devil's advocate), formalized in Catholic canon law. The Church required a designated critic to argue against every proposed canonization to ensure rigor. Adopted in structured decision-making and intelligence analysis to institutionalize dissent.

**Objective:** Force confrontation with the most likely way your plan fails — before you commit.

**How it works:** Identifies the single strongest argument against your decision, surfaces the assumptions you haven't validated, and names the condition under which everything breaks. Deliberately one-sided toward failure, not a balanced review.

**Use when:** You have a plan you believe in and want to find its main vulnerability before presenting or executing it. Not the same as `dixieme-homme` (which builds a full opposing thesis) or `red-team` (which reasons as an external adversary).

---

#### `executor` — Does this hold up in reality?

**Origin:** The *pre-mortem* technique, developed by Gary Klein (1989). Rather than asking "what could go wrong?", you imagine the plan has already failed and work backwards to explain why.

**Objective:** Ground abstract plans in operational reality before execution begins.

**How it works:** Challenges whether the plan is actually executable — tests for missing resources, unrealistic timelines, hidden dependencies, and human factors that strategic thinking ignores. The perspective is that of someone who has to deliver the plan, not design it.

**Use when:** After a plan is formed but before execution starts. Especially useful for plans built by people who will not be the ones executing them.

---

#### `expansionist` — The missing upside

**Origin:** The *adjacent possible* concept from complexity theorist Stuart Kauffman — at any moment, the next possibilities are determined by what currently exists. Applied to strategy to reveal options you didn't consider because they weren't obvious from where you started.

**Objective:** Prevent scope narrowing and missed leverage by mapping what's adjacent to your current position.

**How it works:** Maps adjacent markets, related partnerships, underexplored angles, and leverage points you haven't named. Deliberately optimistic and generative — not a risk analysis.

**Use when:** You have defined a strategy or offer and want to check whether you've left obvious upside on the table.

---

#### `firstprinciples` — The real question beneath the question

**Origin:** Aristotelian first-principle reasoning and the Socratic method. Popularized in technology by Elon Musk — rather than asking "how do we buy rockets cheaply?", SpaceX asked "what are the actual raw material costs of a rocket?" and built from there.

**Objective:** Dissolve false constraints by returning to foundational truths. Separate what is actually true from what is merely conventional.

**How it works:** Strips away analogical thinking ("we do it this way because everyone does") to find the actual question you should be answering, and the actual constraints that are real vs inherited.

**Use when:** A problem feels intractable, conventional answers feel insufficient, or you suspect you're solving the wrong problem.

---

#### `outsider` — Cold read with no implicit context

**Origin:** The "stranger's eyes" technique from communication and intelligence tradecraft — checking whether a document or plan is legible to someone with zero background, exposing all unstated shared knowledge.

**Objective:** Surface the implicit context that experts forget isn't obvious to anyone outside the room.

**How it works:** Reads your content as someone who just walked in — no context, no shared history, no jargon. Flags everything that requires unstated knowledge to understand, and identifies what a naive reader would misinterpret.

**Use when:** Before sharing with a new stakeholder, an external audience, or anyone outside your immediate team.

---

#### `outside-in` — External forces before internal solutions

**Origin:** Porter's Five Forces and strategic environment analysis. The core insight: forces external to the organization (market, competition, regulation, technology, customer behavior) constrain what's possible *before* internal choices become relevant.

**Objective:** Prevent inside-out thinking — stop starting from "what do we want to do" and start from "what does the environment impose."

**How it works:** Maps the external forces shaping your decision space before generating any internal options. The environment is treated as a constraint, not a backdrop.

**Use when:** Starting a strategic analysis, entering a new market, or when internal plans feel disconnected from external reality.

---

#### `dixieme-homme` — Full opposing thesis against consensus

**Origin:** The *10th Man doctrine*, institutionalized by AMAN — the Israeli Military Intelligence Directorate — after the catastrophic intelligence failure of the 1973 Yom Kippur War. The failure was attributed to *conceptzia*: a shared mental model so dominant that signals contradicting it were systematically dismissed. The protocol: if 9 analysts agree, the 10th must construct the strongest possible case for the opposite conclusion — not find flaws, but build a complete counter-thesis. Popularized internationally by the film *World War Z* (2013), where Israel had institutionalized the rule to "believe the unbelievable."

**Objective:** Break groupthink at its root by making dissent mandatory, not optional.

**How it works:** Produces a complete, rigorous thesis arguing the opposite of the current consensus — with its own evidence, logic, and implications. This is not devil's advocate (pointing out flaws) and not red-team (adversary perspective): it is a full alternative interpretation of the same facts.

**Key differences:**
- vs `contrarian`: contrarian finds the main weakness in your plan. `dixieme-homme` argues a completely different conclusion from the same facts.
- vs `red-team`: red-team adopts an external adversary's perspective. `dixieme-homme` argues against your own team's consensus from the inside.
- vs `critique`: critique analyzes an artifact for flaws. `dixieme-homme` builds a counter-narrative against a shared belief.

**Use when:** Strong alignment exists around a conclusion and you suspect groupthink. High-stakes decisions where a wrong consensus is catastrophic.

---

#### `chairman` — Arbitrate contradictory perspectives

**Origin:** Structured synthesis — designed as the meta-skill that integrates outputs from multiple advisory lenses into a single verdict.

**Objective:** Move from competing perspectives to one actionable decision with explicit trade-offs.

**How it works:** Takes the outputs of other advisory analyses (contrarian, expansionist, red-team, etc.) and produces a synthesis: which arguments hold, which cancel out, what the recommended path is, and what the residual risks are.

**Use when:** After running two or more advisory skills on the same problem and needing a single decision. Also useful when actual stakeholders hold genuinely contradictory positions.

---

#### `red-team` — Reason from the adversary's perspective

**Origin:** CIA and NSA red team methodology. A dedicated team is tasked with reasoning and acting *as the adversary* — not to find vulnerabilities, but to plan the attack exactly as the opponent would plan it. Formalized in the US intelligence community in the 1970s after Cold War failures revealed persistent blind spots caused by mirror-imaging (assuming the adversary thinks like you).

**Objective:** Expose blind spots that defenders cannot see because they're reasoning from the wrong side of the problem.

**How it works:** Fully inhabits the adversary's position — their goals, constraints, resources, and reasoning. Produces the strategy the adversary would actually use, not the one you fear they might.

**Key differences:**
- vs `contrarian`: contrarian finds flaws in your plan from a neutral critic's view. `red-team` finds them from the perspective of someone actively trying to defeat you.
- vs `dixieme-homme`: `dixieme-homme` argues against internal consensus. `red-team` adopts an external adversary's goals and reasoning.

**Use when:** Competitive strategy, security analysis, negotiation preparation, any scenario with an active opponent who has their own goals.

---

#### `futurs-alternatifs` — Three plausible futures with leading indicators

**Origin:** Scenario planning, developed by Herman Kahn at the RAND Corporation in the 1950s for nuclear strategy. Refined by Shell's Group Planning under Pierre Wack in the 1970s — Shell was the only major oil company to anticipate the 1973 oil shock because it had built scenarios rather than forecasts. Subsequently adopted by the CIA for geopolitical intelligence and by corporate strategists worldwide.

**Objective:** Prepare for genuine uncertainty rather than optimizing for a single forecast that may be wrong.

**How it works:** Produces three distinct, plausible futures — not best/worst/base case (that is sensitivity analysis), but genuinely different trajectories that stem from different underlying assumptions. Each future comes with leading indicators: early signals that tell you *which* future is materializing so you can adjust before it's obvious.

**Use when:** Long-horizon decisions where prediction is impossible. Strategy under deep uncertainty. Planning that needs to remain robust across multiple possible outcomes.

---

### 🗺️ Strategy & Intelligence

| id | Role |
|---|---|
| `ach` | Analysis of Competing Hypotheses — find which explanation the evidence eliminates least |
| `key-assumptions` | Surface the implicit assumptions behind a reasoning |
| `indicateurs` | Confirmation and alert signals to track a plan |
| `quality-check` | Assess the structural soundness of cited information |
| `note-strategique` | Produce a structured and argued strategic memo |
| `strategie-prix` | Pricing strategy with perceived value, segmentation, and scenarios |
| `business-case-draft` | Structure an investment decision with costs, benefits, and risks |
| `tam-sam-som` | Estimate total, serviceable, and obtainable market |

---

### 🔍 Research & Analysis

| id | Role |
|---|---|
| `analyse-concurrentielle` | Factual foundation on the competitive landscape |
| `analyse-cdc` | Analyze a received specification document |
| `budget-variance-analysis` | Analyze budget/actual variances with corrective hypotheses |
| `metriques-saas` | Diagnose CAC, LTV, NRR, churn |
| `total-cost-analysis` | Structure a total cost of ownership with hidden costs |
| `financial-narrative` | Raw financial figures → executive narrative |
| `data-storytelling` | Turn data into a clear narrative with insight and recommendation |

---

### 📊 Metrics & Tracking

| id | Role |
|---|---|
| `okr` | Turn a vague objective into a structured OKR |
| `tableau-de-bord-kpi` | Define and structure a KPI dashboard |
| `offer-comparison` | Compare supplier offers on a weighted grid |
| `vendor-scorecard` | Reusable vendor evaluation grid |
| `compliance-checklist` | Generate a GDPR / labor law / sector compliance checklist |

---

### ⚖️ Legal & Contracts

| id | Role |
|---|---|
| `contract-review` | Analyze a contract clause by clause |
| `cgv-checker` | Identify unbalanced clauses in terms and conditions |
| `conformite-rgpd` | GDPR compliance checklist from a technical document |
| `legal-risk-flag` | Quickly surface legal red flags in a document |
| `nda-draft` | Generate an NDA adapted to the context |
| `contrat-fournisseur` | Analyze or draft a supplier contract from the buyer's side |

---

### 👥 HR & People

| id | Role |
|---|---|
| `fiche-poste` | Produce a structured and publishable job description |
| `entretien-professionnel` | Prepare a mandatory professional development interview |
| `interview-guide-recruteur` | Recruiter-side interview guide with STAR questions |
| `interview-loop-planner` | Design the full recruitment interview process |
| `onboarding-plan` | 30-60-90 day integration plan for a new hire |
| `offboarding-structure` | Departure plan with knowledge handover |
| `people-review` | Structure a collective talent review |
| `performance-review-helper` | Prepare an annual review with SMART objectives |
| `plan-developpement-competences` | Individual or collective skills development plan |
| `grille-remuneration` | Structure a salary grid by family and level |
| `contrat-emploi` | Analyze or draft an employment contract |
| `lettre-cadrage-disciplinaire` | Draft a factual disciplinary framing letter |
| `org-design-brief` | Formalize an organizational target with current diagnosis |

---

### 💻 Product & Tech

| id | Role |
|---|---|
| `prd` | Produce a complete Product Requirements Document |
| `feature-spec` | Functional spec: user stories, MoSCoW, acceptance criteria |
| `product-spec` | Actionable spec from a brief or scoped need |
| `brief` | Transform a vague need into an actionable brief |
| `cadrage` | Clarify a need before any production starts |
| `analysis` | Break down a complex need into actionable lots |
| `persona` | Produce structured user personas from research or a product brief |
| `journey-map` | User journey map with stages, emotions, and friction points |
| `mockup` | Produce a standalone HTML mockup from a brief or spec |
| `reformulation-us` | Rewrite poorly-written user stories into clean, testable US |
| `ticket-triage` | Categorize, prioritize P1–P4, and route a support ticket |
| `code-review` | Code review: security, performance, correctness, maintainability |
| `system-design` | Design a system or technical architecture |
| `tech-debt` | Identify, categorize, and prioritize technical debt |

---

### 🚀 Business & Sales

| id | Role |
|---|---|
| `offre-commerciale` | Produce the content of a structured client offer |
| `negotiation-brief` | Structured position before a negotiation |
| `rfp-draft` | Generate a structured request for proposal |
| `stakeholder-comms` | Write communications adapted to the audience |
| `compte-rendu` | Raw meeting notes → structured record with decisions and actions |
| `retrospective` | Blameless retrospective with facts, causes, and actions |

---

## Typical pipelines

```
critique → correction → deliver
explorer → decision   → deliver
research → analyse-concurrentielle → decision
brief    → prd → feature-spec
          simplify  (standalone)
          rephrase  (standalone)
```

---

## Installation

### Claude Code

Claude Code scans `~/.claude/skills/` at startup — one subdirectory per skill, each containing a `SKILL.md`.

```bash
git clone https://github.com/amiel-35/ix-skills /tmp/ix-skills
for f in /tmp/ix-skills/skills/*.md; do
  id=$(basename "$f" .md)
  mkdir -p ~/.claude/skills/$id
  cp "$f" ~/.claude/skills/$id/SKILL.md
done
```

Or to install a single skill:

```bash
mkdir -p ~/.claude/skills/critique
cp skills/critique.md ~/.claude/skills/critique/SKILL.md
```

### Claude.ai

**Option A — direct upload (one skill at a time)**

In **Settings → Skills**, drag and drop `skills/<id>.md` directly.

**Option B — `.skill` bundle (batch)**

```bash
git clone https://github.com/amiel-35/ix-skills
cd ix-skills
pip install -r requirements.txt
python3 build.py --target claude-ai
```

Drop the `dist/*.skill` files into **Settings → Skills**.

### mystaffy

```bash
python3 build.py --target mystaffy
# or to regenerate the native ix-memory format:
python3 build.py --target ix-memory
```

### GPT / Gemini / other LLMs

Copy-paste the content of `skills/<id>.md` as a system prompt. The YAML frontmatter is ignored without side effects.

---

## Structure

```
ix-skills/
├── skills/                 ← canonical source (one .md + .mystaffy.json per skill)
├── scripts/
│   └── migrate_from_ix_memory.py
├── dist/                   ← .skill files for claude.ai (gitignored)
├── mystaffy-dist/          ← mystaffy artifacts (gitignored)
├── .claude-plugin/
│   └── plugin.json
├── build.py                ← multi-target packager
├── requirements.txt
└── CLAUDE.md               ← contribution guide
```

---

## Build

```bash
python3 build.py --validate
python3 build.py
python3 build.py critique
python3 build.py --target claude-ai
python3 build.py --target mystaffy --domain cognitif
python3 build.py --target ix-memory
```

---

## Contributing

Fork, modify, PR. Read `CLAUDE.md` for conventions.

---

## License

MIT
