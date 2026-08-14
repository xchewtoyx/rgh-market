---
type: concept
title: Adaptive Client-Side Throttling
description: A client-side technique where each client locally estimates a backend's health from its own recent accept/reject history and probabilistically drops requests before sending them, to avoid amplifying an overload with retries.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 21"
---

**Adaptive throttling** addresses a specific overload-amplification problem: when an overloaded server starts rejecting requests, naive clients retry, adding more load to an already-overloaded server — the [synchronized retry storm](synchronized-retry-storm.md) pattern, but here driven by sustained overload rather than a single restart event. Adaptive throttling has each client locally decide to drop some of its own requests *before* sending them over the network, based on its own recent observed accept/reject ratio, without needing a central coordinator or any extra round trip.

## The Formula

Each client tracks two rolling counters over a recent time window: total `requests` attempted and `accepts` (requests the server actually accepted). Before sending a new request, the client computes a local rejection probability:

$$P_{\text{reject}} = \max\left(0, \frac{\text{requests} - K \times \text{accepts}}{\text{requests} + 1}\right)$$

Where $K$ is a tunable multiplier (typically around 2). The client draws a random number and locally drops the request (without sending it) if it falls below $P_{\text{reject}}$.

## Why It Works

*   **Self-correcting:** as the server's accept rate falls, $P_{\text{reject}}$ rises automatically, without either side needing to communicate an explicit "back off" signal — the client infers server health purely from its own recent success rate.
*   **The $K$ multiplier sets tolerance:** $K = 2$ means the client tolerates sending roughly twice as many requests as the server is currently accepting before it starts throttling itself locally — giving the server some slack for transient blips without triggering client-side throttling, while still capping the worst-case amplification a single overloaded server can experience from a fleet of clients.
*   **Reduces wasted work on both ends:** a request the client drops locally never consumes network bandwidth or server-side [resource-holding time](rpc-deadlines-and-resource-holding.md) that the server would have spent on a request it was going to reject anyway.

## Relationship to Server-Side Shedding

Adaptive throttling is a client-side complement to [server-side load shedding by priority](request-priority-shedding.md) — the client mechanism reduces how much load reaches the server in the first place, while server-side shedding decides what to do with whatever load does arrive. A system with only server-side shedding still pays the network and connection-setup cost for every rejected request; adaptive throttling avoids that cost for the fraction of requests the client itself decides to drop.
