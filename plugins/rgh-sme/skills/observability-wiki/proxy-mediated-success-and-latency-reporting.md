---
type: concept
title: Proxy-Mediated Success and Latency Reporting
description: Self-reported application-level success/failure and latency can be inaccurate or entirely absent for a sufficiently broken instance, so putting an ingress proxy or service mesh in front of a service to independently report these values makes measurement survive the exact failures it needs to detect.
sources:
  - title: "Implementing Service Level Objectives"
    resource: "Implementing Service Level Objectives (Alex Hidalgo), ch. 7"
---

Instrumenting request success/failure and latency directly in application code has two failure modes that are easy to overlook:

- **Self-reporting can't survive its own worst case.** A sufficiently broken service instance (crashed, deadlocked, out of memory) may be unable to emit the very telemetry that would report it as failing — the measurement depends on the health of the thing being measured.
- **Self-reported latency is often inaccurate.** Application-level timers typically start after the request has already passed through kernel network queuing and the HTTP stack, so they systematically under-report true end-to-end latency, especially under load when queuing delay grows.

Putting an **ingress proxy or service mesh** in front of the service addresses both: it observes and reports success/failure and latency from outside the process, so it keeps reporting even when the instrumented service itself cannot, and it can time a request from actual arrival rather than from whenever application code got around to starting its own timer. The trade-off is that the proxy/mesh sits in the request path and can add its own latency, so it isn't a strictly free substitute for in-process instrumentation — the two are complementary, not one replacing the other.

This is a specific instance of the general principle that [what to capture on a wide event](wide-event-attribute-checklist.md) needs a stable, canonical endpoint identifier and accurate success/latency fields — see [telemetry naming conventions](telemetry-naming-conventions.md) for keeping that identifier free of high-[cardinality](cardinality.md) path segments.
