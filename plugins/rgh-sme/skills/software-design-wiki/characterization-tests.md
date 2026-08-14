---
type: concept
title: Characterization Tests
description: >
  A characterization test documents a piece of code's actual current
  behavior, discovered by asserting a guess, reading the failure to learn
  the truth, and rewriting the assertion to match — not a judgment of what
  the code should do.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 13"
---

A characterization test "characterizes the actual behavior of a piece of
code... The tests document the actual current behavior of the system,"
explicitly *not* what the system "should" do per old requirements documents
— "what the system does is more important than what it is supposed to do"
for the purpose of making changes safely. This directly serves
[preserving behavior](preserving-behavior-is-the-real-challenge.md) and
resolves [the legacy code dilemma](the-legacy-code-dilemma.md) by giving you
a way to pin down behavior you don't otherwise understand well enough to
protect.

**Algorithm**: put a piece of code in a test harness; write an assertion you
know or suspect will fail; let the failure message tell you the actual
behavior; rewrite the assertion to match that actual behavior; repeat.
Deliberately asserting a wrong guess and letting the harness report the real
value, then harvesting that value directly into the corrected assertion,
documents exactly what the code does right now.

The natural objection — "if we're just copying the software's own output
into the test, are we testing anything, or just enshrining a possible bug?"
— dissolves once you relocate what these tests are for: not a moral "gold
standard" of correctness, but a mechanism to detect future drift from
documented current behavior. Absent tests, the only way to know what a
system actually does is manually "playing computer," reading code and
mentally tracing values — tedious and wasteful to redo over and over. If a
characterization test surfaces something that looks wrong, don't silently
omit it — include it, but flag it as suspicious, and investigate separately;
see [handling bugs found during characterization](handling-bugs-found-during-characterization.md).

See [tests preserve behavior more than they find bugs](tests-preserve-more-than-they-find-bugs.md)
for why this reframing matters, and
[a stopping condition for characterization tests](stopping-condition-for-characterization-tests.md)
for how to know when you've written enough. When the goal is validating a
*replacement* implementation rather than pinning down one implementation in
isolation, see [differential testing against a reference
implementation](differential-testing-against-reference-implementation.md).
