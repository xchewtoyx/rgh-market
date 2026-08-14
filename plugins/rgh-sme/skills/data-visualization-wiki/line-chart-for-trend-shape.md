---
type: concept
title: Line Chart for Trend Shape
description: >
  Line charts exist to reveal shape — trend, fluctuation, cycle, rate of
  change, or co-variation — not to support reading off individual values, so
  their quantitative scale need not start at zero.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.2.1"
  - title: Data Science from Scratch, 2nd Edition
    resource: "Data Science from Scratch, 2nd Edition (Joel Grus), ch. 3"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

Line charts are best for revealing the *shape* of data — trends,
fluctuations, cycles, rates of change, and how two series co-vary — especially
over time. Multiple series can share one figure (each as its own line) when
the goal is comparing trend shapes side by side — for example, plotting
variance, bias-squared, and total error against model complexity to illustrate
a tradeoff. A line can also carry a summary statistic with a range or
confidence band layered around it (e.g., min/average/max wait times). Use
distinct line styles or colors plus a legend so each series remains
identifiable — or [label directly](direct-labeling-over-legends.md). On a
dashboard, a line chart is usually the best quick overview of a time series,
because "is it going up, down, volatile, or seasonal" is generally the needed
picture, not individual values (for individual values, see
[text vs. graphics tradeoff](text-vs-graphics-tradeoff.md)).

Time on the x-axis must use **consistent intervals**. Mixing decade-spaced
points with year-spaced points makes unequal spans look equal — the same
failure mode as [uneven tick spacing](axis-manipulation-antipatterns.md).
For change between exactly two points across many categories, prefer a
[slopegraph](slopegraph.md) over a multi-period line chart.

Unlike a [bar graph, which must start its scale at zero](bar-graph-zero-baseline-rule.md),
a line chart's quantitative scale can be narrowed to just above/below the
actual data range to show more shape detail — because a line's meaning comes
from its shape, not from a filled length read against a zero baseline. Always
keep the data-encoding line visually more prominent than any other element in
the chart (axes, gridlines — see [data-ink ratio](data-ink-ratio.md)).

See [sparklines](sparklines.md) for a minimal, axis-less variant built purely
for at-a-glance historical context rather than precise reading, and
[categorical scale types and bar vs. line choice](categorical-scale-types-and-bar-vs-line-choice.md)
for when a line is the wrong choice.
