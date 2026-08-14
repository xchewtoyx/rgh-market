---
type: concept
title: Direct Labeling Over Legends
description: >
  Label data directly on the chart wherever possible, instead of forcing the
  viewer's eye to bounce back and forth between the chart and a separate key.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.7, ch. 8 §8.1"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 4"
---

A legend or separate key requires the viewer to hold a color/shape mapping in
[short-term memory](short-term-memory-chunk-limit.md) and repeatedly glance
away from the data to check it — extra work that direct labels avoid
entirely. Prefer labeling bars, lines, or regions directly at the point of
use; [Gestalt proximity](gestalt-proximity.md) makes a label next to its
series cheaper to bind than a distant key. Selective numeric labels or
markers — kept only where the story needs them, not on every point — also
act as a [visual-hierarchy](visual-hierarchy-with-preattentive-attributes.md)
"look here" cue without reintroducing clutter.

This failure mode gets worse, not just slower, when the legend lives entirely
off the dashboard — one worked example used colored/shaped rectangles in a
fixed grid whose meaning was defined only in a separately supplied key.
Viewers found it confusing on first look and still only got a rough
comparative sense of the data even after memorizing the key. A legend that
must be memorized and consulted defeats the at-a-glance purpose of a
[dashboard](dashboard-definition.md); if a chart needs a legend at all, keep
it immediately adjacent to the data it explains.
