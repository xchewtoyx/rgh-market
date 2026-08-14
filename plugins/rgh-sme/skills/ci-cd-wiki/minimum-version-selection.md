---
type: concept
title: Minimum Version Selection
description: >
  When a dependency requirement bumps, resolve to exactly the requested minimum
  version rather than the newest available, staying closer to what the author tested.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 23"
---

# Minimum Version Selection

Classic package solvers, given `liba requires libbase ≥ 1.7`, often jump to
the **newest** available version (1.8+). **Minimum Version Selection (MVS)**
(Russ Cox, Go modules) selects **exactly 1.7** — the version the requiring
author developed and tested against — producing builds closer to the author's
known-good dependency set.

Rationale: smaller forward steps are safer, analogous to integrating an hour
of work vs. a year at once. MVS does not fix [semantic versioning](semantic-versioning.md)'s
fundamental limitations (human judgment, Hyrum's Law, library-granularity
overconstraint) but is a practical improvement over "always newest."

Contrast [live at head dependency model](live-at-head-dependency-model.md)
(always current stable) and [dependency pinning](dependency-pinning.md) (exact
immutable pins for release reproducibility — compatible with MVS at resolve time).
