---
type: concept
title: Spaghetti Graph Strategies
description: >
  A spaghetti graph — many overlapping lines on one plot — is hard to track;
  fix it by emphasizing one series at a time, separating series into matched-
  scale small multiples, or combining separation with muted context lines.
sources:
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 9"
---

A **spaghetti graph** packs many overlapping series onto one line chart so
that no single series can be followed. Prefer not to ship it. Three recovery
strategies, chosen by the story:

1. **Emphasize one line at a time** — color, thickness, and an endpoint
   marker/label on the focal series; mute the rest. Works well live while
   cycling through series; needs voiceover or
   [annotation](action-titles-and-on-chart-annotation.md) explaining *why*
   each is highlighted ([progressive emphasis](progressive-emphasis-across-slides.md)).
2. **Separate spatially** into
   [small multiples](small-multiples.md) (vertical or horizontal):
   - Vertical stack with a shared x-axis favors each category's own trend
     (sparkline-like when shrunk).
   - Horizontal row with a shared y-axis favors comparing heights across
     categories at the same time.
   Hold y-axis min/max constant across panels so relative position stays
   comparable.
3. **Combine** separation with one-line emphasis inside each panel, keeping
   other lines visible but backgrounded for context — denser, better for
   circulated reports than for live delivery.

Also ask whether all series or years are needed; fewer categories can remove
the spaghetti problem at the source. No single strategy wins — pick by the
comparison the audience must make.
