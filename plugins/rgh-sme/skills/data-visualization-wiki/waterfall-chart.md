---
type: concept
title: Waterfall Chart for Sequential Increases and Decreases
description: >
  A waterfall chart unpacks a starting value into sequential positive and
  negative contributions that reach an ending value, making composition of
  change readable without forcing every segment onto a shared stacked
  baseline.
sources:
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

Where a [stacked bar](stacked-bar-chart-tradeoffs.md) shows parts of a whole
at one moment, a waterfall shows **how you got from A to B**: a starting
quantity, then floating bars for each increase or decrease in order, then an
ending quantity. Classic use: headcount (start → hires/transfers-in →
transfers-out/attrition → end) or any bridge from one total to another.

Each step keeps a clear length encoding against its own baseline segment, so
the eye can read individual contributions that would be hard to compare as
middle segments in a stack. When a tool lacks a native waterfall, one
workaround is a stacked bar with an invisible "spacer" series that lifts each
visible segment into place — clumsy, but it preserves the sequential story.
Use a waterfall when the question is composition of *change*; use stacked or
side-by-side bars when the question is composition of a *static* whole.
