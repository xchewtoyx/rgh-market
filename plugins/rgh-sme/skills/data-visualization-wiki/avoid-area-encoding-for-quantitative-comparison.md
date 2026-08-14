---
type: concept
title: Avoid Area Encoding for Quantitative Comparison
description: >
  People judge circle/shape size by a linear dimension (like diameter), not
  true 2-D area, so encoding a quantitative value as shape area systematically
  distorts how much bigger one value looks compared to another.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.5, ch. 4 §4.2.5"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

Bubble/circle-size charts encode quantity via the 2-D area of (often
overlapping) circles, but viewers instinctively compare circle *diameter*
(a 1-D attribute), not area. A revenue circle that is actually about 9x the
true area (and value) of a cost circle reads as only about 3x by diameter.
Surrounding-circle size further distorts perceived size of an enclosed
circle — a classic optical illusion. Shown a pair of circles with a true size
ratio of 16x, most viewers guess a much smaller ratio. Area graphs share the
same weakness: eyes are poor at ascribing quantitative value to
two-dimensional space, so prefer length or position encodings for ordinary
comparison.

This is a specific case of a general perceptual finding: of the preattentive
attributes usable for encoding quantity, [2-D position and line length are
read accurately](preattentive-attributes-for-dashboards.md); size/area is
only "yes, but limited." Be wary of using area differences to encode
quantitative values anywhere speed and accuracy of interpretation matter,
which on a dashboard is always. A plain bar graph — where value is encoded as
line length against a shared baseline — fixes this class of problem outright.
One narrow exception is when magnitudes differ so extremely that a
one-dimensional bar cannot show both extremes usefully on one scale: a square
area encoding can compact the range by using height and width together —
accept that perceptual cost only when compactness is the explicit goal. This
is also why [pie charts](pie-charts-are-rarely-appropriate.md) are
weak for comparison (they rely on the same area/angle encoding), and it's the
reason [treemaps](treemap.md) are explicitly designed only for spotting
outliers, not for precise quantitative comparison.
