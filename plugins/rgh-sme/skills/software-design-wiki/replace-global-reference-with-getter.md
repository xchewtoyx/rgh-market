---
type: concept
title: Replace Global Reference with Getter
description: >
  A static call returning a shared or singleton-backed object still counts
  as a global dependency in practice — wrap it in an overridable getter so
  a testing subclass can substitute a fake, the same fix as Extract and
  Override Call scaled to many call sites of the same global.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

A companion technique to
[breaking singleton dependencies](breaking-singleton-dependencies.md) for
the same underlying problem: a call to a static method that returns a
shared or singleton-backed object counts as a global for practical
purposes, even though syntactically it's "just a call to a static method on
a class" — the class itself functions as a global object holding state
needed to do its work.

Mechanism: introduce a `protected` getter method wrapping the global access,
replace every direct reference to the global with a call to this new
getter, then use [Subclass and Override Method](subclass-and-override-method.md)
on a test-only subclass to override the getter and return a fake instead.
This is [Extract and Override Call](extract-and-override-call.md) at the
scale it's meant for: many call sites against the *same* global collapse to
one overridable choke point instead of needing a wrapper per call site.

Worked example: code calling a global inventory lookup directly is
refactored to call a new protected getter instead; since the inventory
object is itself a singleton, its constructor is loosened enough that a fake
subclass can exist; a testing subclass then overrides the getter to return
the fake, fully decoupling the test from the real inventory system. This can
be pushed further with [Extract Interface](extract-interface.md) to also
break the dependency on the global's concrete *class*, not just the
specific instance it returns.

Steps: identify the global reference to replace; write a getter wrapping
it, with access protection loose enough to be overridden in a subclass;
replace direct references with calls to the getter; create a testing
subclass and override the getter there.
