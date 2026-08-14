---
type: concept
title: Sprout Method
description: >
  When a needed change can be expressed as a self-contained new method, but
  the surrounding method or class can't easily be brought under test,
  extract the change into a new method developed test-first and call it
  from the untested code, rather than inlining the change.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 6"
---

Worked example: a method needs a "skip duplicate entries" check. A naive
inline fix mixes the existing logic with the new duplicate-detection logic in
one method and adds a temp variable that invites further inline additions
later. The better fix: extract a standalone method for the new check, built
test-first (TDD), and call it from the original method — keeping old and new
logic cleanly separated and the calling method small.

Steps: identify the change point; if it's expressible as one sequence of
statements in one place, write (and comment out) a call to a not-yet-written
method; turn the local variables it needs into arguments; if it must return a
value, assign the call's result to a variable; develop the sprout method
test-first; uncomment the call.

If the class's own dependencies are too tangled to construct an instance
even for the sprout method's tests, fall back to passing null for what isn't
needed, or make the sprout a `public static` method, passing needed instance
variables as arguments. Static methods can act as a temporary staging area —
once several accumulate and share variables, that's often a sign a genuinely
new class wants to be extracted; when the original class eventually gets
under test, the accidental statics can move back in as instance methods.

The trade-off: you're implicitly giving up, for now, on bringing the source
method or class itself under test, leaving it in an odd state with a lone
tested sprout amid untested code. In exchange you get a clean, explicit
interface between new and old code, and full visibility of the variables the
new code touches. See [sprout class](sprout-class.md) for the escalation when
even instantiating the source class isn't feasible.
