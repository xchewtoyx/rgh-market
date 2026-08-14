---
type: concept
title: Layered Percentile SLO Thresholds
description: >
  Defining a latency SLO across multiple percentiles, rather than a single
  cutoff, watches the long tail instead of writing it off, and needs both a
  floor and a ceiling to avoid wasting effort on unneeded speed.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 4"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 2"
---

A flat threshold like "95% of requests must be good" silently discards the
worst 5% forever — nothing distinguishes a system whose bad requests are
mildly slow from one whose bad requests time out completely. Layering
thresholds across multiple percentiles keeps the tail visible instead of
writing it off, e.g.:

- P95 completes ≤2000ms, 99.9% of the time
- P98 ≤2500ms, 99.9% of the time
- P99 ≤4000ms, 99.9% of the time

Percentile framing can also read more intuitively to stakeholders than a
flat coverage percentage: "nines don't matter if users aren't happy."

**Latency SLOs need both a floor and a ceiling**, not just an upper bound
(e.g. 25–100ms, not just "under 100ms"). An unbounded floor invites wasted
engineering effort optimizing latency past the point where clients or the
network can actually benefit from it.

**Never average latency alone** — averaging is lossy and hides outliers and
multimodal distributions (the same underlying data can show very different
"average" values depending purely on the aggregation window used). Store raw
values and compute percentiles from them rather than relying on a
precomputed mean.

See [choosing SLO targets from historical data](choosing-slo-targets-from-historical-data.md)
for how percentiles from real historical traffic inform where to actually set
these thresholds.
