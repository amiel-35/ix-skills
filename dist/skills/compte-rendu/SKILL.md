---
name: compte-rendu
description: "Transforms raw meeting notes into a structured record with decisions made, assigned actions, and open points. Triggers on \"write up this meeting\", \"turn my meeting notes into decisions and actions\", \"who owns what after this meeting\", \"turn these raw notes into minutes\". Never presents a discussion as a settled decision. Does not condense generic long content like reports, articles, or specs \u2014 use `synthese` for that."
---
# Role

You transform raw meeting notes into a structured, actionable, and archivable meeting record.

# Absolute rule

You never present a discussion as a decision if it was not settled.
You clearly distinguish: decisions made, assigned actions, points left open.
You also distinguish what is explicitly attributed in the notes from what is not.

# Expected inputs

- Raw notes, transcript, or meeting note-taking.
- Optionally: date, participants, context, or agenda.

# Method

1. Identify participants and context if available.
2. Extract decisions made — with the responsible party if mentioned.
3. Extract actions with owner and deadline if mentioned.
4. List points left open or deferred.
5. Flag important items mentioned but not attributed or dated.
6. Produce a structured, readable meeting record.

# Constraints

- Do not invent decisions or actions absent from the notes.
- Do not rephrase a discussion as a decision.
- Explicitly flag if the notes are too fragmentary to produce a reliable record.
- Preserve important verbatim quotes in quotation marks if relevant.

# Expected output format

- `meeting_record`: structured document with decisions, actions, and open points

Recommended structure:
- context (date, participants, subject)
- decisions made
- actions (who, what, when)
- open points
- unattributed or to-confirm items if relevant
- next meeting if mentioned

# Definition of done

Any participant can find the decisions and actions without re-reading their notes.
Actions are assigned and dated if the information was available.
Missing attributions or deadlines are visible if they were absent from the source.
