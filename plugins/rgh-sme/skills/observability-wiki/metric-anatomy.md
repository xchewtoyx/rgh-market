---
type: concept
title: Metric Anatomy and Types
description: A metric is a timestamped numeric measurement with a name, a type describing how to combine it, and attributes/labels, and comes in three basic shapes — counters, gauges, and histograms — each combined differently.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 10"
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 5"
  - title: "Implementing Service Level Objectives"
    resource: "Implementing Service Level Objectives (Alex Hidalgo), ch. 7"
---

A metric data point is structured as `name{label1=val1, label2=val2} timestamp value` — a name, a set of key-value attributes/labels, a timestamp, and a numeric measurement. Its **type** determines how to combine it correctly across instances or over time:

- **Counters** — monotonically increasing numbers (e.g. total requests handled). Read via a rate function over a window, e.g. `rate(http_requests_total[5m])`, rather than the raw cumulative value.
- **Gauges** — arbitrary values that fluctuate up and down (e.g. active memory usage, queue depth). Read directly; averaging gauges across instances is meaningful, averaging counters usually isn't.
- **Histograms** — binned distributions that track counts of observations falling into buckets, used to compute percentiles (p50, p90, p99) for values like latency. See [latency percentiles, not averages](latency-percentiles-not-averages.md).

**Computing percentiles from a TSDB in practice**: native histogram support varies by system, and where it exists it typically stores exponential/geometric bucket boundaries or a compressed probabilistic sketch (e.g. the **t-digest** algorithm) for cheap, precise percentile estimation without retaining every raw observation. Where native support is absent, percentiles can be faked with plain counter/gauge tags: emit `foo_count` (total observations) and `foo_total` (sum) to derive an average, plus a set of `foo_bucket_count{bucket_min=X}` tags to approximate a histogram — a percentile is then estimated by summing bucket counts below a threshold, interpolating within the containing bucket, and dividing by the total count. A cheaper fallback still is storing a running sum-of-squares to derive standard deviation/variance, though this needs a numerically stable online algorithm rather than naive summation once means grow large and observation counts get high.

**A key pitfall of metrics as a telemetry type**: because a metric pre-aggregates at write time (e.g. averaging per-instance response times into one number), you can lose the ability to answer questions you didn't anticipate — a true weighted average across instances requires knowing the datapoint count per bucket, which an average-of-averages silently discards. Histogram metrics (recording count + total, not just a mean) partially mitigate this, but only if configured that way in advance. See [pre-aggregation is a one-way trip](pre-aggregation-is-irreversible.md) for the general principle this is an instance of.
