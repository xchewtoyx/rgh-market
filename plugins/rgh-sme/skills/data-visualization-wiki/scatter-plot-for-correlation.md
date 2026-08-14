---
type: concept
title: Scatter Plot for Correlation
description: >
  Purpose-built to show whether, how strongly, and in what direction two
  paired quantitative variables correlate — something a time-series line
  graph of the same data cannot reveal clearly.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.2.1"
  - title: Data Science from Scratch, 2nd Edition
    resource: "Data Science from Scratch, 2nd Edition (Joel Grus), ch. 3"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

A scatter plot (e.g., number of broadcast ads vs. sales revenue over 24
months) reveals correlation strength and direction far more clearly than
plotting the same paired data as two separate time series would. It can be
split into multiple point-sets (e.g., radio ads vs. revenue, TV ads vs.
revenue, both in one plot) to compare correlation strength/direction across
groups.

Two firm recommendations: avoid 3-D scatter plots or other techniques for
encoding more than two correlated variables in one plot — too much study is
required for dashboard viewing (see
[avoid 3-D effects and occlusion](avoid-3d-effects-and-occlusion.md)). And
add a straight **trend line** (line of best fit) so correlation direction and
strength are immediately visible rather than left for the viewer to infer
from a raw point cloud — stick to a simple straight line of best fit unless
the audience has statistical training for curved fits (see
[customize numeric presentation to the audience](customize-numeric-presentation-to-audience.md)).

When the two variables are **meant to be comparable on the same scale** (e.g.,
two test scores both on 0–100), letting each axis auto-scale independently
can mislead: one axis may stretch to fill its range while the other stays
compressed, exaggerating variation along one dimension. Force **equal axis
scaling** so the plot's geometry reflects the actual relative spread — see
[axis manipulation antipatterns](axis-manipulation-antipatterns.md) for
related scale distortions.

This is the dashboard's tool for the "correlation" analytical question,
distinct from [line charts](line-chart-for-trend-shape.md) (trend over time)
and [box plots](box-plot.md) (distribution).
