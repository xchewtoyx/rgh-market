---
type: concept
title: Self-Testing Code
description: >
  Tests that are fully automatic and check their own pass/fail result,
  rather than requiring a human to eyeball output, compound into a fast bug
  detector precisely because they can be run constantly.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 4"
---

**"Make sure all tests are fully automatic and that they check their own
results."** Self-testing means tests go green or red on their own — no
manual eyeballing of printed values, which is slow and defeats the purpose
of running tests often. This is a near-hard prerequisite for
[refactoring](refactoring-preserves-behavior.md): the whole discipline of
the [refactoring rhythm](rhythm-of-refactoring.md) — small step, verify,
commit, repeat — has no feedback loop to run on without it.

The mechanism behind why this compounds: running tests frequently — every
compile, or every few minutes — means that when a previously-passing test
breaks, the change that broke it is necessarily something written in just
the last few minutes: small, fresh in memory, and fast to find. "A suite of
tests is a powerful bug detector that decapitates the time it takes to find
bugs" — this is the same underlying value as [regression testing as a
software vise](regression-testing-as-a-software-vise.md), stated from the
angle of debugging speed rather than behavior lock-in.

A concrete habit that follows from treating tests this way: when you get a
bug report, start by writing a unit test that exposes the bug, and only fix
it once that failing test exists — both to guarantee the bug stays fixed
and to prompt reflection on what other coverage gaps the bug revealed.
