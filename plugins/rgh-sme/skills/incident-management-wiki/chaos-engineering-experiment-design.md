---
type: concept
title: Chaos Engineering Experiment Design
description: The four-step method for designing a chaos experiment (steady state, hypothesis, injection, verification) and the blast-radius controls that keep it safe to run.
sources:
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Michael T. Nygard), ch. 17"
---

Chaos engineering as an organizational practice — deliberately injecting
controlled failure into a system, in staging or production, to surface
systemic weaknesses before an unannounced outage does — is designed as a
formal experiment, not an ad hoc fault injection:

1. **Define steady state**: establish measurable baseline metrics for
   normal operational health (e.g., steady throughput, p99 latency under a
   threshold, error rate near zero).
2. **Hypothesize the outcome**: state, explicitly and falsifiably, what
   should happen to those metrics under the planned fault (e.g., "if we
   terminate 20% of payment service instances, p99 latency rises by less
   than 50ms and the error rate stays at zero").
3. **Inject controlled stress**: execute the experiment against the target
   environment.
4. **Observe and verify**: measure deviation from steady state. An
   invalidated hypothesis is the point of the exercise — it identifies a
   systemic weakness to fix before it fails on its own schedule instead of
   the team's.

A chaos experiment is only as safe as its blast-radius controls. Running one
against an already-unstable system, or without solid observability and an
automated rollback path, turns the experiment itself into the outage it was
meant to prevent. Start with the smallest reasonable scope — a single
non-critical service, or a low-traffic canary — before widening to the full
production fleet, and always provide an automated "stop" that can abort
the experiment immediately if safety metrics degrade past a preset limit.

This experiment structure is a more rigorous, hypothesis-driven sibling of
the scheduled fault-injection exercises described in
[preparedness drills](preparedness-drills.md) — DiRT and game days test
whether a *response* to a known scenario works, while a chaos experiment
tests whether a specific belief about the system's resilience is actually
true.

Netflix's "Simian Army" is the canonical early example of running these
experiments continuously rather than as one-off events: Chaos Monkey
randomly terminates production instances during business hours to verify
stateless recovery, Chaos Gorilla simulates the loss of an entire
availability zone, Latency Monkey injects artificial network latency to
verify timeout and circuit-breaker behavior holds, and Conformity Monkey
terminates instances that violate a defined operational/security baseline
— each a narrow, repeatable instance of the same steady-state/hypothesis/
inject/verify structure above.
