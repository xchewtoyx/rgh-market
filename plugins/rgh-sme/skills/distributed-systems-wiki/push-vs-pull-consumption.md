---
type: concept
title: Push vs. Pull Consumption
description: >
  Whether a sender forwards data to a consumer as soon as it's available or
  a consumer requests it at its own pace — pull gives the consumer natural
  flow control and a free replay position, at the cost of poll latency.
sources:
  - title: "Kafka: a Distributed Messaging System for Log Processing"
    resource: "Kafka: a Distributed Messaging System for Log Processing (Kreps, Narkhede, Rao), §2"
---

# Push vs. Pull Consumption

A sender moving data to a consumer has two shapes to choose from: **push**
— the sender forwards each item as soon as it exists — or **pull** — the
consumer requests items when it is ready for more. The choice determines who
controls the rate of flow.

**Push's failure mode is overload.** A sender with no notion of the
consumer's actual processing capacity can forward data faster than the
consumer can keep up, and needs an explicit flow-control mechanism bolted on
to avoid flooding it — the same [backpressure](state-watch.md) problem a
push-based watch/notification stream faces. Early log-aggregation systems
built on the push model (Facebook's Scribe, early Flume) inherited exactly
this risk.

**Pull inverts the failure mode into a design feature.** Each consumer
retrieves messages at whatever rate it can sustain — it simply doesn't ask
for more until it's ready — so flow control falls out of the protocol shape
for free rather than needing separate signaling. Kafka chose pull over the
push-based log aggregators that came before it for exactly this reason.

## The free side effect: rewind

Pull consumption pairs naturally with request-a-position semantics: a
consumer that pulls by explicitly specifying what it wants next (e.g. an
[offset](log-based-messaging.md)) can just as easily ask for an *earlier*
position as the next one — rewinding is not a special operation, only a
different argument to the same request. A push sender, by contrast, would
need to track and resend backlog on the consumer's behalf to offer the same
capability. This is the same principle behind [Kafka's newer controller
architecture](state-watch.md), where brokers pull the metadata log by offset
from a controller quorum rather than having the controller push
notifications — resuming after a disconnect is just "ask from the last
offset you have," with nothing to lose track of.

## The cost

Pure pull pays a latency cost a push design doesn't: if the consumer polls
on a fixed interval, new data waits out the remainder of that interval even
when the consumer is idle and ready. Long-polling (the consumer's pull
request blocks until data is available, rather than returning empty and
requiring a retry loop) closes most of this gap, trading a small amount of
held-open-connection overhead for pull's flow-control benefits without full
polling latency.
