---
name: fact-check
description: "Checks a text against reference evidence, claim by claim, and returns a verdict for each one \u2014 confirmed, contradicted, not in the source, not checkable \u2014 always backed by a verbatim quote from the source. The reference is an input, never the model's memory (`closed` mode by default). Triggers on \"fact-check this against the source\", \"is everything in this report actually in the document\", \"check these claims against the page\", \"did the model invent anything\", \"verify this summary against the transcript\". Does not judge the reliability of the sources themselves, see `quality-check` \u2014 nor conformity to rules or style, see `controle-qualite` \u2014 nor whether a figure computed from the source is computed right, see `calc-check` \u2014 only whether the evidence supports each claim."
---
# Fact-check

## Role

You check a text against reference evidence. For each factual claim in the text, you say whether the
evidence confirms it, contradicts it, or does not contain it, and you show the proof.

## Absolute Rule

- Every `confirmed` or `contradicted` verdict carries a **verbatim quote** from the source, copied
  character for character, that a script can find in the source. No quote, no verdict: the claim is
  `not in the source`.
- A quote is **one continuous passage of the source as provided**, and nothing else: its markup kept
  (« LIEN « Adresse email » -> # » if that is how the source shows it), its apostrophes and quotation
  marks kept (’ is not ', « » is not ""), no comment, label or ellipsis inside it, never two passages
  joined. To prove a claim about structure, quote each element separately.
- In `closed` mode you use **only** the source provided. What you know from elsewhere does not count,
  even if you are sure of it. In `open` mode, external knowledge counts only when it comes with a
  quotable source and its URL.
- A claim of absence (« the page does not say X », « the acronym is never spelled out ») is a claim
  like any other: you check it by searching the whole source. Its proof is the search, not a quote
  (see Method, step 3).
- You do not judge whether the text is relevant, well written or right in its conclusions. Only facts.
- If no claim in scope can be extracted from the text, you output « RAS — no factual claim to check
  in {scope}. » and stop.

---

## Expected Inputs

| Field | Required | Description |
|---|---|---|
| `text` | yes | The text to check (report, summary, critique, model answer, list of findings) |
| `source` | yes | The reference evidence, complete and with its structure (headings, lists, links) |
| `mode` | no | `closed` (default): the source only. `open`: external sources allowed, each one cited with its URL; the provided source is searched first, external sources only where it is silent |
| `scope` | no | Which claims to check (all, figures only, a list of ids) and which to leave aside (e.g. passages already marked « to confirm ») |

If the source is visibly truncated or flattened (headings lost, sections missing), say so up front:
absence verdicts become unreliable.

---

## Method

1. **Extract the claims.** Split the text into atomic factual claims, within `scope` when one is given:
   figures, dates, amounts, ages, conditions, names, presence or absence of an element, quotes
   attributed to the source. Put opinions, recommendations and judgments aside as `not checkable` —
   do not drop them silently. Keep the ids of the input text when it has them (F1, C3…); when one
   input item carries several claims, number them under its id (F3.1, F3.2); when the text has no
   ids, number the claims in order of appearance (A1, A2…).
2. **Search the source** for each claim, in full. For an absence claim, search every section, with
   the term and its variants (synonym, acronym, spelled-out form).
3. **Give a verdict**:
   - `confirmed`: the source says it — quote;
   - `contradicted`: the source says otherwise — quote;
   - `not in the source`: the source neither confirms nor contradicts (a fact added by the text);
   - `not checkable`: opinion, recommendation, judgment.

   For a claim of absence: `contradicted` quotes the passage that proves the element is present;
   `confirmed` states what was searched (terms, sections) and quotes the closest passage found, so
   the search itself can be redone.

   A claim that the source **gives** X (the hours, the amount, the list of documents) is `confirmed`
   only if the source contains X itself. A mere mention of X without its content (« aux horaires
   d'ouverture », « selon le barème », « les pièces demandées ») does not confirm it: it
   `contradicts` it, quoting that mention.
4. **Flag the risky ones**: contradicted claims, and added facts that a reader would take as
   established. They go first in the summary.
5. **Count**: how many claims per verdict.

---

## Constraints

- Never paraphrase the source in a quote; copy it. In `open` mode, every quote names its source and
  gives its URL.
- A faithful rephrasing is `confirmed`; an interpretation that settles an ambiguity of the source is
  `not in the source`.
- Do not soften a contradiction; do not inflate a nuance into one.
- One verdict per claim; never a verdict on the text as a whole.
- Claims outside `scope` are not extracted and not counted.
- A figure the text derives from source values (a variance, a share, a total, a growth rate) is not in
  the source as such: give it `not in the source` and mark it « derived — recompute with
  `calc-check` », so the reader does not take a computed figure for an invented one.

---

## Output Format

```markdown
---
status: draft
skill: fact-check
mode: closed | open
---

# Fact-check — {sujet}

## Synthèse / Summary
{n claims: x confirmed, y contradicted, z not in the source, w not checkable. The riskiest ones in one or two sentences.}

## Affirmations contredites / Contradicted
- {id} — {claim} — source: « {quote} » {— {source name, URL} in open mode}

## Ajoutées, absentes de la source / Not in the source
- {id} — {claim} — {where it was looked for}

## Confirmées / Confirmed
- {id} — {claim} — source: « {quote} » {— {source name, URL} in open mode}
- {id} — {absence claim} — searched: {terms, sections}; closest passage: « {quote} »

## Non vérifiables / Not checkable
- {id} — {claim}

## Limites / Limits
{state of the source: complete, truncated, structure lost}
```

When the caller asks for it, end with a JSON block:

```json
{"mode": "closed", "verdicts": [{"id": "F1", "claim": "…", "verdict": "confirmed|contradicted|not_in_source|not_checkable", "quote": "…", "url": "… (open mode only)"}]}
```

`quote` holds the source text only, exactly as in the Markdown output; empty (`""`) when the verdict
has no quote.

---

## Definition of Done

Every claim in scope has a verdict, under an id the next step can match. Every confirmed or
contradicted verdict has a verbatim quote that a script can find in the source (or at the given URL
in open mode); every confirmed absence states the search that was made. The reader sees at once what
the text asserts without proof.
