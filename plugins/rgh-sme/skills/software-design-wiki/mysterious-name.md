---
type: concept
title: "Code Smell: Mysterious Name"
description: >
  A name that fails to communicate what a function, variable, class, or
  module does or represents is often a symptom of deeper design trouble, not
  just a labeling problem.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Naming is one of "the two hard things" in programming, and renames —
[Change Function Declaration](change-function-declaration.md),
[Rename Variable](rename-variable.md), [Rename Field](rename-field.md) —
are among the most common refactorings performed. The useful diagnostic is what happens when
naming turns out to be genuinely hard: struggling to find a good name is
often a symptom of deeper design trouble, not merely a wording problem —
working through the difficulty has frequently led to real simplification of
the thing being named, not just a better label for the same thing. See [a
name should create a clear mental image](names-should-create-a-clear-image.md)
and [precise names](precise-names.md) for what a successful rename is aiming
at.
