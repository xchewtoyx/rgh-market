---
type: concept
title: Pull-Based Consumer Model
description: >
  Having consumers pull messages from a broker at their own pace, rather
  than the broker pushing to consumers, and why that shifts flow control to
  the consumer.
sources:
  - title: "Kafka: a Distributed Messaging System for Log Processing"
    resource: "Kafka: a Distributed Messaging System for Log Processing (Kreps, Narkhede, Rao), §3, §2"
---

A [log-based message broker](log-based-message-broker.md) can hand messages
to consumers one of two ways: **push**, where the broker decides when to
send the next message, or **pull**, where the consumer requests messages
from the broker (typically via a blocking-iterator interface: read the next
message if one is available, otherwise wait until one is published) and the
broker never initiates a send on its own.

Pulling puts flow control on the consumer's side of the connection: a slow
or overloaded consumer simply requests less often, and never has to signal
back-pressure to a broker that's trying to push faster than it can keep up.
It also removes the need for the broker to track each individual consumer's
delivery state beyond the last offset served — the consumer's own request
cadence already governs its rate.

This matters for pipeline design because it makes consumer-side throughput
and scaling entirely the consumer's problem to size: a downstream job reading
from the broker can be scaled up or down, paused, or restarted without any
coordination with the producing side, since nothing about production depends
on how fast any particular consumer is pulling.

Pull is also what makes [replaying history](stream-replay-for-reprocessing.md)
a natural extension of ordinary consumption rather than a special operation:
because a pull-based consumer already requests specific offsets at its own
pace, requesting an *earlier* offset than it last read is no different a
request in kind — a push-based broker, by contrast, would need a distinct
mechanism to hand a consumer data it already sent.

Push-model log aggregators built for purely offline consumption (batch
dumps into a warehouse or Hadoop) tend to degrade badly once messages
accumulate faster than the offline consumer drains them — exactly the
situation a pull-based consumer sidesteps by simply pulling at whatever rate
it can actually sustain, whether that's continuous or a periodic large
batch.
