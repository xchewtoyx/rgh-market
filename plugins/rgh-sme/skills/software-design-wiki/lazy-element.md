---
type: concept
title: "Code Smell: Lazy Element"
description: >
  A function or class that isn't earning its own structural overhead — a
  function whose name says no more than its one-line body, or a hook built
  for growth that never came.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

A Lazy Element is a program element — a function or a class — that isn't
earning the structural overhead of existing separately: a function whose
name says no more than its one-line body already does, a class reduced to
near-nothing by prior refactoring, or a hook that was built for anticipated
growth that never came. Cure: [Inline Function](inline-function.md) or [Inline Class](inline-class.md); for
inheritance specifically, [Collapse Hierarchy](collapse-hierarchy.md). Framed sympathetically as
needing to "die with dignity" — the element earned its keep once, or was a
reasonable bet, and removing it is tidying up rather than admitting a
mistake.

Distinct from [deleting unused code](delete-unused-code.md): a Lazy Element
is still called and still doing something, just not enough to justify a
separate name and boundary; unused code is not called at all.
