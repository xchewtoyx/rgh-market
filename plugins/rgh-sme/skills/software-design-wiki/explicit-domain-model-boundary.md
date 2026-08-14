---
type: concept
title: Explicit Domain Model Boundary
description: >
  Give domain logic a distinct, well-known place in the codebase so unit tests
  (domain/algorithms) and integration tests (controllers) have a clear target
  separation.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 8"
---

Always give the domain model an explicit, well-known place — separate assembly,
namespace, or folder; the mechanism matters less than that all domain logic
sits under one umbrella rather than scattered.

Benefits:

- Easier reasoning about where business rules live.
- Clear split between [unit tests targeting domain model/algorithms](four-types-of-code-for-testing-priority.md)
  and integration tests targeting controllers/application services.

Pairs with keeping **as few layers as possible** — most backend systems need
three: domain layer, application services/controllers, infrastructure (repos,
ORM, gateways). Excess layers obscure controller/domain boundaries and encourage
mock-heavy, low-value per-layer tests.

See [eliminate circular dependencies for testability](eliminate-circular-dependencies-for-testability.md)
and [ports and adapters architecture](ports-and-adapters-architecture.md).
