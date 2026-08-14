---
type: concept
title: "Application Service: Orchestration, Not Business Logic"
description: >
  A layer that coordinates a use case — invoking domain objects, persisting
  results, handling transactions and security — should contain no business
  logic of its own; logic spanning multiple domain objects belongs in a
  domain service instead.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow (Kaiser), ch. 4"
---

An application service is a thin client of the domain model: it invokes
the domain model's own business methods, coordinates persistence (through
a [repository](ports-and-adapters-architecture.md)), and handles
cross-cutting orchestration concerns for a use case — identity generation,
[transaction boundaries](repository-and-transaction-separation.md),
authorization checks. What it must *not* do is
contain business logic itself: no validation of a business rule, no
decision that belongs to the domain, executed at this layer instead of
inside a domain object.

The rule for where logic that spans multiple domain objects should live:
if it's a rule intrinsic to one object's own state, it belongs on that
object — see [aggregate consistency
boundaries](aggregate-consistency-boundary.md). If it's domain logic that
doesn't belong to any single entity or value object, because it operates
across several of them, it belongs in a dedicated **domain service** —
still part of the domain model, still expressing a business rule — not in
the application service, which exists purely to orchestrate the use case
around whatever domain logic those objects already carry.

Getting this wrong in the direction of putting business logic in the
application service is exactly how a codebase drifts into an
[anemic domain model](anemic-domain-model.md): domain objects become passive
data holders, and every actual decision migrates into "service" or
"manager" classes that manipulate them from outside. The application
service isn't wrong to exist — orchestration is a real, distinct
responsibility from business logic — but its job is to call the domain
model's behavior, not to reimplement it.
