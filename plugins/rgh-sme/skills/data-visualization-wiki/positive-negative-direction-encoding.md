---
type: concept
title: Positive-Negative Direction Encoding
description: >
  Plot reductions below a baseline and additions above it (or use empty
  outline for a gap) so direction itself carries meaning, then reinforce with
  matching label colors and deliberate stack order.
sources:
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 6"
---

When a display must show both gains and losses against a shared pool,
direction on the quantitative axis is an affordance: plot attrition or other
reductions in the **negative** direction and additions (hires, promotions)
above the baseline so "down = shrink, up = grow" matches intuition. Keep a
muted y-axis spanning both directions for magnitude; reserve direct numeric
labels for the focal series (e.g., unmet need).

Reinforce with encoding that does not fight the story:

- **Color** — tie related series with related hues (pool in medium blue,
  attrition in a less-saturated blue); use a positive-connotation accent for
  additions; render a "gap" as outline/empty space rather than solid fill so
  absence reads as absence.
- **Stack order** — put the baseline population on the axis, reductions
  below, additions above, and the gap where the eye lands soonest (often
  top), matching
  [order by message priority](order-categorical-values-by-magnitude.md).
- **Matching labels** — color series labels like their marks so
  [Gestalt similarity](gestalt-similarity.md) binds name to data without a
  distant legend.

This is the directional cousin of
[horizontal 100%-stacked Likert bars](horizontal-bars-for-categorical-labels.md)
and of [secondary-axis caution](secondary-y-axis-alternatives.md): encode the
signed story in one honest frame rather than forcing the viewer to decode
two scales. Still obey the
[zero-baseline rule](bar-graph-zero-baseline-rule.md) for any length-encoded
bar.
