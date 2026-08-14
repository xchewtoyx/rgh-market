---
type: concept
title: LIFO vs. FIFO Queueing Under Overload
description: Under sustained overload, a FIFO queue lets every request age toward its deadline before being served, causing near-total failure, while a LIFO queue serves the freshest requests first and sheds the stale ones — trading fairness for a higher fraction of successful responses.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 21"
---

Queue discipline — the order in which queued requests are picked up for processing — normally defaults to **FIFO (first-in, first-out)** for fairness: the request that arrived first is served first. Under sustained overload, this default becomes actively harmful. This is one specific instance of the broader choice covered in [request scheduling policy selection](request-scheduling-policy-selection.md): LIFO-under-overload is a dynamic-priority policy, prioritizing by remaining deadline slack rather than arrival order.

## The FIFO Hazard Under Overload

When arrival rate exceeds service rate for a sustained period, a FIFO queue grows without bound (the [M/M/1 queue model](mm1-queue-model.md)'s response time diverging as utilization approaches 100%). Every request sits in the queue behind all the ones that arrived before it. If each request carries a deadline, requests near the front of a long FIFO queue may already be close to timing out by the time they're finally dequeued — and by the time the server gets to them, they may have exceeded their deadline and be worthless to the client that sent them, yet the server still spends processing capacity on them. Under sustained overload, this can degrade toward every request in the queue failing, since the queue never gets short enough for any request to be served within its deadline.

## The LIFO Alternative

A **LIFO (last-in, first-out)** discipline processes the *newest* arrivals first — the requests with the most deadline budget remaining. Under the same overload conditions:

*   Freshly arrived requests are served immediately, with their full deadline still available, so they have the best chance of completing successfully.
*   Older, queued requests are served later or not at all — but many of them were already past or close to their deadline anyway, so the capacity that would have been spent serving them (unsuccessfully) is instead spent serving requests that can actually succeed.
*   Net effect: a higher fraction of *served* requests succeed, at the cost of some requests being starved entirely if overload persists long enough — the opposite fairness trade-off from FIFO.

## When to Use Which

LIFO under overload is a deliberate trade of fairness for throughput of *successful* responses: it accepts that some requests will be starved so that the requests that are served aren't wasted effort on responses the client will discard anyway due to deadline expiry. This only pays off when requests carry meaningful deadlines the server can reason about — see [RPC deadlines and resource holding](rpc-deadlines-and-resource-holding.md) for why every request needs one in the first place. Under normal (non-overloaded) load, FIFO's fairness has no throughput cost and remains the better default; the LIFO trade-off is specifically a saturation-response tool.
