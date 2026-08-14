---
type: concept
title: Chaos Engineering
description: The discipline of experimenting on a system in production by injecting controlled failures to reveal systemic weaknesses.
sources:
  - title: Release It!
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 17"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 19"
---

Chaos engineering is a proactive method of embracing risk by deliberately injecting controlled failures—such as instance termination, network latency, disk exhaustion, or packet drops—into a distributed system. Rather than waiting for unannounced infrastructure outages to occur, teams create controlled experiments to reveal weaknesses before they cause catastrophic outages. This addresses a structural blind spot: [resilience is invisible during normal operation](resilience-vs-stability.md), so the only way to find out whether a system actually has it is to test the system's limits deliberately, on your own terms, rather than discovering the gap during a real incident.

An effective chaos experiment begins by defining the steady state of the system, often mapped to its [service level indicators](service-level-indicator.md). A hypothesis is then formulated regarding how the system should handle a specific failure (e.g., that a [circuit breaker](circuit-breaker-pattern.md) will trip and prevent a [cascading failure](cascading-failure.md)). [Failure scenario mapping](failure-scenario-mapping.md) is the planning exercise that decides which failure hypotheses are worth testing in the first place.

Safety is critical when executing chaos experiments. Teams must control the blast radius by starting small—perhaps with a single non-critical service or low-traffic canary target—before expanding to production fleets. Comprehensive observability and an automated "stop button" to abort the experiment if metrics degrade beyond acceptable limits are essential.

## Origin: Netflix's Chaos Monkey

The paradigm case is Netflix's **Chaos Monkey**, a service that randomly kills
production instances during business hours to force engineering teams to get
used to a constant background level of failure, so that services are built to
recover automatically rather than depend on any single instance staying up.
The payoff showed up empirically: when Netflix re-architected to be
cloud-native around 2009 — building in [loose architectural
coupling](loose-architectural-coupling.md), aggressive timeouts, [circuit
breakers](circuit-breaker-pattern.md), and [graceful
degradation](graceful-degradation.md) — it was the only major service
unaffected by a 2011 outage that took down an entire AWS availability zone
and several other well-known sites with it. The resilience wasn't luck; it
was the direct, tested result of continuously injecting the failure mode
chaos engineering rehearses.

Chaos engineering run continuously and automatically at the level of
individual instances is complementary to — but distinct from —
[game day exercises](game-day-exercises.md), which rehearse much larger,
scheduled failures (e.g. a simulated full data-center loss) and test the
human response process as much as the system itself.

## Scaling Blast Radius: the Netflix Simian Army

Chaos Monkey's single-instance failure injection is one point on a spectrum
of blast radius that's worth deliberately climbing, not a ceiling. Netflix
extended it into a full toolset ("the Simian Army") that injects failure at
progressively larger scopes and failure types, each validating a different
resilience assumption:

- **Chaos Gorilla** — simulates the loss of an entire availability zone,
  validating cross-zone redundancy rather than just single-instance
  recovery.
- **Chaos Kong** — simulates the loss of an entire region, validating
  cross-region failover.
- **Latency Monkey** — injects artificial delay into service-to-service
  calls rather than killing anything outright, validating that dependent
  services time out and [degrade gracefully](graceful-degradation.md)
  instead of blocking.
- **Doctor Monkey** and **Conformity/Security Monkey** — continuously find
  instances that are unhealthy or that violate operational/security best
  practices and proactively remove them, rather than waiting for an
  experiment to trigger a check.

The general lesson: a mature chaos engineering practice deliberately injects
failure at multiple distinct scopes (instance, zone, region) and multiple
distinct failure types (hard kill vs. added latency vs. policy violation),
because each targets a different layer of the system's resilience
assumptions.
