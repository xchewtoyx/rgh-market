---
type: concept
title: Categorical Scale Types and Bar vs. Line Choice
description: >
  Categorical axes are nominal, ordinal, or interval, and this classification
  directly determines whether the data should be shown as bars or as a line.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.2.1"
  - title: Data Science from Scratch, 2nd Edition
    resource: "Data Science from Scratch, 2nd Edition (Joel Grus), ch. 3"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

Three types of categorical scale:

- **Nominal** — discrete, unordered categories (e.g., regions, departments)
  that differ "in name only."
- **Ordinal** — intrinsically ordered, but not quantitative (e.g., rankings
  like poor/below-average/average/above-average/excellent).
- **Interval** — ordered *and* quantitative, formed by dividing a continuous
  range into equal sub-ranges (e.g., 55-60, 60-65, ...); time units
  (years/months/weeks/days) are treated as interval scales for practical
  purposes, despite months and years not being perfectly equal length.

The rule that follows: **use bars, never lines, for nominal or ordinal
scales.** A bar chart is the right form when a quantity varies among a
**discrete set of items** — movie counts by title, sales by region, exam
grades bucketed into deciles. Embrace bars *because* they are familiar:
familiarity reduces decoding cost so attention stays on the message. Eyes
compare bar end points, which makes biggest/smallest and incremental
differences easy — provided bars are wider than the gaps between them
without becoming so wide that viewers slip into comparing areas instead of
lengths. Prefer
[horizontal bars when labels are long](horizontal-bars-for-categorical-labels.md).
Histograms are the same idea applied to continuous data grouped into ranges:
each bar represents a bin count. A bar's visual weight emphasizes individual
values and supports direct value-to-value comparison; a line implies
continuity — that consecutive points are genuinely connected — which is only
meaningful along an interval scale. Even on an interval scale, prefer bars
over a line when the goal is emphasizing individual values or close
comparison between adjacent values (e.g., comparing daytime vs. nighttime
productivity by month), rather than revealing the overall trend shape, which
is a line's actual strength — see
[line chart for trend shape](line-chart-for-trend-shape.md). For histogram
integrity when bin widths differ, see
[variable bin width distortion](variable-bin-width-distortion.md).

Part-to-whole data specifically should use a bar graph (clearly labeled as
parts of a whole), not a [pie chart](pie-charts-are-rarely-appropriate.md).

The one deliberate exception to "never a line on a nominal/ordinal scale" is
the [Pareto chart](pareto-chart.md), where the line shows a *cumulative
total* mathematically derived from the ranked bars — each point is genuinely
connected to the previous one, so a line is legitimate there even though the
underlying axis is ordinal. A [slopegraph](slopegraph.md) is another
legitimate line use across categories when the line connects the *same*
category across two comparable states rather than implying continuity along
the category axis.
