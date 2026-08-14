---
type: concept
title: Sparklines
description: >
  A tiny, axis-less line graph giving quick historical context without a
  precise quantitative readout — ideal for dense dashboards where a full
  chart won't fit.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.2.1"
---

Invented by Edward Tufte, described as "data-intense, design-simple,
word-size graphics." A sparkline is a tiny line graph (e.g., a 12-month
account-balance history) with no axis or scale — it deliberately trades
precise readability for pure historical *context*, small enough to sit
inline next to a text value the way a word sits next to other words. Ideal
for dashboards and other highly condensed contexts (Few's example: a medical
diagnostic report showing a patient's history at a glance).

Useful enhancements: a light background band marking an acceptable range, so
out-of-range excursions are visible immediately (e.g., defect counts
exceeding the band on 3 of the last 30 days); a colored end-point dot tying
the sparkline's final value to a "current" figure shown alongside it in text.

Sparklines are explicitly preferred over simple up/down trend arrows, which
are ambiguous about *what period* the trend covers (this year? this quarter?
since yesterday?) — a sparkline makes the covered period visually explicit by
showing the whole history rather than collapsing it to a single directional
symbol. Few's verdict: "every dashboard vendor ought to support them." See
[line chart for trend shape](line-chart-for-trend-shape.md) for the
full-scale version this trades precision for.
