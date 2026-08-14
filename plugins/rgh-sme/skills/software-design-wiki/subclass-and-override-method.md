---
type: concept
title: Subclass and Override Method (Dependency-Breaking)
description: >
  Create a test-only subclass that overrides just the one method causing a
  dependency problem, leaving the rest of the class's behavior — including
  the behavior actually under test — untouched.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 9"
---

When a single method on a class is what makes it hard to test — a
constructor calling something slow, or an otherwise-harmless method
silently opening a live connection — create a test-only subclass overriding
just that method, rather than extracting an interface for the whole class.
A throwaway subclass can even be defined inline inside a single test method
purely to fix one troublesome method, exposing a way to directly set
whatever result the real method would have computed (e.g. a boolean flag the
overridden method returns instead of hitting a database).

The technique's whole value depends on **not accidentally altering the
behavior you actually intend to test** — the override must remove exactly
the problem dependency and nothing else, or the test stops verifying real
behavior.

**This is the core technique underlying most of the rest of the dependency-
breaking catalog** — "many of the other dependency-breaking techniques in
this chapter are variations on it." The governing constraint: "the
factoring that you have in a class determines how well you can use
inheritance to separate out dependencies." Sometimes the unwanted
dependency is already isolated in a small method (an easy override); other
times you must override a much larger method just to reach the dependency
buried inside it — sacrificing the ability to test everything else that
larger method did, which is only acceptable if the test at hand genuinely
doesn't care about those other details.

**The "paper view" mental model**: visualize a class's source as a sheet of
paper; for any extractable snippet, imagine a translucent sheet placed on
top carrying a different implementation of just that snippet — what you
ultimately test is the *stack* of sheets, and whichever implementation shows
through the top sheet for each snippet is what actually executes. Practical
discipline this suggests: when applying Subclass and Override Method
specifically (as opposed to a fresh Extract Method), prefer overriding
methods that already exist rather than extracting new ones on the fly,
since extracting methods without a safety net already in place carries its
own risk.

Steps: find the smallest possible set of methods to override that achieves
separation or sensing; make each overridable per the language's rules
(`virtual` in C++, not `final` in Java); loosen visibility only as far as
the language requires for subclass overriding; create the subclass and
confirm it builds in the test harness.

It's the lightest-weight fix in the dependency-breaking catalog for
this shape of problem: see
[diagnosing why a dependency is actually bad](diagnose-why-a-dependency-is-bad.md)
for when it applies instead of full [Extract Interface](extract-interface.md), and
[dependency-breaking for deeply nested construction](deep-construction-dependencies.md)
for a related but distinct escalation ([Extract and Override *Factory*
Method](extract-and-override-getter.md)) used when the problem is which object gets *constructed*, not which
method's behavior runs.
