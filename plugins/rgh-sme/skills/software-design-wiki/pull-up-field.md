---
type: concept
title: "Refactoring: Pull Up Field"
description: >
  Relocate a field duplicated across sibling subclasses up onto their
  shared superclass once every use of it agrees, removing both the
  duplicate declaration and clearing the way to pull up behavior that
  depends on it too.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 12"
---

When subclasses were developed independently — or merged via other
refactoring — they often end up duplicating not just behavior but **data**:
fields that may or may not share a name, discoverable only by inspecting
how each is actually used. If they're used the same way, pulling the field
up removes duplication on two fronts at once: the duplicate field
declaration itself, and, as a natural follow-on, any behavior using that
field that can now also move up via
[Pull Up Method](pull-up-method.md).

In dynamic languages where fields aren't declared up front but simply
spring into existence on first assignment, "pulling up a field" is really
just a natural side effect of doing
[Pull Up Constructor Body](pull-up-constructor-body.md) correctly, rather
than a distinct mechanical step.

**Mechanics**: inspect every user of the candidate field across subclasses
to confirm they're all using it consistently. If the fields have different
names, apply [Rename Field](rename-field.md) first to unify them. Create
the corresponding field on the superclass (with a visibility subclasses
can reach). Delete each subclass's own copy. Test.

This is the inverse of [Push Down Field](push-down-field.md).
