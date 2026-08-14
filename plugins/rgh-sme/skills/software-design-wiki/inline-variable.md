---
type: concept
title: Inline Variable
description: >
  Remove a variable when its name adds nothing over the expression it holds,
  or when it's actively getting in the way of refactoring the code around
  it.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 6 (formerly Inline Temp; inverse of Extract Variable)"
---

Variables naming expressions are usually good — see [Extract
Variable](extract-variable.md) — but sometimes a variable's name adds
nothing over the expression itself, or the variable actively gets in the way
of refactoring the surrounding code. In those cases, inline it away.

**Mechanics**: confirm the right-hand side of the assignment is free of
side effects; if the variable isn't already declared immutable, make it so
and test — this confirms it's assigned exactly once, a necessary
precondition, since a reassigned variable can't be safely inlined this way;
find the first reference and replace it with the right-hand-side expression,
testing; repeat for each remaining reference; remove the now-unused
declaration.
