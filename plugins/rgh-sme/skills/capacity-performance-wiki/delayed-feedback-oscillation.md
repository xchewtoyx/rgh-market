---
type: concept
title: Delayed Feedback Loop Oscillation
description: A corrective control loop with a lag between taking action and observing its effect tends to overshoot and oscillate, and reacting faster to the delayed signal often makes the oscillation worse rather than better.
sources:
  - title: "Thinking in Systems: A Primer"
    resource: "Thinking in Systems: A Primer (Donella H. Meadows), ch. 2, ch. 4, ch. 6"
---

Any control loop that corrects a system toward a target — an autoscaler, a retry policy, a capacity-provisioning process — is a **balancing feedback loop**: it measures a discrepancy between actual and desired state, then acts on a flow to close the gap. When there is a **delay** between taking that corrective action and being able to observe its effect, the loop is structurally prone to overshoot its target and oscillate around it instead of settling.

## Why delay causes oscillation

A balancing loop with delay is composed of up to three separate lags, each of which can contribute:

- **Perception/measurement delay** — the time to average or confirm a signal before trusting it (e.g., smoothing noisy metrics over a window before triggering a scaling decision).
- **Response delay** — the time the corrective action takes to actually execute once decided (e.g., only correcting a fraction of the perceived gap per cycle, to avoid overreacting to noise).
- **Effect/propagation delay** — the time between an action being taken and its effect actually landing in the stock being controlled (e.g., new capacity coming online, a retried request completing).

While the controller is waiting for its last correction to take effect, the underlying state keeps changing — so the controller, still working from stale information, keeps correcting as if nothing had happened yet. By the time the correction lands, it can be too large, too small, or pointed the wrong direction relative to the *current* state, producing an overshoot. The loop then corrects the overshoot, overshoots again in the opposite direction, and rings down toward the target instead of approaching it smoothly. The general rule: **a delay in a balancing feedback loop makes the system likely to oscillate**, and the relationship between delay length and the rate of change the loop is trying to control determines whether the ringing damps out, sustains, or grows.

## The counterintuitive tuning implication

Because the instinct when a control loop is misbehaving is to "react faster," it's easy to tune in the wrong direction. Which fix actually helps depends on which failure mode is present:

- If the loop is **underreacting** to a real, sustained change (too slow to notice and correct), shortening its perception or response delay helps.
- If the loop is **overreacting** to noise or to its own not-yet-landed prior corrections, shortening the delay makes oscillation *worse* — the controller is already jumping the gun, and reacting faster only lets it jump the gun more often, with less time to observe whether the last correction was working before firing the next one. In that case, **lengthening** the response delay (waiting longer to confirm a trend, correcting only a fraction of the perceived gap per cycle, widening a smoothing window) damps the oscillation and lets the system settle.

Diagnosing which regime a given control loop is in — underreacting or overreacting — is a prerequisite for tuning it correctly; blindly tightening reaction time is a coin flip that can make things measurably worse.

## Application to capacity and load-management control loops

This is the general mechanism behind several concrete failure modes in this domain:

- [Autoscaling safety bounds](autoscaling-safety-bounds.md)'s guidance to react fast to load increases but cautiously to decreases is an asymmetric application of this principle: the up-direction is tuned to underreact-avoidance (a missed spike is costly), while the down-direction is deliberately damped to avoid oscillating capacity down and back up on noise.
- A [synchronized retry storm](synchronized-retry-storm.md) is a delayed-feedback oscillation at the population-of-clients scale: clients "correct" for a failure by retrying, but the correction (the retry) lands on a backend that hasn't yet recovered, producing an overshoot that triggers the next round of retries — jittered exponential backoff works by deliberately lengthening and desynchronizing the effective response delay.
- [Coordinated load management](coordinated-load-management.md)'s cross-system feedback loops are vulnerable to the same dynamic when autoscaling, load balancing, and load shedding each react to a delayed, partial view of the others' effect.
- At the longest timescale, physical capacity-provisioning lead time (hardware procurement, data-center buildout) is itself an effect delay large enough, relative to demand-change rates, to produce industry-wide overcapacity/undercapacity cycles — a structural reason [capacity headroom](capacity-headroom-safety-margin.md) needs to be sized against forecast uncertainty rather than assuming provisioning can simply track demand closely.
