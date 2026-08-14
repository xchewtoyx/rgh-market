---
type: concept
title: Extremizing Algorithm
description: >
  Post-aggregation adjustment pushing crowd estimates toward 0 or 1 when judges
  hold diverse, non-overlapping information — ineffective when diversity is zero.
sources:
  - title: Superforecasting
    resource: "Superforecasting (Tetlock, Gardner), ch. 9"
  - title: Superforecasting
    resource: "Superforecasting (Tetlock, Gardner), ch. 4"
---

When independent judges hold **different scraps of information** pointing the same
way, a simple average **understates** the pooled signal. The **extremizing
algorithm** (introduced in Tetlock's chapter on aggregation) adjusts a crowd
estimate further toward 0 or 1 to reflect that pooling.

Example: advisers' bin Laden-in-compound estimates ranged **30%–95%**, mostly above
50%, averaging ~**70%**. With diverse non-overlapping evidence, extremizing could
in theory push the aggregate toward **80–85%**.

**Effectiveness depends on diversity**:

- **Zero-diversity team** (everyone knows what everyone else knows): do **not**
  extremize — you would double-count the same information.
- **Superforecaster teams** shared information well; extremizing helped little.
- **Ordinary forecaster teams** shared information less effectively; extremizing
  gave a **large** boost — enough for some ordinary teams to surpass some
  superteams.
- Extremizing a large pool of regular forecasters produced tournament-winning
  aggregate results referenced elsewhere in the book.

Collect [independent judgments before discussion](independent-judgments-before-discussion.md)
first; then aggregate; then extremize only when diversity of information warrants
it. Connect to [dragonfly-eye perspective aggregation](dragonfly-eye-perspective-aggregation.md)
and [forecast aggregation hierarchy](forecast-aggregation-hierarchy.md).

## IARPA tournament context

IARPA's Good Judgment Project tournament (2010+) targeted questions in a **Goldilocks
zone** — not trivially easy, not impossible — where skill differences are detectable
(unlike multi-year turning points in Expert Political Judgment). Competing teams had
to beat a control group's wisdom of the crowd by 20% in year 1, rising to 50% by year 4.

GJP's winning pipeline: identify top performers, weight the crowd toward them, then
**extremize**. This beat every other group/method, including intelligence analysts
with classified access — by a margin that remains classified. Washington Post (Nov 2013):
superforecasters "performed about 30 percent better than the average for intelligence
community analysts who could read intercepts and other secret data."

Doug Lorch (retired IBM programmer, no credentials or classified access): year 1 Brier
0.22 (5th of 2,800); year 2 on a superforecaster team, 0.14 — beat a real-money
prediction market by 40%, was the only person to beat the extremizing algorithm, and
beat crowd wisdom by over 60%, exceeding IARPA's year-4 target single-handedly.
58 others scored at the top in year 1 — first **superforecasters** cohort; collective
year-1 Brier 0.25 vs. 0.37 for regulars; by tournament end superforecasters outperformed
regulars by over 60%. Superforecasters at 300 days out beat regulars at 100 days out.
Snellen analogy: 60% Brier improvement ≈ vision from 20/100 to 20/40 — not perfect,
but life-changing practically.
