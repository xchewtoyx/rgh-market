---
type: concept
title: Coordinated Omission
description: A load-testing measurement error where a closed-loop generator that waits for each response before sending the next request systematically undercounts tail latency.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 1"
---

**Coordinated omission** is a measurement error that occurs when a load generator issues each request only after the previous one has completed, rather than at a fixed, response-independent rate. This is a specific case of the closed-loop behavior described in [load generator bottlenecks](load-generator-bottlenecks.md), but its consequence is distinct: it doesn't just cap throughput, it silently corrupts the reported latency distribution.

## The Mechanism

When a target system experiences a slow period (e.g., a garbage collection pause, a queueing spike, a saturated resource), a closed-loop generator that waits for each response naturally sends *fewer* requests during that slow period — its own queue stays artificially short because it never issues the requests it "would have" sent had it not been coordinating with the target's response times. Those never-issued requests never appear in the results, so they cannot pull the measured latency distribution toward the tail. The slow period gets systematically under-represented in the sample.

## Consequences

*   **Reported percentiles are optimistic.** Measured p99/p999 latency looks better than what real, independently-arriving clients would experience, precisely during the periods that matter most (when the system is struggling).
*   **The effect gets worse the slower the outlier is** — a single very slow response corresponds to many requests that a real, uncoordinated arrival process would have sent (and which would have queued and also been slow), but coordinated omission represents it as just one slow data point.

## Mitigation

Load generators must issue requests on a **fixed schedule set independently of response times** — modeling how real traffic actually arrives (e.g., a fixed rate, or a Poisson arrival process) rather than pacing off the target's own responses. Tooling designed to avoid this (e.g., generators with dedicated request-scheduling threads decoupled from response-handling threads) is necessary to get an honest read on tail latency under load; a naive request-response loop in a benchmarking script will not.

This matters most for the same reason [tail latency amplification](tail-latency-amplification.md) matters: if a load test cannot see the true tail, it cannot validate whether a system meets a tail-latency-based budget.
