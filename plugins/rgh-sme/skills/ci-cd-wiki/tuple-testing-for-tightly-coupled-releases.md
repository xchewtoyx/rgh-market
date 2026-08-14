---
type: concept
title: Tuple-Testing for Tightly Coupled Releases
description: >
  Testing, approving, and deploying a specific named combination of
  component versions as a single atomic unit, for component sets too
  tightly coupled to release and version independently.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 11"
---

# Tuple-Testing for Tightly Coupled Releases

[Independent deployability](independent-deployability.md) assumes components
are loosely coupled enough to version and release on their own schedules.
Some component sets aren't: a load balancer, its plugins, and the OS kernel
it runs on, or a virtualization stack's management layer, hypervisor, and
storage layer, can behave correctly only in specific combinations — testing
every theoretically possible version pairing is infeasible, and most
combinations would never occur in practice anyway.

Tuple-testing names and tests a specific combination directly, as one unit:
"Service A@101 + Service B@456 + Service D@246" is the thing under test, not
Service A or Service B individually. If any part of the tuple fails testing,
the whole tuple is rejected — fix and retest the tuple from scratch, not just
the failing member. Only combinations that have been explicitly tested and
approved as a tuple are ever deployed, and rollback means reverting to the
last approved tuple as a whole, not reverting individual components to
whatever their own last-good versions happened to be.

## The cost

Lock-step tuple versioning caps the system's overall rate of change: one
component's delayed release blocks every other component in the tuple that
would otherwise be ready to ship. This is the direct trade-off against
[independent deployability](independent-deployability.md) — tuple-testing
buys safety for genuinely interdependent components at the cost of the
release velocity loose coupling would otherwise provide.

## When to use which

Test genuinely tightly coupled components as a tuple. For everything else,
prefer decoupling into independently releasable components in the first
place — an ecosystem of loosely coupled services, each independently
versioned and released, scales change velocity far better than any tuple
scheme can, but only works if the components stay backward- and
upward-compatible with each other as a continuous discipline (see
[API version coexistence](api-version-coexistence.md)), since there's no
single point where the whole system's version set is ever tested together.
