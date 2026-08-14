---
type: concept
title: Strangler Fig Pattern
description: Migrating away from a tightly-coupled system by freezing it behind a stable API and building all new functionality in the new architecture around it, rather than attempting a full rewrite.
sources:
  - title: The DevOps Handbook
    resource: "The DevOps Handbook (Gene Kim, Jez Humble, Patrick Debois, John Willis, Nicole Forsgren), ch. 13"
---

Named by Martin Fowler after strangler vines, which seed in a host tree's branches and gradually grow down and root in the soil, eventually enveloping and outliving the tree they grew on: the pattern puts an existing system's functionality behind a stable, versioned API and freezes further changes to it, then builds all new functionality in new components using the desired architecture, calling into the old system only where still necessary. Over time, functionality migrates out of the old system piece by piece; eventually the old system may shrink to nothing and disappear.

This is a deliberate alternative to a full rewrite, which Fowler himself warns tends to be riskier and more complex than it looks — old bugs and edge cases the rewrite quietly needs to reproduce, a looming cutover date, and pressure to keep adding new features to the very system being replaced. The strangler fig pattern avoids ever needing a single big-bang cutover: value is delivered incrementally, each migrated piece is a small, independently testable and deliverable change, and the risk of any one step is bounded, the same [incremental infrastructure change](incremental-infrastructure-change.md) discipline applied at the scale of an entire system's architecture rather than a single stack.

For the pattern to actually achieve loose coupling rather than just relocating the tight coupling, the new components built around the frozen old system must themselves stay properly decoupled — reaching directly into the old system's database, for instance, defeats the purpose just as thoroughly as if the strangler application were part of the monolith itself. If the old system lacks a clean API to call, one has to be built for it, or the messy interaction wrapped inside a client library that exposes a clean interface to everything else — the same discipline behind the [facade module pattern](facade-module-pattern.md) and [infrastructure dependency patterns](infrastructure-dependency-patterns.md) applied to a legacy interface rather than a purpose-built one.
