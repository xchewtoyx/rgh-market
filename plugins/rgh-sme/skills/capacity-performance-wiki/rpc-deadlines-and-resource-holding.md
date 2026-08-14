---
type: concept
title: RPC Deadlines and Resource Holding
description: Without an explicit deadline, a stalled request holds server-side resources (memory, connections, threads) for as long as a language or framework default allows, turning a slow dependency into a resource-exhaustion risk.
sources:
  - title: "The Site Reliability Workbook"
    resource: "The Site Reliability Workbook (Google SRE series), ch. 11"
---

A request without an explicit **deadline** (a maximum time it is allowed to remain in flight) holds whatever resources it has acquired — memory buffers, connections, a worker thread — for as long as it takes to complete or fail, which in the absence of an explicit bound defaults to whatever ceiling the language or RPC framework happens to impose (often effectively unbounded).

## Why This Is a Capacity Risk

When a downstream dependency slows down rather than failing outright, requests waiting on it accumulate: each one is individually still "in progress," so nothing automatically frees the resources it's holding. Under sustained slowness, this accumulation can exhaust memory or connection pools even though the request *rate* hasn't changed — the problem is requests piling up in flight, not requests arriving too fast. This compounds any existing [tail latency amplification](tail-latency-amplification.md) risk: a fan-out call with no deadline on its sub-calls can have its resource footprint held open by whichever single sub-call is slowest.

## Mitigation

*   **Set sensible default deadlines** on every RPC — a resource-holding budget the request is allowed, after which it is aborted rather than left open-ended. Framework-level defaults (e.g., documented via a `.proto` comment convention) make this the norm rather than something each call site has to opt into.
*   **Propagate cancellation to clients.** A client that no longer needs a response (the user navigated away, a retry already superseded it) should actively cancel the in-flight request, freeing server-side resources immediately rather than waiting for the deadline to expire.
*   **Propagate the deadline itself, as an absolute timestamp, not a relative timeout.** Carrying an absolute deadline through an RPC lets a server check, the moment it dequeues a request, whether that request has already spent its entire allotted time sitting in the queue — and if so, drop it immediately without processing rather than wastefully executing a response the client will discard anyway. A relative "give me 5 seconds" timeout re-armed at each hop can't make this check; only an absolute deadline set once at the origin survives being passed hop-to-hop with its meaning intact.

Deadlines are a resource-holding safeguard, distinct from — but complementary to — the [jittered backoff](synchronized-retry-storm.md) that keeps client retries from synchronizing into a demand spike, and they are the prerequisite that makes [LIFO queueing under overload](lifo-vs-fifo-queueing-under-overload.md) possible at all.
