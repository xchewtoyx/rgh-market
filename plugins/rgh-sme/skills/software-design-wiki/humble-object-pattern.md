---
type: concept
title: Humble Object Pattern
description: >
  Extract testable logic from a hard-to-test dependency, leaving a thin
  wrapper that glues the dependency and the extracted component together —
  the wrapper has little logic and needs no tests.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 7"
---

Introduced by Gerard Meszaros (*xUnit Test Patterns*). Code is often hard to
test because it is coupled to a hard-to-test framework dependency — async
execution, UI, out-of-process communication. The fix: extract the testable
logic, leaving behind a thin **humble wrapper** that glues the hard-to-test
dependency and the extracted component. The wrapper contains little or no
logic and does not need testing.

Both [ports and adapters (hexagonal) architecture](ports-and-adapters-architecture.md)
and [functional architecture for testability](functional-architecture-for-testability.md)
implement this pattern. Hexagonal architecture separates business logic from
out-of-process communication; functional architecture goes further, separating
business logic from communication with *all* collaborators.

Useful metaphor: **code depth versus code width** — code can be deep
(complex/important) or wide (many collaborators), but not both. Other
instances: MVP/MVC (Model = business logic; Presenter/Controller = humble
glue), and DDD aggregates (cluster classes to reduce inter-class connectivity).

In Single Responsibility Principle terms, Humble Object separates "business
logic" from "orchestration." The separation aids testability and manages
long-term complexity — not just test setup cost.

Worked CRM refactor: move database and message-bus calls out of `User` into
`UserController`; extract reconstruction into factories; introduce `Company`
for employee-count logic. Result: `User`/`Company` sit in the domain-model
quadrant; `UserController` sits in the controllers quadrant; the
overcomplicated quadrant is empty. See [four types of code for testing
priority](four-types-of-code-for-testing-priority.md).

Splitting a class that both fetches from out-of-process dependencies and
computes domain totals — then mocking the concrete class to preserve part of
its behavior — is an SRP violation and an anti-pattern; extract a gateway
plus a pure calculator instead.
