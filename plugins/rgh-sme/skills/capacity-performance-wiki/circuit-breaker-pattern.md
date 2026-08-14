---
type: concept
title: Circuit Breaker Pattern
description: A client-side pattern that stops sending requests to a failing dependency for a cooldown period, protecting both the struggling backend's recovery and the caller's own resources from being spent on calls that are unlikely to succeed.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 22"
---

A **circuit breaker** wraps an RPC or downstream call with logic that tracks the recent error rate for that dependency. Once the error rate crosses a threshold, the breaker "opens": subsequent calls fail immediately on the client side, without ever reaching the network or the struggling backend, for a cooldown period. After the cooldown, the breaker allows a small trial volume of real calls through to test whether the dependency has recovered ("half-open") before fully closing again.

## Why This Protects Capacity, Not Just Correctness

A backend that is failing or badly overloaded is often *slow* to fail rather than fast — requests hang until a timeout, tying up caller-side threads, connections, and memory for every one of those calls. Continuing to send traffic to a backend in this state does two kinds of damage at once: it keeps the backend pinned under load that is actively preventing its own recovery, and it burns the caller's own limited resources (thread pool slots, connection pool entries) on calls that are statistically unlikely to succeed. An open circuit breaker removes both costs simultaneously — the backend gets a clean window with reduced load in which to recover, and the caller's resources go back to serving requests that can actually succeed.

## Relationship to Adjacent Patterns

*   **Complements [concurrency limiting as admission control](concurrency-limiting-as-admission-control.md).** Admission control caps how much concurrent work reaches a resource that is *healthy but nearing its throughput limit*; a circuit breaker instead stops sending work entirely to a resource that is *already failing*. The two are often layered: admission control on the way in during normal operation, a circuit breaker as the response once error rate indicates the resource is not recovering under that load.
*   **Distinct from a [synchronized retry storm](synchronized-retry-storm.md)'s mitigation.** Jittered backoff spreads out *when* retries happen; a circuit breaker instead decides *whether* to attempt the call at all, short-circuiting the retry-and-fail cycle altogether once it's clear the backend isn't recovering — the two combine naturally, since a breaker's half-open trial calls still benefit from being jittered rather than synchronized.
*   **A structural instance of [delayed feedback loop oscillation](delayed-feedback-oscillation.md).** A breaker with too short a cooldown reopens against a backend that hasn't actually finished recovering, flapping between open and closed in the same way an over-eager control loop overshoots — the cooldown period is the deliberately lengthened response delay that lets the backend's recovery actually be observed before the next correction (trial call) fires.

## Failure Mode: Breaker Threshold Coupled to the Wrong Signal

A circuit breaker tuned to trip on a health check that measures more than basic process vitality (e.g., a health check that itself checks a downstream dependency) risks a self-inflicted cascading failure: one struggling dependency trips health checks on everything that transitively depends on it, pulling healthy capacity out of rotation and concentrating load onto whatever remains — the same [automated rebalancing failure cascade](automated-rebalancing-failure-cascade.md) mechanism, triggered by an overly broad breaker condition instead of a rebalancer's own leader-failover logic.
