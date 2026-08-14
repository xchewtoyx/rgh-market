---
type: concept
title: Visual Consistency Principle
description: >
  Anything that means the same thing, or works the same way, should look the
  same everywhere on a dashboard — including which chart type is used for a
  given kind of data relationship.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.6, ch. 7 §7.2"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 4"
---

Even a small, functionally meaningless inconsistency — dark axis lines on one
graph, light axis lines on another, for no reason — makes viewers suspect a
meaningful difference exists where none does. Differences are never
perceptually "free": a viewer's visual system treats any distinguishing
attribute as a signal worth investigating (see
[preattentive processing](preattentive-processing.md)). So regularize styling
of anything that repeats: axis lines, borders, fills, color meanings, icon
shapes.

This extends to the choice of display medium itself. Designers sometimes vary
chart type or colors across a dashboard or presentation purely to avoid
"boring" the viewer with repetition — this is backwards. The story, not
novelty in the encoding, should hold attention. Always pick whichever medium
communicates a given piece of data best, even if that means using the same
chart type many times over. Real viewers given the data they actually need
are not bored by repetition; they are aggravated by unnecessary variety that
forces them to switch interpretive strategy for every panel. If two sections
show the same type of relationship (e.g., both are "measure vs. target over
time"), use the same chart type for both. If grey plus one accent color is
the schema, keep that schema throughout so the audience learns "accent means
look here" and carries the expectation forward; when colors are tied to
categories (e.g., regions), preserve that mapping for the whole
report/presentation and do not reuse those hues for unrelated purposes.

This principle is what lets a viewer reuse one perceptual strategy across an
entire dashboard instead of re-learning how to read each panel — it is a
direct payoff of the [Gestalt similarity](gestalt-similarity.md) principle
applied deliberately, and it is why [colors should carry consistent
meaning](colorblind-safe-color-encoding.md) across every panel that uses
them.
