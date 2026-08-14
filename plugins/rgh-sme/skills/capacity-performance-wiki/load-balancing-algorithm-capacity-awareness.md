---
type: concept
title: Load Balancing Algorithm Capacity Awareness
description: Load balancing algorithms differ in whether they use any signal about a backend's actual current load, and picking one that ignores capacity or in-flight work concentrates queueing delay on already-busy backends even when total offered load is well within the pool's aggregate capacity.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 20"
---

A load balancing algorithm's choice of which backend to send the next request to determines how evenly [utilization](utilization-law.md) is actually spread across a pool — and by the [M/M/1 queue model](mm1-queue-model.md), an unevenly loaded pool produces worse tail latency than a perfectly balanced one running at the same aggregate utilization, because response time rises non-linearly as any individual backend's utilization climbs.

## Algorithms, in Order of Capacity Awareness

*   **Round robin:** cycles through backends in fixed order, sending each an equal share of *requests*. It has no notion of backend capacity, current load, or per-request cost — two backends with very different processing power, or very different in-flight work, receive the same request rate anyway. Round robin is only load-balanced in the narrow sense of request count; it is not utilization-balanced.
*   **Weighted round robin:** backends report a capacity or utilization metric back to the client (e.g., in RPC response headers), and the client weights how often each backend is chosen accordingly, sending less-capable or more-loaded backends a smaller share. This adds a real capacity signal but only as heavy as the reporting interval — a backend's load can change materially between one weight update and the next.
*   **Least loaded / least outstanding requests:** the client tracks how many requests it currently has in flight to each backend and always sends the next request to whichever has the fewest. This uses each client's own local view of load as a live, per-request signal rather than a periodically reported one, so it reacts to load changes without waiting for a backend to publish an updated metric.

## Why This Matters for Capacity, Not Just Correctness

A pool that is, in aggregate, comfortably under-utilized can still deliver poor tail latency if the algorithm distributing requests across it is capacity-blind: round robin can leave one backend running hot (high per-backend utilization, and by the M/M/1 relationship, disproportionately high queueing delay) while others sit comparatively idle, purely because request *count* was balanced and per-request *cost* or backend *capacity* wasn't. This is the same underlying shape as [hotspotting](hotspotting.md) — load concentrating on part of a pool that has spare aggregate capacity — but caused by the balancing algorithm itself rather than the workload's key/access pattern.

Whichever algorithm is used, it only balances *load*; a backend that has stopped serving correctly (not merely slow, but unhealthy) needs a separate active health-checking mechanism to remove it from rotation entirely, since no amount of load-aware weighting fixes sending traffic to a backend that can't serve it.

## The Naive Least-Loaded Cold-Start Trap

Naive least-loaded balancing has a specific, serious failure mode when a new or freshly restarted backend joins an already-loaded pool: an empty backend has zero measured load, so a least-loaded algorithm sends it *all* incoming traffic until its load catches up to the rest of the pool — by which point it has already been driven far past a sustainable rate and can crash or fail health checks. The pool then routes that traffic to the next backend it considers least loaded (possibly the one that just failed, if it recovers, or another newly-added one), repeating the same overload cycle. This is exactly the crash-loop mechanism a mass, unstaggered simultaneous reboot of an entire backend pool under sudden traffic surge can trigger: whichever node finishes rebooting first gets treated as "least loaded" and receives a traffic flood before the rest of the pool is even back.

**Mitigation — slow start:** cap the number of requests (or the request rate) any single backend, and especially a newly added or just-recovered one, can receive in a bounded window, regardless of how favorably "least loaded" ranks it. This trades a short period of under-utilizing the new backend's real capacity for avoiding the overload-crash-repeat cycle, and is a standard feature in production-grade load balancers precisely because of this failure mode. A pool-wide incident caused by staggered backend restarts is often best resolved by bringing all backends back into rotation simultaneously rather than one at a time, so no single freshly-restarted node is ever singled out as the "obviously least loaded" target during the overload window.
