---
type: concept
title: Blue-Green Infrastructure Change
description: Delivering a disruptive change by building a complete new instance, switching live traffic over to it, and only then removing the old instance — rather than changing the running instance in place.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 21"
---

A blue-green change creates a full new instance of a component, switches usage over to it, and then removes the old instance — the whole-instance-level counterpart to the [expand and contract pattern](expand-and-contract-pattern.md), which does the equivalent add/migrate/remove sequence at the level of individual resources within an instance. It's the standard technique for delivering [immutable infrastructure](immutable-server-pattern.md) changes, since immutable components are, by definition, replaced rather than edited in place.

Switching traffic over needs some mechanism to redirect the workload — commonly a load balancer, and in more sophisticated implementations one that can "drain" the old instance, routing new work to the new instance while letting in-flight work on the old one finish before it's torn down. Automated server or application clustering solutions often provide this as a built-in "rolling upgrade" feature. The names *blue* and *green* are deliberately symmetric — both environments are equally capable of being live, taking turns, rather than one being a primary and the other a lesser standby.

Blue-green can be applied at very different scales, from a single service instance up to (in one extreme real example) an entire data center; very large-scale blue-green tends to become unwieldy to execute safely, so it's often worth scoping it down to just the specific service being changed rather than the whole environment. Blue-green is one of a family of [zero downtime change](testing-infrastructure-in-production.md) techniques, alongside progressive/canary deployment supported by a [service mesh](service-mesh.md).
