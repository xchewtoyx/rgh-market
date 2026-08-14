---
type: concept
title: Tuple-Versioned Deployment for Tightly Coupled Components
description: Testing, approving, and deploying a specific named combination of component versions as a single unit, rather than any component's latest version independently, when the components are too tightly coupled to vary separately.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 11"
---

When infrastructure is assembled from several independently-versioned components — a load balancer plus its plugins plus the kernel it runs on, or a virtualization stack's management layer plus hypervisor plus storage layer — testing every possible version combination is usually infeasible, and most combinations would never actually occur in practice anyway. Tuple versioning narrows this: test, approve, and deploy one specific named combination (for example, "load balancer 4.2 + plugin-set 1.9 + kernel 5.15") as a single indivisible unit. If a test against that combination fails, the fix and retest happens against the whole tuple, not a single component in isolation; only combinations that have been explicitly tested and approved as a tuple are ever deployed; and a rollback reverts to the last approved tuple rather than to some arbitrary independent mix of component versions.

This is the right tool specifically for components with real, high [coupling](infrastructure-component-coupling-and-cohesion.md) — where a version change in one component routinely forces a compatible change in another, and where an untested combination is genuinely likely to fail rather than just theoretically possible. Its cost is that lock-step tuple versioning caps the whole group's rate of change: one component's delayed release blocks every other component's otherwise-ready release from shipping, so it should be scoped to only the components that actually need it rather than applied as a default habit.

Where components are instead genuinely loosely coupled, each can be tested and pushed independently at its own pace, and a failure is more cleanly attributable — a broken component that just changed points at itself, while other components breaking afterward signals a real, previously-hidden incompatibility. Sustaining that independence at scale requires the components to take backward and forward compatibility seriously as an ongoing discipline — announcing breaking API changes well ahead of making them — since there's no shared release train forcing every consumer to update in lockstep.
