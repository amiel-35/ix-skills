# TODO

## Skill idea: `structured-analysis`

- Source: [CIA - A Tradecraft Primer: Structured Analytic Techniques for Improving Intelligence Analysis](https://www.cia.gov/resources/csi/static/Tradecraft-Primer-apr09.pdf), March 2009.
- Related source: [CIA FOIA - The "Red Team"](https://www.cia.gov/readingroom/docs/CIA-RDP88B00443R001500040025-4.pdf), February 1, 1984.
- Related source: [CIA - Combatting Mind-Set](https://www.cia.gov/resources/csi/static/Combating-Mindset.pdf), Jack Davis.
- Related operational source: [NCSC - Key Assumptions Check](https://www.ncsc.nl/analysetools/key-assumptions-check).
- Initial trigger: article notes on key assumptions, but the source goes broader than the existing `key-assumptions` skill.
- Positioning: create a broader structured analysis skill, with `key-assumptions` kept as a focused sub-skill.
- Likely domain: `strategy`.
- Likely category: `critique` or `decision`.
- Possible id: `structured-analysis` or `analyse-structuree`.

Scope to explore:

- Key Assumptions Check
- Quality of Information Check
- Indicators / signposts of change
- Analysis of Competing Hypotheses
- Devil's Advocacy
- High-impact / low-probability scenarios
- What-if analysis
- Red Team Analysis
- Alternative Futures Analysis

Specific Red Team angle from the 1984 CIA memo:

- Treat red teaming as an independent advisory challenge function, not as a replacement for existing analysis teams.
- Focus on how an adversary or counterparty could exploit blind spots in assumptions, monitoring, verification, compliance, concealment, or deception.
- Keep outputs simple and short enough for senior decision-makers to use.
- Avoid purely ideological challenge roles; prioritize practical, reality-based opposition analysis.

Specific mind-set angle from Jack Davis:

- Mind-set is inevitable and useful when evidence is incomplete, ambiguous, time-constrained, or predictive.
- The risk is not having a mind-set, but letting it silently filter new information, dismiss anomalies, or force premature simplification.
- The skill should help externalize the reasoning: write down knowns, assumptions, variables, sequences, actors, incentives, and uncertainty.
- Include "mind-set insurance": multiple explanations, multiple projections, specific decision questions, low-probability/high-impact alternatives, and practical implications.
- Encourage testing the one or two assumptions that would undermine the dominant mental model if false.

Specific Key Assumptions Check angle from NCSC:

- Use the method to make assumptions explicit and assess confidence when information is incomplete.
- Apply early in an analysis, and also when reviewing a risky, uncertain, or groupthink-prone analysis.
- Run as a small diverse-group workshop when possible: individual assumption generation, shared visibility, critical discussion, then categorization.
- Use practical challenge questions: Why do we believe this? When would it stop being true? What if it is wrong? How much would it affect the analysis?
- Classify assumptions as S/C/U: Solid, Correct with caveats, or Uncertain.
- Turn uncertain assumptions into follow-up research, monitoring, or validation actions.

Draft output shape:

1. Facts, assumptions, unknowns
2. Key assumptions and invalidation conditions
3. Evidence quality and missing information
4. Competing hypotheses
5. Disconfirming evidence
6. Indicators to monitor
7. Low-probability / high-impact scenarios
8. Red-team challenge
9. Decision-ready synthesis

Open question:

- Should this be a single broad skill, or a parent skill that routes to existing/future focused skills such as `key-assumptions`, `ach`, `red-team`, `outside-in`, and `futurs-alternatifs`?
