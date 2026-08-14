---
type: concept
title: "Overabstracted Tests: Asserting Call Mechanics Instead of Behavior"
description: >
  A test that asserts the exact order or arguments of internal function
  calls is testing the language's control-flow machinery rather than the
  system's actual behavior, and tends to break on every implementation
  change regardless of whether the behavior stayed correct.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 13, How Unit Testing Affects Code"
---

[Mock objects](mock-objects.md) and [fakes](fake-objects.md) let a test
isolate the code under test from its collaborators, but it's easy to fall
into overabstraction: a test that asserts mechanical facts, like the exact
order in which a collaborator's methods were called or the precise
arguments passed on each individual call, rather than asserting on the
system's observable behavior. Such a test "tests" the language's control
flow implementation more than it tests anything a caller of the system
actually cares about, and it provides little of the value a test is
supposed to provide.

The diagnostic symptom is fragility disproportionate to the risk: if a
test has to be completely rewritten every time the method under test
changes — even a change that doesn't alter observable behavior — the test
was coupled to *how* the behavior was produced, not to the behavior itself.
That's a signal to rethink the test, or possibly the architecture that
made such fine-grained coupling necessary in the first place, rather than
a normal cost of testing.

One mitigation: when a nontrivial collaborator needs a fake for testing,
have the team that owns that collaborator provide and maintain the fake
implementation, rather than each consuming team writing and re-writing its
own. This benefits both sides — the owning team keeps the fake's behavior
tracking the real service as it evolves, and consuming teams get a more
realistic double than one guessed at from the outside, reducing exactly the
kind of over-specified, implementation-coupled assertions this failure mode
produces.
