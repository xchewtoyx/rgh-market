---
type: concept
title: Hard vs Soft Dependency
description: >
  A hard dependency is one a service cannot be reliable without; converting
  a hard dependency into a soft one is one of the most effective reliability
  improvements available.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 4"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 12"
---

- **Hard dependency** — something the service cannot be reliable without
  (e.g. a required database read on the critical path).
- **Soft dependency** — something that improves the experience but isn't
  required for baseline function (e.g. a maps app's traffic overlay, which
  can fail without breaking navigation).

Converting a hard dependency into a soft one — for example, adding a cache
layer so the service can tolerate a backend database issue — is one of the
most effective reliability improvements available. It prevents downstream
dependency failures from escalating into a [cascading failure](cascading-failure.md)
and directly raises the achievable ceiling described in
[dependency reliability composition](dependency-reliability-composition.md):
a service's reliability ceiling is bounded by its hard dependencies, so
removing a hard dependency removes a hard bound.

This distinction is a standing design question, not a one-time
classification — as a system evolves, dependencies can quietly harden (a
soft dependency becomes load-bearing without anyone deciding that) or
soften (a formerly-required call gets made optional). Revisiting the
hard/soft classification is one of the checks worth folding into
[SLO evolution triggers](slo-evolution-triggers.md) whenever dependencies
change. To support this runtime decoupling, the underlying system must also maintain [loose architectural coupling](loose-architectural-coupling.md), permitting teams to deploy and test their services independently.

**Unrecognized hard dependencies are the dangerous case.** A dependency
doesn't have to be architecturally obvious to be hard — a case study of an
upstream click-logging pipeline feeding an ML training pipeline found the
click-logging team didn't realize their system was a hard dependency for
downstream model training at all; they treated their own multi-day outage as
low-urgency because it only delayed ad billing from their own vantage point,
not realizing a training pipeline downstream assumed their feed's
completeness to produce correct [training labels](training-label-correctness-as-sli.md).
The postmortem fix was to make the relationship explicit: establish a
concrete availability/SLO target for the upstream data-processing system,
specifically because it was a hard dependency, and set up a communication
path so the downstream owner can be told when that dependency's data
completeness is in doubt. The general lesson: an unrecognized hard
dependency gets none of the protections a recognized one does — no
[dependency-composition](dependency-reliability-composition.md) math accounts
for it, no [error-budget policy](error-budget-policy.md) treats its outages
as a signal to pause consuming its output — until someone actually names it
as hard.

### Framework-Driven Dependency Management

Modern application frameworks can formalize and automate the handling of dependency failures at runtime:
- **Hard Dependency Monitoring**: If a framework-level health checker detects that a registered hard dependency is down, it can immediately mark the parent service as unhealthy, stopping traffic routing and redirecting users to other functional instances before resources become exhausted.
- **Soft Dependency Isolation**: When a soft dependency fails, the framework intercepts the failure (e.g., via a circuit breaker) and automatically returns a degraded default, cached value, or empty state — an instance of [graceful degradation](graceful-degradation.md) — allowing the core user transaction to complete successfully.
- **Automatic Deadline Propagation**: To prevent slow dependency calls from locking threads and creating thundering herd retry loops, frameworks propagate deadlines downstream. If a request cannot complete in time, the framework cancels the request early, preserving server capacity.
