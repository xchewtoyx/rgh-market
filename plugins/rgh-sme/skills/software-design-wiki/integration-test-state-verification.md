---
type: concept
title: Integration Test State Verification
description: >
  Integration tests should re-read managed-dependency state through the same
  paths production code uses — not assert on input objects — and mock only
  unmanaged dependencies at the system edge.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 8"
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 10"
---

CRM email-change example (`UserController.ChangeEmail`): two out-of-process
dependencies — `Database` (managed) and `MessageBus` (unmanaged).

**Scenarios**: the longest happy path (corporate → non-corporate email) produces
maximum side effects — DB updates user and company, message goes to bus. Edge
cases already covered by unit tests or [fail fast](integration-testing-fundamentals.md)
need no integration test. Result: often a **single integration test** per
controller for the longest happy path.

**Dependency treatment**:

- Database → managed → **real instance**; verify state after the scenario.
- Message bus → unmanaged → **mock**; verify `SendEmailChangedMessage` interaction.

**State verification rules**:

- Use reusable arrange helpers (`CreateUser`, `CreateCompany`) shared across
  integration tests — not ad hoc row inserts.
- **Re-query state through independent reads**, not input parameters. Re-fetch
  `userFromDb` and `companyFromDb` via the same paths production code uses —
  exercising both write and read paths — but through a **fresh**
  [unit of work](unit-of-work-pattern.md) or database context for the assert
  section, not the instance shared with arrange or act. Shared ORM contexts
  cache loaded entities and can make assertions pass against stale in-memory
  copies; see [database integration test
  patterns](database-integration-test-patterns.md).
- Assert helpers can shrink the assert section further (deferred refinements).

**End-to-end alternative**: runs deployed with no mocks; emulates external client.
Integration tests with real managed deps and mocked unmanaged deps often suffice;
optional one or two end-to-end sanity checks post-deployment through the longest
happy path. In end-to-end tests, check the message bus directly but verify database
state only through the application API, not by querying the DB directly.

See [integration testing fundamentals](integration-testing-fundamentals.md),
[mocks for integration tests only](mocks-for-integration-tests-only.md), and
[database integration test patterns](database-integration-test-patterns.md).
