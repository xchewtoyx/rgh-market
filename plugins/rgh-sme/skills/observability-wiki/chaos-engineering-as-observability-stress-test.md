---
type: concept
title: Chaos Engineering as a Stress Test of Observability Coverage
description: Deliberately injecting faults into production (killing processes, adding artificial latency, misconfiguring instances) is as much a test of whether monitoring and telemetry actually surface the resulting degradation as it is a test of the system's fault tolerance.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 12"
---

Chaos engineering tools (the canonical example being Netflix's Simian Army: Chaos Monkey randomly kills running processes, Latency Monkey injects artificial network delay, Doctor Monkey uses health checks plus signals like CPU load to find unhealthy instances, Conformity/Security Monkey flags instances violating operational or security best practices) deliberately introduce faults into a running production system rather than only a test environment.

From an observability angle, the point of these tools is not fully captured by "did the system stay up." A chaos experiment that degrades the system in a way nobody notices — no alert fires, no dashboard shows it, no trace makes the slowdown visible — has found a monitoring gap at least as significant as any fault-tolerance gap: it demonstrates that if this fault happened for real, the team would find out from users before finding out from telemetry. So a mature chaos-engineering practice checks both things at once: did the fault get masked/recovered, and did the observability stack actually surface it while it was happening. Discovering the latter kind of gap is itself the more common practical outcome for teams new to the practice.

Some systems are adaptive/complex enough (emergent behavior under real production traffic and real dependency failures) that no feasible amount of pre-production testing substitutes for this — the complementary practice is treating production itself as a source of ground truth, capturing operational telemetry richly enough that a chaos-induced (or naturally occurring) failure can be reproduced and analyzed after the fact using the same recorded data, rather than needing to reproduce it live. This is the same underlying need [structured wide events](structured-events-as-observability-substrate.md) are designed to satisfy: enough context captured at the time of the failure that root-causing doesn't require re-triggering it.

A [telemetry premortem](telemetry-premortem.md) is the cheap, imagined version of the same check — reasoning through whether a hypothetical failure would be legible, without actually injecting it.
