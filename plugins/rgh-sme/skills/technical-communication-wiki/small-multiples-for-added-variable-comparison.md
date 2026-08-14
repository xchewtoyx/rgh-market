---
type: concept
title: Small Multiples for Added-Variable Comparison
description: >
  Repeating the same simple chart once per category, stripped of
  redundant chrome, lets a reader compare an extra variable that
  wouldn't fit as another dimension inside a single chart.
sources:
  - title: "Information Dashboard Design"
    resource: "Information Dashboard Design (Stephen Few), ch. 6"
---

A single chart can usually only encode two or three variables clearly before it becomes hard to read — a bar's position and length, maybe a color. When a reader genuinely needs to compare across one more variable than that — the same measure broken out by region, by channel, by team — cramming it into one chart (via more colors, more series, more axes) usually costs more clarity than it delivers. **Small multiples** — Edward Tufte's term — solve this by repeating the identical simple chart once per value of the extra variable, laid out in a grid or row so all instances sit within the reader's eye span at once and can be compared directly, the same way [keeping comparable information within one view](keeping-comparable-information-within-one-view.md) argues any comparison-worthy content should be.

Because every instance in the set uses the same chart type, scale, and layout, a reader who's learned to read one of them can read all of them without re-orienting — this is the same payoff described in [consistent visual encoding across a document](consistent-visual-encoding-across-a-document.md), applied to a whole grid of charts instead of one chart repeated across a document. That repetition also makes most of each individual chart's chrome redundant: axis labels, legends, and titles only need to appear once for the whole set (or once per row/column), not duplicated inside every instance, which is what keeps a small-multiples grid compact enough to fit in the same space a single, more complex chart would have needed.
