---
type: concept
title: Visual Hierarchy with Preattentive Attributes
description: >
  Used sparingly, preattentive attributes do more than make one element pop —
  variance within and across attributes creates an ordered path through a
  graphic so the audience reads the most important points first.
sources:
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 4"
---

[Preattentive attributes](preattentive-attributes-for-dashboards.md) can draw
attention to a single spot, but their fuller design use is building a
**visual hierarchy**: an implicit processing order that tells the audience
what to look at first, second, and later, while pushing necessary-but-not-
message-bearing components into the background so they do not compete.

Two levers create that order:

- **Variance within one attribute.** Bright blue pulls harder than muted
  blue, which pulls harder than light grey. Intensity and size gradients
  alone can rank elements without introducing a second encoding channel.
- **Combining attributes.** Pairing size with color (or color with
  enclosure) lets some components be emphasized and others de-emphasized in
  the same view, making the graphic scannable rather than uniformly dense.

Audience attention is brief: studies cited for this practice put the decision
window at roughly **3–8 seconds** before a viewer keeps looking or moves on.
A clear hierarchy conveys the gist even inside that window. Without it, a
viewer defaults to a zigzag "Z" scan from top-left across the page and only
eventually reaches the intended focal region — slower and less reliable than
an explicit [preattentive](preattentive-processing.md) cue.

A practical construction tactic: **push everything to the background first**
(mute axes, labels, and series into light grey), then bring forward only what
the story needs — data series thicker/darker than axis chrome, the focal
series darker than supporting ones, selective markers or numeric labels only
where the eye should land. That forces an explicit decision about what earns
emphasis, and selective labels double as a "look here" signal while still
serving [direct labeling over legends](direct-labeling-over-legends.md).

Highlighting always trades off: emphasizing one point makes other points
harder to see. Reserve strong hierarchy for
[explanatory communication](visualization-for-exploration-vs-communication.md),
where there is already a specific story; during exploration, mostly avoid
preattentive emphasis so no single point monopolizes attention before you
know which one matters. Over-hierarchy fails the same way as
[over-highlighting on a dashboard](static-vs-dynamic-highlighting.md) — if
everything is emphasized, nothing is.
