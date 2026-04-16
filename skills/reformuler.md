---
id: reformuler
label: Reformuler
version: 1.0.0
description_fr: Interprète et restitue le sens réel d'un contenu dense, ambigu ou jargonneux dans un contexte donné. Déclenche quand l'utilisateur veut comprendre ce que quelque chose veut vraiment dire dans un autre registre — analyse de besoin, lecture juridique, traduction métier↔tech, transposition réglementaire. Déclenche sur "qu'est-ce que ça veut dire concrètement", "reformule pour l'équipe tech", "traduis en termes métier", "restitue le sens". Ne simplifie pas, ne critique pas — transpose le sens.
description_en: Interprets and restates the real meaning of dense, ambiguous, or jargon-heavy content in a given context. Triggers when the user wants to understand what something really means in another register — requirements analysis, legal reading, business↔tech translation, regulatory transposition. Triggers on "what does this concretely mean", "rephrase for the tech team", "translate into business terms", "restate the meaning". Does not simplify, does not critique — transposes the meaning.
icon: ⟳
domain: cognitif
category: atome
input_types: [brief, markdown, reference, spec, critique]
output_types: [reformulation]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Reformuler

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
5. If a target context is provided, anchor it: *"in our context, this concretely means..."*
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
skill: reformuler
register: [target register]
target_context: [if provided]
---

# Rephrasing — {subject}

## Source Register and Context
{identification}

## Rephrased Content
{rephrasing with status: certain / probable / fragile}

## Implications
- ...

## Resistant Areas
- [area] → [reason]

## Open Questions
- ...
```

---

## Definition of Done

- The rephrased content is readable in the target register without re-reading the source.
- Fragile interpretations are visible.
- Ambiguous areas are flagged, not filled in.
