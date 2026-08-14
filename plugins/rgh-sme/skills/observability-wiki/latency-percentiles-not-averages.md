---
type: concept
title: Track Latency Percentiles, Not Averages
description: Latency should be tracked as a histogram/distribution and queried by percentile (p50, p95, p99), not reduced to a mean, because averages hide the tail behavior that most affects real users and can be skewed by fast failures.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 6"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 10"
  - title: "Implementing Service Level Objectives"
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 9"
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §6.2"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 9"
---

An average latency figure is actively misleading for two reasons:

- It collapses a distribution into one number, hiding whether the badness is a uniform shift or a long tail affecting a small fraction of requests. The same distortion shows up in LLM inference: one 3,000 ms outlier among ten ~100 ms requests pulls the mean to 390 ms and overstates typical [TTFT/TPOT](llm-inference-latency-metrics.md) experience.
- Failed requests often return *faster* than successful ones (an immediate HTTP 500 might take 2ms), so mixing failure latency into a success-latency average drags the number down and masks real degradation.

The fix is to bucket latency into a **histogram metric** and query specific percentiles (p50, p95, p99) — and to keep successful-request latency and failed-request latency as separate series. See [metric anatomy](metric-anatomy.md) for how histogram metrics are structured, and [percentile aggregates can still mislead when the underlying population is heterogeneous](percentile-aggregates-misleading-with-heterogeneous-population.md) for a further caveat about what percentiles do and don't tell you.

High percentiles also need enough underlying samples to mean anything: a p95 computed from only a handful of data points is noise, not signal — as a rule of thumb, aim for at least ~20 samples in the window before trusting a p95 figure. Low-traffic services or short windows that can't reach that sample size should track a lower, more data-dense percentile, mean latency, or raw utilization instead, and widen the window before querying a high percentile again. This also explains why tail latency is a good *leading indicator* of saturation: in a queueing system approaching its capacity limit, high percentiles inflate faster than the mean as utilization rises, so p99 latency crosses an alerting threshold before the average does — provided the sample-size floor above is met.

This is also why a merely *momentary* degradation can be a real problem worth chasing even when aggregate metrics look fine: Google's tail-latency analysis of universal search found that transient network degradation somewhere along a request's critical path had negligible effect on overall system throughput, yet a profound effect on outlier (tail) latency specifically — the average and the throughput graphs stayed flat while the tail fattened. A metric that only reports throughput or mean latency can miss this class of problem entirely; it only shows up once you're looking at the distribution's tail.

Below even that floor, [the Rule of Five](rule-of-five-for-small-sample-confidence.md) gives a cheap fallback: the min/max range of as few as five random samples still brackets the true median with over 93% confidence, even though it says nothing about tail behavior. Note that collecting more samples only helps with *random* noise in the first place — see [systemic vs. random error in telemetry](systemic-vs-random-error-in-telemetry.md) for why a systemically biased metric doesn't improve no matter how large the window gets.
