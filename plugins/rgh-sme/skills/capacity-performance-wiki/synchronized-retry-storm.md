---
type: concept
title: Synchronized Retry Storm
description: A client-side load amplification failure mode where many clients retry a failed request at nearly the same moment, producing a traffic spike far above normal peak when the shared backend recovers.
sources:
  - title: "The Site Reliability Workbook"
    resource: "The Site Reliability Workbook (Google SRE series), ch. 11"
---

A **synchronized retry storm** (also called a thundering herd, in this specific client-retry sense) occurs when a large population of clients experience a request failure at roughly the same time — typically because a shared backend restarted or briefly failed — and then retry in a way that is itself synchronized, producing a demand spike far larger than the traffic that caused the original failure.

## Distinguishing from Cache Stampede

This is a distinct mechanism from a [cache stampede](cache-stampede.md), even though both are colloquially called "thundering herd." A cache stampede is triggered by a single key's expiration causing many requests to simultaneously miss the cache and hit the backend directly. A synchronized retry storm is triggered by many independent *clients* reacting to a shared failure event with correlated retry timing — the amplification comes from client behavior, not from a shared cache's state transition.

## The Mechanism

1.  A shared backend instance restarts, deploys, or briefly fails, causing in-flight requests from many clients to fail simultaneously.
2.  Naive client retry logic (a single immediate retry, or a fixed-delay retry with no randomization) causes a large fraction of those clients to resend their request at nearly the same instant.
3.  The retry spike lands on the recovering (and therefore still resource-constrained) backend, which can push it back into failure, triggering another synchronized wave of retries — a positive feedback loop that can spike traffic to many multiples of normal peak (e.g., a documented case reached roughly 20x prior peak requests/second from this mechanism alone). This is [delayed feedback loop oscillation](delayed-feedback-oscillation.md) playing out across a population of clients: each client's retry is a correction fired before the client can observe whether the backend has actually recovered.
4.  Backends under this load tend to become **slow rather than outright fail**, which is worse for capacity: slow responses cause client-side timeouts, which themselves trigger further retries, compounding the load rather than shedding it cleanly.

## Mitigation

*   **Jittered, truncated exponential backoff:** each retrying client waits a randomized, exponentially increasing delay (capped at a maximum) before retrying, so retries spread out over time instead of arriving as a single spike. This is the standard client-side fix and should be built into any client that talks to a shared backend.
*   **[Circuit breakers](circuit-breaker-pattern.md):** rather than only spacing retries out, a client can stop attempting calls to a backend entirely once its error rate crosses a threshold, removing retry load from the equation altogether until a cooldown period passes.
*   **Request deadlines** so a hung request doesn't hold resources indefinitely, waiting for a timeout to trigger the retry — see [RPC deadlines and resource holding](rpc-deadlines-and-resource-holding.md).
*   **Isolate blast radius:** route the affected traffic to a dedicated pool while it stabilizes, so the retry storm doesn't degrade capacity for unrelated traffic sharing the same backend pool.
