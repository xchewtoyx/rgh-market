---
type: concept
title: Dead-Letter Queues
description: >
  A secondary queue that receives messages a primary queue's workers cannot
  process after a bounded number of attempts — stopping infinite retry
  loops while preserving failed messages for inspection.
sources:
  - title: Serverless Design Patterns and Best Practices
    resource: "Serverless Design Patterns and Best Practices (Zambrano), ch. 6"
---

# Dead-Letter Queues

On a transient [message broker](message-brokers.md), a worker that fails
to process a message must not call delete/ack — the message becomes visible
again after a **visibility timeout** and is retried. That is correct for
transient faults, but a **permanent failure** (bad payload, deleted upstream
resource, unhandled error class) produces an infinite loop: the same message
is delivered, fails identically, and returns to the queue forever,
consuming worker capacity and blocking head-of-line progress.

A **dead-letter queue (DLQ)** is a separate queue configured to receive
messages the primary queue's consumers could not successfully process after
**N attempts** (e.g. ten). Configuration is broker-specific, but the
contract is uniform:

- Successful processing still deletes from the primary queue as usual.
- After N failures, the broker **forcibly removes** the message from the
  primary queue and enqueues a copy on the DLQ.
- Operators inspect, replay, or discard DLQ contents after fixing the
  application bug or bad data.

The DLQ itself is a queue — monitor its depth and health like any other
buffer. It pairs naturally with [retry design](retry-design.md)'s rule to
bound attempts: the DLQ is where bounded retries land when exhaustion means
"give up on automatic processing," not where infinite [retry
amplification](cascading-failures.md) continues silently.

Permanent errors deserve no retry at all when detectable early; the DLQ
catches the cases where the worker only discovers failure at processing time
and has no inline path to reject without going through the visibility-timeout
cycle.
