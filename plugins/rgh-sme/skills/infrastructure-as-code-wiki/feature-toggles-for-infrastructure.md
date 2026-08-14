---
type: concept
title: Feature Toggles for Infrastructure
description: Using a stack parameter to switch between old and new code paths within a single stack project, so a multi-day infrastructure change can be pushed incrementally without branching.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 21"
---

When a change to a [stack](infrastructure-stack.md) takes more than a trivial amount of work but doesn't warrant standing up a whole [parallel instance](incremental-infrastructure-change.md) to build it alongside the old version, a feature toggle lets the new and old code paths coexist in the same stack project, selected by a [stack instance parameter](stack-parameter-design-principles.md) — production stays on the old path while other environments exercise the new one, still getting the benefit of pushing small changes into the shared, [continuously tested](progressive-testing-for-infrastructure.md) codebase along the way.

This avoids the classic problems of branching the code itself for a long-running change: bugfixes needing to be merged into two branches, one branch getting less rigorous testing than the other, and a risky "big bang" cutover once the branch is finally ready to merge. A feature toggle keeps everything on the mainline, tested together the whole time.

Two practical rules keep toggles from becoming their own maintenance burden: minimize how many are active at once and remove each one — along with the old code path it guards — as soon as the migration completes; a toggle that survives more than a few weeks has usually turned into a permanent configuration parameter and should be renamed and treated as one rather than left looking temporary. And name each toggle for exactly what it does and which direction it points — `toggle_use_multiple_vlans` is unambiguous, while `toggle_vlans` invites someone to get the polarity backwards.

Feature toggles are one of the pushing-incomplete-changes-to-production techniques alongside [backward compatible transformations](backward-compatible-infrastructure-transformation.md) and running full [parallel instances](incremental-infrastructure-change.md); which one fits depends on how large and how disruptive the underlying change is.
