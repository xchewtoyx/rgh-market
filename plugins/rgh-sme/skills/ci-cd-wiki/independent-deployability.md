---
type: concept
title: Independent Deployability
description: >
  A service should be deployable and releasable on its own schedule, without
  requiring simultaneous deployment of other services it depends on or that
  depend on it — a defining pipeline-design goal for componentized systems.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 5"
---

# Independent Deployability

One of the clearest empirical correlates of low delivery performance is a
system that must be deployed simultaneously as a single monolithic block —
every deployment becomes a large, synchronized, high-coordination event
regardless of how small the actual change was. Independent deployability is
the opposite property: each service can move through its own
[deployment pipeline](deployment-pipeline.md) and reach production on its own
schedule, without waiting for or coordinating with other services' releases.

This depends on the [component and dependency management](cyclic-dependency-elimination.md)
practices already in the bundle: [semantic versioning](semantic-versioning.md)
and [dependency pinning](dependency-pinning.md) so a consumer can choose when
to move to a new version rather than being forced to move in lockstep, and
[backward-compatible schema migration](backward-compatible-schema-migration.md)
so a service's own release doesn't require every consumer to update
simultaneously.

The pipeline-level payoff: [deployment frequency](dora-four-key-metrics.md)
scales with the number of independently-deployable units, since teams stop
queuing behind each other's release windows — the same mechanism
[capacity utilization and lead time](capacity-utilization-antipattern.md)
describes at the team level applies here at the service level.

Not every component set can honestly claim this property — some are coupled
tightly enough that independent versioning is unsafe. See
[tuple-testing for tightly coupled releases](tuple-testing-for-tightly-coupled-releases.md)
for the deliberate alternative: testing and releasing a named version
combination as one atomic unit rather than pretending the components are
more independent than they actually are.
