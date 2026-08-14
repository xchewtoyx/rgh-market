---
type: concept
title: Programming by Difference
description: >
  Introduce a feature via a new subclass overriding one method, buying time
  to figure out the right long-term structure — a legitimate initial move
  precisely because tests let you migrate away from inheritance later if it
  becomes a liability.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 8"
---

A historically prominent technique (1980s) that fell out of favor once the OO
community recognized overuse of inheritance as problematic — reclaimed here
as a legitimate *initial* move because tests provide an exit: you can safely
migrate off the inheritance structure later if it becomes a liability. Core
idea: rather than editing a base class directly, loosen the method that needs
to vary from `private` to `protected`, subclass, override just that method,
and pin the new behavior down with a test against the subclass. Fast to
implement, and the resulting test becomes a durable spec of the new behavior,
reusable across later redesigns.

**The trap it exposes**: a second feature request naturally gets reached for
via a *second* subclass overriding a different method — but this fails as
soon as both features are needed on the same object simultaneously, since
"if we put features into distinct subclasses, we can only have one of those
features at a time." This is a fundamental limit of single-inheritance-based
feature variation, not a coding mistake.

**Refactoring path out**, preserved by the test already written: convert the
subclass-per-feature scheme into a
[context-object](context-object-pattern.md)-flavored configuration scheme —
give the base class a constructor accepting a properties/flags collection,
fold each override's logic directly into the base method as a conditional
branch gated on the corresponding flag, verify the existing test still
passes with the override commented out (confirming behavior parity), then
delete the subclass and update call sites. The same mechanism then absorbs
further feature variations as more flags, sidestepping the one-subclass-
at-a-time ceiling entirely. The underlying lesson: **tests, not the
inheritance structure itself, are what make it safe to swap implementation
strategies mid-stream.**

As the flags and conditionals accumulate in the base method,
[Extract Method](splitting-and-joining-methods.md) cleans the branches into
separate named methods, and — once the growing responsibility looks large
enough to warrant it — the configuration data and the behavior that consumes
it can be moved together into a dedicated collaborator class, which may in
turn deserve a [rename](renaming-reveals-possibilities.md) once its role has
shifted from passive data holder to active computation. Whether folding both
variants' logic into one class this way is good design is judged case-by-
case, by how large and tangled the resulting responsibility becomes — not as
an absolute rule.

Programming by difference is only a safe *starting* move — see the
[Liskov Substitution Principle](liskov-substitution-principle.md) for the
risk it introduces by overriding a concrete method, and
[normalized hierarchies](normalized-hierarchy.md) for the property it
trades away.
