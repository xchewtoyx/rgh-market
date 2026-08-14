---
type: concept
title: Module View
description: >
  A module view documents a system's code-time structure — implementation
  units, their responsibilities and interfaces, and the relations between
  them — as distinct from how the system behaves at runtime.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

A module is an implementation unit that provides its responsibilities
through an interface. A module view documents code-time structure: how the
system is divided into modules (often hierarchically), and the relations
between them — decomposition, uses, generalization, and allowed-to-use are
the standard relation types. This is a different structure from a
[component-and-connector view](component-and-connector-view.md), which
shows runtime units instead; conflating the two — treating a source module
as if it were a runtime process, or vice versa — damages both the design
and its documentation.

For each element, document its responsibility, visibility, interface, and
implementation constraints. A module's interface is broader than a
programming-language signature: it includes every resource the module
provides or requires. For each relation, define its meaning and the
topology it is and is not allowed to form (e.g., whether cycles are
permitted).

Module views support division of labor, information hiding, change-impact
analysis, incremental construction, reuse, and source-code navigation —
which relation you're showing determines which of these tasks the view
serves. See [decomposition](decomposition-view.md),
[uses](uses-view.md), [layered](layered-view.md), and
[generalization](generalization-view.md) views for the specific module
styles.

Notation must distinguish module kinds and relation semantics explicitly.
UML packages and classes can represent modules, but their meaning is
overloaded across contexts, so a legend and textual supplement are
required — visual resemblance between diagrams is not evidence that the
underlying relations mean the same thing. A module view should also
identify its roots, its levels of decomposition, and which modules are
external to the system being documented.
