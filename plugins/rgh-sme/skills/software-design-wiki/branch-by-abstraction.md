---
type: concept
title: Branch by Abstraction
description: >
  A technique for making a large structural change (such as replacing a
  component) directly on mainline, by inserting an abstraction layer that
  lets old and new implementations coexist until the switch is complete.
sources:
  - title: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation"
    resource: "Continuous Delivery (Humble, Farley), ch. 14"
---

Branch by abstraction avoids the alternative of doing a large refactoring —
replacing an ORM, swapping out a subsystem — on a long-lived feature branch,
where the change accumulates merge debt and stays unverified against the rest
of the system until it lands. Instead, the change is made incrementally on
mainline itself, in five steps:

1. Introduce an abstraction layer in front of the component being replaced.
2. Refactor existing callers to go through the abstraction layer, still
   backed by the old implementation.
3. Build the new implementation behind the same abstraction layer,
   incrementally, committing to mainline daily.
4. Switch the abstraction layer to route to the new implementation (a
   one-line change, often behind a feature toggle for a fast revert).
5. Remove the old implementation and, if it is no longer earning its keep,
   the abstraction layer itself.

Every step is a small, independently committable, behavior-preserving change
— the application stays green and releasable throughout, even mid-migration.
This is the same underlying move as introducing a [seam](seam.md) — a place
where behavior can be swapped without editing the call site — applied at the
scale of a whole component rather than a single function call, and worked
incrementally rather than in one [refactoring binge](incremental-extraction-over-refactoring-binges.md).
It is the mainline-development counterpart to the [strangler fig
pattern](strangler-fig-pattern.md): both replace something piece by piece
behind a dispatching layer instead of a big-bang cutover, but strangler fig
routes live traffic between two running systems while branch by abstraction
routes calls between two implementations linked into the same codebase, and
is what makes the replacement possible without ever branching away from
mainline for more than a day.
