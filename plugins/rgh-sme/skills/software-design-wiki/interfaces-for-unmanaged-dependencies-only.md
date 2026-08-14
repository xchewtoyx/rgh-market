---
type: concept
title: Interfaces for Unmanaged Dependencies Only
description: >
  A single-implementation interface is not a genuine abstraction and violates
  YAGNI unless it exists to enable mocking an out-of-process dependency at
  the system boundary.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 8"
---

Developers often add interfaces for out-of-process dependencies (`IMessageBus`/
`MessageBus`) citing loose coupling and Open-Closed extensibility. Both reasons
are usually misconceptions:

- **Loose coupling** — an interface with one implementation is not a genuine
  abstraction; genuine abstractions are *discovered* post factum and need **at
  least two implementations**.
- **Future extensibility** — violates [YAGNI](yagni.md): opportunity cost and
  extra code to own without current need.

**Real reason for out-of-process interfaces: mocking.** Without an interface
you cannot create a test double for interaction with an unmanaged dependency.
Guideline: **interfaces for unmanaged dependencies only**; inject managed
(in-process) dependencies as concrete classes.

Example controller shape: `UserController(Database database, IMessageBus
messageBus)` — database concrete, message bus behind interface. Alternative
(virtual methods on concrete class) is inferior to interfaces.

**In-process domain interfaces** (`IUser`/`User` with one impl) are a red flag —
only reason is mocking, but you should **never verify interactions between
domain classes**; that produces brittle tests failing
[resistance to refactoring](four-pillars-of-a-good-unit-test.md).

Genuine abstractions (2+ implementations) may use interfaces regardless of
mocking needs.

See [mock only types you own](mock-only-types-you-own.md) and [mock at system
edges](mock-at-system-edges.md).
