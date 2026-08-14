---
type: concept
title: Stacked Bar Chart Tradeoffs
description: >
  Stacked bars make the whole easy to compare across instances but make every
  segment above the bottom one hard to compare, since its baseline shifts
  with the segments beneath it.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.2.1"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

For a single instance of part-to-whole data, a plain bar graph reads faster
than a stacked one — don't reach for stacking by default (see
[pie charts are rarely appropriate](pie-charts-are-rarely-appropriate.md) for
the same principle applied to pies).

Stacking is legitimate when there are multiple instances (e.g., one stack per
quarter) of a whole-and-its-parts, and the **whole** matters more than
precise part-level comparison across instances. The catch: only the segment
at the very bottom of each stack (against the fixed baseline) is easy to
compare across instances — every segment above it has a baseline that shifts
depending on the segments beneath it, making its own changes hard to track
visually. Default color schemes compound the overload; keep the palette
restrained ([vivid color restraint](vivid-color-restraint.md)).

Stacks may encode absolute values or **100%-stacked** shares. With
100%-stacked columns, consider also showing absolute totals (on the chart or
in a footnote) so share changes are not mistaken for volume changes.
[Horizontal 100%-stacked bars](horizontal-bars-for-categorical-labels.md)
fit negative-to-positive scales (e.g., Likert survey items) especially well,
because both outer ends share consistent baselines. When the story is
sequential composition of *change* rather than a static whole, prefer a
[waterfall chart](waterfall-chart.md).

If both the whole and the individual parts need clear comparison across
instances, don't force it into one stacked chart — use two side-by-side (or
stacked) graphs instead, or a
[combination bar and line chart](combination-bar-and-line-chart.md) showing
parts as bars and the whole as a line.
