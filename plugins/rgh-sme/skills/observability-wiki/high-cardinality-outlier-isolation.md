---
type: concept
title: High-Cardinality Outlier Isolation
description: Instead of manually guessing which field explains an anomaly, rank every candidate field by how differently its value distribution behaves inside the anomalous region versus the overall baseline, and surface the top few automatically.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 8"
---

The specific technique behind step 3 of the [core analysis loop](core-analysis-loop.md): given a region of telemetry already identified as anomalous (e.g. a box drawn around a latency spike on a heatmap), compute, for every field on every event, how its value distribution inside the anomalous region differs from its distribution in the overall baseline — then rank fields by how strongly they diverge.

This turns "which of my 200 attributes explains this spike" from a manual guessing game (try a `GROUP BY` on one plausible field at a time) into an automated ranking. Honeycomb's **BubbleUp** is a concrete implementation of this idea: draw a box around an anomaly on a heatmap, and it ranks every field by the percentage difference between the anomalous region and the baseline, surfacing the fields most worth investigating first.

This technique fundamentally depends on data with high [cardinality](cardinality.md) and [dimensionality](dimensionality.md) preserved per-event — it can't be done against pre-aggregated [metrics](metric-anatomy.md), because the per-event field values needed to compute the distributional difference no longer exist once they've been aggregated away (see [pre-aggregation is irreversible](pre-aggregation-is-irreversible.md)).
