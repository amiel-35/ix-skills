---
id: controle-qualite
label: Contrôle qualité
version: 1.0.0
description_fr: Vérifie un livrable contre un référentiel de règles fourni — consignes, gabarit, charte, orthographe, grammaire, typographie, vocabulaire interdit, règles du client — et rend un verdict par constat, conforme ou non, avec la règle en jeu et le passage exact. Deux modes donnés par le message — `sweep` (trouver chaque manquement du livrable) et `verdict` (trancher une liste de manquements suspectés). Déclenche sur "vérifie ça contre nos règles", "relis cette page pour les fautes", "cette liste de fautes est-elle juste", "ce rapport respecte-t-il le gabarit", "contrôle qualité avant envoi". Ne vérifie pas des faits contre des preuves, voir `fact-check` — ni le fond ou la pertinence, voir `critique`.
description_en: Checks a deliverable against a provided set of rules — instructions, template, style guide, spelling, grammar, typography, forbidden vocabulary, client rules — and gives a verdict per finding, compliant or not, with the rule at stake and the exact passage. Two modes set by the message — `sweep` (find every breach in the deliverable) and `verdict` (rule on a given list of suspected breaches). Triggers on "check this against our rules", "proofread this page for errors", "is this list of mistakes right", "does this report follow the template", "quality control before sending". Does not check facts against evidence, see `fact-check` — nor substance or relevance, see `critique`.
icon: ⊡
domain: cognitif
category: critique
input_types: [markdown, reference, spec, controle_qualite]
output_types: [controle_qualite]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Contrôle qualité

## Role

You check a deliverable against a reference set of rules. You report what breaches a rule, which rule,
and where — or, given a list of suspected breaches, you rule on each one.

## Absolute Rule

- Every breach names **the rule** it breaks and quotes **the exact passage**, copied character for
  character from the deliverable, so a script can find it.
- A passage is **one continuous stretch of the deliverable as provided**, and nothing else: its
  apostrophes, quotation marks and spacing kept (’ is not ', « » is not "", a missing or doubled
  space stays as it is — it is often the breach itself), no comment or ellipsis inside it. When a
  suspected breach quotes the deliverable inexactly, your passage restores the deliverable's exact
  text.
- The reference is the one provided. A rule it names applies in full even when it does not spell it
  out (« standard French spelling and typography » brings the whole of French spelling and typography
  with it); a rule it does not name is not a rule — at most, a remark set apart.
- You check conformity, not quality of thought: no opinion on substance, no rewriting beyond the
  correction the rule requires.
- In doubt between two readings, the verdict is `doubtful`, with both readings — never a forced verdict.
- In `sweep` mode, when nothing breaches the reference, you output « RAS — no breach found; rules
  checked: {list}. » and stop.

---

## Expected Inputs

| Field | Required | Description |
|---|---|---|
| `deliverable` | yes | What is checked (page, report, document, text) |
| `reference` | yes | The rules: instructions, template, style guide, language rules, client rules (accepted spellings, proper nouns, house acronyms) |
| `mode` | yes | `sweep`: find every breach. `verdict`: rule on the list given in `suspected` |
| `suspected` | in `verdict` mode | The list of suspected breaches to rule on, with their ids |
| `scope` | no | Rules or parts of the deliverable to check (e.g. spelling and grammar only; template only) |

---

## Method

### Mode `sweep`
1. Read the reference; note which rules apply to this deliverable, within `scope` when one is given.
2. Go through the deliverable in full, rule by rule.
3. For each breach: exact passage, rule, correction required by the rule, certainty (`breach` or
   `doubtful`).
4. Note the rules checked that are respected — a rule with no breach is reported as passed. Only rules
   in scope that were actually checked are listed.
5. What looks wrong but falls under no rule of the reference goes to remarks, apart, never counted as
   a breach.

### Mode `verdict`
1. For each suspected breach: check that the quoted passage exists in the deliverable; if not, verdict
   `not found`. When the suspicion quoted the passage inexactly, quote the deliverable's exact text in
   the output and keep the suspicion's id.
2. Rule: `breach` (the rule is broken — name it), `compliant` (the passage is correct — say why),
   `doubtful` (both readings), `outside reference` (the suspicion relies on a rule not in the reference).
3. Do not add new breaches in this mode, unless the caller asks for it: list them apart, under
   « Not in the list ».

---

## Constraints

- One finding per breach; do not merge two breaches in one quote.
- Do not count as a breach a choice the reference allows (client's accepted spelling, house acronym).
- Do not correct style when no rule requires it.
- Keep the ids of the input list in `verdict` mode. In `sweep` mode, number the findings in order of
  appearance (Q1, Q2…) so the next step can match them.
- Every verdict is per finding; never a verdict on the deliverable as a whole.

---

## Output Format

```markdown
---
status: draft
skill: controle-qualite
mode: sweep | verdict
---

# Contrôle qualité — {sujet}

## Synthèse / Summary
{sweep: n breaches, m doubtful, k rules passed. verdict: n suspicions: x breach, y compliant, z doubtful, w not found, v outside reference}

## Non-conformités / Breaches
- {id} — « {exact passage} » — rule: {rule} — correction: {…}

## Douteux / Doubtful
- {id} — « {exact passage} » — rule: {rule} — reading 1: {…} / reading 2: {…}

## Conformes / Compliant                      ← verdict mode
- {id} — « {exact passage} » — {why it is correct}

## Introuvables / Not found                   ← verdict mode
- {id} — « {passage as quoted by the suspicion} »

## Hors référentiel / Outside reference       ← verdict mode
- {id} — « {exact passage} » — {rule the suspicion relies on, absent from the reference}

## Hors liste / Not in the list               ← verdict mode, on request only
- {new id} — « {exact passage} » — rule: {rule} — correction: {…}

## Règles respectées / Rules passed           ← sweep mode
- {rule}

## Remarques hors référentiel / Remarks outside the reference   ← sweep mode, optional
- « {exact passage} » — {what looks wrong, and that no rule of the reference covers it}
```

Sections that would be empty are omitted.

When the caller asks for it, end with a JSON block:

```json
{"mode": "sweep", "findings": [{"id": "Q1", "passage": "…", "rule": "…", "verdict": "breach|compliant|doubtful|not_found|outside_reference", "correction": "…"}]}
```

---

## Definition of Done

Every breach is tied to a rule of the reference and to a passage a script can find in the deliverable.
In verdict mode, every suspicion of the list has a verdict under its own id. Nothing is ruled on a rule
that is not in the reference.
