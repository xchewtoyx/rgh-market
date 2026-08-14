---
type: concept
title: Long Lived Dev Branch Anti Pattern
description: >
  Feature branches that defer integration to trunk accumulate merge debt,
  isolate regressions, and invite coordination overhead that testing and CI
  address better.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# Long Lived Dev Branch Anti Pattern

Before reliable automated testing, teams used **dev branches** to protect trunk
stability. The same commits must merge eventually; the pattern is misguided at
scale:

- Small merges by the authoring engineer beat large batched merges by a coordinator.
- Isolating a regression is harder when many changes land in one merge.
- Long-lived branches create expensive re-sync and retest overhead.
- Organizations often respond with merge coordinators and strategy meetings
  instead of [trunk-based development](trunk-based-development.md), CI, and
  [feature toggles](feature-toggle.md).

Uncommitted local work is already a branch (explicit in DVCS). The alternative:
integrate to trunk continuously, gate incomplete features at runtime, keep the
build green. DORA research correlates absence of long-lived dev branches with
high delivery performance.

**Release branches** differ — short-lived stabilization with cherry-picks,
expected to be abandoned, not merged wholesale. See
[branch-for-release pattern](release-branching-pattern.md). Highest performers
with [continuous deployment](continuous-deployment.md) often skip release branches
entirely.

One clear **source of truth** branch (usually trunk) is required for sublinear
scaling — otherwise "which features are in this release?" reinvents centralized
truth manually.
