---
type: concept
title: Fault-Error-Failure Chain
description: >
  The three-stage model — a latent fault triggers an error, which if
  uncontained becomes a failure — that explains why localized defects must be
  stopped at explicit boundaries before they reach users.
sources:
  - title: Release It!
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 3"
---

Three distinct stages separate a latent defect from a user-visible outage:

1. **Fault** — the underlying static flaw in software, configuration, or
   environment (an unhandled null case, a missing index, an infinite loop). A
   fault can sit dormant indefinitely without being triggered.
2. **Error** — an invalid internal execution state produced when the fault is
   actually executed under some specific operational condition (an invalid
   variable state, a thrown exception).
3. **Failure** — the inability of a system or component to deliver its
   required service (an HTTP 500, a socket timeout, total unavailability).

## Why the chain matters: containment vs. propagation

The chain doesn't have to reach failure, and a failure at one component
doesn't have to reach the whole system. The useful analogy is crack
propagation in materials science (as with the De Havilland Comet's
square-window fatigue fractures): a micro-crack — a fault — only becomes a
structural failure if the stress it introduces is allowed to propagate along
stress lines unchecked. In software, an uncaught exception, a slow socket
read, or a single locked database row is the micro-crack; if it's uncontained
it propagates across thread pools, process boundaries, network links, and
dependent services until it becomes a system-wide
[cascading failure](cascading-failure.md).

Stopping the chain from advancing means building explicit failure boundaries
into the architecture rather than trusting that errors stay local:
[circuit breakers](circuit-breaker-pattern.md) stop a struggling dependency
from consuming caller resources, and [bulkheads](bulkhead-pattern.md)
partition shared resources so an error in one function can't starve another.
Both exist specifically to arrest the fault-error-failure chain before an
error in one place becomes a failure everywhere.
