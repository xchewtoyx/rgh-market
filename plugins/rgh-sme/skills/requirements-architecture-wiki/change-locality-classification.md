---
type: concept
title: Change Locality Classification
description: >
  Classifying an anticipated change as local, nonlocal, or architectural
  tells you whether the current design can absorb it incrementally or
  whether it will ripple through the whole system.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 2"
---

Every architecture partitions the space of possible future changes into
three categories, and which category a given change falls into is a
direct consequence of the design, not of how hard the change sounds in
isolation:

- **Local**: fixed by modifying a single element (e.g., adding a pricing
  rule inside one module).
- **Nonlocal**: requires changes to multiple elements, but the
  architectural approach itself stays intact (e.g., a new business rule
  that also needs new database fields and a new UI display) — these can
  usually be staged and rolled out incrementally because no element's
  fundamental role changes.
- **Architectural**: changes the fundamental interaction pattern itself
  (e.g., single-threaded to multi-threaded), and is likely to touch the
  whole system rather than a bounded subset of it.

An architecture is effective, from a modifiability standpoint, to the
extent that the changes actually expected over the system's life fall
into the local category — this is the concrete, checkable form of "design
for anticipated change," as opposed to an unfalsifiable claim that a
system is "flexible." Classifying a proposed change this way before
committing to it is also what distinguishes a genuine [requirement vs
design decision](requirement-vs-design-decision.md) question from a
routine implementation task: an architectural-category change usually
means the request needs architecture-level rationale and review, not just
a ticket. Failing to keep expected changes local over time is what
accumulates as architecture debt.
