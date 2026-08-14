---
type: concept
title: "Code Smell: Feature Envy"
description: >
  A function that interacts more with another module's data than its own —
  classically, half a dozen getter calls on another object just to compute a
  value — usually belongs closer to the data it envies.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Feature Envy is a function that interacts more with another module's data or
functions than with its own — the classic case is half a dozen getter calls
on another object just to compute a value locally. The underlying heuristic
is "put things together that change together": data and the behavior that
references it usually change together, so the cure is
[Move Function](move-function.md) to relocate the envious function near the
data it actually uses. If only part of a function is envious,
[Extract Function](extract-function.md) the envious part first, then Move
Function just that piece. When a function touches several other modules, the
heuristic is to co-locate it with whichever module holds most of the data it
uses.

Two named exceptions to "put things together that change together": the
Strategy and Visitor design patterns, and Kent Beck's Self Delegation. These
deliberately isolate small, override-prone behavior in its own place at the
cost of extra indirection, and are the standard countermeasure to [Divergent
Change](divergent-change.md) — a case where the smell's usual cure would
recreate the very problem it's meant to solve.
