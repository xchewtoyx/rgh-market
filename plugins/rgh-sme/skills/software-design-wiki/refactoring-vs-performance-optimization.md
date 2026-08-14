---
type: concept
title: Refactoring Is Not Performance Optimization
description: >
  Refactoring and performance optimization both preserve overall
  functionality while changing code, but they optimize for different
  things — refactoring for understandability and cheap future change,
  optimization only for speed, even at comprehensibility's expense.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 2"
---

[Refactoring](refactoring-preserves-behavior.md) and performance
optimization look similar from the outside — both change code while
preserving overall functionality — but they target different things.
Refactoring optimizes for "easier to understand and cheaper to modify,"
which may speed up or slow down execution as a side effect. Performance
optimization cares only about speed, even at the cost of comprehensibility.

The recommended sequencing (outside hard real-time systems) is to write
tunable software first, ignoring performance, then tune it for sufficient
speed once measurement shows it's needed — see [measuring before
modifying for performance](measure-before-modifying.md) and [simplicity and
performance are compatible goals](simplicity-and-performance-are-compatible.md).
Well-factored code helps this sequencing twice over: it frees up time, since
features get added faster, leaving room for a later tuning pass; and it
gives finer profiling granularity, since smaller functions let a profiler
point at a more precise hot-spot.
