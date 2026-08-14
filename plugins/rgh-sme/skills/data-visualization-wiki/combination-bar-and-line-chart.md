---
type: concept
title: Combination Bar and Line Chart
description: >
  Combine bars and a line in one chart when part of the data is best shown
  as individual values (bars) and part is best shown as overall shape
  (a line) — for example, monthly revenue and expenses as bars with profit
  trend as a line.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.2.1"
---

Appropriate only when a chart genuinely needs to show both: values that
benefit from bar-style local, value-to-value comparison, and a derived series
that benefits from a line's trend-shape strength. Classic example: monthly
revenue and expenses as bars, with the resulting profit trend overlaid as a
line.

Also usable across time instances to show both the parts (as bars, e.g.
per-channel revenue) and the whole (as a line, e.g. total revenue) in one
chart — this is a compact alternative to the tradeoffs in
[stacked bar chart tradeoffs](stacked-bar-chart-tradeoffs.md), since the
line makes the whole's trend directly readable without stacking distorting
the parts. Two separate quantitative scales (left and right axes) can be used
when the bar series and line series have very different magnitudes, avoiding
wasted space that a single shared scale would create.

See [categorical scale types and bar vs. line choice](categorical-scale-types-and-bar-vs-line-choice.md)
for why bars and lines each suit different data, and
[Pareto chart](pareto-chart.md) for a specific, well-known instance of this
combination.
