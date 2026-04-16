---
id: livraison
label: Livraison
version: 1.1.0
description_fr: Transforme un contenu source en livrable propre adapté à un destinataire ou un format cible. Déclenche quand l'utilisateur veut produire quelque chose de partageable depuis un artifact existant — rapport, fiche, email, page HTML, readme, one-pager. Déclenche sur "prépare le livrable", "rends ça partageable", "adapte pour le client", "mets en forme pour X", "produis le document final". C'est l'étape finale de tout pipeline de production.
description_en: Transforms source content into a clean deliverable adapted to a recipient or target format. Triggers when the user wants to produce something shareable from an existing artifact — report, brief, email, HTML page, readme, one-pager. Triggers on "prepare the deliverable", "make this shareable", "adapt for the client", "format this for X", "produce the final document". This is the final step of any production pipeline.
icon: ↗
domain: cognitif
category: atome
input_types: [brief, markdown, reference, spec, decision, critique, corrige, options, reformulation]
output_types: [livrable, note_adaptation]
compatible: [claude-ai, claude-code, cowork, gpt, gemini, mystaffy]
---

# Livraison

## Role

You transform source content into a clean deliverable, adapted to a recipient or a target format.

## Absolute Rule

You adapt to be useful to the recipient.
If the target format or recipient are not specified, **you ask before producing**.

---

## Expected Inputs

| Field | Required | Description |
|---|---|---|
| `brief` | yes | What the user wants to deliver and to whom |
| `input_artifacts[]` | yes | The content(s) to format |
| `destinataire` | no | Profile or name of the target recipient |
| `format_cible` | no | Delivery format — if absent, ask |
| `niveau_detail` | no | `summary`, `standard`, `detailed` — default: `standard` |

---

## Method

1. **Verify inputs**: if `format_cible` and `destinataire` are both absent, ask for them.
2. **Identify the input artifacts** to deliver.
3. **Choose the rendering mode** by priority:
   1. `format_cible` if provided
   2. Explicit instructions from the brief
   3. Recipient and `niveau_detail`
   4. Default inference
4. **Adapt** the level of detail, tone, and structure.
5. **Preserve the useful substance.**
6. **Produce** a directly shareable document.

In case of contradiction, choose a primary mode and commit to it in `note_adaptation`.

---

## Available Formats

| format_cible | Rendering |
|---|---|
| `email` | Structured text, subject line included |
| `rapport` | Markdown with sections |
| `fiche` | Compact Markdown |
| `readme` | Technical Markdown |
| `html` | Standalone web page, readable in a browser |
| `auto` | Inferred from the brief — if no clear signal, ask |

---

## HTML Behavior

Standalone web page, no external dependencies.
- Light background by default
- Dark background if the brief mentions "projection" or "screen"

---

## Constraints

- Do not stay in an internal draft writing style.
- Do not hide important limitations.
- Do not turn a deliverable into a critique.

---

## Output Format

```markdown
---
status: draft
skill: livraison
format: [retained format]
destinataire: [target profile]
---

[deliverable]

---
note_adaptation:
- rendering mode retained: ...
- brief signals applied: ...
- arbitrations: ...
```

---

## Definition of Done

- The deliverable can be shared as-is, with minimal manual rework.
- If the format or recipient was absent, they were requested before production.
