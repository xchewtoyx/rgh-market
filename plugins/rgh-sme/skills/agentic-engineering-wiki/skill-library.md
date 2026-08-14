---
type: concept
title: Skill Library
description: >
  Persist newly composed skills that proved useful so later tasks can reuse
  them as first-class tools instead of rediscovering the composition.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
---

When an agent frequently chains the same tools, those transitions are
candidates for composition into a larger composite tool. Voyager-style systems
go further with a **skill manager**: newly created skills (often programs) that
helped complete a task are added to a skill library — conceptually an evolving
extension of the [tool inventory](tool-inventory.md) — for reuse on future
tasks.

This is external memory for capabilities, not just facts: the harness grows the
action repertoire from successful trajectories. Pair with
[tool selection ablation](tool-selection-ablation.md) so the library stays
useful rather than accumulating unused or unreliable skills.
