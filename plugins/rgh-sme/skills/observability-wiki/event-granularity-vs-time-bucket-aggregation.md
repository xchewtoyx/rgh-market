---
type: concept
title: Event Granularity vs. Time-Bucket Aggregation
description: Evaluating telemetry at per-event granularity is meaningfully more precise than evaluating it as pre-aggregated time buckets, because a coarse bucket forces an entire window to be binarized as one outcome even when only a fraction of the events in it were actually bad.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 12"
  - title: "Implementing Service Level Objectives"
    resource: "Implementing Service Level Objectives (Alex Hidalgo), ch. 7"
---

A [metric](metric-anatomy.md) built on top of a time-series system typically has to aggregate a whole time bucket (e.g. one minute) into a single "good" or "bad" verdict. This is too coarse whenever the questions being asked need sub-bucket precision: a bucket where 94% of events succeeded and 6% failed is treated identically to a bucket where 100% failed, unless the underlying evaluation happens per-event rather than per-bucket.

Evaluating at **per-event granularity** — using [wide structured events](structured-events-as-observability-substrate.md) rather than pre-aggregated time-series buckets — avoids this coarsening: each individual event contributes its own outcome, so a mostly-successful bucket is correctly reflected as mostly successful rather than rounded to entirely bad or entirely good. It also means the evaluation criteria can be revisited and backfilled against raw historical data later, which is impossible once data has been pre-aggregated to metrics (see [pre-aggregation is irreversible](pre-aggregation-is-irreversible.md)).

This is a general precision trade-off between telemetry types, distinct from any particular use of it (such as how tightly an error-budget-style target can be tracked, which belongs to reliability engineering) — the underlying point is that time-bucket aggregation always discards information a per-event evaluation would have kept.

**Practical backend selection heuristics**, applying this trade-off to choosing a measurement store: a TSDB's per-bucket aggregation happens at write time, so freshness is usually good (often ≤60 seconds end-to-end) and cost scales with the number of distinct tag combinations rather than with request volume — see [cardinality explosion in TSDBs](cardinality-explosion-in-tsdbs.md). A [structured event store](structured-events-as-observability-substrate.md) evaluates at query time instead, so cost scales roughly linearly with request throughput (making it a harder sell above roughly 10,000 events/sec) and freshness is typically the weaker point (minutes, not seconds, of pipeline lag) — but any new grouping or threshold can be backtested against history without having pre-decided it at write time, which a TSDB's already-aggregated buckets can't offer. See [tiered hot/cold storage](tiered-storage-and-log-retention.md) for a related limit on how far back that backtesting can actually reach.
