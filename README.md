<p align="center">
  <img src="docs/assets/banner.svg" alt="ix-skills: atomic knowledge-work skills" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/github/license/amiel-35/ix-skills?color=7f9a96"></a>
  <img alt="Plugin version" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Famiel-35%2Fix-skills%2Fmain%2Fdist%2F.claude-plugin%2Fplugin.json&query=%24.version&label=plugin&color=7fc8bd">
  <img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-plugin-D97757">
  <img alt="Skills" src="https://img.shields.io/badge/skills-35-3d6b73">
  <img alt="Platforms" src="https://img.shields.io/badge/also-Codex%20%C2%B7%20GPT%20%C2%B7%20Gemini%20%C2%B7%20mystaffy-56707a">
</p>

<p align="center">
  <a href="#quick-start"><b>Quick start</b></a> ·
  <a href="#available-skills"><b>Skill catalog</b></a> ·
  <a href="#typical-pipelines"><b>Pipelines</b></a> ·
  <a href="#contributing"><b>Contributing</b></a> ·
  <a href="README-fr.md"><b>Français</b></a>
</p>

---

<details>
<summary><b>Table of contents</b></summary>

- [About](#about)
- [Quick start](#quick-start)
- [Corpus convention — the null output](#corpus-convention--the-null-output)
- [Available skills](#available-skills)
- [Typical pipelines](#typical-pipelines)
- [Installation](#installation)
- [Structure](#structure)
- [Build](#build)
- [Sibling projects](#sibling-projects)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

</details>

## About

Atomic knowledge-work skills — portable across Claude, GPT, Gemini, and mystaffy.

35 skills in 4 categories (2 in draft). Each skill encodes a **cognitive process**, not domain expertise. Domain skills (HR, legal, finance, procurement, product, tech) live in [ix-recipes](https://github.com/amiel-35/ix-recipes), which builds on these atoms.

---

## Quick start

Install the plugin in Claude Code:

```bash
claude plugin marketplace add amiel-35/ix-skills
claude plugin install ix-skills@ix-skills
```

Restart Claude Code. Skills are namespaced (`critique` becomes `/ix-skills:critique`), and Claude also picks them up from plain requests:

- *"Critique this brief: what's wrong with it?"*
- *"Before we decide, explore the options."*
- *"Fact-check this note against the source."*

Other platforms (Cowork, Codex CLI, Antigravity CLI, mystaffy, GPT, Gemini): see [Installation](#installation).

---

## Corpus convention — the null output

A skill that has nothing to produce opens its response with « RAS — » followed
by the reason, and stops. The token is literal and identical across the whole
corpus: that is what makes it greppable and testable.

---

## Available skills

Click a category to expand it.

<details>
<summary><b>🧠 Cognitive — core process atoms</b> — 17 skills</summary>


Primitive operations on content, problems, and decisions. Each encodes a single cognitive move — they are designed to chain, not to replace each other.

| id | Role | Key constraint |
|---|---|---|
| `critique` | Identify flaws in content without proposing solutions | Analysis only — **does not fix** |
| `correction` | Turn a critique into actionable directives | Transforms a critique — **does not re-analyze** |
| `simplify` | Identify what can be removed without changing the meaning | Identifies removals — **does not apply them** (use `correction`) |
| `rephrase` | Restate the real meaning of dense or ambiguous content | Reinterprets — meaning may shift, not just trimmed |
| `explorer` | Generate an option space — writes the default answer first, then sets it aside; `breadth` decides whether the vehicle named in the input stays a constraint (`standard`) or is set aside too (`broad`) | Breadth — **does not choose** |
| `decision` | Arbitrate with visible trade-offs and a clear recommendation | Chooses among existing options — **does not generate** |
| `deliver` | Transform an artifact into a shareable deliverable | Formatting and audience calibration |
| `research` | Build a sourced factual foundation before any decision | Sources required in standard and deep mode — `flash` answers from model memory alone |
| `synthese` | Condense long content into an actionable summary | Lossy compression — detail is intentionally discarded |
| `decomposer` | Break a complex problem into actionable sub-problems | Dependencies between sub-problems are identified, not hidden |
| `revue-feedback` | Evaluate feedback rigorously before accepting or rejecting it | Evaluates incoming critique — not your own artifact |
| `fact-check` | Check a text against reference evidence, claim by claim — confirmed, contradicted, not in the source, not checkable | One verdict per claim, each backed by a verbatim quote of the source — **the source is an input**, `closed` mode ignores what the model knows |
| `controle-qualite` | Check a deliverable against a provided set of rules — template, style guide, spelling, forbidden vocabulary — in `sweep` (find every breach) or `verdict` (rule on a suspected list) mode | One verdict per finding, with the rule and the exact passage — **a rule not in the reference is not a rule** |
| `prioritize` | Rank a list of items by attack order with explicit criteria — 8 methods (ICE, RICE, WSJF, MoSCoW, Kano, Eisenhower, value/effort, weighted scoring), each detailed in a reference read only when chosen | Sequences items — **does not choose between exclusive options** (use `decision`) |
| `problem-framing` *(draft)* | Reformulate a vague subject into an actionable problem | Formulates the central question — **does not solve it** |
| `questioning` | Generate the right questions to ask — flags every named solution (umbrella term first, then sizing, then sub-artefacts) and asks whether it was chosen or was the first idea | Questions only — **does not answer or explore**, never strips a named term (use `explorer`) |
| `argumentation` *(draft)* | Build a structured argument to defend or attack a position | Constructs the case — **does not evaluate it** (use `critique`) |

#### Key distinctions

**`critique` vs `revue-feedback`**
`critique` analyzes *your own artifact* (a document, a plan, a proposal) to find its flaws. `revue-feedback` processes *feedback someone else gave you* — evaluating whether to accept, nuance, or reject it before responding. One is editorial, the other is diplomatic.

**`critique` vs `fact-check` vs `controle-qualite` vs `quality-check`**
`critique` judges substance — what is weak, unclear, missing — and needs no reference. `fact-check` checks a text against *evidence*: one verdict per claim (confirmed, contradicted, not in the source, not checkable), each backed by a verbatim quote of the source. `controle-qualite` checks a deliverable against *rules* given as input — template, style guide, spelling, forbidden vocabulary: one verdict per finding, with the rule and the exact passage. Both verifiers quote text a script can find, which is what lets them run on a cheaper model and be checked in turn. `quality-check` is a different question again: not whether a text matches its source, but whether the sources themselves can be trusted.

**`simplify` vs `rephrase` vs `synthese`**
- `simplify` names the noise that could go while keeping all the information — it identifies the removals, `correction` applies them.
- `rephrase` rewrites dense or ambiguous content to make the actual meaning legible — it reinterprets, not just trims.
- `synthese` deliberately loses detail to extract the essential — lossy compression that produces an actionable summary.

**`explorer` vs `decision`**
Designed to run in sequence. `explorer` maps the option space without committing (breadth first). `decision` arbitrates among existing options with explicit trade-offs and a recommendation (depth). Running `decision` without `explorer` risks locking in too early from an incomplete set.

**`critique` vs Advisory archetypes (e.g. `dixieme-homme`, `contrarian`)**
`critique` is a quality check on *your own artifact* — editorial, finding flaws in what you produced. Advisory archetypes challenge *a belief, plan, or decision* from a specific perspective — they operate at the level of reasoning and conviction, not text quality. Use `critique` to improve a document; use Advisory to stress-test a conclusion.

</details>

<details>
<summary><b>⚔️ Advisory — perspective archetypes</b> — 10 skills</summary>


Each skill forces a specific cognitive stance. They are not interchangeable — pick based on what you need to stress-test. Run `chairman` after several to synthesize.

`contrarian`, `firstprinciples`, `expansionist`, `outsider`, `executor` and `chairman` take their roles from Ole Lehmann's "LLM Council", built on Andrej Karpathy's method; see [Credits](#credits).

---

#### `contrarian` — Failure points & unverified assumptions

**Origin:** The *advocatus diaboli* (devil's advocate), formalized in Catholic canon law. The Church required a designated critic to argue against every proposed canonization to ensure rigor. Adopted in structured decision-making and intelligence analysis to institutionalize dissent. As a *request*, though, "play devil's advocate" routes to `dixieme-homme`, which pleads the full opposing thesis — `contrarian` digs into the single breaking point.

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

</details>

<details>
<summary><b>🗺️ Strategy & Intelligence</b> — 4 skills</summary>


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

**What it doesn't do:** Does not track KPIs in real time (that's a KPI dashboard's job, see [ix-recipes](https://github.com/amiel-35/ix-recipes)). Does not evaluate current performance. It defines the monitoring setup before execution begins.

**Use when:** After a decision or plan is formed, before execution starts. Especially powerful after `futurs-alternatifs` (leading indicators per scenario) or `ach` (signals that would confirm or invalidate the retained hypothesis).

---

#### `quality-check` — Audit the raw evidence

**What it does:** Evaluates the structural solidity of the information on which a reasoning, decision, or analysis rests — before it becomes a foundation. Checks source type, corroboration, freshness, author bias, and flags informational gaps.

**What it doesn't do:** Does not evaluate the conclusions. Does not evaluate the reasoning itself. Only the quality of the raw material. Does not check a text claim by claim against a given source — that is `fact-check`.

**Use when:** Before making a decision that rests on external data, market figures, or cited sources. Use it before `decision` or a recommendation note when you're not sure the sources are solid.

> `quality-check` audits information sources. `key-assumptions` audits the hidden premises of a reasoning. Both are pre-decision hygiene, different layers.

</details>

<details>
<summary><b>🧩 Scoping & production</b> — 4 skills</summary>


From a vague need to material ready to produce: clarify, structure, split, record. The domain deliverables that follow (PRD, specs, offers, job descriptions…) live in [ix-recipes](https://github.com/amiel-35/ix-recipes).

---

#### `cadrage` — Clarify before producing

**What it does:** Explores and clarifies a vague or incomplete need — surfacing intent, constraints, hypotheses, and decision points before any production begins. The reformulated need states the goal, never the artefact the request names: that artefact is a constraint when justified, a hypothesis with its own open question otherwise, and consultation-imposed deliverables are listed apart as constraints on the response. Produces a clarification report and recommended next steps.

**What it doesn't do:** Does not produce a brief or spec directly. It's the step that makes `brief` possible when the input is too fuzzy.

**Use when:** The request is too ambiguous to brief directly. When you need to align on what's actually being asked before committing.

> `cadrage` asks the right questions. `brief` writes the structured answer. Run them in sequence when the need is unclear.

---

#### `brief` — Vague need → structured brief

**What it does:** Transforms a vague need, request, or idea into a structured, actionable brief — purpose, constraints, success criteria, and exclusions. Separates the need from the solutions the request names: the intent states the goal; a named solution becomes a constraint when the input says why this means rather than another, a hypothesis « to validate » otherwise; what a consultation imposes on the response (deliverables, pieces) is listed apart. The output is usable as input for any downstream production skill.

**What it doesn't do:** Does not clarify an incomplete brief when you don't yet know what you want (use `cadrage` for that). Does not produce a spec.

**Use when:** You know what you want to build but need to structure it before handing it off.

---

#### `analysis` — Decompose before specifying

**What it does:** Decomposes a complex need into independent, prioritized lots before spec or delivery begins. Produces a structured decomposition that feeds a PRD, a sprint, or a project plan.

**Use when:** The subject is dense or multi-dimensional and needs to be broken down before anyone can spec or estimate it. Upstream of a PRD or a feature spec (see [ix-recipes](https://github.com/amiel-35/ix-recipes)) for complex initiatives.

---

#### `compte-rendu` — Raw notes → structured record

**What it does:** Transforms raw meeting notes into a structured meeting record — decisions made, actions assigned (owner + due date), open questions, and next steps. Distinguishes what was decided from what was discussed.

**Use when:** After any meeting that produced decisions or actions. Output is directly shareable and keeps accountability clear.

</details>

---

## Typical pipelines

```
critique → correction → deliver
explorer → decision   → deliver
cadrage  → questioning → explorer → decision
          (named solutions: hypotheses → questions → default set aside;
           explorer breadth `standard` stays inside the named vehicle,
           `broad` leaves it with one positive constraint per run)
critique → fact-check → correction → fact-check → deliver → controle-qualite
          (fact-check first on what the critique says it observed, then on
           the facts the corrections add; controle-qualite on the deliverable
           against the template and the client's rules before it goes out)
controle-qualite sweep → controle-qualite verdict
          (detector, then judge, on the same reference)
          simplify  (standalone)
          rephrase  (standalone)
```

Chains that go through domain skills (`research` → `analyse-concurrentielle` → `decision`, `brief` → `prd` → `feature-spec`, procurement, hiring) live in [ix-recipes](https://github.com/amiel-35/ix-recipes#workflows).

---

## Installation

### Claude Code (plugin — recommended)

The repo is a Claude Code plugin marketplace (`.claude-plugin/marketplace.json` points at the `dist/` plugin root). One-time install, works on macOS and Linux:

```bash
claude plugin marketplace add amiel-35/ix-skills
claude plugin install ix-skills@ix-skills
```

Skills are namespaced: `critique` becomes `/ix-skills:critique`. To pull updates later:

```bash
claude plugin marketplace update ix-skills
claude plugin update ix-skills
```

Then restart Claude Code. Releases are resolved by the manifest version (`dist/.claude-plugin/plugin.json`), see `CHANGELOG.md`.

In the Claude Code desktop app, the same two steps are available through the `/plugin` command.

The domain skills (HR, legal, finance, procurement, product, tech) are a separate plugin that builds on this one: `claude plugin marketplace add amiel-35/ix-recipes`, then `claude plugin install ix-recipes@ix-recipes` (see [ix-recipes](https://github.com/amiel-35/ix-recipes)).

**Manual fallback** (no plugin mechanism available): symlink or copy `dist/skills` into `~/.claude/skills/`, whole folders, so that the `references/` subfolders come along (see [References](#references-annexes-read-on-demand)). Use `dist/skills` — not `skills/`: the source files carry the canonical frontmatter (`id`, `label`, `description_fr`…), not the `name`/`description` frontmatter the Agent Skills format requires, so raw `skills/<id>.md` files are **not** valid `SKILL.md` files.

### One catalogue for all the plugins (`amiel-35`)

[amiel-35/plugins](https://github.com/amiel-35/plugins) is a marketplace (named `amiel-35`) that lists ix-skills, ix-recipes and [ghost-council](https://github.com/amiel-35/ghost-council) together. Each entry points at the `dist/` folder of the plugin's own repo, so nothing changes here when a plugin is updated. In Claude Code:

```bash
claude plugin marketplace add amiel-35/plugins
claude plugin install ix-skills@amiel-35
claude plugin install ix-recipes@amiel-35      # optional, builds on ix-skills
claude plugin marketplace update amiel-35      # later: refresh, then claude plugin update ix-skills@amiel-35
```

Install a given plugin from **one** marketplace only (this catalogue *or* the repo's own): installed from both, it shows up twice. The catalogue works in the CLI; whether Cowork's "Add from repository" accepts it is **not tested yet**, so for Cowork the per-repo path below stays the documented one.

### Claude Cowork / claude.ai

**Option A — install as a plugin (batch, recommended)**

Add the repo as a plugin source: **"Add from repository"** with `amiel-35/ix-skills`. The marketplace manifest does the rest. Plugin installs carry the `references/` subfolders.

**Option B — upload a single skill**

`dist/skills/<id>/` folders are valid Agent Skills: upload one as-is in **Cowork → Customize** (or the ChatGPT Skills editor), or zip the folder yourself if a `.skill` archive is needed. Upload or zip the whole folder, `references/` subfolder included, for the skills that have one (`prioritize`, `deliver`, `critique`): without it they fall back as described in [References](#references-annexes-read-on-demand). Regenerate the folders with:

```bash
pip install -r requirements.txt
python3 build.py --target agentskills
```

### Codex CLI

Codex reads the same marketplace as Claude Code (tested with codex-cli 0.155.1):

```bash
codex plugin marketplace add amiel-35/ix-skills
codex plugin add ix-skills@ix-skills
```

The plugin lands in `~/.codex/plugins/cache/ix-skills/ix-skills/<version>/skills/<id>/`, with the `references/` subfolders. To update, run `codex plugin marketplace upgrade` and re-add the plugin if needed (see `codex plugin --help`). To remove:

```bash
codex plugin remove ix-skills@ix-skills
codex plugin marketplace remove ix-skills
```

**Name the skill in your request** ("use the prioritize skill from the ix-skills plugin to…"). Codex then reads `SKILL.md` and only the reference file it needs. On a plain request that does not name the skill, Codex did not use it in our tests.

The `amiel-35/plugins` catalogue uses `git-subdir` sources and is **not tested with Codex**: for Codex, use the per-repo marketplace above.

**Legacy installer** (copies into `~/.codex/skills/`, not re-tested on Codex 0.155):

```bash
git clone https://github.com/amiel-35/ix-skills /tmp/ix-skills
cd /tmp/ix-skills
pip install -r requirements.txt
bash scripts/install-codex.sh          # all skills
bash scripts/install-codex.sh critique # one skill
bash scripts/install-codex.sh --dry-run
```

The installer builds `codex-dist/` with `build.py` (so `python3` must have the `requirements.txt` packages), then copies each skill to `~/.codex/skills/<id>/SKILL.md`, with its `references/` subfolder when it has one. `--dry-run` writes nothing to `~/.codex` but still rebuilds `codex-dist/` locally. Without an id, everything found in `codex-dist/` is installed. Restart Codex to activate.

### Antigravity CLI (agy, Gemini)

`agy` imports a Claude-format plugin folder (tested with agy 1.3.3):

```bash
git clone https://github.com/amiel-35/ix-skills
agy plugin import ix-skills/dist
```

All skills are imported with their `references/` into `~/.gemini/config/plugins/<plugin>/`. Use `import`: `agy plugin validate` and `agy plugin install` expect a `plugin.json` at the root and do not accept this format. To import the plugins already installed in Claude Code instead (all of them): `agy plugin import claude`. To remove: `agy plugin uninstall ix-skills`.

As with Codex, **name the skill in your request**: agy then reads `SKILL.md` and only the reference file it needs.

### mystaffy

```bash
python3 build.py --target mystaffy
# or to regenerate the native ix-memory format:
python3 build.py --target ix-memory
```

Both write `mystaffy-dist/<id>/` (`manifest.json` + `skill.md`). The `references/` annexes are not copied there.

### GPT / Gemini / other LLMs (chat interfaces)

For plain chat UIs with no CLI: copy-paste the content of `skills/<id>.md` as a system prompt. The YAML frontmatter is ignored without side effects. This route has no `references/` folder: for `prioritize`, `deliver` and `critique`, paste the annexes you need after the skill (see [References](#references-annexes-read-on-demand)).

### References (annexes read on demand)

Three skills ship annexes in a `references/` subfolder next to their `SKILL.md`, and read only the one a given request needs: `prioritize` (one file per method: ICE, RICE, WSJF, MoSCoW, Kano, Eisenhower, value/effort, weighted scoring), `deliver` (HTML templates, recipient profiles) and `critique` (lenses by content type). The sources are in `partials/`; `build.py` copies them into `dist/skills/<id>/references/` (and `codex-dist/<id>/references/`).

| Installation | References |
|---|---|
| Claude Code / Cowork plugin (either marketplace) | included |
| Manual copy of `dist/skills` into `~/.claude/skills/` | included if the folders are copied whole |
| Codex (`codex plugin add`, or legacy `install-codex.sh`) | included / copied |
| Antigravity (`agy plugin import ix-skills/dist`) | included |
| Upload of a single `dist/skills/<id>/` folder (Cowork Customize, ChatGPT Skills) | included only if the `references/` subfolder is uploaded or zipped with it |
| mystaffy / ix-memory | not carried |
| GPT / Gemini (paste `skills/<id>.md`) | not carried |

Without the folder: `prioritize` applies its generic criteria and says the detailed method was unavailable, and `critique` picks lenses from its canonical list. `deliver` loses the HTML and recipient-profile guidance, so paste `partials/deliver_html.md` (HTML target) and `partials/deliver_recipient_profiles.md` (recipient given) after it. For `prioritize`, paste the file of the method you want, e.g. `partials/framework_rice.md`; for `critique`, `partials/critique_lenses.md`.

---

## Structure

```
ix-skills/
├── skills/                 ← canonical source (one .md + .mystaffy.json per skill)
├── partials/               ← reference annexes, copied into references/ of the skills that list them
├── docs/                   ← banner and design notes
├── scripts/
│   ├── install-codex.sh    ← Codex CLI installer
│   └── migrate_from_ix_memory.py
├── dist/                   ← plugin root, committed
│   ├── .claude-plugin/plugin.json   ← plugin manifest (hand-maintained, bump per release)
│   └── skills/<id>/SKILL.md         ← Agent Skills artifacts, generated by build.py
│       └── references/              ← annexes copied from partials/ (3 skills)
├── .claude-plugin/
│   └── marketplace.json    ← marketplace manifest, points at ./dist
├── mystaffy-dist/          ← mystaffy artifacts (gitignored)
├── codex-dist/             ← Codex CLI artifacts (gitignored)
├── tests/                  ← tests of the migration script
├── build.py                ← multi-target packager
├── requirements.txt
├── CHANGELOG.md            ← releases, by date
├── THIRD_PARTY.md          ← sources and licences of what skills take from public projects
├── TODO.md                 ← next chantiers (design-thinking method chains)
└── CLAUDE.md               ← contribution guide
```

---

## Build

```bash
pip install -r requirements.txt         # jsonschema, pyyaml
python3 build.py --validate
python3 build.py
python3 build.py critique
python3 build.py --target agentskills   # dist/skills/<id>/SKILL.md + references/ — commit the result
python3 build.py --target cowork        # validate dist/.claude-plugin/plugin.json
python3 build.py --target mystaffy --domain cognitif
python3 build.py --target ix-memory
python3 build.py --target codex         # codex-dist/<id>/SKILL.md + references/
claude plugin validate dist             # validate the plugin (Claude Code CLI)
```

---

## Sibling projects

[ix-recipes](https://github.com/amiel-35/ix-recipes) holds the recipes built on these atoms: the domain skills (HR, legal, finance, procurement, product, tech), moved out of ix-skills in 4.0.0 with their history, and workflows that chain the atoms. ix-recipes depends on ix-skills, never the other way round.

[ghost-council](https://github.com/amiel-35/ghost-council) is the author's other collection: philosophers' reasoning methods encoded as skills (Popper, Kant, Pascal, Wittgenstein…), and `/council`, which makes several independent angles deliberate on a decision and returns the map of disagreements. The two complement each other: ix-skills encodes ways of working, ghost-council ways of thinking. The advisory postures of ix-skills (`dixieme-homme`, `contrarian`, `red-team`, `key-assumptions`, `expansionist`…) can sit on the council as `ix:<id>`, next to `ghost:popper`.

---

## Contributing

Fork, modify, PR. Read `CLAUDE.md` for conventions.

Read [`CLAUDE.md`](CLAUDE.md) for the canonical skill format, naming rules and checklists, and [`CHANGELOG.md`](CHANGELOG.md) for releases.

---

## Credits

Several skills take roles or ideas from public projects: Ole Lehmann's and Andrej Karpathy's "LLM Council" for the advisory postures, Jesse Vincent's obra/superpowers for `cadrage` and `revue-feedback`, Anthropic's knowledge-work-plugins for `prioritize`. Details, with licences and what was taken, are in [`THIRD_PARTY.md`](THIRD_PARTY.md).

---

## License

MIT, see [LICENSE](LICENSE).
