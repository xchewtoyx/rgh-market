---
type: concept
title: Proportional Ink Principle
description: >
  Whenever shaded area or length represents a numerical value, that visual
  quantity must be directly proportional to the value it represents — the
  general rule that explains why bar charts need a zero baseline and several
  other common chart distortions.
sources:
  - title: Calling Bullshit
    resource: "Calling Bullshit: The Art of Skepticism in a Data-Driven World (Carl T. Bergstrom, Jevin D. West), ch. 7"
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.8"
---

Edward Tufte's formal principle: "the representation of numbers... should be
directly proportional to the numerical quantities represented." This is the
general rule underneath [why bar graphs must start their scale at
zero](bar-graph-zero-baseline-rule.md) — a bar's *ink* (its filled area)
represents the value, so cutting the baseline breaks the proportionality
between ink and value. A line graph is exempt from the zero-start requirement
specifically because it encodes value through point *position*, not through
filled area — no ink is being used to represent magnitude, so there's nothing
for a non-zero baseline to distort (see
[line chart for trend shape](line-chart-for-trend-shape.md)).

Concrete violations of proportional ink, beyond the bar-baseline case:

- **Encoding one value in two dimensions of ink at once** (e.g., a shape
  scaled in both width and height to represent a single ratio): area scales
  with the *square* of a linear shrink, so a value that's actually 1/6 of
  another can end up rendered with only 1/36 the ink — a much more severe
  understatement than a simple truncated axis produces. See
  [dual-dimension encoding antipattern](dual-dimension-encoding-antipattern.md).
- **Filled ("area") line charts** inherit the bar chart's zero-baseline
  requirement, because shading the area under the line turns it back into an
  ink-encodes-value chart — truncating the axis exaggerates the shaded area's
  apparent change exactly as it would for bars.
- **Donut/ring charts**, where value is encoded as a band's radial position:
  outer rings sweep more physical area per unit of underlying value than
  inner rings covering the same angular width, so ink is never proportional
  to value across the rings — ordering bands smallest-to-largest from the
  center out exaggerates differences between them, and reversing the order
  understates them.
- **3-D perspective rendering** distorts ink independent of the data:
  gridlines and bars receding toward a vanishing point shrink progressively
  regardless of their true value, and front-facing wedges in a 3-D pie chart
  can visually occupy a noticeably different share of the disk than their
  real percentage. See [avoid 3-D effects and occlusion](avoid-3d-effects-and-occlusion.md).

The practical test for any chart: if a reader measured the actual pixels of
ink (or the rendered area/length) devoted to two values, would that
measurement ratio match the underlying data's ratio? If not, the chart
violates proportional ink regardless of what the axis labels say.
