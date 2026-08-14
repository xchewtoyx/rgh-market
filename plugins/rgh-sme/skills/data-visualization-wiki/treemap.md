---
type: concept
title: Treemap
description: >
  A space-efficient display of large hierarchical or categorical data as
  nested rectangles, sized and colored to make outliers jump out — not
  designed for precise quantitative comparison or ranking.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.2.1"
---

Developed in the 1990s by Ben Shneiderman. A treemap displays a large
hierarchical/categorical data set as nested, contiguous rectangles: rectangle
**size** encodes one quantitative variable, rectangle **color** can encode a
second, and the nesting encodes hierarchy.

Explicitly *not* designed for fine quantitative comparison or ranking — 2-D
area and color don't support precise value comparison (see
[avoid area encoding for quantitative comparison](avoid-area-encoding-for-quantitative-comparison.md)).
The point instead is to make particular conditions of interest — outliers,
problem areas — visually jump out for discovery. Worked example:
sales-by-state, size = revenue, color = % of quota using a **single-hue
intensity ramp** (white = high attainment, saturated red = low attainment).
Large red rectangles instantly flag high-revenue, low-quota-attainment states
needing attention; large pale rectangles flag high-revenue, high-attainment
states driving positive results.

Few argues for a single-hue intensity ramp rather than a two-hue (red-to-green
through black) diverging scheme, questioning whether "slightly below quota"
vs. "slightly above quota" really deserves a qualitative red/green
distinction rather than a shade of the same concern — see
[colorblind-safe color encoding](colorblind-safe-color-encoding.md). Treemaps
are usually interactive/drillable through the hierarchy — see
[dashboard as launch pad](dashboard-as-launch-pad.md).
