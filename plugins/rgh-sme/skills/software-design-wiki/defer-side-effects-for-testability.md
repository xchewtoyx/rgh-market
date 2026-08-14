---
type: concept
title: Defer Side Effects for Testability
description: >
  Keep business mutations in memory until an operation completes, then apply
  persistence and messaging at the edges — abstractions of upcoming side
  effects are easier to test than the side effects themselves.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 7"
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 6"
---

Theme across hexagonal and [functional architecture for testability](functional-architecture-for-testability.md):
abstract the *application* of side effects — defer them in memory until
business logic finishes, so domain code tests without out-of-process systems.

- [Domain events](domain-events-for-deferred-side-effects.md) abstract upcoming
  bus messages.
- Mutations on domain objects abstract upcoming DB writes (controller persists
  at the end).

**Tip**: it's easier to test abstractions than the things they abstract.

CRM refactor parallel: domain layer (`User`, `Company`) performs in-memory
side effects; application service persists and notifies. Differs from pure
functional core (which has no side effects at all) but shares the "last
moment" persistence pattern enabling state-based unit tests without mocks.

Don't mock inter-domain-class interactions — they aren't
[observable behavior](observable-behavior-vs-implementation-details.md) from
outside clients. One to three in-process collaborators on a domain class is
fine if none are out-of-process.

Full containment isn't always achievable (uniqueness checks, failure handling
altering flow live in controllers). See [four types of code for testing
priority](four-types-of-code-for-testing-priority.md) and [humble object
pattern](humble-object-pattern.md).
