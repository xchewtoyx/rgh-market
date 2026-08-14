---
type: concept
title: "Refactoring: Consolidate Conditional Expression"
description: >
  Fold a sequence of separate-looking condition checks that all lead to
  the same outcome into one combined condition, making explicit that
  they're really one composite question rather than several independent
  ones — and giving that combined question a name.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 10"
---

Sometimes several conditional checks, each testing something different, all
lead to the *same* resulting action — a sequential run of near-identical-
looking `if` statements that are really testing one composite question, not
several independent ones. Folding these into a single condition matters for
two reasons: **clarity** — a sequence of separate-looking checks visually
implies separate concerns even when they're really one combined check with
one combined meaning, and consolidating makes that single-check nature
explicit; and it sets up
[Extract Function](extract-function.md) on the resulting condition — naming
the combined check replaces a statement of *what* is being tested with
*why* it matters, one of the most useful things a name can do for a piece
of code. The corresponding reason *not* to consolidate: if the checks
really are independent concerns that just happen to produce the same
result, forcing them into one combined expression would misrepresent that
independence.

**Mechanics**: first confirm none of the conditions being combined have
side effects — if any do, apply
[Separate Query from Modifier](separate-query-from-modifier.md) to clean
that up before proceeding, since combining conditions with side effects would
risk changing how many times, or whether, those side effects fire. Combine
two of the conditions at a time using the appropriate logical operator: a
**sequence of sibling checks** combines with `or` (any one being true
triggers the shared outcome); **nested `if` statements** combine with `and`
(all must be true together). Test after each combination. Repeat until
every condition has folded into one. Finally, consider Extract Function on
the resulting combined condition to give it a name.

A mixed bag of sequential and nested checks can be combined using both
`and` and `or` as needed — but the resulting expression tends to get messy
quickly when it does, making liberal use of Extract Function on sub-pieces
especially important to keep the result understandable.
