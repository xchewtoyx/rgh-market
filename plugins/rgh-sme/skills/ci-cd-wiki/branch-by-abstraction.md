---
type: concept
title: Branch by Abstraction
description: >
  A technique for making large structural changes (replacing a library,
  swapping a component) directly on mainline, incrementally, by introducing an
  abstraction layer instead of diverging onto a long-lived branch.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 14"
---

# Branch by Abstraction

Large refactorings (e.g. replacing an ORM library) look like they need a
long-lived branch, because the change touches a lot of code and can't be
finished in a day. Branch by abstraction achieves the same result without
[integration hell](integration-hell.md), by making the change incrementally on
[trunk](trunk-based-development.md):

1. Introduce an abstraction layer over the old component, still on mainline.
2. Refactor existing call sites to go through the abstraction layer (calling
   the old implementation underneath) — mainline stays green throughout.
3. Build the new component's implementation behind the same abstraction layer,
   incrementally, over however many days it takes — still committed to
   mainline daily, still fully working via the old implementation.
4. Switch the abstraction layer to point at the new implementation, via a
   [feature toggle](feature-toggle.md) or configuration change.
5. Remove the old implementation and, once it's no longer needed, the
   abstraction layer itself.

Every one of these steps is a normal commit to mainline; the application
remains testable and releasable throughout the entire multi-week effort. This
is the general pattern for reconciling "this change is too big to do in a
day" with [continuous integration](continuous-integration.md)'s requirement
to integrate daily: the change is still too big to finish in a day, but it's
decomposed into steps that are each small enough to commit safely.

When the unit being replaced is an entire application or service rather than
an internal component, the same incremental logic applies at a larger scale
as the [strangler fig pattern](strangler-fig-pattern.md): freeze the legacy
system behind an API instead of an in-process abstraction layer, and migrate
callers to a new implementation over time.
