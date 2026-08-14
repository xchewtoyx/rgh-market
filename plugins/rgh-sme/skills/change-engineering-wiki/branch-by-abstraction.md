---
type: concept
title: Branch by Abstraction
description: >
  Replace a large architectural component through a sequence of small,
  independently deployable commits on trunk by inserting an abstraction
  layer first, instead of doing the replacement on a long-lived branch.
sources:
  - title: "Continuous Delivery"
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 14"
  - title: "Refactoring (2nd ed.)"
    resource: "Refactoring: Improving the Design of Existing Code (Fowler, Beck), ch. 2"
---

# Branch by Abstraction

A large structural change — replacing a library, swapping a storage
backend, rewriting a subsystem — feels like it needs a long-lived feature
branch, because the change can't be released half-finished. Branch by
abstraction gets the same isolation without a branch, keeping every commit
on [trunk](trunk-based-development.md) and the application releasable
throughout:

1. Introduce an abstraction layer in front of the component being replaced;
   existing callers are refactored to go through it, with the old
   implementation behind it. No behavior changes yet.
2. Build the new implementation behind the same abstraction, incrementally,
   commit by commit on trunk, while the old implementation still serves
   real traffic.
3. Switch the abstraction to the new implementation, typically via a
   feature flag so the cutover itself can be staged and reverted like any
   other change.
4. Remove the old implementation and the now-unneeded abstraction layer.

Every step is a small, independently safe commit, so this is the technique
that reconciles [working in small batches](working-in-small-batches.md)
with changes that are individually large in scope — it decomposes a
large change into a sequence of small ones rather than accepting either a
long-lived branch or an unsafely large single commit. The cutover step
composes directly with [feature flag blast radius isolation](feature-flag-blast-radius-isolation.md):
flipping the abstraction back to the old implementation is the rollback
path if the new one misbehaves.

For replacing a whole service, database, or system boundary rather than an
in-codebase component, see the [strangler fig pattern](strangler-fig-pattern.md) —
the same incremental-replacement idea, but routed externally (a proxy or
gateway) instead of through an in-process abstraction layer.
