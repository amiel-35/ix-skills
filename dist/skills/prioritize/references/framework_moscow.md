# Reference: MoSCoW

**Origin:** Dai Clegg (Oracle, 1994), formalised in the DSDM / Agile Business Consortium method. Scope negotiation for a fixed deadline or budget.

## When to use
Deciding what goes into a release, a project phase or a contract scope. It sorts into classes, it does not rank inside a class — combine with another framework if an order within "Must" is needed.

## Classes
- **Must have** — without it the delivery fails: unusable, unsafe, unlawful, or the goal is not met, and there is no workaround. Test: "If this is missing, do we cancel or delay the delivery?" Yes → Must.
- **Should have** — important, painful to leave out, but a workaround exists (manual step, temporary process).
- **Could have** — desirable, small impact if left out. The contingency: dropped first when time runs short.
- **Won't have (this time)** — explicitly out of this delivery, recorded so it is not lost.

## Balance rule (DSDM guidance)
Musts should not exceed about 60% of the available effort; Coulds around 20% act as contingency. If Musts exceed 60%, the plan has no margin: say so.

## Procedure
1. State the delivery and its deadline or budget.
2. Start every item as "Won't" or "Could" and make each one argue its way up — not the reverse.
3. Challenge every Must with the test above; downgrade any Must that has a workaround.
4. Check the 60% rule against effort estimates.

## Pitfalls
- Everything is Must: then nothing is. Report the share of Musts.
- "Won't" read as "never": it means not this time.
- Classes assigned by who shouts loudest — write the reason for every Must.

## Output columns
Item | Class | reason (for Must: what fails without it) | effort | running % of capacity
