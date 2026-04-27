# ix-skills

Atomic knowledge-work skills — portable across Claude, GPT, Gemini, and mystaffy.

84 skills in 10 categories (3 in draft). Each skill encodes a **cognitive process**, not domain expertise.

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
| `prioritize` | Rank a list of items by attack order with explicit criteria | Sequences items — **does not choose between exclusive options** (use `decision`) |
| `problem-framing` *(draft)* | Reformulate a vague subject into an actionable problem | Formulates the central question — **does not solve it** |
| `questioning` *(draft)* | Generate the right questions to ask about a subject | Questions only — **does not answer or explore** (use `explorer`) |
| `argumentation` *(draft)* | Build a structured argument to defend or attack a position | Constructs the case — **does not evaluate it** (use `critique`) |

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

Structured intelligence tools — each audits a different dimension of a reasoning or plan before you commit to it.

---

#### `ach` — Analysis of Competing Hypotheses

**What it does:** Puts 3–4 competing hypotheses to the test against available evidence. For each piece of information, marks whether it supports, contradicts, or is neutral to each hypothesis. Retains the hypothesis the evidence eliminates the least — not the one you started with.

**What it doesn't do:** Does not validate a conclusion. Does not confirm what you already believe.

**Use when:** You have an explanation for something and want to check if you've fallen in love with it. Pairs naturally with `key-assumptions` (which surfaces the hidden premises of each hypothesis) and `indicateurs` (which defines what to watch to see which hypothesis materializes).

---

#### `key-assumptions` — Surface hidden assumptions

**What it does:** Pulls out the implicit premises of a reasoning, decision, or plan — what is taken for granted without being stated. Qualifies each assumption (solid / fragile / unknown) and identifies the critical ones whose collapse would bring the whole thing down.

**What it doesn't do:** Does not validate the reasoning. Does not check facts. It makes the foundation visible — what you do with that is up to you.

**Use when:** Before committing to a plan, before presenting an analysis to a decision-maker, or when you suspect that what you're calling "facts" are actually assumptions you haven't tested.

> Pairs with `ach` (which tests hypotheses against evidence) and `quality-check` (which audits the sources themselves).

---

#### `indicateurs` — Define what to watch

**What it does:** Defines in advance the observable signals that will tell you whether a plan is holding, a hypothesis is materializing, or a pivot is coming. Produces confirmation signals (the plan is working) and alert signals (something is wrong), plus weak signals to watch.

**What it doesn't do:** Does not track KPIs in real time (that's `tableau-de-bord-kpi`). Does not evaluate current performance. It defines the monitoring setup before execution begins.

**Use when:** After a decision or plan is formed, before execution starts. Especially powerful after `futurs-alternatifs` (leading indicators per scenario) or `ach` (signals that would confirm or invalidate the retained hypothesis).

---

#### `quality-check` — Audit the raw evidence

**What it does:** Evaluates the structural solidity of the information on which a reasoning, decision, or analysis rests — before it becomes a foundation. Checks source type, corroboration, freshness, author bias, and flags informational gaps.

**What it doesn't do:** Does not evaluate the conclusions. Does not evaluate the reasoning itself. Only the quality of the raw material.

**Use when:** Before making a decision that rests on external data, market figures, or cited sources. Use it before `decision` or `note-strategique` when you're not sure the sources are solid.

> `quality-check` audits information sources. `key-assumptions` audits the hidden premises of a reasoning. Both are pre-decision hygiene, different layers.

---

#### `note-strategique` — Strategic memo, conclusion first

**What it does:** Produces a structured, shareable strategic memo — for a decision-maker, board, or executive. Starts with the conclusion, then the argument, then the options, then the recommendation with explicit trade-offs. Two pages maximum without justification.

**What it doesn't do:** Does not start with context and bury the recommendation at the end. If you don't have a clear position yet, run `decision` first.

**Use when:** You have a recommendation to make and need to package it for a decision-maker. Output is directly shareable.

---

#### `strategie-prix` — Pricing strategy with trade-offs

**What it does:** Formulates a pricing strategy by linking perceived value, customer segmentation, and business trade-offs. Compares pricing models (freemium, value-based, usage-based, tiered…) and produces a recommendation with explicit hypotheses.

**What it doesn't do:** Does not produce a price list. Does not recommend a price without stating the assumptions behind it.

**Use when:** Product launch, market repositioning, or under competitive pricing pressure. Requires context on the offer, target customers, and competitive benchmarks if available.

---

#### `business-case-draft` — Investment decision structure

**What it does:** Structures an investment decision with explicit costs, expected benefits, risk scenarios, and financial hypotheses. Distinguishes certain costs from estimated costs. Clearly marks what is a hypothesis vs a fact. If financial data is too fragile, says so and suggests `note-strategique` as an alternative.

**What it doesn't do:** Does not invent figures.

**Use when:** You have numbers to work with and need to frame a buy/build/invest decision. If you don't have numbers, use `note-strategique` instead.

---

#### `tam-sam-som` — Market sizing with method

**What it does:** Estimates Total Addressable Market, Serviceable Addressable Market, and Serviceable Obtainable Market using top-down and bottom-up methods with explicit hypotheses. Surfaces the method, the figures, and the degree of uncertainty. Web search required in standard/deep mode.

**What it doesn't do:** Does not produce figures from memory without flagging it. TAM/SAM/SOM without hypotheses is a guess, not a sizing.

**Use when:** Preparing a pitch, validating a market opportunity, or building a business case.

---

### 🔍 Research & Analysis

Each tool builds a factual foundation on a specific analytical object — competitive landscape, specification, budget, SaaS metrics, costs, financial data, or data narrative.

---

#### `analyse-concurrentielle` — Competitive landscape with differentiation logic

**What it does:** Structures a competitive analysis around differentiation logic — not a list of players. Identifies market forces, compares players on a common framework, surfaces positioning risks and differentiation zones. Web search required in standard/deep mode.

**What it doesn't do:** Does not produce a bullet list of competitors. Does not make strategic recommendations — use `decision` for that.

**Use when:** Before a market entry, a positioning decision, or a fundraising narrative. Pairs with `note-strategique` or `decision` downstream.

---

#### `analyse-cdc` — Specification document analysis

**What it does:** Analyzes a received specification document (CDC) from the respondent's perspective. Surfaces explicit requirements, implicit requirements, grey areas, contradictions, and the blocking questions to ask before committing to a response.

**What it doesn't do:** Does not summarize the spec — it critiques it. Does not produce a response plan.

**Use when:** You receive a spec, RFP, or requirements document and need to understand what's really being asked before engaging. Output feeds a response strategy or clarification meeting.

---

#### `budget-variance-analysis` — Budget vs. actual diagnosis

**What it does:** Analyzes gaps between budget and actual figures. Identifies significant variances, qualifies them by nature (volume, price, mix, timing, operational), and produces corrective hypotheses and watch points.

**What it doesn't do:** Does not invent causes or figures. Does not make management decisions — produces a factual diagnosis.

**Use when:** Monthly or quarterly budget review, P&L analysis, or when you need to explain performance to a board or controller.

---

#### `metriques-saas` — SaaS business model health

**What it does:** Reads SaaS key metrics together — CAC, LTV, NRR, churn, payback period — and interprets them as a system, not in isolation. Surfaces implications for business model health, growth sustainability, and piloting priorities.

**What it doesn't do:** Does not produce benchmarks from memory in standard/deep mode. Does not recommend actions — produces a diagnosis.

**Use when:** Board preparation, fundraising, operational review, or when metric trends are contradictory and you need to understand what they mean together.

---

#### `total-cost-analysis` — Full lifecycle cost (TCO)

**What it does:** Structures a Total Cost of Ownership analysis covering direct costs, hidden costs (implementation, training, integration, migration, exit), and financial risks over a given horizon. Distinguishes confirmed costs, estimated costs, and unquantified risks.

**What it doesn't do:** Does not look at the sticker price alone. Does not invent figures without marking them as hypotheses.

**Use when:** Before any significant purchase or vendor decision where the visible price doesn't capture the full economic impact. Pairs with `offer-comparison` and `vendor-scorecard`.

---

#### `financial-narrative` — Numbers → executive story

**What it does:** Transforms raw financial figures (P&L, KPIs, reporting) into a clear, message-first narrative for an executive or board audience. Starts with key messages, contextualizes figures, connects variations to explanatory factors.

**What it doesn't do:** Does not invent numbers or trends. Does not reproduce the raw data. Does not distort figures to tell a better story.

**Use when:** Board presentations, investor updates, quarterly reviews — any time numbers need to be communicated to an audience that needs the "so what" before the detail.

> Different from `data-storytelling`: `financial-narrative` is specifically for financial data with an executive or board audience. `data-storytelling` handles any type of data for any audience.

---

#### `data-storytelling` — Data → narrative with insight

**What it does:** Transforms any data (metrics, tables, analysis results) into a clear narrative with a main insight and a recommendation. Reorganizes the data around the insight — not in raw order.

**What it doesn't do:** Does not tell a story that doesn't rest on the data. Does not stack numbers without a narrative angle.

**Use when:** Product reviews, user research readouts, operational reporting — any data presentation where the audience needs to understand what the data means and what to do about it.

---

### 📊 Metrics & Tracking

Tools for defining and evaluating measurement systems — from objectives to dashboards to vendor selection grids.

---

#### `okr` — Vague objective → structured OKR

**What it does:** Transforms a vague strategic intent into a structured OKR — an inspiring Objective paired with 3–4 measurable Key Results. Refuses non-measurable KRs and proposes quantified formulations instead.

**What it doesn't do:** Does not validate KRs that lack a metric. Does not confuse KRs with tasks or initiatives.

**Use when:** Quarterly planning, strategic alignment, or when leadership has a direction but no measurable goals. Output feeds `tableau-de-bord-kpi` and `indicateurs`.

---

#### `tableau-de-bord-kpi` — KPI dashboard structure

**What it does:** Defines and structures a KPI dashboard from business objectives, OKRs, or a business context. Distinguishes directly measurable KPIs, estimable KPIs (with stated hypotheses), and problematic KPIs (missing reliable source). Refuses vanity metrics.

**Use when:** After OKRs are set, or when you need to put a monitoring structure in place for a team, product, or business unit.

---

#### `offer-comparison` — Weighted comparison with recommendation

**What it does:** Compares already-received supplier offers on a normalized weighted grid and produces an argued recommendation. Makes the scoring method and uncertainty visible — does not hide trade-offs.

**What it doesn't do:** Does not evaluate offers you haven't received yet. If the proposals are too different in scope, manual normalization is required first.

**Use when:** After receiving multiple quotes for a significant purchase.

> Pipeline: `vendor-scorecard` → `offer-comparison` → `total-cost-analysis` → `decision`.

---

#### `vendor-scorecard` — Reusable vendor evaluation grid

**What it does:** Builds a weighted vendor scorecard from a procurement context — criteria, weightings, scoring scale, qualitative comment fields. Produces the scoring **tool**, not the decision.

**What it doesn't do:** Does not score vendors (that's `offer-comparison`). Does not invent weightings without justifying them.

**Use when:** Before a consultation process begins, to align stakeholders on evaluation criteria. Reusable for future consultations of the same type.

---

#### `compliance-checklist` — Legal compliance checklist

**What it does:** Generates a compliance checklist covering legal, contractual, and regulatory obligations — GDPR, labor law, sector-specific regulation — from a project context or document.

**What it doesn't do:** Does not replace professional legal or regulatory advice. Always requires expert validation before operational use.

**Use when:** Before any product launch, contractualization, or operational change with legal implications. A structured pre-validation to orient the conversation with a lawyer, not replace it.

---

### ⚖️ Legal & Contracts

Pre-legal tools — all require professional validation before use. They orient reviews, surface risks, and produce drafts. None replace a lawyer.

---

#### `legal-risk-flag` — Fast red flag scan

**What it does:** Quickly reads a legal or contractual document and extracts priority risk signals with graduated severity levels (critical / high / medium). Designed for speed — a flash assessment before deciding whether a deeper review is needed.

**What it doesn't do:** Does not perform a full analysis. Flags, does not conclude. Never replace a lawyer.

**Use when:** You receive a document and need to decide in minutes whether to escalate or which clauses to focus on.

> Use `legal-risk-flag` first (fast scan), then `contract-review` for the full clause-by-clause analysis.

---

#### `contract-review` — Clause-by-clause with redlines

**What it does:** Analyzes a contract clause by clause, identifies deviations from standard positions, produces priority redlines with justification and proposed alternative language.

**What it doesn't do:** Does not provide legal advice. Output must be reviewed by a qualified professional before use or negotiation.

**Use when:** Before signing a significant contract. Faster than a full lawyer review for the first pass — then the lawyer validates.

---

#### `cgv-checker` — Unbalanced clauses in T&Cs

**What it does:** Identifies unbalanced, unusual, or sensitive clauses in General Terms and Conditions (sales or use), depending on the reading position (buyer, user, subscriber).

**What it doesn't do:** Does not assess the full legal validity of the T&Cs. Does not replace legal advice.

**Use when:** Before accepting T&Cs for a significant vendor or platform relationship, or when drafting your own T&Cs.

> Different from `contract-review`: `cgv-checker` is for standard adhesion T&Cs. `contract-review` is for negotiable contracts with custom clauses.

---

#### `conformite-rgpd` — GDPR compliance checklist

**What it does:** Produces a GDPR compliance checklist from a technical specification, product description, or data processing document. Distinguishes observed processing, inferred processing, and obligations to confirm.

**What it doesn't do:** Does not replace a DPO or qualified legal professional. Requires expert validation before operational use.

**Use when:** Before launching a product or feature that processes personal data. A structured first-pass self-assessment before the DPO review.

---

#### `nda-draft` — NDA draft adapted to context

**What it does:** Generates a confidentiality agreement draft adapted to the context — type of parties, subject of exchanges, duration. Produces a document ready for legal review, not for immediate signing.

**What it doesn't do:** Does not provide legal advice. Always requires lawyer validation before signing.

**Use when:** You need a starting point for NDA negotiations and don't want to start from a generic template.

---

#### `contrat-fournisseur` — Supplier contract, buyer's side

**What it does:** Analyzes **or** drafts a supplier or service provider contract from the buyer's perspective. Surfaces unbalanced conditions, clauses to renegotiate (SLA, liability, termination, penalties, exclusivity, renewal), and contractual risks. Can also produce a first draft when no contract exists yet.

**What it doesn't do:** Does not replace legal advice. Requires professional validation before use.

**Use when:** Before signing a supplier contract, before entering negotiations, or when drafting initial terms for a new supplier relationship.

---

### 👥 HR & People

Tools for the full employee lifecycle — recruiting, onboarding, development, assessment, organization design, and employment law. French labor law context is embedded where relevant.

---

#### `fiche-poste` — Structured job description

**What it does:** Produces a structured, publishable job description from an HR brief or recruitment need. Distinguishes required from desirable criteria, identifies grey areas, and produces output that feeds the downstream recruiting workflow.

**Use when:** Starting a recruitment process. Output feeds `interview-loop-planner`.

---

#### `entretien-professionnel` — Mandatory professional development interview

**What it does:** Prepares a mandatory professional development interview (French Labor Code, art. L6315-1) — required every 2 years for all employees. Produces a framework, questions, and a meeting record template compliant with legal requirements.

**What it doesn't do:** Not the same as an annual performance review. This is a legally required career development conversation, not a performance assessment.

**Use when:** Every 2 years per employee, or after specific events (return from parental leave, sick leave…) as required by French law.

---

#### `interview-guide-recruteur` — Recruiter-side interview guide

**What it does:** Produces a full recruiter or manager interview guide with STAR-structured questions, evaluation annotations, scenario-based questions, a weighted 1–4 scoring grid, graduated red flags, and a Go/No-go debrief sheet.

**Use when:** For a specific interview round. Best used downstream of `interview-loop-planner`, which defines the rounds and competencies.

---

#### `interview-loop-planner` — Full interview process design

**What it does:** Designs the complete interview loop for a recruitment — number of rounds, competencies per round, consolidated scorecard, and schedule. Produces round briefs that directly feed `interview-guide-recruteur`.

**Use when:** Before starting interviews for a significant hire. Ensures each round assesses different dimensions.

> Pipeline: `fiche-poste` → `interview-loop-planner` → `interview-guide-recruteur` (one per round).

---

#### `onboarding-plan` — 30-60-90 day integration plan

**What it does:** Builds a structured integration plan covering the first 30, 60, and 90 days — objectives, key relationships, deliverables, and success criteria per phase.

**Use when:** Before a new hire starts, to give both manager and employee a shared roadmap.

---

#### `offboarding-structure` — Departure plan with continuity

**What it does:** Structures an offboarding plan covering knowledge handover, admin checklist, exit interview framework, and continuity risk mapping.

**Use when:** When an employee gives notice. The earlier it starts, the better the knowledge transfer.

---

#### `people-review` — Collective talent review

**What it does:** Structures a collective talent review with a positioning matrix (performance × potential), succession planning, retention and flight risk assessment, and priority actions per profile.

**Use when:** Annual or bi-annual talent reviews, before an organizational change, or when preparing a workforce plan.

---

#### `performance-review-helper` — Annual review preparation

**What it does:** Prepares an annual performance review with a structured assessment of the past year and SMART objectives for the next. Supports both manager prep and employee self-assessment.

**What it doesn't do:** Not the mandatory professional development interview (`entretien-professionnel`). This is about performance — results, objectives, compensation context.

**Use when:** Ahead of annual review cycles.

---

#### `plan-developpement-competences` — Skills development plan

**What it does:** Builds an individual or collective skills development plan with training actions, schedule, success indicators, and budget. Links identified gaps to concrete development paths.

**Use when:** After a performance review, a people review, or a skills gap assessment.

---

#### `grille-remuneration` — Compensation grid

**What it does:** Structures a compensation grid by job family and seniority level — salary ranges, positioning criteria (internal equity, market benchmarks), and governance rules (who can offer what).

**Use when:** When scaling a team and needing consistent, defensible compensation decisions across hires and existing employees.

---

#### `contrat-emploi` — Employment contract

**What it does:** Analyzes or drafts an employment contract, job offer letter, or HR amendment. Surfaces key clauses and points of attention. Produces compliant draft language.

**What it doesn't do:** Does not provide legal advice. Requires validation by a labor lawyer before use.

**Use when:** Drafting a new employment contract, reviewing one received, or preparing an amendment (role change, part-time arrangement…).

---

#### `lettre-cadrage-disciplinaire` — Disciplinary framing letter

**What it does:** Drafts a factual and proportionate disciplinary framing letter — documenting observed facts, their impact, and expected behavior change. Calibrated to the severity of the situation.

**What it doesn't do:** Does not produce a formal sanction letter. Must be validated by a labor lawyer before sending.

**Use when:** A documented conversation is needed before a formal disciplinary procedure, or to create a written record of a behavioral issue.

---

#### `org-design-brief` — Organizational redesign target

**What it does:** Formalizes an organizational target with a current state diagnosis, design rationale, human risks, and sequencing — before any announcement or implementation. Surfaces what the new structure solves, what new risks it creates, and how to phase the transition.

**Use when:** Before announcing a reorganization. Also useful as pre-work before engaging a management team in the design.

---

### 💻 Product & Tech

Tools for the full product development lifecycle — from clarifying a need to specifying, designing, building, and maintaining.

---

#### `brief` — Vague need → structured brief

**What it does:** Transforms a vague need, request, or idea into a structured, actionable brief — purpose, constraints, success criteria, and exclusions. The output is usable as input for any downstream production skill.

**What it doesn't do:** Does not clarify an incomplete brief when you don't yet know what you want (use `cadrage` for that). Does not produce a spec.

**Use when:** You know what you want to build but need to structure it before handing it off.

---

#### `cadrage` — Clarify before producing

**What it does:** Explores and clarifies a vague or incomplete need — surfacing intent, constraints, hypotheses, and decision points before any production begins. Produces a clarification report and recommended next steps.

**What it doesn't do:** Does not produce a brief or spec directly. It's the step that makes `brief` possible when the input is too fuzzy.

**Use when:** The request is too ambiguous to brief directly. When you need to align on what's actually being asked before committing.

> `cadrage` asks the right questions. `brief` writes the structured answer. Run them in sequence when the need is unclear.

---

#### `analysis` — Decompose before specifying

**What it does:** Decomposes a complex need into independent, prioritized lots before spec or delivery begins. Produces a structured decomposition that feeds a PRD, a sprint, or a project plan.

**Use when:** The subject is dense or multi-dimensional and needs to be broken down before anyone can spec or estimate it. Upstream of `prd` or `feature-spec` for complex initiatives.

---

#### `prd` — Complete Product Requirements Document

**What it does:** Produces a full PRD — context, problem statement, goals, functional and non-functional requirements, out-of-scope items, success metrics, and open questions.

**Use when:** You need a comprehensive product document to align the team, communicate with engineering, or frame a significant investment.

---

#### `feature-spec` — Feature-level functional specification

**What it does:** Produces a complete functional spec for a feature — user stories, MoSCoW requirements, acceptance criteria, edge cases, and success metrics.

**Use when:** A feature is approved and needs to be specified for engineering. More granular than a PRD — operates at the level of a single feature or epic.

---

#### `product-spec` — Lightweight actionable spec

**What it does:** Produces an actionable specification from a brief or scoped need. Lighter than a PRD, more structured than a brief — a rapid spec that teams can act on.

**Use when:** You need something between a brief and a full PRD. Good for smaller features, MVPs, or rapid iteration contexts.

> Hierarchy: `brief` → `product-spec` → `feature-spec` → `prd` (increasingly detailed).

---

#### `persona` — Structured user personas

**What it does:** Produces structured user personas from research data or a product brief — goals, frustrations, behaviors, context, and decision triggers. Designed to be actionable for product decisions, not just decorative.

**Use when:** At the start of a product initiative, or when the team has diverging assumptions about who they're building for.

---

#### `journey-map` — User journey with friction and opportunities

**What it does:** Produces a user journey map covering stages, actions, emotions, friction points, and improvement opportunities. Structured around the user's perspective, not the product's features.

**Use when:** Before redesigning an experience, identifying where to invest in UX improvement, or aligning a cross-functional team on how users actually experience the product.

---

#### `mockup` — Standalone HTML mockup

**What it does:** Produces a standalone, presentable HTML mockup from a brief, spec, or visual references. A visual deliverable for alignment and feedback.

**What it doesn't do:** Not a functional prototype. Not production-ready code.

**Use when:** You need something visual to present to stakeholders, validate with users, or communicate a layout before investing in design or engineering.

---

#### `reformulation-us` — Rewrite poorly-written user stories

**What it does:** Rewrites existing user stories that are vague, developer-centric, or untestable into clean, testable user stories with proper structure and explicit acceptance criteria.

**Use when:** In backlog refinement, when stories are being pulled into a sprint but aren't ready, or after a discovery phase where stories were written informally.

---

#### `ticket-triage` — Support ticket categorization and routing

**What it does:** Categorizes an incoming support ticket, assigns a P1–P4 priority based on impact and urgency, identifies missing information needed for handling, and routes to the appropriate team or queue.

**Use when:** Processing incoming support or bug tickets, especially in high-volume contexts where consistent prioritization is needed.

---

#### `code-review` — Code review across 4 dimensions

**What it does:** Reviews code across security, performance, correctness, and maintainability. For each finding: identifies the issue, explains the impact, and proposes a fix. Filters by confidence — only reports high-priority issues.

**Use when:** Before merging a PR, during a codebase audit, or when onboarding to a new codebase.

---

#### `system-design` — Technical architecture design

**What it does:** Designs a system or technical architecture — components, data flows, API contracts, storage, scalability decisions, and explicit trade-offs. Documents what was decided and why, including options rejected.

**Use when:** Before building a new system, when refactoring an existing architecture, or when a team needs a shared technical blueprint.

---

#### `tech-debt` — Technical debt audit with remediation plan

**What it does:** Identifies, categorizes (structural / code quality / dependency / documentation / test coverage), and prioritizes technical debt with a realistic remediation plan. Distinguishes quick wins from structural work.

**Use when:** Before a significant sprint, during quarterly engineering planning, when velocity has degraded, or before an acquisition due diligence.

> `code-review` evaluates a specific changeset (a PR, a file). `tech-debt` audits accumulated structural issues across the full codebase.

---

### 🚀 Business & Sales

Tools for commercial execution — offer writing, negotiation, RFPs, stakeholder communications, meeting records, and retrospectives.

---

#### `offre-commerciale` — Client offer content

**What it does:** Produces the structured content of a client offer — context understanding, proposed solution, value argument, pricing logic, and next steps. Focus is on content and argument, not final formatting.

**What it doesn't do:** Does not format the final document (use `deliver` for that). Does not negotiate.

**Use when:** Responding to an inbound request, after a discovery call, or when you need to structure a proposal before putting it into a deck or document.

---

#### `negotiation-brief` — Structured position before a negotiation

**What it does:** Prepares a complete negotiation position — objectives, non-negotiables, tradeable points, BATNA (best alternative if no agreement), and concession logic. Designed for preparation, not to hand to the other party.

**What it doesn't do:** Not a negotiation script. Not a template for the other party.

**Use when:** Before any high-stakes negotiation — supplier, partnership, client, employment. The clearer the position going in, the better the outcome.

---

#### `rfp-draft` — Request for proposal

**What it does:** Generates a structured request for proposal — context, scope, requirements, evaluation criteria, expected deliverables, and timeline.

**Use when:** You are the buyer and need to solicit structured offers from multiple vendors. Output feeds `offer-comparison` and `vendor-scorecard`.

---

#### `stakeholder-comms` — Audience-calibrated communications

**What it does:** Writes communications adapted to a specific stakeholder audience — executive summary for a board, technical briefing for an engineering team, status update for a client, or partner announcement. Adapts register, depth, and format to the audience.

**Use when:** You have something to communicate and the message needs to land differently with different audiences. Especially useful for sensitive news, change announcements, or complex status updates.

---

#### `compte-rendu` — Raw notes → structured record

**What it does:** Transforms raw meeting notes into a structured meeting record — decisions made, actions assigned (owner + due date), open questions, and next steps. Distinguishes what was decided from what was discussed.

**Use when:** After any meeting that produced decisions or actions. Output is directly shareable and keeps accountability clear.

---

#### `retrospective` — Blameless retrospective

**What it does:** Produces a structured blameless retrospective — separating observed facts from interpretations, identifying root causes without blame attribution, and producing concrete, owned action items.

**What it doesn't do:** Not a complaints session. Not an evaluation of individuals. Blameless means the system, not the people.

**Use when:** At the end of a sprint, project, incident, or significant initiative. The blameless constraint is what makes the output actionable rather than defensive.

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

### Codex CLI

```bash
git clone https://github.com/amiel-35/ix-skills /tmp/ix-skills
cd /tmp/ix-skills
pip install -r requirements.txt
bash scripts/install-codex.sh          # all skills
bash scripts/install-codex.sh critique # one skill
bash scripts/install-codex.sh --dry-run
```

Skills are installed to `~/.codex/skills/<id>/SKILL.md`. Restart Codex to activate.

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
│   ├── install-codex.sh    ← Codex CLI installer
│   └── migrate_from_ix_memory.py
├── dist/                   ← .skill files for claude.ai (gitignored)
├── mystaffy-dist/          ← mystaffy artifacts (gitignored)
├── codex-dist/             ← Codex CLI artifacts (gitignored)
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
