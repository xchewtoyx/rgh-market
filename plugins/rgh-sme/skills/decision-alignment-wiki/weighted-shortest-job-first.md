---
type: concept
title: Weighted Shortest Job First (WSJF)
description: >
  Sequence competing initiatives by cost-of-delay divided by
  size, not by raw value or raw effort alone, because naive
  ROI-only prioritization ignores how fast value decays if
  delayed.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements (Dean Leffingwell), ch. 13, 21, 23"
---

A higher-value initiative is not automatically higher priority,
because the economics of sequencing depend on how each
initiative's value decays over time, not just its size. A
high-value item whose profit is insensitive to a delay can
safely go later; a lower-value item whose profit collapses fast
if delayed should go first even though it scores lower on value
alone. Naive ROI (value divided by effort) misses this entirely,
because it has no time dimension.

**Weighted Shortest Job First** fixes this by defining
**Weight = Cost of Delay / Effort** and sequencing by highest
weight first. Cost of Delay itself has three components, each a
relative (not absolute) estimate sufficient for ranking:

1. **User/business value** — how much this is worth relative to
   other candidates.
2. **Time value** — how fast that value decays if delayed, from
   negligible (a cosmetic rebrand) to severe (missing a fixed
   external deadline).
3. **Risk reduction / opportunity enablement** — value earned
   purely from the risk retired or the future option unlocked,
   independent of direct user value.

A common refinement adds an explicit aging term to the weight
formula — for example scoring the queue-time an item has already
waited and adding it to the numerator at a fractional weight
(such as ×0.5) alongside business value, time value, and risk
reduction. This keeps a genuinely valuable but perpetually
outranked item from starving indefinitely in the queue, without
letting age alone override a clearly higher-priority newcomer.

A worked illustration: the item with the single highest value
and the best raw ROI can still rank *last* under WSJF if its
time value is low, while an item with the lowest raw value ranks
first because its time value is extreme — the naive,
ROI-intuitive ordering and the WSJF ordering can invert
completely. The same Cost-of-Delay-over-effort formula applies
one level up the hierarchy: ranking architecture-level or
portfolio-level initiatives against each other uses the
identical ratio (there, effort and value are estimated relative
to other epics rather than other features), so the technique is
not tied to any one granularity of decision.

**All prioritizations are local and temporal**: a WSJF ranking is
not a fixed, permanent order — it must be recalculated as
context changes, on whatever cadence the organization re-plans.
Treating a hard-won prioritization as permanent left over from
one planning session is a common failure this technique
guards against.

This is a genuine weighted-scoring formula, the kind
[multi-lens-comparison-without-false-precision](multi-lens-comparison-without-false-precision.md)
warns can manufacture false objectivity out of judgment calls
dressed as arithmetic. The difference that makes WSJF defensible
despite that risk: its inputs (value, time-decay, risk reduction)
are named and debated individually before combining, the
combination rule itself is transparent and fixed in advance
rather than reverse-engineered to fit a preferred answer, and
the technique is reserved for situations — competing initiatives
drawing from one shared capacity — where a single sequencing
decision is actually required, not for open-ended qualitative
comparisons where
[multi-lens-comparison-without-false-precision](multi-lens-comparison-without-false-precision.md)'s
resist-the-formula stance is the better fit.
