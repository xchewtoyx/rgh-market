---
type: concept
title: Invariants
description: >
  An invariant is a property that always holds for a variable or data
  structure, which cuts down the number of special cases code has to
  consider and makes it easier to reason correctly about behavior.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 17"
---

Example: "every line in this text data structure is always newline-
terminated." An invariant is a form of
[consistency](consistency-as-a-design-tool.md) at the data level — code that
can rely on the invariant holding everywhere doesn't need to check for or
handle the case where it doesn't, which is the same underlying mechanism as
[designing special cases out of existence](design-special-cases-out-of-existence.md).
Invariants need to be documented explicitly (see
[precision-adding comments](precision-adding-comments.md)), since they are
exactly the kind of fact that isn't obvious from a single read of the code
that maintains them, but every piece of code touching the data implicitly
depends on them holding.
