---
type: concept
title: Release Atomicity and Tuple Testing
description: >
  For tightly coupled components that cannot be made independently
  deployable, test and deploy a specific named combination of component
  versions as one atomic unit instead of versioning each independently.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 11"
---

# Release Atomicity and Tuple Testing

[Independent deployability](independent-deployability.md) is the goal, but
some components are genuinely tightly coupled — a load balancer plus its
plugins plus the kernel it runs on, or a virtualization stack's management
layer plus hypervisor plus storage layer — where testing every version of
one component against every version of the others is infeasible, and most
combinations would never occur in practice anyway.

**Tuple testing** is the fallback for this case: test, approve, and deploy
a specific *named combination* of component versions as a single atomic
unit (e.g. "Service A@101 + Service B@456 + Service D@246"). If a test
against that tuple fails, the fix-and-retest cycle restarts from the whole
tuple, not from one component in isolation. Only combinations that have
been explicitly tested and approved as a tuple are ever deployed, and
[rollback](rollback-vs-roll-forward.md) means reverting to the last
approved tuple as a whole, never an arbitrary mix of component versions.

The cost is coupled velocity: lock-step tuple versioning caps the overall
rate of change, since one component's delayed release blocks every other
component that would otherwise be ready to ship. Where components are
genuinely loosely coupled, this cost disappears — each can be tested and
released independently, on its own cadence, with a failure more cleanly
attributable to whichever component actually changed. Sustaining that
independence at scale requires the components to treat backward
compatibility as an ongoing discipline (see [parallel API version
coexistence](parallel-api-version-coexistence.md)), including advance
announcement of incompatible changes and tooling that detects who is still
depending on an interface slated for a breaking change.
