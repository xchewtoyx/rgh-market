---
type: concept
title: "Code Smell: Primitive Obsession"
description: >
  Reluctance to create small domain-specific types leads to money as a bare
  number, unit-less physical quantities, and manual range checks — strings
  standing in for structured domain concepts are the worst offender.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Primitive Obsession is reluctance to create small domain-specific types —
money, coordinates, ranges — which shows up as money represented as a plain
number, unit-less physical quantities (silently mixing inches and
millimeters), and manual range checks (`if (a < upper && a > lower)`)
scattered wherever the concept is used. Strings are the worst offender:
"stringly typed" is the pejorative term for representing a structured domain
concept, like a phone number, as a bare string — which loses the consistent
display and validation logic a real type would centralize.

Cure: [Replace Primitive with Object](replace-primitive-with-object.md) gives the concept its own type. For a
type code driving conditional logic specifically, follow up with [Replace
Type Code with Subclasses](replace-type-code-with-subclasses.md) and then
[Replace Conditional with Polymorphism](replace-conditional-with-polymorphism.md).
Recurring groups of primitives are really [Data Clumps](data-clumps.md) —
[Extract Class](extract-class.md) or
[Introduce Parameter Object](introduce-parameter-object.md).

A specific, compiler-enforceable payoff of the cure: see [strong types
prevent parameter and unit
confusion](strong-types-prevent-parameter-and-unit-confusion.md) for how
wrapping same-typed parameters and physical quantities in their own types
turns argument-order and unit-mismatch bugs into compile errors.
