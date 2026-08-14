---
type: concept
title: "Testability: A Design Property, Not Just a Test-Writing Skill"
description: >
  Testability is the probability that, given a fault exists in the code, it
  actually surfaces on the next test run — a property of the code's own
  structure (controllability and observability), not just of how carefully
  tests are written.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 12"
---

Formally: testability is the probability that, given the software has at
least one fault, it fails on its next test execution. A highly testable
piece of code "reveals" its faults easily and quickly; a poorly testable
one can hide a real bug behind many passing test runs simply because
nothing exercised the conditions that trigger it. This reframes testing
effort: a codebase with low testability makes even careful, thorough test
*writing* fight an uphill battle, because the code's own structure is what
determines how much of it a test can actually reach and check.

Two properties are jointly necessary, and inseparable in practice —
controlling something you can't observe is pointless: a piece of code's
inputs (and often its internal state) must be **controllable** — a test
can drive it into the state needed to exercise a given behavior — and its
outputs (and often its internal state) must be **observable** — a test can
tell what actually happened. [Seams](seam.md) and [dependency-breaking for
testability](dependency-breaking-for-testability.md) are exactly the
techniques that buy controllability where a design didn't originally
provide it; [fakes](fake-objects.md) buy the observability half by giving a
test a place to inspect what a collaborator was told to do.

**Structure predicts testability.** A class with a smaller "footprint" —
its own method count plus how many other classes' methods it invokes — is
empirically easier to test than one with a large footprint, because each
method call to another class is a place the state space under test can
diverge based on that other class's behavior. This is the same underlying
quantity as [coupling](coupling.md): a class low in coupling has fewer
places its correctness depends on, so fewer states a test has to
account for to pin its behavior down. High [cohesion](cohesion.md), low
coupling, and clear [separation of concerns](single-responsibility-principle.md)
each limit an element's interaction surface and the state space a test has
to reach — the same properties that serve modifiability serve testability
for essentially the same reason, not by coincidence.

**Nondeterminism is testability's enemy.** A test needs repeatable
behavior, not merely failure-inducing behavior — a bug that only shows up
under unpredictable timing or ordering is much harder to pin down than one
that reproduces the same way every time. [Rebuilding fixtures fresh per
test](fresh-fixtures-over-shared-fixtures.md) and avoiding shared mutable
state are both, from this angle, testability moves as much as correctness
moves: they remove one common source of run-to-run nondeterminism.

**Treat hard-to-test code as a design defect, not a fixed cost.** If unit
or acceptance tests for a piece of code are consistently hard or expensive
to write and maintain, that's a symptom of an overly tight-coupled
architecture lacking real module boundaries, not an inherent property of
the problem being solved. The fix is the design fix — reduce
[coupling](coupling.md), find the real seams — not lowering the bar on
test coverage or accepting slow, brittle tests as the price of doing
business. Even genuinely complex applications can have fast test suites
once the underlying design actually supports isolating pieces of it.

**A real tension worth naming explicitly**: testability (a system that
gives up its faults easily) and fault tolerance (a system designed to hide
or mask faults so it keeps running despite them) can pull in opposite
directions — a system built to gracefully mask a fault is, by that same
design, harder to catch failing on it during a test. This isn't a reason to
avoid fault tolerance, but it's worth reasoning through explicitly rather
than assuming the two design goals are automatically compatible.
