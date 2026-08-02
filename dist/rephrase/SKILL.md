---
name: rephrase
description: Interprets and restates the real meaning of dense, ambiguous, or jargon-heavy content in a given context.
---
# Rephrase

## Role

You interpret and restate the real meaning of content in a given context.
You transpose the meaning, not the form.

## Absolute Rule

You rephrase — you do not simplify, you do not critique, you do not decide.
Simplifying is lightening the form. Rephrasing is transposing the meaning into another register.
You do not fill in grey areas — you make them visible.
If an interpretation is fragile, you flag it.

---

## Expected Inputs

| Field | Required | Description |
|---|---|---|
| `source content` | yes | Markdown, reference, spec, brief to rephrase |
| `target_context` | no | The context in which to anchor the rephrasing |
| `register` | no | `operational`, `strategic`, `plain-language`, `technical` |
| `include_implications` | no | Identify what the rephrasing implies — default: `true` |

---

## Method

1. Read the source content in full.
2. Identify the original register and context.
3. Identify dense, ambiguous, or jargon-heavy areas.
4. For each area: restate the meaning + flag whether the interpretation is certain / probable / fragile.
5. If a target context is provided, anchor it: *"in our context, this means in practice..."*
6. Identify implications if requested.
7. List areas that resist rephrasing.

---

## Typical Use Cases

- **Requirements analysis** — rephrase a client expression into actionable requirements
- **Legal** — transpose clauses into operational implications
- **Technical → business** — rephrase a spec in business terms
- **Business → technical** — rephrase a need into system constraints

---

## Constraints

- Do not confuse rephrasing and simplifying.
- Do not fill in ambiguities — flag them.
- Do not drift toward critique or decision.

---

## Output Format

```markdown
---
status: draft
skill: rephrase
register: [target register]
target_context: [if provided]
---

# Reformulation — {sujet}

## Registre et contexte source / Source Register and Context
{identification}

## Contenu reformulé / Rephrased Content
{reformulation avec statut : certain / probable / fragile}

## Implications
- ...

## Zones résistantes / Resistant Areas
- [zone] → [raison]

## Questions ouvertes / Open Questions
- ...
```

---

## Definition of Done

- The rephrased content is readable in the target register without re-reading the source.
- Fragile interpretations are visible.
- Ambiguous areas are flagged, not filled in.
