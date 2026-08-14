---
type: concept
title: Message Brokers and Delivery Semantics
description: >
  How messages travel between services — direct messaging, transient
  AMQP-style brokers, and log-based brokers — and the ordering and loss
  semantics each implies.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 11"
  - title: Serverless Design Patterns and Best Practices
    resource: "Serverless Design Patterns and Best Practices (Zambrano), ch. 6"
---

# Message Brokers and Delivery Semantics

An event is a small, immutable record of something that happened; producers
publish events and consumers subscribe, usually grouped into topics. Three
transport designs, with very different semantics:

1. **Direct messaging (brokerless):** UDP multicast, ZeroMQ, webhooks,
   StatsD. Lowest latency, but producer and consumer must be up
   simultaneously; a missed message is simply lost. Acceptable where loss is
   tolerated (metrics) or handled at the application layer.
2. **Transient message brokers** (JMS/AMQP: RabbitMQ, ActiveMQ, AWS SQS).
   A queue server buffers messages while consumers are slow or down.
   Messages are **destructively read**: deleted once a consumer
   acknowledges. Three architectural properties follow from decoupling
   producers from consumers through this buffer:
   - **Durability:** once a producer's write succeeds and the broker is
     healthy, messages survive until a consumer processes and removes them
     — work is not lost because the downstream was momentarily unavailable.
   - **Scalability:** most queue designs parallelize by adding more
     workers that pull from the same queue.
   - **Predictable downstream load:** the queue absorbs bursts so workers
     can be tuned to a sustainable parallelism — e.g. enough concurrent
     consumers to keep up without overwhelming a shared database with
     reads and writes. See [queue as load buffer](queue-as-load-buffer.md)
     for deliberate use of this property.

   The abstraction's benefits do not replace broker **redundancy**: running
   the queue server itself as a single node (one EC2 instance carrying all
   business-critical traffic) means that node's death loses in-flight
   messages and breaks every client — the queue pattern still needs a
   replicated or managed service underneath.

   Two
   consumption patterns: *load balancing* (each message to one of several
   consumers, dividing work — also called **point-to-point** delivery) and
   *fan-out* (each message to all consumers — also called
   **publish/subscribe**).
   The trap: when a consumer crashes mid-processing, its unacknowledged
   messages are redelivered to other consumers — **out of order** relative
   to messages already processed. Combined with load balancing, ordering
   guarantees are effectively gone.
3. **[Log-based brokers](log-based-messaging.md)** (Kafka, Kinesis): the
   queue is a durable append-only log; consumers track offsets and nothing
   is deleted on read — preserving order per partition and enabling replay.

## Queues vs. log-based streams

Both implement asynchronous [messaging](#message-brokers-and-delivery-semantics),
but the consumption contract differs:

| | Transient queue | Log-based stream |
| --- | --- | --- |
| Read semantics | Destructive — message removed after ack | Non-destructive — consumer advances an [offset](log-based-messaging.md) |
| Consumer registration | Producer typically need not know consumers | Producer need not know consumers |
| Same message, many consumers | One consumer per message (load balancing); fan-out needs duplicate sends or defer-delete logic | Independent consumer groups each read the same record |
| Replay | Lost after consumption unless re-published | Retained for a configurable period; new consumers can start at an old offset and replay |
| Ordering | Often best-effort or per-FIFO-queue | Total order per partition |

Choose transient brokers when messages are expensive to process, strict
single-consumer semantics matter, order doesn't matter (or a dedicated FIFO
queue covers the case), and per-message parallelism is the goal. Choose
[log-based brokers](log-based-messaging.md) when ordering, high throughput,
multiple independent readers of the same event, and re-consumption matter —
which is why the log style anchors [derived-data
integration](change-data-capture.md).

When evaluating a hosted queue or stream service, the semantics that vary by
provider and tier include: [pull vs push](push-vs-pull-consumption.md)
consumption, maximum message lifetime and queue depth, [dead-letter
queue](dead-letter-queues.md) support, at-least-once vs claimed exactly-once
delivery, and ordering guarantees.

In all cases, redelivery after ambiguous failure means consumers see
duplicates — processing must be [idempotent](idempotency.md) unless the
broker offers a scoped exactly-once guarantee you can rely on end-to-end.

A system built on best-effort delivery (brokerless, or a broker that drops
messages during a long consumer outage rather than buffering indefinitely)
typically pairs the bus with an out-of-band reconciliation pass — e.g. a
periodic full dump of every record's key and last-modified time, letting a
consumer diff against its own state and backfill anything the bus never
delivered. This is the same shape as [anti-entropy](read-repair-and-anti-entropy.md)
in leaderless replication, generalized: a background comparison that repairs
whatever the primary propagation path silently lost.
