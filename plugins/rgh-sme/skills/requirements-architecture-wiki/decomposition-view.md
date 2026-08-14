---
type: concept
title: Decomposition View
description: >
  A decomposition view assigns system responsibilities to modules and
  submodules, using information hiding and anticipated change as the
  guides for where to draw the boundaries.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

Decomposition is the module style that assigns responsibilities to modules
and their submodules. A good decomposition is guided by information
hiding (each module encapsulates a design decision likely to change) and
by anticipated change (things that are likely to change together are
grouped together), because these are what let people work independently
on different modules without constantly stepping on each other.

A **subsystem** is a grouping that is meaningful to some stakeholder — for
example, a deployable unit, or a team's area of ownership — and it may cut
across the decomposition hierarchy rather than aligning with it. Document
both structures explicitly rather than assuming one implies the other; see
[module view](module-view.md) for what to record about each element.

Decomposition is the view most directly answering "what has to be built
and who owns it," which is why it's typically the first view developers
and new team members need. It is a different question from a [uses
view](uses-view.md) (what depends on what to be correct) or a [layered
view](layered-view.md) (what is allowed to depend on what) — a
decomposition can exist without answering either.
