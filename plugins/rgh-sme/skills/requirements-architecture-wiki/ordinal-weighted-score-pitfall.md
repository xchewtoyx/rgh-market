---
type: concept
title: Ordinal Weighted-Score Pitfall
description: >
  Multiplying and summing arbitrary 1-5-style scores and importance
  weights feels rigorous but has no valid arithmetic behind it, and no
  published evidence that it improves decisions over simpler methods.
sources:
  - title: How to Measure Anything
    resource: "How to Measure Anything: Finding the Value of Intangibles in Business (Douglas W. Hubbard), ch. 12"
---

A common prioritization technique scores each candidate on several
criteria (say, "strategic alignment," "risk") from 1 to 5, multiplies each
score by a similarly arbitrary 1-to-5 importance weight, and sums the
results into a ranking. This looks quantitative but rests on operations
that ordinal scales don't actually support: nothing establishes that the
distance between a "2" and a "3" equals the distance between a "4" and a
"5," so multiplying and adding these numbers together produces a result
with no defined meaning, however precise it looks. Concretely, this fails
in several specific ways: it discards real cardinal data that already
existed (converting an actual ROI percentage into a coarse 1-5 bucket
throws away information that was already measured); how many buckets a
scale has and where the cut points fall changes how people answer even
when the underlying quantity hasn't changed (**partition dependence**);
and verbal or numeric labels get interpreted inconsistently across
evaluators, producing an "illusion of communication" — apparent agreement
that a project is "high risk" while each evaluator privately means a
different magnitude by it.

The deeper problem is that no published, outcome-based evidence shows
these scoring methods actually improve decisions compared to simpler
alternatives — in contrast to methods like calibrated estimation or a
consistent linear model built from real units, which do have that
evidence. Structuring a scoring exercise can still be a genuine
improvement over a completely unstructured discussion (comparing
candidates side by side surfaces differences a free-form conversation
misses), but that benefit comes from the *organization*, not from the
arithmetic performed on the resulting numbers — treating the final
weighted-sum score as meaningfully more precise than "roughly ranks
these in this order" is not supported.

This is directly relevant to [requirements
prioritization](requirements-prioritization.md): a Kano rating, an
impact/feasibility placement, or an H/M/L risk rating (see [risk and
tradeoff points](risk-and-tradeoff-point.md)) are legitimate exactly
because they're used as coarse triage or as ordinal rankings, not
multiplied together into a single composite score presented as precise.
Where a decision is big enough to be worth getting right, and the
underlying quantities are already known in real units (cost, time,
probability), [decomposition for
measurability](decomposition-for-measurability.md) into an actual
cost/benefit or risk model is the more defensible path.
