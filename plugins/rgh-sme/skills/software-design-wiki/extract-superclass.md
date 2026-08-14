---
type: concept
title: "Refactoring: Extract Superclass"
description: >
  Unify overlapping structure between two classes by introducing a shared
  superclass and pulling the common data and behavior onto it — usually
  the simpler first move compared to Extract Class, and reversible later
  via Replace Superclass with Delegate if inheritance turns out wrong.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 12"
---

When two classes are doing similar things, inheritance offers a direct
mechanism for unifying the overlap: introduce a shared superclass and use
[Pull Up Field](pull-up-field.md) / [Pull Up Method](pull-up-method.md) to
relocate the common data and behavior onto it. Inheritance hierarchies
don't need to be planned up front against some real-world classification
scheme — in practice, inheritance is just as often *discovered*
mid-development, as commonalities between classes become apparent through
the act of building and evolving the software, not decided ahead of time.

The direct alternative is [Extract Class](extract-class.md) — the
underlying choice is really inheritance versus delegation as the mechanism
for unifying duplicated behavior between two classes. Extract Superclass is
usually the *simpler* of the two to attempt first, and it's not a one-way
door: if inheritance later proves to be the wrong choice,
[Replace Superclass with Delegate](replace-superclass-with-delegate.md) can
convert it to delegation afterward. Starting with the simpler structure and
keeping the ability to correct course later is a reason not to agonize over
the inheritance-vs-delegation decision up front.

**Mechanics**: create an empty superclass and make the original classes
extend it. If needed, adjust the classes' constructors via
[Change Function Declaration](change-function-declaration.md). Test. Then,
one common element at a time, use
[Pull Up Constructor Body](pull-up-constructor-body.md),
[Pull Up Method](pull-up-method.md), and
[Pull Up Field](pull-up-field.md) to migrate shared elements onto the new
superclass. For methods that are only *partially* shared, apply
[Extract Function](extract-function.md) first to isolate the common part,
then Pull Up Method on that extracted piece. Finally, review the classes'
existing clients and consider whether any of them should now depend on the
new superclass's interface directly, rather than the original concrete
classes.

**A practical habit**: start with the data, since data manipulation lives
in the constructor — pulling up shared fields and constructor logic
naturally comes first, before behavior. When two methods to be pulled up
aren't identical yet — differently named, built from differently-named
underlying values — the diagnostic question is whether they represent the
same intent; if so, rename one to match the other via
[Change Function Declaration](change-function-declaration.md) before
attempting the pull-up, rather than trying to unify differently-shaped code
in one step.
