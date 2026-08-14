---
type: concept
title: Box Plot
description: >
  Shows the distribution of a set of values, not just a single summary
  statistic — necessary because sets with identical medians (or averages)
  can have very differently shaped distributions.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.2.1"
---

Invented in the 1970s by John Wilder Tukey, to show the shape of a
**distribution**, which a single summary number (like a median) can hide
entirely — sets of values with identical medians can look completely
different once their full spread is shown.

A progression of increasingly informative displays for the same data leads
up to it: a median-only bar (least informative) → range bars showing only
low/high, no shape → range bars plus a median marker (a crude proxy for skew:
median position within the range hints at where values cluster) → the full
box-and-whisker plot (a rectangle spanning two meaningful values — typically
not the extremes — plus "whisker" lines and separately marked outliers beyond
them).

Few notes the full box-and-whisker form may be "too rich" for most dashboard
audiences unfamiliar with the convention, and recommends a simplified
box-plot variant for dashboard use rather than dropping distribution
information back down to a single summary number. This is the dashboard's
main tool for the "distribution" analytical question, distinct from
[scatter plots](scatter-plot-for-correlation.md) (correlation) and
[bar/line charts](categorical-scale-types-and-bar-vs-line-choice.md)
(comparison/trend). A box plot shows one distribution at a single point in
time; when the distribution itself needs tracking across many parallel
series or across time, see
[heat map for distribution across many series](heat-map-for-distribution-over-many-series.md)
instead.
