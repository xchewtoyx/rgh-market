---
type: concept
title: Eliminate Circular Dependencies for Testability
description: >
  Cycles force interface-and-mock workarounds that mask runtime coupling;
  refactor to return values instead of callbacks so classes can be understood
  and tested in isolation.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 8"
---

A **circular dependency** is two or more classes that directly or indirectly
depend on each other. Classic pattern: service A constructs service B and
passes `this`; B calls back into A when done.

Cycles add heavy [cognitive load](cognitive-load.md) — no clear starting point;
understanding one class requires the whole cluster.

Cycles interfere with testing — isolating behavior often forces interfaces plus
mocking, which is a no-go for domain-model testing per
[observable behavior](observable-behavior-vs-implementation-details.md) guidance.
Introducing `ICheckOutService` removes the compile-time cycle but the runtime
cycle remains — cognitive load doesn't shrink.

**Better fix: eliminate the cycle.** Have the callee return a result value;
caller receives it directly without back-reference (e.g. `GenerateReport`
returns `Report` instead of calling back into checkout service).

Rare to eliminate all cycles; minimize damage by keeping any remaining
interdependent graphs as small as possible.

See [coupling](coupling.md) and [four types of code for testing priority](four-types-of-code-for-testing-priority.md).
