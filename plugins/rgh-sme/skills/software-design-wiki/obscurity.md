---
type: concept
title: Obscurity as a Cause of Complexity
description: >
  Obscurity is when important information about a system is not obvious from
  the code, and it is one of the two underlying causes of software
  complexity, chiefly responsible for unknown unknowns.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 2"
---

Examples: an overly generic variable name (`time`) that conveys nothing about
what it holds; a variable's units left undocumented; a new error status that
requires a corresponding entry in a separate message table, where nothing
about the status declaration hints that table exists; the same variable name
reused for different purposes in different places.

Obscurity often gets treated as a documentation gap (fix it by writing more
comments), but it's fundamentally a design issue: a clean, obvious design
needs less documentation to begin with. Leaning heavily on documentation to
compensate for an obscure design is itself a [red flag](red-flags-as-design-smells.md)
that the design is off — the better fix is to simplify the design, not to
write more prose around it.

Obscurity is what produces [unknown unknowns](unknown-unknowns.md) and
compounds [cognitive load](cognitive-load.md), the way
[dependencies](dependencies-as-a-cause-of-complexity.md) produce
[change amplification](change-amplification.md).
