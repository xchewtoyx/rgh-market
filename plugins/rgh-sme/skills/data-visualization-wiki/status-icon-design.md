---
type: concept
title: Status Icon Design
description: >
  Dashboard icons only need to cover three meanings — alert, up/down, on/off
  — and each should use one simple, consistent shape with as few severity
  levels as possible.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.2.2"
---

Only a few icon types are actually needed on a dashboard, covering three
meanings:

- **Alert icons** — must be exceptionally simple and noticeable; limit to at
  most 2 distinct alert levels (ideally 1), since many icon variants are too
  complex to scan quickly. The classic traffic-light metaphor is critiqued
  directly: green ("all is well") draws attention needlessly since it doesn't
  need to be flagged, and because the icon is always present (just
  recolored), it fails to get the benefit of a preattentive "added mark" that
  only appears when something's actually wrong. Prefer one consistent simple
  shape (circle or square) that varies only in intensity of a single hue for
  severity — see [colorblind-safe color encoding](colorblind-safe-color-encoding.md).
- **Up/down icons** — a conventional triangle or arrow showing movement
  relative to the past or a target. Colorblind-safe approach: vary hue *and*
  intensity together (e.g., fully saturated red for "wrong direction," pale
  green for the other) rather than hue alone.
- **On/off icons** — flag an item as distinct from others in a list (e.g.,
  which of the top-10 opportunities are closest to closing). Checkmarks,
  asterisks, and Xs are the most intuitive; pick one and use it consistently
  (see [visual consistency principle](visual-consistency-principle.md)).

Icons rely on being perceived preattentively, which is only reliable for
simple shapes — see [preattentive processing](preattentive-processing.md) and
[perceptual distinctness limits](perceptual-distinctness-limits.md).
