---
type: concept
title: Small Multiples
description: >
  Repeat the same basic graph many times, each instance varying along one
  variable, to fit a three-variable comparison within eye span that wouldn't
  fit in a single graph.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.2.6"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 8"
---

Tufte's term. A matrix or row/column series of the *same* basic chart, each
instance varying along one variable — e.g., bar graphs of bookings/billings
by region, one graph per sales channel, arranged side by side. This lets a
comparison across three variables (region, channel, and the measure itself)
fit within the [single-screen constraint](single-screen-constraint.md) by
splitting it across several small, repeated graphs rather than trying to
cram it into one.

Tradeoff versus one shared-axis multi-series chart: small multiples make each
series' individual trend easy to see, but make it harder to compare products
(or other series) **at the same point in time**. When cross-series comparison
at a date matters more than isolated shapes, prefer one combined
[line chart](line-chart-for-trend-shape.md) with shared scales and
[direct labels](direct-labeling-over-legends.md).

Redundant elements — axis labels, legend, overall title — can be stripped
from the repeated instances and shown once, saving space and reducing reading
load; this only works because
[Gestalt similarity](gestalt-similarity.md) lets the viewer recognize the
repeated chart shape without needing every instance fully re-labeled. Few
notes that dashboard software of the time made building small multiples hard
rather than easy — worth checking whether a given toolset actually supports
this pattern before relying on it.
