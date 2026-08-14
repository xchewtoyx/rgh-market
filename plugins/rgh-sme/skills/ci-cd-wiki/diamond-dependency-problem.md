---
type: concept
title: Diamond Dependency Problem
description: >
  When two dependency paths require incompatible versions of the same library,
  the consumer cannot reconcile both without upgrading, downgrading, or patching.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 23"
---

# Diamond Dependency Problem

Dependency management is a **network** problem, not a single import. The
classic conflict: `libuser` depends on `liba` and `libb`, both depend on
`libbase`, but `liba` requires `libbase` v1 and `libb` requires v2 after
asynchronous upgrades. Any node required in two incompatible versions via
different paths creates the same shape.

Language tolerance varies: Java shading can embed isolated copies until types
cross boundaries; C++ One Definition Rule makes multiple versions undefined
behavior. OS, compiler, and language version requirements act like hidden
nodes in the graph.

Fixes when conflict appears: move versions forward/backward until compatible,
or patch locally — hard because the discovering engineer rarely owns both
sides. Prevention: [one version rule](one-version-rule.md),
[minimum version selection](minimum-version-selection.md), bundled
distributions, or [live at head dependency model](live-at-head-dependency-model.md)
with downstream CI.

Prefer [source-level integration](source-vs-binary-component-integration.md)
over binary dependency graphs when organizational boundaries allow — source
control problems are cheaper than dependency management problems at scale.
