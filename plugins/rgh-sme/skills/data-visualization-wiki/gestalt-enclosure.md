---
type: concept
title: "Gestalt Principle: Enclosure"
description: >
  A visual border or shared background fill makes viewers perceive the
  enclosed objects as one distinct group, and it works even when the border
  is very subtle.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 4 §4.3"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 3"
---

One of six Gestalt grouping principles. Enclosure: objects surrounded by a
visible border (a line, or a shared fill/background color) are perceived as a
distinct group, set apart from everything outside the border. It doesn't
require a strong (bright, thick) border to work — even a subtle enclosure
creates a strong grouping perception, which is why muted, low-contrast
borders and fills are usually sufficient (see
[data-ink ratio](data-ink-ratio.md)'s guidance to mute necessary non-data
pixels rather than remove them entirely). On a graph, light background
shading can separate forecast from actual without heavy boxes.

Enclosure is the **strongest** of the Gestalt grouping cues covered — stronger
than [connection](gestalt-connection.md), which is in turn stronger than
[proximity](gestalt-proximity.md) or [similarity](gestalt-similarity.md).
Reach for it when a group genuinely needs to be visually separated from
everything else and proximity alone isn't doing the job (e.g., data packed
too tightly for white space to read as a gap) — but prefer
[white space over an added border](delineate-groups-with-least-visible-means.md)
whenever density allows it, since white space is the least visible (and
cheapest in data-ink terms) way to delineate a group.
