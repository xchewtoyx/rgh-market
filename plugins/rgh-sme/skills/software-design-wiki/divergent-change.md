---
type: concept
title: "Code Smell: Divergent Change"
description: >
  One module gets changed in different ways for different, unrelated
  reasons — a sign that unrelated contexts have been tangled together inside
  it, usually only visible after several instances have accumulated.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Divergent Change is one module getting changed in different ways for
different, unrelated reasons — for example, "change these three functions
for every new database; these four for every new financial instrument."
It's [low cohesion](cohesion.md) made visible: the module's responsibilities
don't actually share a unifying purpose, so different change scenarios each
only exercise part of it. It is also a concrete instance of [change
amplification](change-amplification.md):
a single design decision (adding a database, adding a financial instrument)
ends up touching more of the module than it should, because the module
tangles two unrelated concerns together. This smell usually only becomes
visible after several instances of one category have accumulated, since
context boundaries are unclear early on.

The fix is separating the tangled contexts into their own modules: if the
two aspects form a natural sequence, use [Split Phase](split-phase.md); if
there's more back-and-forth between them, create separate modules and use
[Move Function](move-function.md); if individual functions internally mix
both concerns, [Extract Function](extract-function.md) first, then move the
piece that belongs elsewhere. For classes,
[Extract Class](extract-class.md) formalizes the same split.

Compare [Shotgun Surgery](shotgun-surgery.md), the mirror-image smell: there,
one change requires touching many modules; here, many kinds of change are
forced through one module.
