---
type: concept
title: Qualities of a Good Automated Test Suite
description: >
  A pipeline's test suites should be reliable, consistent, fast enough to
  reproduce locally, and owned inclusively across developers and testers, not
  siloed to a separate QA function.
sources:
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 10"
---

# Qualities of a Good Automated Test Suite

A short checklist for judging any test suite in a
[deployment pipeline](deployment-pipeline.md), not only the
[commit stage](commit-stage.md)'s:

- **Reliable**: a failure means a real defect; a pass gives genuine
  confidence the code is safe to progress. See
  [a few reliable tests beat many unreliable ones](reliable-tests-over-coverage.md).
  A pass should also mean the tests actually asserted something — see
  [mutation testing](mutation-testing.md) for how to check a suite for tests
  that execute code without meaningfully verifying it.
- **Consistent**: every commit triggers the same test set — coverage isn't
  optional or dependent on someone remembering to run it.
- **Fast and reproducible**: fast enough (a common target is under ~10
  minutes for the fastest suite) that a developer can reproduce and fix a
  failure locally rather than losing the thread waiting on a slow remote run.
- **Inclusive**: not owned solely by a separate testing function — best
  outcomes come from developers practicing
  [test-driven development](test-driven-development.md) themselves, with
  testers contributing exploratory and scenario-design work rather than
  carrying sole responsibility for automation. See
  [developer-owned test suite maintenance](developer-owned-test-maintenance.md).

These qualities apply differently at different pipeline stages — the
commit-stage suite optimizes hardest for speed (see
[commit test suite design principles](commit-test-suite-design.md)), while an
[automated acceptance test](automated-acceptance-testing.md) suite trades
some speed for broader, more realistic coverage — but reliability and
consistency are non-negotiable at every stage.
