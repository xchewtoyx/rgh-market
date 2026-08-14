---
type: concept
title: Autoscaling Signal Selection
description: Choosing what metric drives an autoscaler's scaling decisions, and why naive utilization averages can silently defeat autoscaling when unhealthy instances are counted alongside healthy ones.
sources:
  - title: "The Site Reliability Workbook"
    resource: "The Site Reliability Workbook (Google SRE series), ch. 11"
---

An autoscaler's correctness depends entirely on the signal it scales from. The choice of signal — not just the target threshold — is what determines whether autoscaling responds to real load or is silently defeated by it. This is a capacity-modelling policy decision about *what to scale on*, distinct from the mechanism that actually carries out adding or removing instances.

## The Unhealthy-Instance Trap

A naive average-utilization signal (e.g., "average CPU across the pool") can be silently corrupted by unhealthy instances: an instance that is up but not actually serving traffic (crashed application process, failed health check, stuck in a bad state) still reports low resource utilization, because it isn't doing any work. Averaged into the pool's utilization metric, unhealthy instances drag the reported average down, making the pool look like it has spare capacity precisely when it has less real serving capacity than it appears to.

## Fixes

*   **Scale from a load-balancer-observed capacity metric** rather than raw instance-reported utilization — a metric that only counts instances the load balancer is actually routing to automatically excludes unhealthy instances from the calculation, since they aren't receiving traffic to report utilization on in the first place.
*   **Use a cool-down period** before counting a newly launched instance's metrics in scaling decisions — a fresh instance is often still warming up (empty caches, JIT warm-up, connection pool establishment) and will report artificially low utilization if measured too early, which can trigger premature scale-down or mask the need for further scale-up.
*   **Pair autoscaling with autohealing** — a separate mechanism that detects and restarts unhealthy instances based on a health signal, with enough grace time after restart for the instance to actually become healthy before being judged again. Autoscaling alone cannot fix a capacity shortfall caused by instances that are counted but not contributing; autohealing addresses the root cause that autoscaling's signal selection can only work around.
