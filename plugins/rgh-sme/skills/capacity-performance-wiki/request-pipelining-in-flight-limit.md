---
type: concept
title: Request Pipelining and the In-Flight Request Limit
description: Sending multiple requests on a connection without waiting for each prior response keeps both the network and the receiver's queued-work capacity utilized, but the number of unacknowledged requests allowed in flight must be capped to avoid overwhelming the receiver.
sources:
  - title: "Patterns of Distributed Systems"
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 32, Request Pipeline"
---

Over a single connection, a client that strictly waits for each response before sending the next request under-utilizes both the network link and the receiver's own capacity to accept queued work. A server that internally queues incoming requests (for example, one built around a single dedicated processing thread) can keep accepting and buffering new work while it's still finishing an earlier request — but a client sending one-at-a-time leaves that available capacity idle regardless of how much slack the server actually has.

## The Mechanism

Decouple sending from receiving on the connection: one path fires requests without blocking for a response, a separate path reads responses as they arrive. This lets the client keep the connection full of outstanding requests rather than gated by round-trip latency, which raises achievable throughput on a single connection substantially compared to a strict request-response-request cycle — directly mitigating [bandwidth-delay product](bandwidth-delay-product.md) limits imposed by round-trip time.

## The In-Flight Cap Is Not Optional

Pipelining without a limit on unacknowledged (sent-but-not-yet-responded-to) requests can flood the receiver faster than it can drain its queue, defeating the purpose. A pipelined connection must cap the number of in-flight requests per connection — a small constant (implementations commonly use values in the single digits) — and have new sends block once that cap is reached, which throttles the sender naturally back to the receiver's actual processing rate rather than an unbounded rate. This is a connection-local instance of the same admission-control idea as [concurrency limiting as admission control](concurrency-limiting-as-admission-control.md): the cap converts unlimited offered concurrency into bounded queueing at the sender, protecting the receiver's own throughput.

## Reordering Risk Under Retry

Pipelining introduces a correctness hazard that a request-per-round-trip design never has to consider: if an earlier in-flight request fails and is retried while a later one (sent after it, on the same pipelined connection) already succeeded and was processed, the receiver can end up applying the retried earlier request *after* the later one — silently reordering effects relative to send order. This must be actively prevented rather than tolerated, typically either by having the receiver reject anything that doesn't match its expected next-position marker (forcing the sender to resync), or by attaching a per-request monotonic sequence number that the receiver checks and rejects out of order. This reordering hazard is a correctness concern that sits outside this bundle's charter, but it is the direct cost of the capacity gain pipelining buys, so it must be budgeted for whenever pipelining is adopted purely for throughput.

## Pairing With Batching

Pipelining and [request batching](request-batching-for-throughput.md) attack the same throughput ceiling from different angles and are commonly used together: batching amortizes fixed per-request overhead by combining several logical requests into one network call, while pipelining keeps multiple such calls outstanding simultaneously instead of waiting for each to round-trip before sending the next.
