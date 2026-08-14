---
type: concept
title: Goal of Unit Testing
description: >
  Unit testing exists to enable sustainable project growth — not to improve
  design directly, though testability is a useful negative indicator of poor
  structure when code is hard to isolate.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 1"
---

The industry question has shifted from "should we write unit tests?" to "what
makes a good unit test?" Many projects with large suites still deliver slowly
and ship recurring bugs because the tests don't do their job.

**Design improvement is a side effect, not the goal.** Testability is a **good
negative indicator, bad positive indicator**: hard-to-test code reliably signals
poor quality (usually tight [coupling](coupling.md)), but easily testable code
does not guarantee good quality.

**The actual goal: sustainable project growth.** Growing from scratch is easy;
sustaining growth over time is hard. Without tests, speed decreases as
[software entropy](complexity.md) accumulates — each change increases disorder,
fixes spawn new bugs, and stabilization becomes difficult. Tests are a safety
net against regressions, requiring upfront effort that pays back by sustaining
velocity. Development without tests "doesn't scale."

**Not all tests are equal.** Bad tests slow decline versus no tests but don't
change the long-run trajectory. Every test has **value** and **upkeep cost**
(refactoring the test when code refactors, running it on every change, false
alarms, reading cost). Net value can be zero or negative — keep only tests
where value exceeds cost by a good margin. **Code is a liability** — test code
included.

See [test value versus maintenance cost](test-value-vs-maintenance-cost.md),
[four pillars of a good unit test](four-pillars-of-a-good-unit-test.md), and
[coverage metrics as negative indicator](coverage-metrics-as-negative-indicator.md).

A successful suite is integrated into the development cycle, targets the most
important parts (primarily domain/business logic), and maximizes value with
minimum maintenance cost.
