---
type: concept
title: Capacity Test Environment Fidelity
description: >
  A capacity test environment must mirror production's architecture, scale,
  and data volume closely enough that the results it produces predict
  production behavior, whether via a full replica or a deterministically scaled fraction.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 9"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 10"
---

# Capacity Test Environment Fidelity

A [nonfunctional test gate](nonfunctional-test-gate.md)'s results are only
meaningful if the environment it runs against is representative of production:

- **Production equivalency**: architecture, network topology, OS settings,
  middleware configuration, and database scale should mirror production as
  closely as possible.
- **Scaled fraction environment**: when a full 1:1 replica is cost-prohibitive,
  use a deterministically scaled-down fraction (e.g. a quarter of production's
  node count) with load scaled proportionally, ensuring network, CPU, and
  database bottlenecks scale down together rather than one becoming an
  artificial bottleneck the others don't share.
- **Realistic data volume**: the database must hold data volume and
  distribution representative of production scale — query and index
  performance depend heavily on data shape, and a capacity test against a
  near-empty database will miss the exact problems (slow queries, index
  misses) that only appear at production data scale.

Without this fidelity, a passing nonfunctional gate provides false confidence:
it proves the build performs well in an environment that doesn't resemble
where it's actually going to run.

A performance test environment can end up *more* complex and resource-
intensive to build than production itself, since it may need to simulate
production-scale load generation on top of production-equivalent
infrastructure. Because of that, it pays to build it early in a project with
dedicated resources, rather than treating it as an afterthought to be
assembled once the application is otherwise complete.

A developer's local benchmark is the extreme low-fidelity end of this
spectrum: it can stay predictive for simple workloads and then silently stop
being predictive once complexity (e.g. model size, in an ML inference
service) crosses some threshold — see [self-service model latency load
testing](self-service-model-latency-load-testing.md) for a case where that
gap was closed by giving developers direct access to a real staging
environment instead of trusting local numbers further.
