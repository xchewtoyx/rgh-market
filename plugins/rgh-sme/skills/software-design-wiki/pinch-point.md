---
type: concept
title: Pinch Point
description: >
  A narrowing in an effect sketch where tests against one or two methods can
  detect changes across a whole cluster of related classes — relative to
  the specific set of change points, not an intrinsic property of a class.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 12"
---

When a single feature forces edits to several closely related classes, each
individually expensive to bring under test, the question isn't "must I break
dependencies in every one of them separately?" The core strategy is to test
**"one level back"**: find one place — a single public method, or one
object's interface over a whole collaboration — that catches problems from
several classes' worth of changes at once. This gives "cover" for aggressive
refactoring underneath, since "the structure of code below the tests can
change radically as long as the tests pin down their behavior." Such tests
are valuable and often easier to work with than expected, evolving alongside
the code in small safe steps — but they are explicitly **not a substitute
for unit tests**, only "a first step toward getting unit tests in place." See
[pinch point traps](pinch-point-traps.md) for what happens when that
distinction gets lost.

A **pinch point** is "a narrowing in an effect sketch, a place where it is
possible to write tests to cover a wide set of changes" — where tests
against a couple of methods can detect changes across many methods. Worked
example: when `Invoice`, `Item`, and `BillingStatement` all need related
changes (a new shipping-carrier field, a per-shipper billing breakdown),
rather than instrumenting each class individually, a test against
`BillingStatement.makeStatement()` alone can detect every effect of the
planned `Invoice`/`Item` changes — that single method is the pinch point for
this cluster of changes.

**Pinch points are relative to the specific set of change points, not an
intrinsic property of a class.** Adding an unrelated feature to one of the
classes in the cluster might not disturb an existing pinch point at all, if
the new field doesn't feed into anything the pinch point observes. But
adding a field used by *two different* downstream consumers can break a
single clean pinch point into needing two methods together as the narrowest
available pinch — still far narrower than instrumenting every affected class
individually.

**When no pinch point can be found** (a tangled effect sketch with many
independent branches), two fallback moves: (1) narrow scope — look for a
pinch point covering just one or two of the intended changes at a time,
rather than all of them; (2) look for **common usage patterns** across the
sketch — a method with several apparent callers might really have only one
*kind* of use, if those callers all use it the same way on comparable
objects, in which case testing through just one caller can safely stand in
for the others. This kind of analysis benefits from a second person to
reason it through with.

See [pinch points as a design diagnostic](pinch-points-as-design-diagnostic.md)
for what a pinch point's location reveals about a codebase's actual
encapsulation boundaries.
