---
type: concept
title: Consistent Visual Encoding Across a Document
description: >
  Varying chart types, colors, or icons purely to avoid monotony forces
  a reader to relearn an interpretive strategy on every instance, so
  the same kind of data should get the same visual treatment everywhere
  it appears in a document or document set.
sources:
  - title: "Information Dashboard Design"
    resource: "Information Dashboard Design (Stephen Few), ch. 3"
---

There's a temptation, especially across a long document or a set of related visuals, to vary the display medium — a pie chart here, a gauge there, a different color scheme on each page — on the assumption that repetition bores the reader. This gets the actual tradeoff backwards: a reader given the data they came for, presented the same way each time, doesn't get bored by the repetition — they get *faster*, because they only have to learn how to read one kind of display once and can then reuse that same interpretive strategy everywhere it recurs. Meaningless variety does the opposite: it forces the reader to consciously re-derive what a new chart type or new color mapping means every time it changes, which is pure overhead with no informational payoff.

The corrective isn't "never vary anything" — a different measure that genuinely calls for a different graphic form should get one, per the ordinary matching of [display medium to the reader's task](communicating-evidence-visually.md). The corrective is that variety should only ever track a real difference in the underlying data or its comparison type, never be introduced for its own sake to seem less repetitive. The same discipline applies to color and shape as attributes in their own right: because [short-term memory holds the meaning of only a handful of distinct attribute values at a time](preattentive-attributes-for-rapid-visual-perception.md), predefining a fixed, small palette of colors, shapes, and intensities up front — and reusing that same set consistently, so the same color always means the same thing everywhere — costs the reader nothing to relearn and pays off every time the same encoding recurs across the document.

The same rule has a flip side that's easy to violate by accident: because a reader naturally infers that same visual treatment means related content (the [Gestalt similarity principle](gestalt-principles-for-visual-grouping.md)), reusing one color or shape for two genuinely unrelated things — yellow meaning "satisfactory" in one chart and just "the month of June" in another — creates a false signal of connection the writer never intended. Guarding against this means checking not only "is the same thing always shown the same way" but also "is anything shown the same way that isn't actually the same thing," and fixing the latter by spatial separation or a different visual attribute rather than letting the coincidence stand.
