---
type: concept
title: "Refactoring: Collapse Hierarchy"
description: >
  Merge a class and its parent into one once ongoing pull-up/push-down
  refactoring has left them no longer different enough to justify existing
  as two separate classes.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 12, Dealing with Inheritance — Collapse Hierarchy"
---

A natural end state of ongoing pull-up/push-down refactoring on a class
hierarchy: a class and its parent gradually converge until they're no
longer different enough to justify existing as two separate classes. At
that point, merge them into one.

**Mechanics**: decide which of the two classes to keep and which to remove
— the tiebreaker is picking whichever **name** will serve better going
forward; if neither name is clearly better, the choice is arbitrary. Use
whichever combination of [Pull Up Field](pull-up-field.md), [Push Down
Field](push-down-field.md), [Pull Up Method](pull-up-method.md), and [Push
Down Method](push-down-method.md) is needed to consolidate every remaining
element into the single surviving class. Update any external references
that pointed at the class being removed so they point at the surviving one
instead. Delete the now-empty class. Test.
