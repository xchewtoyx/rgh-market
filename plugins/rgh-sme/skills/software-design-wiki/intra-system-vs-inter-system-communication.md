---
type: concept
title: Intra-System Versus Inter-System Communication
description: >
  Collaborations between your own classes are implementation details; only
  communications that cross the application boundary to external systems are
  observable behavior — and that distinction governs where mocks belong.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 5"
---

In a [ports and adapters (hexagonal) architecture](ports-and-adapters-architecture.md),
the **domain layer** owns business logic; the **application services layer**
orchestrates external communication and persistence without containing business
rules. Dependencies flow one way — from application services toward the domain;
domain classes never depend on application services or the outside world. External
systems connect only through application services.

Each layer has its own [observable behavior versus implementation
details](observable-behavior-vs-implementation-details.md), and the well-designed-API
principle applies fractally — to a whole layer or a single class. Tests mirror
that structure: an application-service test verifies a coarse-grained business
goal; a domain-class test verifies a subgoal on the way there. Observable
behavior flows inward from outer layers to the center — every piece of domain
behavior should trace back, through an application service, to an external
client's goal. A test that cannot be traced to a business requirement signals
coupling to implementation details.

Two communication types:

- **Intra-system** — between classes inside your application. These are always
  **implementation details**: the collaborations domain classes use to perform
  an operation have no immediate connection to the client's goal. Coupling
  tests to them causes fragility.
- **Inter-system** — your application talking to other applications. These form
  the **observable behavior of the application as a whole** and are part of the
  contract the application must uphold — driven by backward compatibility, since
  external systems may deploy on a different cycle.

**Core rule**: mocking is beneficial for verifying inter-system communication
patterns; mocking intra-system class-to-class collaborations produces tests
coupled to implementation details that fail [resistance to
refactoring](four-pillars-of-a-good-unit-test.md).

Purchase example: verifying `IEmailGateway.SendReceipt(...)` was called is
legitimate — inter-system, visible externally. Verifying `Customer`'s call to
`IStore.RemoveInventory(...)` is not — intra-system; the client's goal is
"make a purchase," satisfied by `customer.Purchase()` and observable inventory
state, not by the intermediate removal step.

**Application-owned out-of-process dependencies** (e.g. a database reachable
only through your API) are still **implementation details** — you and the
database can redeploy together without breaking external clients. Mocking such
a dependency (asserting exact repository calls) produces brittle tests that
break on harmless refactors like splitting a table. Treat "the database and
your application" as one system; test their combined state, not call patterns.

Mocks verify behavior only when the interaction crosses the application boundary
*and* the resulting side effect is visible externally — not when checking
inter-class interaction analogous to inferring a person's actions from neuron
firings.

See [classical versus London unit testing schools](classical-vs-london-unit-testing-schools.md),
[mocks for integration tests only](mocks-for-integration-tests-only.md), and
[mock at system edges](mock-at-system-edges.md).
