# ix-skills

Atomic knowledge-work skills — portable across Claude, GPT, Gemini, and mystaffy.

78 skills in 10 categories. Each skill encodes a **cognitive process**, not domain expertise.

[🇫🇷 Version française](README-fr.md)

---

## Available skills

### 🧠 Cognitive — core process atoms

| id | Role |
|---|---|
| `critique` | Identify flaws in content without proposing solutions |
| `correction` | Turn a critique into actionable directives |
| `simplify` | Strip content down to its essentials without changing the meaning |
| `rephrase` | Restate the real meaning of dense or ambiguous content |
| `explorer` | Generate an option space without committing to a choice |
| `decision` | Arbitrate with visible trade-offs and a clear recommendation |
| `deliver` | Transform an artifact into a shareable deliverable |
| `research` | Build a sourced factual foundation before any decision |
| `synthese` | Condense long content into an actionable summary |
| `decomposer` | Break a complex problem into independent, actionable sub-problems |
| `compte-rendu` | Raw meeting notes → structured record with decisions and actions |
| `revue-feedback` | Evaluate feedback rigorously before accepting or rejecting it |

---

### ⚔️ Advisory — perspective archetypes

Challenge a decision, plan, or brief from five distinct angles.

| id | Angle |
|---|---|
| `contrarian` | Main failure point and unverified assumptions |
| `executor` | Does this hold up in reality? |
| `expansionist` | The missing upside and adjacent opportunities |
| `firstprinciples` | The real question beneath the question |
| `outsider` | Read cold, with no implicit context |
| `outside-in` | External forces imposed before internal solutions |
| `dixieme-homme` | Full opposing thesis against the consensus |
| `chairman` | Arbitrate contradictory perspectives |
| `red-team` | Reason from the adversary's perspective |
| `futurs-alternatifs` | Three plausible futures with leading indicators |

---

### 🗺️ Strategy & Intelligence

| id | Role |
|---|---|
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
| `contrat-emploi` | Analyze or generate an employment contract |
| `contrat-fournisseur` | Analyze a supplier contract from the buyer's side |

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

### Claude Code / Cowork

```bash
claude plugin install ix-skills
```

### Claude.ai

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
