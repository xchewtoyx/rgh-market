---
type: concept
title: Pie Charts Are Rarely Appropriate
description: >
  Pie charts encode quantity as 2-D area and angle, which humans compare
  poorly, and are frequently misused for data that isn't even parts of a
  whole; a bar graph almost always communicates the same data better.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.5, ch. 6 §6.2.1.10"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

Few is blunt: "I never recommend the use of pie charts." Knaflic calls them
"evil" for the same perceptual reasons. Two separate problems compound:

1. **Misuse for data that isn't actually parts of a whole.** A pie chart only
   means anything if its slices sum to 100% of one whole. A cancer-statistics
   pie chart of *probabilities of developing different cancer types* was
   shown to visually mislead — a 13.30% slice read as roughly 40% of the pie —
   precisely because the values didn't sum to a single whole at all.
2. **Even when correctly used for true parts-of-a-whole data, pies are hard to
   read accurately**, because people cannot accurately compare 2-D areas or
   angles — the two encodings a pie chart relies on. When slices are close in
   size it is nearly impossible to tell which is bigger; when they are not,
   direction is clear but magnitude is not. 3-D or tilted pies make this
   worse: nearer (bottom) slices look larger than farther (top) ones even at
   equal values — see
   [avoid 3-D effects and occlusion](avoid-3d-effects-and-occlusion.md).
   Data labels can patch lookup but rarely justify the footprint. See
   [avoid area encoding for quantitative comparison](avoid-area-encoding-for-quantitative-comparison.md)
   for the underlying perceptual reason.

**Donut charts** are not a rescue: they replace angle/area comparison with
arc-length comparison, an even less reliable judgment, and they also violate
[proportional ink](proportional-ink-principle.md) across rings. Do not use
them.

For genuine part-to-whole data, use a
[horizontal bar chart](horizontal-bars-for-categorical-labels.md) ordered
greatest-to-least (or the reverse that matches the message), with a
title/label that makes clear the bars represent parts of a whole — aligned
end points against a common
[zero baseline](bar-graph-zero-baseline-rule.md) show not only which is
largest but by how much. If comparing the whole across several instances
(e.g., per quarter) while parts also matter, see
[stacked bar chart tradeoffs](stacked-bar-chart-tradeoffs.md). Rule of thumb:
if tempted to use a pie, first ask why.
