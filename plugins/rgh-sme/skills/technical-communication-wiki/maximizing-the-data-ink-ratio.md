---
type: concept
title: Maximizing the Data-Ink Ratio
description: >
  Every mark on a graphic should earn its place by carrying information;
  the ratio of information-bearing ink to total ink is a concrete metric
  for deciding what to remove and what to visually mute instead.
sources:
  - title: "Information Dashboard Design"
    resource: "Information Dashboard Design (Stephen Few), ch. 5"
---

Edward Tufte's data-ink ratio gives a concrete, checkable form to "cut what doesn't earn its place" when the medium is a graphic rather than prose: data-ink is the non-redundant ink that changes as the underlying data changes, and the ratio is data-ink divided by total ink used to print the graphic. Grid lines, borders, background fills, gradients, and 3-D depth that encode no data are all non-data ink by this definition — every one of them can be erased without losing any actual information, which is precisely the test for whether they belong.

Applying the ratio is a two-step sequence, not one pass: first **eliminate** every non-data element that can simply be removed outright (decorative graphics, meaningless color variation, borders and fills that white space alone would achieve, full boxes around a chart's plot area where two axis lines already close the shape via the [closure principle](gestalt-principles-for-visual-grouping.md)); then, for whatever non-data elements turn out to be genuinely necessary — a line separating densely packed sections, grid lines needed to read off a value — **de-emphasize and regularize** them instead of removing them, using light, low-saturation colors and thin strokes so they recede rather than compete with the data, and applying the same muted treatment consistently everywhere that kind of element appears, since an inconsistency in an otherwise-muted element draws exactly the attention it was muted to avoid.

The reduction step by itself only gets the display to be less cluttered; the same discipline then applies in reverse to what remains, per [highlighting what matters](highlighting-what-matters-in-a-visual-display.md) — after non-data ink is minimized, the data ink that's left still needs its own internal hierarchy so the most important figures stand out from the merely-present ones. See [decoration competes with data for attention](decoration-competes-with-data-for-attention.md) for the same underlying instinct applied to outright ornamental content rather than to structurally-motivated but over-emphasized elements like grid lines and borders.
