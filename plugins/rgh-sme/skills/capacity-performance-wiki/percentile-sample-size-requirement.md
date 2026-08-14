---
type: concept
title: Percentile Sample Size Requirement
description: A percentile computed from too few observations is statistically unstable — low-traffic systems should track the mean or raw utilization instead of a high percentile.
sources:
  - title: "Implementing Service Level Objectives"
    resource: "Implementing Service Level Objectives (Alex Hidalgo), ch. 8-9"
---

[Latency percentiles](latency-percentiles-vs-mean.md) are a better summary of tail behavior than the mean, but a percentile estimate is only as trustworthy as the number of observations behind it. A p95 computed from a handful of data points is not a stable statistic — it can swing wildly between measurement windows purely from sampling noise, independent of any real change in the system.

## The Low-Volume Problem

A rough rule of thumb: estimating a p95 meaningfully wants on the order of 20+ samples in the window (enough that the tail percentile is actually interpolating between several genuine slow observations, not extrapolating from one or two). A low-throughput service measured over a short window can easily fall well short of that — e.g., a service handling roughly one request per minute has only about five data points in a five-minute window, so a single slow request swings the "measured p95" by tens of percentage points, even though nothing about the system's real behavior changed.

This compounds with alerting: a window sized to catch problems quickly on a high-traffic service can produce a statistically meaningless — and therefore noisy, false-positive-prone — percentile on a low-traffic one.

## Mitigations

*   **Widen the measurement window** so enough events accumulate before a percentile is computed, trading detection speed for statistical stability.
*   **Track the mean or raw utilization instead of a high percentile** when a service's event volume is inherently low — a percentile needs a population to describe; below some volume threshold, a simpler statistic is more honest about what the data can actually support.
*   **Inject synthetic probe traffic** to increase effective sample density, with the caveat that synthetic traffic isn't necessarily representative of real request patterns and can mask genuine customer-specific failures that don't show up in the probe's fixed request shape.

This is a distinct concern from [percentile aggregation across nodes](percentile-aggregation-across-nodes.md) — that note is about combining percentiles that are each individually well-estimated; this one is about whether a single percentile estimate is trustworthy in the first place.
