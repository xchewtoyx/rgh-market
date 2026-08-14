---
type: concept
title: Purposes of Monitoring
description: Monitoring telemetry serves five distinct purposes — trend analysis, comparison, alerting, dashboards, and debugging — and each purpose has different requirements for what data to collect and how long to keep it.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 6"
---

Monitoring data is collected for five distinct purposes, and conflating them leads to systems that serve none of them well:

1. **Analyzing long-term trends** — capacity planning, database growth, user growth patterns. Needs long retention at coarse granularity.
2. **Comparing over time or across experiments** — evaluating performance before/after code releases or A/B experiments. See [overlaying deployment markers on metric graphs](deployment-markers-and-settling-period.md) for a concrete technique.
3. **Alerting** — notifying humans when system failures require manual intervention. See [symptom-based vs. cause-based alerting](symptom-based-vs-cause-based-alerting.md).
4. **Building dashboards** — visualizing system health and metrics during operational reviews.
5. **Debugging and conducting incident investigations** — providing diagnostic data to pinpoint root causes. This requires the highest-fidelity, highest-cardinality data, since you don't know in advance what dimension will matter (see [cardinality](cardinality.md)).

A monitoring system optimized purely for cheap long-term trend storage (heavily aggregated) will be nearly useless for debugging a novel incident, and vice versa — this tension is a recurring theme in [choosing between the three-pillars and wide-event telemetry models](three-pillars-vs-wide-events-model.md).
