---
type: concept
title: Circuit Breaker Pattern
description: A state machine pattern that prevents cascading failures by immediately failing requests to a degraded downstream dependency.
sources:
  - title: Release It!
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 2, ch. 5"
---

The Circuit Breaker is a stability pattern that acts as a state machine to protect [dependency reliability composition](dependency-reliability-composition.md). When a downstream service crosses a failure threshold (e.g., error rate or latency limit), the circuit "trips" from CLOSED to OPEN. 

While OPEN, all outgoing requests to that dependency immediately fail fast without making a network call. This prevents caller threads or sockets from blocking, stopping a [cascading failure](cascading-failure.md) from exhausting resources on the caller. 

After a configured sleep window, the circuit transitions to HALF-OPEN, allowing a limited number of trial requests through to test if the downstream service has recovered. If the trial succeeds, the circuit returns to CLOSED; if it fails, it returns to OPEN.

A circuit breaker only helps if remote calls are wrapped defensively in the first place: it needs an explicit timeout on the call itself, and the caller needs to actually catch and handle whatever exception the dependency can throw, rather than letting it propagate unhandled. In a fleet-grounding airline outage, an uncaught runtime exception from a remote call caused the container to fail to release the thread and database connection it was using; without a timeout or circuit breaker on that call path, every subsequent caller blocked waiting for the same exhausted pool, and the failure crossed from a minor admin tool into the airline's core passenger-facing transactional systems. Pairing a circuit breaker with a [bulkhead](bulkhead-pattern.md) around less-critical call paths keeps that kind of failure from ever reaching shared resources at all.
