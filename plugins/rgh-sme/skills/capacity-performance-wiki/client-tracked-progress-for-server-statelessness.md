---
type: concept
title: Client-Tracked Progress for Server Statelessness
description: Making the client responsible for tracking its own consumption progress, rather than having the server track per-client delivery state, keeps server-side cost independent of how many clients are attached instead of growing with client count.
sources:
  - title: "Kafka: a Distributed Messaging System for Log Processing"
    resource: "Kafka: a Distributed Messaging System for Log Processing (Kreps, Narkhede & Rao), §5"
---

A server handing out a stream of data to many independent consumers has a choice about who tracks how far each consumer has gotten: the server can track per-consumer delivery/acknowledgement state itself, or it can hand each consumer a position marker (an offset, a cursor, a sequence number) and let the consumer track and report its own progress.

## Why Server-Side Tracking Doesn't Scale Cleanly

Tracking delivery state per consumer — which messages a given consumer has received, acknowledged, or still has outstanding — means the server's bookkeeping cost grows with the number of attached consumers, on top of the cost of moving the data itself. A benchmark comparing message-broker designs found this difference measurable directly: brokers that tracked per-message delivery state for every consumer showed the busiest broker thread spending most of its time maintaining that state, while a broker that stayed stateless with respect to consumer progress (consumers track their own offset into the stream and simply request more from a position they specify) had no equivalent bookkeeping cost at all, contributing to a measured 4x+ consumer-throughput advantage.

## The General Pattern

This is the same underlying move as [partition metadata lookup bottleneck](partition-metadata-lookup-bottleneck.md)'s fix — don't make a central component carry O(number of clients) state or work when that state can instead be pushed out to the clients themselves — applied to per-consumer delivery tracking instead of cluster routing metadata. The trade-off: a stateless server no longer knows on its own whether a given consumer is behind, has failed, or has caught up — that visibility, when needed (e.g., for alerting on a stalled consumer), has to be reconstructed by having the consumer report its own position rather than read off server-held ground truth. For a server whose primary job is moving high volumes of data to many consumers, trading that visibility for consumer-count-independent scaling is usually the right side of the trade — the alternative is a server whose achievable throughput degrades as more consumers attach, regardless of how much raw data-transfer capacity it has.
