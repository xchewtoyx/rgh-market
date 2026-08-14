---
type: concept
title: "Refactoring: Extract Class"
description: >
  Split a class that has accreted more than one responsibility into two,
  by moving the fields and methods that belong to the extra responsibility
  into a new class, one member at a time under test.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 7"
---

Extract Class is the mechanical fix for a class that has gradually accreted
more than one responsibility — "you add a responsibility to a class feeling
that it's not worth a separate class... soon, your class is as crisp as a
microwaved duck." See [why big classes are a problem](big-class-problems.md)
for the costs that motivate splitting, and
[the Divergent Change smell](divergent-change.md) — one class changed for
several unrelated reasons — as the concrete symptom Extract Class answers
("for classes, Extract Class formalizes the same split" as [Split
Phase](split-phase.md) or Move Function do for tangled functions).

**Finding the split**: look for a subset of data and a subset of methods
that travel together, or fields that change together or depend heavily on
each other. A useful test: "what would happen if I removed this field or
method — which other fields/methods would then become nonsensical?" A signal
that often surfaces later in a class's life is how it gets subtyped — if
subtyping only really affects a subset of the class's features, or different
features need different subtyping schemes, that's a strong hint the class is
really two classes glued together.

**Mechanics**: decide the responsibility split; create a new, empty child
class to hold it; rename the original class if its old name no longer fits
what remains; wire the parent to construct and hold a reference to the new
child. Move fields across one at a time via [Move Field](move-field.md),
testing after each; move methods across via
[Move Function](move-function.md), starting with lower-level methods
(callees before callers) and testing after each. Once everything has moved,
review both classes' interfaces — drop now-unneeded methods, rename things to
fit their new home. Finally decide whether the new child class should be
exposed directly to the parent's own clients; if so, first make it a proper
immutable value object via
[Change Reference to Value](change-reference-value.md).

This is the manual, under-test procedure; when the class resists testing
altogether, see
[extracting a class without tests](extract-class-without-tests.md) for the
conservative fallback. The inverse operation is
[Inline Class](inline-class.md), including its use as a stepping stone for
re-splitting a class along better lines rather than moving members directly
between two existing classes. Compare
[classitis](classitis.md): extracting responsibility into a class is not the
same as reflexively multiplying tiny classes — the split should follow a real
seam in the data and behavior, not a size threshold.
