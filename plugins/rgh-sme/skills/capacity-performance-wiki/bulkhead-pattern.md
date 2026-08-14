---
type: concept
title: Bulkhead Pattern
description: Partitioning shared resource pools — threads, connections, hosts — by tenant, domain, or dependency so that one consumer's resource exhaustion cannot starve every other consumer sharing the same pool.
sources:
  - title: "Release It!, 2nd Edition"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Michael T. Nygard), ch. 5"
---

A ship's hull is divided into watertight compartments so that a hull breach floods one compartment without sinking the whole ship. The **bulkhead pattern** applies the same idea to shared resource pools: partition thread pools, connection pools, or host capacity by tenant, by business domain, or by downstream dependency, so that one partition's resource exhaustion is contained to that partition instead of starving every consumer sharing an undivided pool.

## The Failure It Prevents

Without partitioning, a single slow or misbehaving downstream dependency can consume an entire shared thread or connection pool — every worker thread ends up blocked waiting on the one slow dependency, and callers with no relationship to that dependency are starved of capacity anyway, simply because they draw from the same undivided pool. This is the mechanism behind incidents where a minor, non-critical subsystem (an internal admin tool, a low-priority feature) takes down an unrelated critical path purely through shared infrastructure — the fault never had to touch the critical path's own code to disable it.

## Where to Draw Partition Boundaries

*   **By downstream dependency:** a separate connection or thread pool per external service or database, so a hang calling one dependency can't exhaust the pool that calls a different, healthy one.
*   **By tenant or customer tier:** isolating a noisy or abusive tenant's resource consumption from other tenants sharing the same infrastructure.
*   **By criticality:** separating administrative, batch, or non-critical-path workloads from user-facing critical-path traffic, even when both would otherwise run on the same application server or cluster — see the case in which an internal admin tool sharing an EJB container and database connection pool with passenger-facing systems propagated an unhandled exception into a system-wide outage.

## Trade-Offs

Partitioning trades away pooling efficiency for isolation: a shared pool can absorb one caller's burst using capacity another caller isn't using at that moment, while a partitioned pool cannot — each partition's ceiling is now fixed at its own allocated size regardless of what's happening in a neighboring partition. Sizing each partition therefore needs the same [load parameter](load-parameters.md) analysis as sizing an undivided pool would, just done per partition instead of once for the whole system — a partition sized too small becomes its own bottleneck even while overall system capacity sits unused elsewhere.

## Relationship to Adjacent Patterns

Bulkheads are a structural, always-on partitioning of capacity; a [circuit breaker](circuit-breaker-pattern.md) is a dynamic, reactive response that stops sending traffic to a specific dependency once it's observed to be failing. The two compose naturally: bulkheads limit the *blast radius* if a partition's pool is exhausted, while circuit breakers reduce how often that exhaustion happens in the first place by cutting off calls to a dependency that's already unhealthy.
