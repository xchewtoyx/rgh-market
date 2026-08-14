---
type: concept
title: N+M Redundancy
description: A capacity-provisioning pattern that sizes a pool with M more units than the N required to serve peak load, so any M units can fail or be taken out of rotation without a capacity shortfall.
sources:
  - title: "The Site Reliability Workbook"
    resource: "The Site Reliability Workbook (Google SRE series), ch. 11"
---

**N+M redundancy** provisions a resource pool with $N + M$ units, where $N$ is the number of units actually required to serve current peak load and $M$ is the extra headroom kept specifically to absorb the loss of up to $M$ units — from failure, maintenance, or a rolling deployment — without a capacity shortfall.

## Contrast with Active/Passive Redundancy

Traditional redundancy is often **1+1 (active/passive)**: one unit does all the work, a second sits idle as a standby, taking over only on failure. N+M generalizes this into a **pool** where all $N+M$ units are simultaneously active and share load, rather than most of them sitting idle:

*   **1+1 active/passive:** simple, but wastes half the provisioned capacity during normal operation, and the failover itself is a discrete, riskier event (state transfer, DNS/routing cutover).
*   **N+M active pool:** every unit does useful work all the time; losing any single unit (or up to $M$ of them) just means the remaining pool absorbs a proportionally larger share of the same total load, rather than triggering an explicit failover.

## Worked Example: Load Balancer Pools

A load balancer pool distributing traffic across backend machines via a technique like consistent hashing with connection tracking can run as an N+1 (or higher) active pool: if any one machine fails, its share of connections is redistributed across the remaining pool members using the same consistent-hashing scheme, without requiring a dedicated standby or dropping in-flight connections tied to other, unaffected machines.

## Sizing Considerations

Choosing $M$ is a capacity-planning trade-off, not a fixed constant:

*   **Larger $M$** tolerates more simultaneous unit loss (multiple failures, or a failure during a rolling deployment that has already taken some units offline) at the cost of provisioning and paying for capacity that sits unused in the common case.
*   **Smaller $M$** is cheaper but risks a capacity shortfall — and a resulting [M/M/1-style latency blowup](mm1-queue-model.md) — if losses exceed what was provisioned for. When the pool is a replica set voting on writes rather than a stateless worker pool, this same headroom trade-off is sharper: see [quorum size vs. write throughput trade-off](quorum-size-throughput-tradeoff.md) for why adding replicas for extra tolerance has a direct, non-linear throughput cost.
*   $M$ should be set relative to the realistic worst-case simultaneous loss the system needs to survive (e.g., one zone's worth of capacity, or the maximum number of units a deployment pipeline takes offline at once), not an arbitrary round number.

Insufficient headroom compounds badly with automated recovery in stateful systems specifically: a node lost to a genuine failure (or wrongly declared failed) triggers data rebalancing onto the remaining pool, and a pool with no spare capacity to absorb that migration load can cascade into further failures — see [automated rebalancing failure cascade](automated-rebalancing-failure-cascade.md).
