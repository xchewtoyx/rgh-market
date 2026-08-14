---
type: concept
title: Scaled Capacity Test Environment
description: How to build a cost-effective capacity test environment that still produces valid results, by proportionally scaling every dimension that could become a bottleneck rather than just running a smaller cluster.
sources:
  - title: "Continuous Delivery"
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Jez Humble, David Farley), ch. 9"
---

A [capacity test](capacity-test-types.md) is only as trustworthy as its resemblance to production. The ideal is **production equivalency**: a test environment matching production's architecture, network topology, OS settings, middleware configuration, and database scale exactly. When a full 1:1 replica is cost-prohibitive, the alternative is a **scaled fraction environment** — but scaling it correctly is easy to get wrong.

## The Scaling Trap

Naively running the same test suite against a cluster with fewer nodes (e.g., 1/4 of production) does not produce results that scale linearly, because different resources scale differently:

*   CPU and application-tier capacity scale roughly with node count.
*   A shared downstream dependency (a single database, a shared cache, a network link) does *not* automatically get 1/4 the capacity just because the client tier was scaled down — it may still be sized for full production, masking a bottleneck that would appear in production, or it may be scaled down disproportionately, creating a false bottleneck that doesn't exist in production.

## Scaling Every Bottleneck Dimension Proportionally

A valid scaled environment requires *deterministic, proportional* scaling of every dimension that could become a bottleneck — network capacity, CPU, and database scale — not just the node count. If the test environment is 1/4 scale, the database, network links, and any shared dependency must also be sized (or the applied load reduced) to preserve the same *ratios* of demand to capacity that production would see at the equivalent load.

## Realistic Data Volume and Distribution

Database size and data distribution matter as much as node count: a capacity test running against a near-empty database will not exercise the same index depth, query plans, or cache behavior as production-scale data. The test environment's data volume and distribution must be representative of production scale, not just its schema — otherwise results reflect the capacity of an unrealistically fast query path rather than the one production actually runs. This is the same distortion described in [benchmarking pitfalls](benchmarking-pitfalls.md) for unrepresentative access-pattern distributions, applied to data volume specifically.
