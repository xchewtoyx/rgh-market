---
type: concept
title: "Refactoring: Split Loop"
description: >
  Separate a loop doing two unrelated things in one pass into two loops
  that each do only one, so each can be understood, returned, and later
  optimized in isolation, deferring any performance concern about the
  extra traversal until profiling actually shows it matters.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 8"
---

Loops often do two unrelated things in one pass purely because a single
pass *can* do that — but this forces anyone modifying either piece of
behavior to understand both. Splitting the loop means each resulting loop
only needs to be understood in isolation. There's a usability payoff too: a
loop computing exactly one value can simply return that value, whereas a
loop computing several things is stuck returning a bundled structure or
populating multiple local variables. Splitting is routinely followed by
[Extract Function](extract-function.md) on each resulting loop, and often
in turn by [Replace Loop with Pipeline](replace-loop-with-pipeline.md) on
one or both.

**Anticipated objection**: many programmers dislike this because it forces
the collection to be traversed twice. The standard reply is to
[separate refactoring from optimization](refactoring-vs-performance-optimization.md):
get the code clear first, and if profiling later shows the extra traversal
is actually a bottleneck, merging the loops back together is easy. In
practice, iterating even a large list is rarely the bottleneck, and
splitting loops often *enables* other, more powerful optimizations
downstream — once each loop does one thing, that one thing can sometimes be
replaced wholesale with a faster built-in operation via
[Substitute Algorithm](substitute-algorithm.md).

**Mechanics**: copy the loop, so two identical copies are running
temporarily. Identify and remove whichever side effects or computations are
duplicated across the two copies until each loop does only one of the
original two things. Test.
