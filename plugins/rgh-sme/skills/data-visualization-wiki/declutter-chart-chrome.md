---
type: concept
title: Declutter Chart Chrome
description: >
  A practical subtraction checklist for default chart chrome — borders,
  gridlines, gratuitous markers, noisy axis labels, legends, and inconsistent
  colors — so data and labels carry the load without competing non-data
  pixels.
sources:
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 3"
---

After choosing the right form, reduce
[extraneous cognitive load](minimize-extraneous-cognitive-load.md) by
stripping tool defaults. A working checklist:

1. **Remove the chart border** — [Gestalt closure](gestalt-closure.md) still
   reads a plot area; use [white space](alignment-and-white-space.md) to
   separate from other page elements.
2. **Remove or mute gridlines** — if kept for tracing, make them thin and
   light grey; better, remove them for stronger data contrast ([data-ink
   ratio](data-ink-ratio.md)).
3. **Remove gratuitous data markers** — on a line chart, markers that merely
   echo every point add load; keep markers only where they bind an
   [annotation](action-titles-and-on-chart-annotation.md) or endpoint.
4. **Clean axis labels** — drop trailing zeros and needless precision; keep
   units/signs that ease interpretation ($ , %, commas) even if the title
   already names them — that redundancy is not clutter.
5. **[Label data directly](direct-labeling-over-legends.md)** — once chrome
   is gone, legend lookup is obviously wasteful; place labels by
   [proximity](gestalt-proximity.md).
6. **Match label color to series** — [similarity](gestalt-similarity.md) ties
   name to mark without a key; reserve accent color for intentional
   [emphasis](visual-hierarchy-with-preattentive-attributes.md).

Lack of clear contrast is itself clutter: if something is the "hawk," make it
the one visually distinct element. Some apparent redundancy (unit symbols on
axis numbers) should be retained so viewers need not remember units from the
title alone. The result of this checklist is often "not yet finished" but
already far more accessible — finish with hierarchy and words, not more
chrome.
