---
type: concept
title: "The Two Hats: Adding Functionality vs. Refactoring"
description: >
  Development time splits into two distinct modes, adding functionality and
  refactoring, and staying consciously aware of which one you're doing
  changes how you program moment to moment.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 2 (Kent Beck)"
---

Kent Beck's framing: development time splits into two distinct modes.
**Adding functionality** means adding new capabilities, measured by new
passing tests, with no restructuring. **Refactoring** means restructuring
only — no new functionality, and no new tests unless a missed case surfaces
along the way. See [refactoring preserves behavior](refactoring-preserves-behavior.md)
for what that restructuring-only constraint actually means.

Practitioners swap hats frequently — sometimes every few minutes — and stay
consciously aware of which hat is on, because it changes how you program:
for example, whether a failing test is expected right now, or a signal
something just broke. Conflating the two modes is a common way small
mistakes creep in — a "quick refactor" that quietly changes behavior, or a
feature addition that also reshapes surrounding code without the
step-by-step safety of the [refactoring rhythm](rhythm-of-refactoring.md).
