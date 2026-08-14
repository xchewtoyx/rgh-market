---
type: concept
title: Independent Testability
description: >
  A component should be verifiable on demand using test doubles, service
  virtualization, or consumer-driven contracts, rather than requiring an
  expensive shared integrated staging environment with every dependency live.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 5"
---

# Independent Testability

A shared integrated staging environment — where every service's dependencies
must be deployed and healthy simultaneously before any test can run — becomes
a bottleneck that scales worse as the number of services grows: more services
means more ways for the shared environment to be broken by someone else's
in-progress change, and more contention for the single shared environment
itself.

Independent testability replaces this with techniques that let a component be
verified in isolation:

- Test doubles / stubs / mocks for a component's own dependencies (the same
  technique [commit test suite design](commit-test-suite-design.md) applies
  at the unit level, applied here at the service level).
- Service virtualization: a lightweight stand-in that simulates a dependency's
  API behavior without running the real thing.
- Consumer-driven contract tests: the consumer specifies the contract it
  needs from a dependency; both sides verify against that contract
  independently, catching a breaking change without either side needing the
  other's real, running instance.

Combined with [ephemeral test environments](ephemeral-test-environments.md),
this is what lets each service's [deployment pipeline](deployment-pipeline.md)
run its own test stages on demand rather than queuing for a shared,
contended staging environment — directly supporting
[independent deployability](independent-deployability.md).
