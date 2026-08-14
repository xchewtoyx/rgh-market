---
type: concept
title: Secondary Y-Axis Alternatives
description: >
  A secondary y-axis can plot two differently unit-ed series on one x-axis,
  but forces the reader to decode which series belongs to which scale and can
  imply a false relationship — prefer direct labels or vertically paired
  charts instead.
sources:
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

Plotting two series with incompatible units against one shared x-axis via a
left and right y-axis looks space-efficient, but the reader must work out
which marks belong to which scale. Color-linking each axis title to its
series (blue axis for blue bars, orange for an orange line) is a weak fix —
it spends [color](vivid-color-restraint.md) on decoding chrome rather than on
the message. Worse, sharing one visual frame can imply a relationship between
the series that the data do not support — adjacent to the
[fabricated dual-axis](axis-manipulation-antipatterns.md) integrity failure
when scales are deliberately twisted to force alignment.

Prefer one of two alternatives:

1. **Drop the second axis and [label the relevant points directly](direct-labeling-over-legends.md)**
   — emphasizes specific numbers.
2. **Split into two charts stacked vertically**, each with its own left-hand
   y-axis but the same x-axis — emphasizes each series' trend without
   forcing a shared frame.

A dual-axis view remains a last resort when space is extreme and both series
truly need simultaneous reading; if you use one, keep both zeros meaningful
and avoid rescaling purely to make curves track each other. For honest
comparison design generally, see
[support meaningful comparisons](support-meaningful-comparisons.md).
