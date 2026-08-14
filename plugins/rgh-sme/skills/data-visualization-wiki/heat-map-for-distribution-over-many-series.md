---
type: concept
title: Heat Map for Distribution Across Many Series or Over Time
description: >
  A color-density grid preserves the full spread across many parallel series
  (or time buckets) that a single aggregate line — mean, median, or a
  percentile — would collapse away.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Charity Majors, Liz Fong-Jones, George Miranda), ch. 20"
---

When the thing being tracked is really a *population* of parallel series
(one line per host, per customer, per shard) rather than one signal, plotting
a single derived statistic per time bucket — a mean, a P50, a P99 — discards
exactly the information that distinguishes "everything is mildly elevated"
from "one outlier is on fire while the rest are fine." Percentile lines are
themselves an aggregate: choosing "rather than percentiles" for something
like per-node CPU/memory saturation across a fleet is a deliberate trade,
because percentiles hide the variance that actually matters for that
question.

A heat map keeps the full distribution visible instead of committing to one
summary number per time slice: bucket the metric's value range on one axis,
time on the other, and encode the count/density of series falling in each
value bucket via color intensity. The result shows not just "where is the
middle" but "how spread out is the population, and is that spread widening or
narrowing" — visible directly as the color band's width and shape at each
point in time, without pre-choosing which percentile to watch.

This is the [distribution](box-plot.md) analytical question extended across
time or across many parallel series, where a
[box plot](box-plot.md) (a single distribution snapshot) or a
[line chart](line-chart-for-trend-shape.md) of one aggregate metric would
otherwise be the default choice. Prefer a heat map specifically when the
audience's decision depends on tail/outlier behavior within the population,
not just its central tendency — see
[choosing the right measure](choosing-the-right-measure.md) for the general
principle of picking the value (or, here, the whole shape of the
distribution) that actually answers the question, rather than whichever
single statistic is cheapest to compute and plot.
