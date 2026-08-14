---
type: concept
title: Transactional Outbox Pattern
description: >
  Writing a state change and its outgoing event in the same local database
  transaction, then relaying the event via change data capture, so a service
  never has to keep two systems consistent through separate writes.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow (Kaiser), ch. 10"
---

# Transactional Outbox Pattern

A service that must both persist a state change and publish an event
announcing it faces the [dual writes problem](dual-writes-problem.md): the
database write and the message-broker publish are two independent
operations, and a crash between them either loses the event or announces a
change that never committed.

The outbox pattern removes the second write path instead of trying to make
it atomic with the first. The event is written as a row in an **outbox
table**, in the *same local transaction* as the state change — a single
transaction the database already makes atomic. A separate relay process then
reads the outbox and publishes each row to a message broker, marking it
sent. That relay is itself an instance of
[change data capture](change-data-capture.md): the database's transaction
log (or a stream built on it, e.g. DynamoDB Streams) is tailed for
committed outbox writes, so the publishing step can never observe a change
that didn't commit, and can never miss one that did.

This only shifts the delivery guarantee, not eliminates the need for one:
the relay typically guarantees at-least-once delivery (a crash after
publishing but before marking a row sent republishes it), so consumers of
the outbox stream must be [idempotent](idempotency.md). Combined with a
log that preserves per-key ordering, at-least-once delivery plus idempotent
consumers gives the same
[effectively-once](effectively-once-delivery.md) outcome that exactly-once
delivery would, without needing a distributed transaction between the
service's database and the message broker.
