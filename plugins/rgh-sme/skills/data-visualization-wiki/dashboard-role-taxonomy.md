---
type: concept
title: Dashboard Role Taxonomy (Strategic, Analytical, Operational)
description: >
  Of the many ways to classify dashboards, the one that actually drives
  different visual-design choices is the role it serves — strategic,
  analytical, or operational.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 2 §2.1"
---

Dashboards can be classified along many independent variables (data domain,
update frequency, span of data, interactivity, and so on), but only one of
these — **role** — significantly correlates with differences in visual
design. The three roles:

- **Strategic dashboards** — the most common type ("executive dashboards").
  Support monitoring the health/opportunities of a business at any
  management level. High-level performance measures plus forecasts, light
  context (comparisons to targets, brief history), simple good/bad
  evaluators — too much context here distracts from the strategic
  decision-maker's goal. Design implications: the simplest possible display
  mechanisms, static snapshots (daily/weekly/monthly, not real time) since
  strategic decisions aren't made at real-time cadence, and usually
  non-interactive (getting a senior decision-maker to look at a screen at
  all, instead of paper, is already a win).
- **Analytical dashboards** — support open-ended data analysis. Need richer
  context: fuller comparisons, more history, subtler evaluators. Can still
  work with static snapshots, but should support interaction — drilling into
  underlying detail — because the goal is understanding *why* a number moved
  and what to do about it, not just observing that it moved. See
  [dashboard as launch pad](dashboard-as-launch-pad.md).
- **Operational dashboards** — monitor operations, shaped by the dynamic,
  immediate nature of what they track. Must reflect constantly changing
  activity that may need a response at a moment's notice, so display media
  must be very simple (misreading is costly under time pressure) and must
  actively grab attention when performance crosses a threshold, rather than
  waiting to be checked. Data is often more granular/specific than on a
  strategic dashboard (not just "shipment at risk" but which shipment,
  handler, location), often surfaced via drill-down or hover.

Deciding a dashboard's role first is what should drive later choices about
interactivity, refresh rate, and how much [context to attach to each
number](contextualizing-metrics-with-comparisons.md) — treat role as an input
to those decisions, not an afterthought applied uniformly to every dashboard.
