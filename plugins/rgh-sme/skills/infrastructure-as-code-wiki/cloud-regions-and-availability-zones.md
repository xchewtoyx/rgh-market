---
type: concept
title: Cloud Regions and Availability Zones
description: The two nested groupings a cloud platform organizes its data centers into, and why choosing them is an explicit infrastructure design decision rather than an implementation detail.
sources:
  - title: Software Architecture in Practice, 4th Edition
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 17"
---

A cloud platform organizes its data centers into **regions** — logical and physical groupings of geographically distributed data centers — and subdivides each region into **availability zones**, engineered with independent power and connectivity sources so that a failure affecting one zone is very unlikely to affect another in the same region. Both are ordinary parameters in infrastructure code (a Terraform provider block, a resource's region/zone argument), which makes the choice of region and zone as much a piece of the declared infrastructure as the resources placed inside them.

Region choice serves two distinct purposes worth separating: placing a service near its users to cut network latency, and complying with data-residency law that restricts where certain data may physically live (for example, regulation barring cross-border transfer). Zone choice within a region is purely an availability decision — spreading redundant instances of a stateless or replicated workload across multiple zones means the simultaneous loss of all of them is extremely unlikely, which is what makes "multi-AZ" a standard checklist item for [production-grade infrastructure](production-grade-infrastructure-checklist.md).

This is the concrete infrastructure-platform mechanism underneath the higher-level [active-passive vs active-active topology](active-passive-vs-active-active-topology.md) choice: an active-passive topology typically places its standby in a different region entirely (so a whole-region failure doesn't take out both), while spreading a single active environment across multiple availability zones within one region is a cheaper, finer-grained way to buy redundancy against a zone-level failure without paying for full cross-region duplication. Consolidating non-production or test infrastructure within a single availability zone, conversely, is a deliberate way to cut cross-zone data-egress cost when the redundancy multi-AZ buys isn't needed for that workload — see [cost controls in infrastructure code](cost-controls-in-infrastructure-code.md).
