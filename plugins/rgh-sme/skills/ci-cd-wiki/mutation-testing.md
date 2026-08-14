---
type: concept
title: Mutation Testing
description: >
  Automatically introducing small deliberate bugs into already-passing code
  and checking whether the test suite catches them, to detect tests that
  exercise code without actually asserting on its behavior.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 13"
---

# Mutation Testing

A [reliable](reliable-tests-over-coverage.md), passing test suite can still
be worthless at its actual job: a test that calls the code under test but
never asserts anything meaningful about the result passes whether the code
is correct or completely broken. Code coverage doesn't catch this — a line
can be executed by a test without the test checking anything about what that
line did.

Mutation testing catches it directly: automatically apply a small change to
already-working code (flip a boolean condition, replace `||` with `&&`,
change a comparison operator, force a branch to always take one path) and
rerun the test suite. If every test still passes despite the code now being
behaviorally wrong, the tests covering that code aren't actually testing
it — a concrete, automatable version of a code reviewer manually asking "if
I replaced this condition with `if (false)`, would any test catch it?"

This is a good complement to [test-driven development](test-driven-development.md):
TDD's discipline (write the failing test before the code) tends to produce
tests that assert something meaningful by construction, since the test has
to fail against a not-yet-implemented behavior before it can pass — mutation
testing is the retrospective check for suites, or portions of a suite, that
weren't built that way.
