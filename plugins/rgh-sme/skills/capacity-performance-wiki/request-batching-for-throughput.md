---
type: concept
title: Request Batching for Throughput
description: Accumulating multiple small requests client-side and shipping them as one network call amortizes fixed per-request overhead, trading added queueing latency for higher sustainable throughput.
sources:
  - title: "Patterns of Distributed Systems"
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 31, Request Batch"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 9"
---

Many small requests each pay a fixed per-request cost — network round-trip overhead, header bytes, server-side (de)serialization — regardless of how little payload each one carries. Past a certain request rate, that fixed cost, not raw bandwidth, becomes the throughput ceiling: a worked illustration on a 1Gbps link with 100-microsecond fixed latency/processing overhead per request shows hundreds of few-byte requests sent independently hitting the fixed-overhead ceiling long before bandwidth is the constraint.

## The Mechanism

A client accumulates outgoing requests in a queue instead of sending each immediately, then flushes the accumulated batch as a single network call once either of two trigger conditions fires:

* **Size trigger** — accumulated queued bytes exceed a configured maximum batch size.
* **Time trigger** — the oldest still-queued request has waited longer than a configured maximum wait time, so batching doesn't stall indefinitely under light traffic.

The receiving side unpacks the batch, processes each contained request through its normal single-request path, and returns one combined response that the client then splits back out per original caller.

## Sizing the Batch

Optimal batch size is workload-specific — it depends on individual message size, available bandwidth, and empirically observed latency/throughput, not a universal constant. Kafka's producer defaults to a 16KB batch size with a 0ms wait-time knob (`linger.ms`), meaning it batches opportunistically but never delays a send waiting to fill a batch by default. Batches sized in the megabytes range tend to hit diminishing returns and can add processing overhead of their own — batching is a tuned trade, not "bigger is always better."

## A Third Trigger: Continuous (In-Flight) Batching

Size and time triggers both share a limitation: once a batch starts executing, every member of that batch is bound to the others' completion — a batch mixing a short job and a long job forces the short job's result to wait until the long job finishes too, even though the resource running it had capacity to move on. This "naive batching" head-of-line-blocking cost grows with how varied the batched jobs' individual durations are.

**Continuous batching** (a.k.a. **in-flight batching**; introduced for LLM serving in the Orca paper, Yu et al., 2022) removes that coupling: instead of waiting for every batch member to finish before returning any result, each job's result is returned the moment *it* finishes, and a new job is immediately slotted into the freed capacity — keeping the resource continuously near-full without holding completed work hostage to the slowest batch member. This is the batch-level analogue of [request pipelining](request-pipelining-in-flight-limit.md): pipelining keeps a connection full of outstanding requests instead of idling on round-trip waits; continuous batching keeps a shared execution resource full of active work instead of idling on the slowest batch member. The two solve adjacent but distinct problems and are commonly used together in high-throughput serving systems.

## Trade-Off and Interactions

Batching is the same throughput-for-latency trade described in [throughput vs. latency trade-off](throughput-vs-latency-tradeoff.md): the fixed per-request overhead is amortized across the batch, raising throughput, but every request inside a batch now waits for the batch to fill (or its wait-time trigger to fire) before being sent at all, adding latency to each individual request compared to sending it alone.

Two operational consequences worth planning for:

* **Batch-level retry requires idempotency.** If a batch fails partway through processing and the whole batch is retried, some contained requests may already have been applied server-side. Safe retries need the server to deduplicate by a per-request identifier rather than re-execute blindly — a correctness mechanism owned outside this bundle, but one that batching cannot be retried safely without.
* **Batching is commonly paired with [request pipelining](request-pipelining-in-flight-limit.md)** for compounding throughput gains: batching amortizes per-request overhead, pipelining keeps the connection saturated with multiple outstanding batches instead of waiting for each one to complete before sending the next.

TCP's Nagle's Algorithm — delaying small outgoing packets briefly to coalesce them — is a lower-level instance of the identical idea applied below the application layer.

Batching amortizes fixed per-request overhead across many requests; a complementary lever shrinks that fixed overhead itself, per unit, regardless of batch size — see [wire/storage format overhead as a throughput ceiling](wire-format-overhead-throughput-ceiling.md).
