# Reference: RICE

**Origin:** Intercom (Sean McBride). Product roadmaps where the number of people affected varies between items.

## When to use
Features or projects with an estimable audience. Not for internal tasks with no audience, nor when deadlines drive value (use WSJF).

## Factors
- **Reach** — people or events affected per time period, in real units (e.g. 800 customers per quarter). Same period for every item.
- **Impact** — per person, on the goal, on a fixed scale: 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal.
- **Confidence** — 100% = high (data), 80% = medium (some evidence), 50% = low (mostly intuition). Below 50%, treat the item as a bet and say so rather than scoring it.
- **Effort** — total person-months across all disciplines (product, design, engineering…). Use whole numbers, or 0.5 for anything well under a month.

## Score
RICE = (Reach × Impact × Confidence) ÷ Effort

## Procedure
1. Fix the time period for Reach and the goal for Impact.
2. Estimate Reach from data when it exists; otherwise mark it `[assumed]` and give the reasoning.
3. Score Impact only with the 5 allowed values — no 1.5 or 4.
4. Compute, rank, and show the inputs, not just the score.

## Pitfalls
- Reach counted over different periods for different items.
- Effort counting engineering only.
- Impact used on a 1–10 scale: it breaks the formula's balance.
- A large Reach hiding a tiny Impact: read both.

## Output columns
Item | Reach (unit/period) | Impact | Confidence | Effort (person-months) | RICE

## Example
Reach 800 customers/quarter × Impact 1 × Confidence 80% ÷ Effort 2 → 320.
