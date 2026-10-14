# Reference: WSJF (Weighted Shortest Job First)

**Origin:** Don Reinertsen's cost-of-delay economics, popularised by SAFe. Sequencing work when delay costs money.

## When to use
A queue of jobs competing for the same capacity, where some lose value fast (deadlines, market windows, risks growing). Not for one-off tasks or when no item is time-sensitive (ICE is enough).

## Formula
WSJF = Cost of Delay ÷ Job size

In SAFe, Cost of Delay = User-business value + Time criticality + Risk reduction / opportunity enablement.

## Scoring (relative, not absolute)
- Use the modified Fibonacci scale 1, 2, 3, 5, 8, 13, 20.
- Score **one column at a time across all items**: give the smallest item in that column a 1 and size the others relative to it. Every column has at least one 1.
- **Time criticality**: does value decay with time? Is there a fixed date? Will users wait or leave?
- **Risk reduction / opportunity enablement**: does it lower future risk or unlock other work?
- **Job size**: relative effort (or duration) — a proxy, not an estimate in days.

## Procedure
1. List items; check they are of comparable granularity.
2. Score the three Cost of Delay columns, then Job size, column by column.
3. Compute and rank by WSJF, highest first.
4. Sanity-check: a small, time-critical item should float to the top.

## Pitfalls
- Scoring row by row (item by item): it breaks the relativity.
- Huge items always sink — split them before scoring.
- Absolute numbers (days, euros) mixed with relative points.

## Output columns
Item | Business value | Time criticality | Risk reduction / opportunity | Cost of Delay | Job size | WSJF
