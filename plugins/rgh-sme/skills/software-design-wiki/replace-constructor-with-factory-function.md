---
type: concept
title: "Refactoring: Replace Constructor with Factory Function"
description: >
  Route object creation through a factory function instead of calling a
  constructor directly, sidestepping constructors' structural limits — a
  fixed return type, a fixed name, and an awkward-to-pass-around
  invocation form — and opening the door to multiple, more specific,
  better-named creation entry points.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 11 (formerly Replace Constructor with Factory Method)"
---

Language-level constructors carry structural limitations ordinary functions
don't: a constructor must return an instance of exactly the class it was
invoked on, ruling out returning a subclass or proxy chosen based on
runtime conditions or arguments; the constructor's name is fixed by the
class name, so it can't be given a clearer, more descriptive name; and
constructors typically need a special invocation form, which makes them
awkward to pass around or use in contexts expecting an ordinary callable. A
**factory function** has none of these constraints — it will typically call
the real constructor as an implementation detail, but the caller-facing
contract is free to do, or later become, something else entirely.

**Mechanics**: create a factory function whose body simply delegates to the
constructor. Replace each direct constructor call with a call to the
factory function, testing after each change. Once migrated, restrict the
constructor's own visibility as much as the language allows, since external
code should now go through the factory.

Introducing a factory function is also a natural opportunity to introduce
*multiple*, more specific, better-named factory functions for common
construction patterns, rather than just one generic pass-through matching
the original constructor's shape — a call site that already knows a
specific variant at the call site (say, passing a raw type-code literal
alongside otherwise-generic construction arguments) can get its own
self-documenting factory that bakes that variant in, rather than
propagating a bare code literal as an argument. This pairs naturally with
[Replace Conditional with Polymorphism](replace-conditional-with-polymorphism.md),
whose factory-function step this refactoring generalizes beyond just the
type-code dispatch case.
