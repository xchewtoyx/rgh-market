---
type: concept
title: Autoscaling Safety Bounds
description: Policy guardrails — min/max limits, asymmetric reaction speed, and kill switches — that keep an autoscaler's scaling decisions safe even when its input signal is misleading.
sources:
  - title: "The Site Reliability Workbook"
    resource: "The Site Reliability Workbook (Google SRE series), ch. 11"
---

Beyond choosing a correct [scaling signal](autoscaling-signal-selection.md), an autoscaling policy needs guardrails that bound how far and how fast it is allowed to act, because a correctly-configured signal can still be fed misleading input by a bug elsewhere in the system. These bounds govern purely *reactive* scaling; when instance startup is too slow to react to a spike as it arrives, [predictive autoscaling](predictive-autoscaling.md) is a complementary lever that provisions ahead of a demand forecast instead.

## Runaway Autoscaling

An autoscaler that scales purely on a resource-consumption signal (e.g., CPU usage) implicitly assumes that resource consumption is correlated with useful work performed. When that correlation breaks — a bug causes a component to burn CPU without producing output, or a failing downstream dependency causes requests to hang and pile up — the autoscaler reads rising resource consumption as rising demand and keeps scaling up, consuming quota and, in the downstream-dependency case, actively worsening the problem it's reacting to (more instances hammering an already-struggling dependency).

**Mitigations:**
*   **Set explicit min/max instance bounds.** Unconstrained autoscaling has no ceiling to stop a runaway loop short of exhausting quota entirely.
*   **Detect and throttle components doing no useful work.** If a component's resource consumption can be checked against actual throughput, aggressively throttle it the moment the two decouple, rather than letting the autoscaler "reward" the misbehavior with more capacity.

## Configure Conservatively and Asymmetrically

*   **React fast to load increases, cautiously to decreases.** Under-reacting to a spike risks an outage; over-reacting to a dip mostly risks a small amount of wasted spend — the two directions do not carry symmetric risk, so the policy shouldn't treat them symmetrically. This asymmetry is a deliberate application of [delayed feedback loop oscillation](delayed-feedback-oscillation.md): the scale-down direction is damped on purpose to avoid oscillating capacity down and back up on noise.
*   **Keep the operating point away from hard resource bottlenecks.** An autoscaler needs lead time to react; if the system is already near a hard ceiling (e.g., CPU saturation) when a spike starts, there may not be enough runway left to scale before [queueing latency blows up](mm1-queue-model.md).
*   **Maintain spare capacity for both overload protection and redundancy** — see [capacity headroom](capacity-headroom-safety-margin.md) and [N+M redundancy](n-plus-m-redundancy.md); autoscaling reduces but does not eliminate the need for standing headroom.

## Downstream and Cross-Service Effects

Scaling up a frontend tier increases load on everything behind it — databases, dependent microservices, shared quotas. An autoscaling policy for one tier needs a dependency analysis of what it will push load onto, and shared-quota services need per-consumer quotas so one autoscaling tier's growth spike can't starve its neighbors.

## Kill Switches

A fast, obvious, well-documented way to disable or manually override autoscaling must exist independent of the autoscaler's own logic — if the autoscaler itself is the thing behaving badly, an operator needs a way to intervene that doesn't depend on the autoscaler agreeing to be intervened on.
