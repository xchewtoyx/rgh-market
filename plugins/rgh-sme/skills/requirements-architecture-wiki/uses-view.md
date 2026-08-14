---
type: concept
title: Uses View
description: >
  A uses view records that one module's correctness depends on another
  module's presence and correctness, supporting change-impact analysis,
  build order, and incremental subsets of the system.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

A **uses** relation between two modules means one requires the other to be
present and correct in order to satisfy its own specification — it is a
statement about correctness dependency, not just about who calls whom. This
is what makes the uses view useful for three practical questions: what
breaks if I change or remove this module (change-impact analysis), what
must be built and tested before what (build order), and what subset of the
system can be built and shipped as a functioning increment
(incremental development).

Acyclic or deliberately controlled uses relations make incremental
development tractable: if module A uses B which uses C, you can build and
verify C, then B, then A, and ship any prefix of that chain as a working
subset. Uncontrolled cyclic uses relations remove this option — the whole
cycle has to be built and verified together. Documenting the uses view
therefore isn't just descriptive; it's the basis for a concrete
constraint (keep this acyclic, or keep cycles to this bounded set) that
the [module view](module-view.md) as a whole should be checked against.

A [layered view](layered-view.md) is a stricter, direction-constrained
special case of a uses structure — a layering is a uses view where the
allowed direction of dependency has been fixed system-wide, rather than
decided module pair by module pair.
