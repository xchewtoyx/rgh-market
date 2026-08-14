---
type: concept
title: Expose Compensating Behavior Instead of Hiding It
description: Layered automatic safeguards that silently absorb small deviations reduce the frequency of visible failures but make the eventual failure both harder to diagnose and more sudden, because operators never saw the system straining until it broke; instrumenting the compensation itself, not just the eventual failure, keeps degradation visible while it's still cheap to act on.
sources:
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power (Gary Klein), ch. 16"
---

Jens Rasmussen's observation about layered safety defenses in the nuclear industry generalizes directly to automated systems: building more automatic safeguards that quietly correct small deviations does reduce how often an operator has to intervene, but it comes at a real cost — when a deviation finally exceeds what the safeguards can absorb, the operator faces a much harder problem, because they must now untangle the original fault *and* the accumulated effects of every defense that tried (and eventually failed) to compensate for it, all at once, usually under time pressure and with no warning it was coming.

A concrete instance: an aircraft's flight management system silently used other flight controls to compensate for an unnoticed rudder misconfiguration, giving the crew no indication anything was wrong — until the compensation capability was exhausted and the system disengaged without warning, handing back control of an aircraft already outside safe operating limits. The system's own corrective effort was invisible right up to the point of catastrophic failure. Rasmussen's recommended alternative to ever-deeper defense-in-depth: make the compensating behavior itself visible, so an operator can notice a system is straining and intervene while there's still margin, rather than trusting silently-nested automation to always fully absorb the problem.

For observability, this argues for treating "how hard is this system working to stay healthy" as telemetry in its own right, not just the pass/fail health check at the end of the chain — retry counts, failover activations, autoscaling near its ceiling, circuit breakers tripping, buffers filling, degraded-mode fallbacks engaging. See [closing telemetry gaps from past incidents](closing-telemetry-gaps-from-past-incidents.md) for the related practice of instrumenting specifically the compensating mechanisms a past incident revealed were invisible, and [deployment markers and settling period](deployment-markers-and-settling-period.md) for a different case of the same principle — making a system's transient, self-correcting behavior visible on a graph instead of assuming it is either fully fine or fully failed.
