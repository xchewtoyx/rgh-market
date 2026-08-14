---
type: concept
title: Test Value Versus Maintenance Cost
description: >
  Every test has ongoing upkeep cost as well as regression-catching value;
  keep tests only when value clearly exceeds cost, because test code is a
  liability like production code.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 1"
---

Badly written tests slow the rate of decline compared to no tests, but
stagnation remains inevitable — they don't fix the long-run trajectory.

Every test has:

- **Value** — regression protection, refactoring confidence, documentation,
  feedback speed (see [four pillars of a good unit test](four-pillars-of-a-good-unit-test.md)).
- **Upkeep cost** — refactoring the test when underlying code refactors;
  running on every change; dealing with false alarms; time spent reading to
  understand behavior.

Net value can be zero or negative once maintenance is accounted for. To achieve
[sustainable growth](goal-of-unit-testing.md), keep only high-quality tests
where value exceeds upkeep by a good margin.

**Code is a liability, not an asset** — more code means more bug surface and
maintenance. Tests are code and equally vulnerable to bugs and burden.

Recognizing a valuable test and writing one are distinct skills — analogous to
recognizing a good song versus composing one. Both require a frame of reference
(the four pillars) and, for writing, design skill to produce testable,
[observable-behavior-focused](observable-behavior-vs-implementation-details.md)
APIs.

Enterprise projects often run production-to-test ratios from 1:1 to 1:10 — volume
alone doesn't imply quality.
