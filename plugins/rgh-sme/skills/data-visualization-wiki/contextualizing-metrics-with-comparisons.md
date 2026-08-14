---
type: concept
title: Contextualizing Metrics with Comparisons
description: >
  A raw measure means little on its own; it becomes meaningful only against
  a comparative yardstick, and there is a standard taxonomy of which
  yardsticks are useful.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 2 §2.2.1.2, ch. 7 §7.1"
---

"$736,502 in QTD sales" means nothing by itself — compared to what, is it
good or bad, on track or not? Useful comparison types, any of which can turn a
bare number into an actionable one:

- The same measure at the same point in a past period (e.g., same day last
  year).
- The same measure at some other past point (e.g., end of last year).
- A current target (e.g., budgeted amount for the period).
- Relationship to a future target (e.g., % of this year's budget reached so
  far).
- A prior prediction of the measure (e.g., a forecast for today made earlier).
- Relationship to a future prediction (e.g., % of this quarter's forecast).
- A norm (average, normal range, benchmark — e.g., typical days-to-ship).
- Extrapolation to a probable future (projection to year end, or the
  measure's own trend as a time series).
- Someone else's version of the same measure (e.g., a competitor's revenue).
- A separate but related measure (e.g., order count vs. order revenue).

These comparisons often communicate best graphically — differences don't
always "leap out" from two adjacent numbers — though text alone is fine when
the comparison itself is the only thing that matters (e.g., a single "119% of
budget"). See [choosing the right measure](choosing-the-right-measure.md) for
when to show the derived comparison value instead of making the viewer
compute it themselves.

To make a comparison actually register perceptually rather than requiring the
viewer to hunt for it, place the compared items close together, combine them
in a single graph or table, or link them with a shared color across separate
graphs — see [support meaningful comparisons](support-meaningful-comparisons.md).
Conversely, be careful not to accidentally imply a comparison that isn't
intended — reusing the same color for unrelated measures invites viewers to
relate them, which is exactly what that note's "discourage meaningless
comparisons" half covers.

A measure can also be enriched by showing multiple instances of it — broken
out categorically (e.g., sales by region) or as a time series — rather than
just one comparison value; a time series in particular provides the richest
context for understanding what's really going on and how it's trending. It
can also carry an explicit good/bad evaluation; see
[evaluative state banding](evaluative-state-banding.md).
