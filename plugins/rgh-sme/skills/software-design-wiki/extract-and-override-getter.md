---
type: concept
title: Extract and Override Factory Method and Getter
description: >
  Extract hard-coded object creation out of a constructor into an
  overridable factory method or lazy getter so a testing subclass can
  substitute a fake — the getter form is the C++-specific workaround where
  the factory-method form is blocked by virtual-call-in-constructor rules.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

"Hard-coded initialization work in constructors can be very hard to work
around in testing." **Extract and Override Factory Method**: extract the
entire object-construction sequence out of a constructor into a new
(commonly `protected`) factory method, have the constructor call it, then
subclass and override that factory method in a test-only subclass to return
a fake instead. This is blocked in C++ specifically, because C++ does not
resolve virtual function calls made from a base class's own constructor to
overrides defined in a derived class — the same limitation covered in
[dependency-breaking for deeply nested construction](deep-construction-dependencies.md).
Java and many other languages allow it without issue.

**Extract and Override Getter** is the C++-specific workaround, applying
*only* when the object is created and nothing else is done with it beyond
that in the constructor. Introduce a **lazy getter** — a method that
constructs the object on its first call (checking a null/zero sentinel) and
returns the cached instance thereafter, the same shape underlying the
Singleton pattern's typical `getInstance()` — then replace every direct use
of the raw instance variable with calls to this getter, and initialize the
variable to null in the constructor instead of constructing eagerly there.
Once every access goes through the getter, a testing subclass can override
just the getter to return a fake, without ever needing the base constructor
to call a virtual method.

Explicit resource-management caution for non-garbage-collected languages:
"you have to be very conscious of object lifetime issues, particularly in a
non-garbage-collected language such as C++. Make sure that you delete the
testing instance in a way that is consistent with how the code deletes the
production instance." A residual risk: the underlying variable can, in
principle, still be touched before the getter has ever been called,
creating a use-before-initialization risk mitigated only by rigorously
routing *every* access through the getter, with none left touching the raw
field directly.

Usage guidance relative to its sibling techniques: not a frequently-reached-
for technique — prefer [Extract and Override Call](extract-and-override-call.md)
when only a single problematic method exists on the dependency; reach for
Extract and Override Getter specifically when **many** problematic methods
exist on the same object, since fixing the single construction point (the
getter) then resolves all of them at once — "a clear win" in that specific
situation.

Steps: identify the object needing a getter; extract its full creation
logic into the getter method; replace every direct use of the variable with
calls to the getter, and initialize the variable to null in every
constructor; add the null-check/first-time-construction logic inside the
getter; subclass and override the getter to substitute a test object.
