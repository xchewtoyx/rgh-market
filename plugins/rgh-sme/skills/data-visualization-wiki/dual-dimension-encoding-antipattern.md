---
type: concept
title: Dual-Dimension Encoding Antipattern
description: >
  Encoding a single quantitative value in two visual dimensions of the same
  object at once (e.g., both bar height and bar width) tempts viewers into
  inaccurate area comparisons and requires too much study to interpret.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 8 §8.1"
---

One entry from Few's judged dashboard-design competition showed revenue and
pipeline data encoded in both a rectangle's height *and* width at once — a
space-saving intent, functioning like an awkward stacked-bar/area hybrid.
The result required too much study to interpret correctly and tempted
viewers into comparing the rectangles' overall 2-D area, which people cannot
judge accurately (see
[avoid area encoding for quantitative comparison](avoid-area-encoding-for-quantitative-comparison.md)).

This is also a [proportional ink](proportional-ink-principle.md) violation:
scaling a shape in two dimensions at once for one value means area grows
with the *square* of the linear change, so a value that's really 1/6 of
another can end up rendered at only 1/36 the visual area — a real-world
example did exactly this with a soccer shots-on-goal graphic, badly
understating an accuracy ratio. The general rule this illustrates: encode
one quantitative value in exactly one visual dimension — [2-D position or line length](preattentive-attributes-for-dashboards.md),
not both height and width of the same shape simultaneously. If two values
genuinely need to be shown together, prefer two separate, clearly-labeled
encodings (e.g., a [bullet graph](bullet-graph.md)'s bar plus tick mark)
over compressing both into different dimensions of one shape.
