---
type: concept
title: Automated Rebalancing Failure Cascade
description: Fully automatic partition rebalancing can turn a single overloaded or falsely-declared-dead node into a cluster-wide cascading failure, because the rebalancing traffic itself consumes the network and disk capacity the remaining nodes needed.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 6"
---

**Automated rebalancing failure cascade** is a failure mode where a system's automatic response to a perceived node failure — moving that node's partitions to the rest of the pool — generates enough network and disk load to overload the *remaining* nodes, which can in turn get marked as failed and trigger further rebalancing.

## The Mechanism

1. A node is slow or overloaded, but not actually dead.
2. The failure detector, unable to distinguish "slow" from "dead," marks it as failed.
3. Automatic rebalancing kicks in and starts migrating that node's partitions to the rest of the cluster.
4. The migration itself is expensive — large amounts of data move over the network and get written to disk on the receiving nodes.
5. That migration load pushes previously-healthy nodes toward their own saturation, and the failure detector can mark *them* as failed too, triggering more rebalancing.

The system's own corrective action is what deepens the incident: each step is locally rational (move data away from a node that looks dead), but the aggregate effect is a load spike that the cluster was not provisioned to absorb on top of its steady-state traffic.

## Why It's Hard to Prevent With Better Detection Alone

Tuning the failure detector to be more conservative (slower to declare a node dead) trades one risk for another — it delays legitimate failover during a real outage. The deeper issue is that rebalancing itself is treated as a cheap, always-safe corrective action, when it is actually a significant load event in its own right that competes for the same resources as normal traffic.

## Mitigations

*   **Human-in-the-loop rebalancing:** the system computes and proposes a partition movement plan, but an operator reviews and triggers the actual migration rather than it executing automatically. This trades response speed for the judgment of someone who can recognize "the cluster is under a traffic spike, not a node failure" before triggering an expensive migration on top of it.
*   **Rate-limit or throttle rebalancing traffic** so a migration cannot itself consume enough bandwidth or I/O to push other nodes into saturation, even if it takes longer to complete.
*   **Provision headroom for rebalancing events specifically**, not just for demand spikes — see [N+M redundancy](n-plus-m-redundancy.md) and [capacity headroom](capacity-headroom-safety-margin.md), which sizes a pool to absorb losing units without a shortfall in the first place, reducing how often rebalancing needs to trigger at all.

This is a specific instance of the broader pattern described in [coordinated load management](coordinated-load-management.md): automated control loops that act on a partial, local view of system state (here, one node's apparent liveness) can produce a destructive feedback loop invisible to any single loop's own health checks. It is also a natural failure point for the [dynamic rebalancing mitigation](hotspotting.md) suggested for hotspots — rebalancing solves the distribution problem but is not itself a free or risk-free action. An overly broad [circuit breaker](circuit-breaker-pattern.md) health-check condition can trigger the same cascade by a different route — pulling healthy capacity out of rotation because it transitively depends on the one struggling node.
