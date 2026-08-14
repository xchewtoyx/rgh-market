---
type: concept
title: Retry Design
description: >
  Retries convert transient distributed faults into success — or multiply an
  outage: bound them, back off exponentially with jitter, and retry only
  what is safe and worth retrying.
sources:
  - title: "Release It! (2nd ed.)"
    resource: "Release It!, 2nd ed. (Nygard), ch. 4"
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 8"
---

# Retry Design

On an [unreliable network](unreliable-networks.md) retries are mandatory —
transient faults are normal, and a single attempt gives up on operations
that would succeed a moment later. But naive retries are a **force
multiplier**: clients retrying failed requests in tight loops multiply
traffic precisely when the target is least able to serve it, turning a
brief brownout into a self-sustaining outage that persists until the
retriers are turned off. A degraded service facing N× its load from
stacked retries cannot recover.

Rules that keep retries on the right side of the ledger:

- **Only retry what's safe.** A timed-out request [may have
  succeeded](unreliable-networks.md); retrying a non-[idempotent](idempotency.md)
  operation risks double effect. Make the operation idempotent or carry an
  [end-to-end request id](end-to-end-argument.md) before retrying it.
- **Exponential backoff with jitter.** Space attempts out increasingly, and
  randomize the spacing — synchronized clients retrying on the same
  schedule arrive as waves that re-overload the target in pulses.
- **Bound the attempts.** A retry budget or maximum count, after which the
  failure propagates or degrades gracefully. Infinite retries assume the
  fault is always transient; real outages aren't.
- **Distinguish error classes.** Overload signals ("too many requests",
  queue-full) deserve *longer* backoff or none — retrying into overload
  [feeds the cascade](cascading-failures.md). Permanent errors (validation,
  authorization) deserve no retry at all (same triage as
  [transaction retries](transaction-aborts-and-retries.md)).
- **Mind retry amplification.** If each layer of a call chain retries 3
  times, a leaf failure generates 3^depth attempts. Retry near the origin
  of the request, not at every hop.

Paired with well-chosen [timeouts](timeouts-and-failure-detection.md),
retries define how your system behaves during every partial failure — they
deserve explicit design, not library defaults.
