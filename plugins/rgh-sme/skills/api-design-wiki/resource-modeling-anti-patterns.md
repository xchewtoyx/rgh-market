---
type: concept
title: Resource Modeling Anti-Patterns
description: >
  Over-promoting concepts to resources, deep parent chains, and over-inlining
  shared data that break API simplicity and integrity.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 4"
---

**Resources for everything** — not every modeled concept needs an id and five
standard methods. One-to-one owned parts with bounded collections belong as
plain data types nested in the parent (bounding box on annotation) unless
independent CRUD is required. Rule: if you never interact with it apart from
its parent, keep it a field; if independent but small, [inlining](embedded-entity-vs-linked-information-holder.md)
may still suffice.

**Deep hierarchies** — each level should earn cascade delete/access. Demote levels
that are really filters (school, semester on a course catalog) to fields or
[cross-references](resource-hierarchy-vs-cross-reference.md) — flatten to
University → Course → Document with `school` and `semester` on `Course`.

**In-line everything** — denormalizing shared entities (author duplicated on
every book) forces integrity questions on update. Shared data referenced by
many owners should stay a separate resource with a pointer.

Optimize for the **common case** without blocking advanced cases — weigh fetch
frequency against related payload size and growth.

Pairs with [resource layout](resource-layout.md) relationship selection.
