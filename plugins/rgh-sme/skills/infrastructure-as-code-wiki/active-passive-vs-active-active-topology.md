---
type: concept
title: Active-Passive vs Active-Active Redundancy Topology
description: The two basic ways to run redundant environments across regions or zones — one serving all live traffic with a standby ready to fail over, versus multiple environments simultaneously sharing live traffic.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 9"
---

**Active-passive** runs a primary environment serving all live traffic and a secondary, idle standby in a separate [region](cloud-regions-and-availability-zones.md), with global load balancing or DNS control ready to fail traffic over quickly if the primary has an outage or a bad change. The standby costs money while doing nothing most of the time, but the failover is conceptually simple: traffic just needs to be redirected to an environment that's already fully built and (ideally) kept up to date.

**Active-active** runs multiple identical environments across regions simultaneously, all sharing live traffic rather than one sitting idle. This gets more value out of the redundant capacity and can improve both availability and throughput, but it requires the system to actually tolerate multiple concurrently-active instances — which is a much bigger design constraint for anything stateful, since data written to one active environment generally needs to be visible to the others.

This choice sets the stage the rest of a team's change-management strategy plays out on: [blue-green infrastructure changes](blue-green-infrastructure-change.md) and [continuous disaster recovery](continuous-disaster-recovery.md) both assume you can stand up and cut over to a parallel environment, which is naturally easier to reason about, and often cheaper to practice regularly, in an active-passive topology than in an active-active one where "standby capacity" doesn't really exist as a separate concept.
