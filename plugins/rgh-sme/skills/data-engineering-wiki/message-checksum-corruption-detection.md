---
type: concept
title: Message Checksum Corruption Detection
description: >
  Storing a checksum with every message in a log-based broker so storage and
  transit corruption can be detected and quarantined at the message level.
sources:
  - title: "Kafka: a Distributed Messaging System for Log Processing"
    resource: "Kafka: a Distributed Messaging System for Log Processing (Kreps, Narkhede, Rao), §3.3"
---

A [log-based message broker](log-based-message-broker.md) stores a **CRC**
alongside every message in the log, giving corruption detection a
per-message granularity instead of relying on the underlying filesystem or
disk to catch it. Two distinct failure classes this catches:

- **Storage corruption**: if a broker experiences an I/O error, a recovery
  process scans the log and removes any message whose stored CRC no longer
  matches its content, rather than leaving a silently corrupted message in
  place for a consumer to read.
- **Transit corruption**: because the checksum travels with the message
  itself, it can also be verified independently at produce time and at
  consume time, catching corruption introduced on the network hop in either
  direction — not just corruption that happened at rest.

This is the cheapest possible [validation gate](data-quality-validation-tests.md):
a single equality check per message, with no dependency on the message's
schema or content. It catches a narrow but important class of problem
(bit-level corruption) that schema validation and business-rule checks don't
address, since a corrupted message can still be well-formed enough to pass
every higher-level check while carrying wrong bytes.
