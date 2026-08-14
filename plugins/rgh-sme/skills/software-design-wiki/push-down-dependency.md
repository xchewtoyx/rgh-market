---
type: concept
title: Push Down Dependency
description: >
  When a class has pervasive problematic dependencies too tangled for
  picking off call by call, make the class abstract and push the bad
  dependencies down into a new concrete subclass, freeing the remaining
  good logic to be tested through a lightweight testing subclass instead.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

Compare [Push Down Method](push-down-method.md) and
[Push Down Field](push-down-field.md), the similarly-named design
refactorings aimed at correctly scoping shared behavior rather than at test
isolation.

A middle-ground technique for a class whose problematic dependencies are too
numerous or tangled for simple
[Subclass and Override Method](subclass-and-override-method.md) on a few
calls, but not clean enough to fully separate via repeated
[Extract Interface](extract-interface.md) either. Instead of isolating
dependencies one call at a time, isolate the whole *cluster* into a
subclass.

Mechanism: make the current class abstract, create a new concrete subclass
that becomes the actual production class, and push all the problematic
dependency-laden code (fields and methods) down into that new subclass —
leaving the original (now-abstract) class's good logic untouched and
instantiable via a separate, lightweight testing subclass. Worked example: a
validator class with real, wanted validation logic alongside a display
method riddled with UI framework calls. Fix: make the display method pure
virtual on the now-abstract original class; move the real UI implementation
into a new concrete subclass; add a separate testing subclass overriding the
display method as a no-op, giving a fully UI-free class to exercise the
validation logic against.

Explicit design self-assessment: "is using inheritance in this way ideal?
No, but it helps us get part of the logic of a class under test." The
intended follow-up trajectory once tests exist: clean up the pushed-down
logic, pull it back up, and eventually replace the whole inheritance
scaffold with delegation to a dedicated new class that holds *only* the
problematic dependency — the same trajectory [Pull Up Feature](pull-up-feature.md)
describes from the opposite direction.

Steps: attempt to build the problematic class in a test harness as-is;
identify exactly which dependencies block the build; create a new,
clearly-named subclass representing the specific environment those
dependencies belong to; move the offending fields/methods into that
subclass ([Preserve Signatures](preserve-signatures.md)), making the corresponding members
protected/abstract on the original class and making the original class
itself abstract; create a separate testing subclass and attempt to
instantiate it in a test; build to confirm the new class is instantiable.
