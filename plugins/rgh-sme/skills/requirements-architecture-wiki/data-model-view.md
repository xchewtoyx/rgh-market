---
type: concept
title: Data Model View
description: >
  A data model view describes the entities, attributes, and relationships
  a system operates on, independent of runtime structure, and materially
  affects performance, integrity, integration, and modifiability.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

A data model view describes the entities a system operates on, their
attributes, and the relationships between them — association,
generalization/specialization, and aggregation are the standard
relationship kinds. It is a module-style view in the sense that it
documents a structure independent of runtime behavior, but its subject is
the shape of the data rather than the shape of the code.

The data model is worth documenting as its own view, separate from the
[decomposition](decomposition-view.md) or [component-and-connector
structure](component-and-connector-view.md), because it drives concerns
those other views don't directly expose: it guides database
implementation, and it has a direct effect on performance (how data is
shaped affects how expensively it can be queried), integrity (what
invariants the model can and can't express), integration (whether two
systems' models can be reconciled), and modifiability (how much of the
system a change to one entity's shape will ripple through).

A data model view is rarely produced in one pass — see [conceptual,
logical, and physical modeling progression](conceptual-logical-physical-modeling-progression.md)
for the staged process that takes a model from a business-facing
conversation through to a deployable, platform-specific schema.
