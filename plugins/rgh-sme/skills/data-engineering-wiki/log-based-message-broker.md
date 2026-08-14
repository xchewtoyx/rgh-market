---
type: concept
title: Log-Based Message Broker
description: >
  Why append-only, partitioned, offset-addressed logs (Kafka, Kinesis) became
  the default streaming-ingestion broker over transient queue brokers.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 11"
---

Streaming-ingestion brokers fall into two families, and the difference shapes
what a pipeline built on top of one can and can't do later.

**Transient message brokers** (JMS, AMQP, RabbitMQ-style) hold messages in a
centralized queue and delete each one once a consumer acknowledges it — a
**destructive read**. They support load-balancing a queue's messages across
multiple consumers, or fanning one message out to every subscriber. Because
redelivering an unacknowledged message after a consumer crash can hand it to a
different consumer than the one that first received it, message order across
retries isn't preserved.

**Log-based message brokers** (Apache Kafka, AWS Kinesis) instead combine a
database's append-only durability with a message queue's publish/subscribe
interface. A topic is split into partitions (see
[stream partition keys and hotspotting](stream-partition-keys-and-hotspotting.md)),
each an append-only log on disk; every message gets a monotonically
increasing **offset** within its partition. Consumers track their own offset
and read non-destructively — nothing is removed on read, so multiple
consumers can read the same partition independently at their own pace without
interfering with each other. Because the broker retains messages on disk
(often for days or weeks, sometimes effectively indefinitely), a consumer can
rewind to an earlier offset and re-read history, which is the mechanism behind
[stream replay for reprocessing](stream-replay-for-reprocessing.md) — replay
is just resetting a consumer's offset, not a special operation.

This durability is also what makes [log compaction](log-compaction.md)
possible: because every message is retained at a stable offset rather than
deleted on read, a broker can selectively discard superseded messages for the
same key while still leaving the topic replayable from any surviving offset.
The same per-message durability is also what makes
[checksum-based corruption detection](message-checksum-corruption-detection.md)
practical at the message level rather than only at the file or disk level.

Consumers connect to a log-based broker through **consumer groups**: every
consumer in the same group jointly divides up a topic's partitions, so the
group as a whole behaves like a load-balanced, point-to-point queue (each
message goes to exactly one consumer in the group), while two different
consumer groups each get their own independent copy of the full topic — the
same underlying log serves both delivery models at once, through how
consumers are grouped rather than through anything the producer or broker
configures per-message. Consumers also
[pull](pull-based-consumer-model.md) from the broker rather than having
messages pushed to them, which is what lets each group's consumption rate
stay entirely decoupled from every other group's.

The practical trade-off when choosing between the two families for a pipeline:
transient brokers are simpler to reason about for pure task distribution
(each unit of work processed exactly once by exactly one worker, then gone),
while log-based brokers are the right choice whenever downstream consumers
need to replay history, add a new consumer after the fact and have it see
everything from the beginning, or fan the same stream out to multiple
independent readers (e.g., one consumer loading a warehouse, another feeding
a real-time dashboard) without the broker having to track per-consumer
delivery state.
