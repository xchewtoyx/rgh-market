---
type: concept
title: "Refactoring: Push Down Method"
description: >
  Relocate a superclass method down to just the one subclass (or handful
  of subclasses) that actually needs it, making that narrower scope
  explicit instead of leaving it implicit on every subclass.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 12"
---

The inverse of [Pull Up Method](pull-up-method.md): if a method on a
superclass is really only relevant to one subclass, or a small subset of
them, relocating it down to just those subclasses makes that scoping
explicit rather than implicit. Compare
[Push Down Dependency](push-down-dependency.md), a similarly-named but
differently-motivated legacy-code technique aimed at isolating
problematic dependencies for testability rather than at scoping shared
behavior correctly.

**Precondition**: this only works if callers already know they're working
with the specific subclass in question. If callers only have a reference
typed or known as the superclass, Push Down Method isn't viable, and
[Replace Conditional with Polymorphism](replace-conditional-with-polymorphism.md)
with an inert, no-op placeholder implementation on the superclass is the
right tool instead.

**Mechanics**: copy the method into every subclass that actually needs it.
Remove it from the superclass. Test. Remove it from any subclass that
doesn't actually need it — one that only received the copy incidentally in
the first blanket copy step. Test.
