---
type: concept
title: Replace Primitive with Object
description: >
  The moment you want to do anything with a value beyond printing it, wrap
  it in a small class — an almost-empty wrapper that becomes an irresistible
  home for validation, comparison, and formatting logic that would otherwise
  scatter and duplicate.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 7 (formerly Replace Data Value with Object)"
---

The direct cure for the [Primitive Obsession](primitive-obsession.md) smell.
Early in development, simple facts often get represented as bare primitives
— a telephone number as a plain string, say — because that's genuinely all
they need at the time. As software grows, that "simple" value usually stops
being simple: formatting rules, validation, comparison logic accrete around
it, and without a dedicated home for that behavior it tends to get
duplicated everywhere the value is touched. Trigger rule: **the moment you
want to do anything with a value beyond printing it, wrap it in a small
class.** At first such a class does almost nothing but hold the primitive —
that's precisely the point, since it creates a place behavior can
accumulate incrementally afterward. Despite looking trivial, many
experienced developers rate this among the single most valuable
refactorings in the whole toolkit, because of its outsized second-order
effects on a codebase over time.

**Mechanics**: apply [Encapsulate Variable](encapsulate-variable.md) first
if not already done. Create a minimal value class wrapping the primitive —
constructor takes the raw value, plus a getter to retrieve it. Change the
field's setter to construct a new instance of the value class instead of
storing the raw value; change the getter to delegate to the wrapped class's
own getter; test. Rename the original accessors if the old names no longer
reflect what's actually being returned once the wrapper exists. Consider
explicitly whether the new class should be a value object or a reference
object, and apply Change Reference to Value or Change Value to Reference to
make that choice explicit rather than accidental.

As the class matures it typically accumulates: validation against a fixed
set of legal values, a derived ordering, and comparison methods — replacing
brittle string-equality checks scattered across call sites with
intention-revealing calls, and centralizing what used to be duplicated
comparison rules in exactly one place.
