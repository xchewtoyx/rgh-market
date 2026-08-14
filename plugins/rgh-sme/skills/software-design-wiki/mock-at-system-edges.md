---
type: concept
title: Mock at System Edges
description: >
  When interaction testing an unmanaged dependency is warranted, mock the last
  type before the call leaves the process — exercising more production code
  and asserting what external systems actually observe.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 9"
---

Mocks belong only on **unmanaged (out-of-process) dependencies**. When
interaction verification is needed, verify at the **very edge** of the system —
mock the *last* type before the dependency leaves the process, not intermediate
wrappers.

CRM example: chain is `UserController` → `EventDispatcher` → `MessageBus` →
`IBus` (SDK adapter). Mock `IBus` and assert literal message text, not
`IMessageBus.SendEmailChangedMessage`. Benefits:

- **More regression protection** — more application code executes (`EventDispatcher`,
  `MessageBus` logic), not replaced by the mock.
- **Better refactoring resistance** — external systems see text messages, not
  calls to your wrapper class; test survives internal refactors preserving message
  structure.

Once `IMessageBus` isn't mocked, a single-implementation interface violates
[YAGNI](yagni.md) unless genuinely abstracted — replace with concrete `MessageBus`.

Never mock intermediate layers like `EventDispatcher`.

**Exception**: logging wrappers may not need edge-level precision — log existence
and content matter more than exact format to sysadmins; mocking `IDomainLogger`
can suffice. Required backward-compatibility precision varies per dependency.

See [test spies at system edges](test-spies-at-system-edges.md), [mocks for
integration tests only](mocks-for-integration-tests-only.md), and [mock only
types you own](mock-only-types-you-own.md).
