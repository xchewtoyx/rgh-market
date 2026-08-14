---
type: concept
title: Slopegraph for Change Between Two Points
description: >
  A slopegraph compares the same categories at two points in time (or two
  states) as paired values connected by lines, so relative increases and
  decreases read directly as slope without needing a second chart.
sources:
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

A slopegraph places categories as parallel lists at two points (e.g., 2014
vs. 2015 survey scores) and connects each category's values with a line.
Direction and steepness of the slope communicate rate of change intuitively —
the audience sees which items rose, fell, or stayed flat without a separate
"percent change" explanation. Prefer it when the analytical question is
**change between two comparable states**, not the full time-series shape a
[line chart](line-chart-for-trend-shape.md) would show across many periods.

Limitations: no sense of a part-to-whole "whole"; category vertical order is
dictated by data value at each point, so a slopegraph is a poor choice when
[fixed ordinal order](order-categorical-values-by-magnitude.md) must be
preserved — use a simple or
[100%-stacked bar](horizontal-bars-for-categorical-labels.md) instead.
Heavy overlap among lines can make a slopegraph unreadable; if that happens,
either switch forms or keep the full set muted for context while
[emphasizing one series](visual-hierarchy-with-preattentive-attributes.md)
against the rest — related to
[spaghetti graph strategies](spaghetti-graph-strategies.md). Slopegraphs are
often missing as a native chart type, so they may need a template or custom
layout — that cost is worth it when the two-point comparison is the message.
