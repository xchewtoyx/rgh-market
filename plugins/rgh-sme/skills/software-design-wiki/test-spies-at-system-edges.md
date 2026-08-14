---
type: concept
title: Test Spies at System Edges
description: >
  Handwritten test doubles at the system boundary beat framework mocks for
  readability and reusable fluent assertions — and they audit production code
  independently instead of trusting it.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 9"
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 5"
---

A **spy** is a handwritten test double serving the same role as a framework
mock — "handwritten mock." At the [system edge](mock-at-system-edges.md), spies
often beat mocking frameworks:

- Reusable assertion-phase code via fluent methods (`ShouldSendNumberOfMessages(1).WithEmailChangedMessage(...)`).
- Smaller, more readable tests than verbose `Verify()` setup.

**Crucial distinction**: `BusSpy` is test code; `MessageBus` is production code.
**Tests shouldn't rely on production code when asserting** — auditors shouldn't
take the auditee's word. Mocking `IMessageBus` trusts production message
formatting; a spy with independent expected literals catches format changes —
avoid **tautology tests** with self-referential assertions.

Naming `BusSpy` as `BusMock` is acceptable if your team doesn't distinguish spy
versus mock.

Spies are functionally identical to mocks in Khorikov's taxonomy — both examine
outgoing interactions (commands). See [mocks versus stubs taxonomy](mocks-vs-stubs-taxonomy.md).

See also [mock objects](mock-objects.md).
