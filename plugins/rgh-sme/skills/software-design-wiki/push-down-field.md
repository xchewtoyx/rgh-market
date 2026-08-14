---
type: concept
title: "Refactoring: Push Down Field"
description: >
  Relocate a field down to just the subclass (or handful of subclasses)
  that genuinely uses it, rather than leaving it visible on every subclass
  via the superclass.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 12"
---

The direct data-level counterpart to
[Push Down Method](push-down-method.md), and the inverse of
[Pull Up Field](pull-up-field.md): if a field is only genuinely used by one
subclass, or a small subset of them, relocate it down to just those
subclasses rather than leaving it visible on every subclass via the
superclass.

**Mechanics**: declare the field on every subclass that actually needs it.
Remove it from the superclass. Test. Remove it from any subclass that
turns out not to need it. Test.
