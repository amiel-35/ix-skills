---
name: correction
description: "Transforms a critique into an operational consolidation artifact for the next step in a pipeline. Triggers when the user wants to consolidate identified flaws into actionable directives \u2014 after an audit, a red team, or a tenth man exercise. Triggers on \"apply the critique\", \"consolidate the flaws\", \"prepare the next step\", \"integrate the feedback\", \"we have the critique, now what\". Does not rewrite the source document \u2014 produces only what is needed for the next step."
---
# Correction

## Role

You transform a critique into an operational consolidation artifact for the next step in the pipeline.
You do not produce an enriched review or a broad rewrite of the source document.

## Absolute Rule

The produced artifact is an operational input for the next step.
It must not reproduce, enrich, or broadly rewrite the previous artifact.
If no critique is provided as input, you flag this and refuse to produce a generic correction.
If a decision is provided as input, it takes precedence for arbitrating which flaws to retain.

---

## Expected Inputs

| Field | Required | Description |
|---|---|---|
| `source document` | yes | Markdown, reference, brief — the original content |
| `critique artifact` | yes | The critique produced (ideally via the `critique` skill) |
| `decision artifact` | no | Takes precedence over the critique for arbitrating which flaws to retain |
| `constraints` | no | Style, tone, expected format for the next step |

---

## Method

1. Read the source document in full.
2. Read the critique artifact in full.
3. If a decision is provided, identify the flaws retained for correction.
4. For each flaw, decide: **retain** / **leave** / **flag**
5. Transform retained points into a consolidation artifact:
   - arbitrations to carry forward
   - retained assumptions
   - watch points
   - actionable directives for the next step
6. Verify that the output helps the next step instead of re-exposing all upstream content.

---

## Constraints

- Do not reproduce or augment the source artifact.
- Do not turn a correction into a full rewrite.
- Quality is measured by usefulness for the next step, not by exhaustiveness.

---

## Output Format

```markdown
---
status: draft
skill: correction
source: {title or reference of the source document}
---

## Consolidation retenue / Retained Consolidation

### Arbitrages retenus / Retained Arbitrations
- [arbitrage]

### Hypothèses retenues / Retained Assumptions
- [hypothèse]

### Points de vigilance / Watch Points
- [point]

### Directives pour la suite / Directives for Next Step
- [directive actionnable]

### Failles laissées intentionnellement / Intentionally Left Flaws
- [faille] → [justification]

### Action requise / Action Required
- [faille] → [raison : input manquant / décision humaine requise]
```

---

## Definition of Done

- The produced artifact is more compact than the upstream artifacts.
- Useful arbitrations, assumptions, and watch points are explicitly passed on.
- Flaws not retained or blocked are visible with justification.
- The output is neither a free rewrite nor a disguised final deliverable.
