---
type: concept
title: Domain Events for Deferred Side Effects
description: >
  Record meaningful past-tense domain events on an aggregate when state changes,
  then let the controller dispatch them — deferring out-of-process notifications
  until after in-memory business logic completes.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 7"
---

A **domain event** describes something meaningful to domain experts — distinct
from a UI event like a button click. Used to defer "notify external systems"
decisions out of controllers and into the domain model.

Implementation sketch: immutable past-tense value (`EmailChangedEvent { UserId,
NewEmail }`), collected on the aggregate (`user.EmailChangedEvents`) inside
`ChangeEmail()` only when the email actually changes. Controller iterates
events and dispatches to the message bus after persistence.

**Observable-behavior nuance**: DB writes may be implementation details (no
external client sees the DB directly; an ORM may skip unchanged rows), while
message-bus sends are observable to external systems and must match "email
actually changed."

Testing payoff: assert event creation on `User` in memory instead of mocking
the bus and verifying controller interactions. Generalization: extract
`DomainEvent` base, base domain class holding events, dedicated dispatcher;
larger systems may merge events before dispatch.

See [defer side effects for testability](defer-side-effects-for-testability.md),
[observable behavior versus implementation details](observable-behavior-vs-implementation-details.md),
and [canExecute execute pattern](can-execute-execute-pattern.md).

`UserTypeChangedEvent` follows the same pattern for support-logging requirements
— the domain raises the event; controller dispatch converts it to
[domain logger](support-logging-vs-diagnostic-logging.md) calls, keeping
out-of-process logging out of domain classes.

Some controller decision logic (email uniqueness checks, out-of-process failure
handling) cannot be deferred — cover with integration tests.
