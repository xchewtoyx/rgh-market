---
type: concept
title: Tunable Per-Request Quorum (N/R/W)
description: In systems that let each request specify how many replicas must respond, three independently tunable numbers — replica count, read quorum, and write quorum — trade off latency, durability, and availability against each other, and durability and availability do not always move together the way intuition suggests.
sources:
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §6"
---

Some replicated data stores don't fix a single quorum size for the whole cluster the way a consensus system does (see [quorum size vs. write throughput trade-off](quorum-size-throughput-tradeoff.md) for that fixed-majority case). Instead they expose three independent, per-request-tunable numbers:

*   **N** — how many nodes a given object is replicated to. Determines durability: more copies means a given write survives more simultaneous node losses.
*   **W** — how many of those N replicas must acknowledge a write before it's returned to the client as successful.
*   **R** — how many of those N replicas must respond to a read before it's returned to the client.

Because a client (or a service built on the store) picks R and W per use case rather than the store fixing them globally, very different workloads can share one cluster: a shopping-cart service tuned for write availability and business-logic-level conflict reconciliation looks nothing like a read-heavy product catalog cache tuned with `R = 1, W = N` for maximum read throughput — the same replication substrate serves both by exposing the trade-off rather than deciding it centrally.

## The Trade-Off Space

*   **Lower W** (down to 1): a write is accepted as soon as any single replica confirms it, minimizing write latency and maximizing write availability (the write almost never gets rejected for lack of live replicas) — but it opens a **durability vulnerability window**: the client is told the write succeeded while it may exist on only one node, so a failure of that one node before the write propagates loses data that was already acknowledged as durable.
*   **Higher W**: shrinks that vulnerability window (more copies must confirm before success is reported), at the cost of write latency (bounded by the slowest of the W replicas that must respond) and write availability (more replicas must be reachable and healthy for the write to succeed at all).
*   **R and W together** also determine read-after-write consistency: only when `R + W > N` is a read guaranteed to overlap with the most recent write's replica set.

## The Counter-Intuitive Part: Durability and Availability Can Move in Opposite Directions

Conventional intuition treats durability and availability as if they move together — a "more reliable" configuration should be better on both fronts at once. This trade-off shows they don't: **increasing W to reduce the durability vulnerability window simultaneously *decreases* write availability**, because a higher W requires more live, reachable replicas to accept any given write — the same change that makes an individual accepted write safer also makes writes more likely to be rejected outright when the cluster is even partially degraded. There is no configuration of W that improves both simultaneously; picking W is picking a point on that trade-off, not avoiding it.

## Practical Sizing

A commonly used production configuration is `(N, R, W) = (3, 2, 2)` — three-way replication with both read and write requiring a strict majority, chosen as a balance point meeting a service's performance, durability, consistency, and availability requirements simultaneously rather than optimizing any single one. There is no universally correct N/R/W; the right values follow from which of latency, durability, availability, or consistency a specific workload most needs to protect, the same way [load parameters](load-parameters.md) are chosen per-architecture rather than from a fixed universal list.
