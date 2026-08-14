---
type: concept
title: Write a Regression Test for Every Production Bug
description: >
  When a production defect is found, first write an automated test that
  reproduces it and confirm the test fails, then fix the code until the test
  passes, and keep the test permanently in the regression suite.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 4"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 10"
---

# Write a Regression Test for Every Production Bug

This is test-driven development applied to defect fixing rather than new
feature work: reproduce the bug as a failing automated test before touching
the implementation. Two things this guarantees that fixing-then-testing does
not:

- The fix is verified against the actual reported failure, not just against
  the developer's mental model of the failure.
- The test stays in the suite after the fix ships, so the same defect cannot
  regress silently later — the [commit stage](commit-stage.md) or acceptance
  gate will catch it automatically if it ever reappears.

Every production defect handled this way permanently grows the test suite's
coverage of the codebase's actual failure history, which is coverage no amount
of upfront test design can substitute for.

## Backfill toward the fastest layer that would have caught it

The same principle generalizes to any bug caught by a slower test layer than
necessary: whenever [an integration or acceptance test](test-automation-pyramid.md)
catches something a unit test could have caught, backfill a unit test for it,
not just a test at the same slow layer. Slow-layer tests are expensive to
run and often serialize on scarce shared environments, so a bug that keeps
being caught (and re-verified) at that layer stays expensive every time it's
touched again; pushing the regression test as far up the pyramid as it will
go is what actually captures the full value of
[catching errors as early as possible](test-automation-pyramid.md).
