---
type: concept
title: "Refactoring: Remove Subclass"
description: >
  Collapse a subclass that no longer earns its comprehension cost back into
  a plain field on the superclass, once the variation it once represented
  has migrated elsewhere or disappeared.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 12, Dealing with Inheritance — Remove Subclass (formerly Replace Subclass with Fields; inverse of Replace Type Code with Subclasses)"
---

Subclasses earn their keep by supporting real variation in data or
polymorphic behavior — a way to [program by
difference](programming-by-difference.md). But as a system evolves, that
variation often migrates elsewhere or disappears entirely — sometimes
because the subclass was built in anticipation of a feature that never
materialized. Once a subclass does too little to justify the comprehension
cost of a whole extra class in the hierarchy, replace it with a plain field
on the superclass instead. This is the inverse of [Replace Type Code with
Subclasses](replace-type-code-with-subclasses.md): once a subclass's only
remaining job is to hold a fixed value, a field says the same thing with
less structure.

**Mechanics**: apply [Replace Constructor with Factory
Function](replace-constructor-with-factory-function.md) to the subclass
constructors first, so the eventual collapse doesn't ripple out to every
call site. If clients decide which subclass to build based on some data
field, move that selection logic into a superclass-level factory method. If
any code performs type tests against the subclasses (`instanceof`), extract
the test into its own function via [Extract
Function](extract-function.md) and relocate it onto the superclass with
[Move Function](move-function.md), testing after each change. Add a field
on the superclass to represent the distinction the subclasses used to
carry. Update every method that referenced the subclass type to consult the
new field instead. Delete the subclass. Test. When collapsing several
subclasses at once, do the encapsulation steps (factory, moved type tests)
for the whole group first, then fold each subclass into the superclass one
at a time.

A worked example collapses `Male`/`Female` subclasses of `Person` — created
solely to override a `genderCode` getter — into a `_genderCode` field. Along
the way it surfaces two judgment calls worth naming explicitly:

- A superclass referencing its own subclass by name (`this instanceof
  Male`, temporarily relocated onto `Person` as an `isMale` accessor mid-
  refactoring) is normally an uncomfortable dependency to introduce
  deliberately — but it's acceptable when the code carrying it has a very
  short remaining lifespan, since it will be deleted again within the same
  refactoring session.
- After removing both subclasses, a factory's `default` branch constructed
  a plain `Person` without an explicit gender code, leaving it asymmetric
  next to the two other, now-explicit branches. Fowler tidies this purely
  for symmetry's sake, on the reasoning that "a future reader of the code
  will always wonder about this lack of symmetry" — worth fixing whenever
  it can be done without introducing any other complexity.
