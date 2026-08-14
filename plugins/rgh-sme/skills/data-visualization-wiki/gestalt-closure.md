---
type: concept
title: "Gestalt Principle: Closure"
description: >
  Viewers perceive ambiguous or incomplete shapes as closed and regular
  whenever reasonably possible, which means a chart doesn't need a full
  border to read as a defined region.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 4 §4.3"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 3"
---

One of six Gestalt grouping principles. Closure: humans dislike "loose ends"
— an ambiguous stimulus that could be read as open, incomplete, or unusual is
instead perceived as closed, complete, and regular whenever reasonably
possible (a broken-line rectangle is still seen as "a rectangle," not four
disconnected segments).

The direct dashboard application: a graph needs only two axis lines (X and
Y) to define its plotting area — viewers' perception will close the implied
rectangle on its own, so a full four-sided border is unnecessary. Default
chart borders and background shading (common tool defaults) can usually be
removed for the same reason: the graph still reads as a cohesive shape, and
the data stands out more without them. This is one of the concrete
eliminations in [reducing non-data pixels](data-ink-ratio.md): removing a
graph's full border costs no clarity, because closure fills in the missing
sides perceptually.
