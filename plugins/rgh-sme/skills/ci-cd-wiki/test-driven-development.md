---
type: concept
title: Test-Driven Development (TDD)
description: >
  Writing a failing automated test before the code that satisfies it, in
  short red-green-refactor cycles, which produces measurably better defect
  density than writing tests after the code.
sources:
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 10"
---

# Test-Driven Development (TDD)

Developed by Kent Beck as part of Extreme Programming. Three-step cycle,
each step ending in a commit:

1. Write a test for the next small increment of functionality; confirm it
   fails (there's no code yet to make it pass).
2. Write just enough functional code to make the test pass.
3. Refactor the new and surrounding code for good structure, confirming the
   tests still pass throughout.

The same discipline applied to acceptance criteria rather than unit-level
behavior is sometimes called acceptance test-driven development (ATDD) — see
[automated acceptance testing](automated-acceptance-testing.md).

## Why it beats writing tests afterward

A controlled study (Nagappan, Maximilien, and Williams; Microsoft Research /
IBM / NC State) found TDD teams produced code with 60–90% better defect
density than non-TDD teams, at a cost of only 15–35% more development time —
a large quality return for a modest time investment. Part of the mechanism:
writing the test first forces the code to be written in a testable shape
(small, decoupled units with clear interfaces), which is the same
[independent testability](independent-testability.md) property that also
pays off at the component and service level.

## A living specification

Because the tests are checked into version control alongside the code they
describe, they double as an always-current specification: a developer can
read the test suite as working, executable usage examples of the system's
actual API and behavior — the same value proposition
[automated acceptance testing](automated-acceptance-testing.md)'s
"executable specifications" describe at the acceptance-test layer.
