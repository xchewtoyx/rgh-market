---
type: concept
title: Bare Metrics Need Comparison Context
description: A single number on a dashboard ("QTD sales $736,502") tells the viewer nothing on its own — it must be paired with a comparison (to a prior period, a target, a forecast, or a norm) so the viewer can judge good or bad at a glance, but the comparison should stay visually subordinate to the primary figure so quick scanning isn't derailed.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 2-3"
---

A raw measure is meaningless without a reference point: is $736,502 in quarter-to-date sales good or bad? The answer requires comparison, and the useful comparison types are a fixed, reusable set — the same measure at an equivalent past point in time, a current or future target, a prior prediction of the same measure, a norm or benchmark, someone else's version of the same measure, or a related-but-different measure. Whichever comparison matters for the objective, it belongs on the display alongside the raw value, not left for the viewer to compute or recall from memory.

Two failure modes sit on either side of this: a bare number with no comparison forces the viewer to already know the context by heart or guess at significance, while a number with a decorative-but-unlabeled evaluator (a gauge with colored zones and no stated scale, for instance) implies judgment without actually supplying it. The fix in both cases is the same — state the comparison explicitly (a percent-of-target, a delta from last period, a small multi-period trend) — but the comparison should stay visually subordinate to the primary figure, since burying the headline number in equally-weighted supporting detail defeats the at-a-glance read just as surely as omitting the comparison entirely. This is the concrete design consequence of [purposes of monitoring](purposes-of-monitoring.md)'s point that dashboards and trend-comparison are two of the five distinct jobs telemetry does — a dashboard panel that shows only the current value is serving neither job well.
