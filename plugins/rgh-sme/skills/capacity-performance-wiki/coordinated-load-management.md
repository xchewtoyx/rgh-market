---
type: concept
title: Coordinated Load Management
description: Load balancing, autoscaling, and load shedding must be designed as one interacting system, because each one optimizes a local signal that the others can misread — miscoordination can create a feedback loop that concentrates load on an already-struggling target.
sources:
  - title: "The Site Reliability Workbook"
    resource: "The Site Reliability Workbook (Google SRE series), ch. 11"
---

Load balancing, [autoscaling](autoscaling-safety-bounds.md), and load shedding are frequently built and configured by different teams as independent systems, each optimizing its own local signal. In practice they interact tightly, and a miscoordination between them can produce a failure mode worse than any one system's individual bug.

## Failure Pattern: The Efficiency Illusion

A utilization-aware load balancer measuring per-request resource cost can be fooled by load shedding happening downstream of it: a region that begins shedding requests (rejecting them outright once it hits capacity) has each *rejected* request show up as cheap, low-resource-cost work, because rejecting a request is far cheaper than serving it. From the load balancer's point of view, that region now looks *more* efficient than its neighbors — so the load balancer routes it *more* traffic, pushing it further into shedding, while genuinely under-loaded regions sit idle. The system's own control loop actively worsens the overload it's supposed to be routing around.

## Why It Happens

The root cause is not a bug in either system individually — the load balancer's cost signal and the load shedder's rejection logic can each be functioning exactly as designed. The failure is structural: neither system has visibility into the other's state, so a locally rational optimization (route to the "cheapest" region) becomes globally irrational once load shedding is in the loop.

## Design Principles for Coordination

*   **Count shed or errored requests as high, not low, capacity usage** in any balancing calculation — a rejected request should make a region look *full*, not efficient, so the balancer routes away from it rather than toward it.
*   **Sequence the triggers deliberately: autoscaling before load shedding.** If autoscaling reacts first, added capacity may resolve the overload before shedding needs to activate at all; if shedding fires first, the system is discarding work it might not have needed to.
*   **Add monitoring specifically for cross-system feedback loops**, not just for each system's own health — a feedback loop can be invisible to per-system dashboards while still being visible in the aggregate traffic-distribution pattern. These loops are also vulnerable to [delayed feedback loop oscillation](delayed-feedback-oscillation.md) when each system reacts to a stale, partial view of the others' effect.
*   **Set a minimum instance floor per location.** Without one, load balancing and autoscaling can compound into concentrating all growth in a single already-popular location, turning it into an unplanned single point of failure.
*   **Coordinate emergency kill/override triggers across all three systems** so an operator disabling one during an incident isn't left fighting the other two, which are still acting on the old signal.

The underlying lesson generalizes beyond these three specific systems: any set of automated control loops that share a resource but each act on a different, partial view of that resource's state can produce this kind of destructive feedback — treat interacting load-management systems as one system to design and test, not several to configure independently. A structurally similar loop occurs between failure detection and partition rebalancing in stateful data systems — see [automated rebalancing failure cascade](automated-rebalancing-failure-cascade.md).
