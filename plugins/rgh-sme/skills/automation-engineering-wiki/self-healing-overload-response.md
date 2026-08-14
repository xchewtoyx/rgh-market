---
type: concept
title: Self-Healing Overload Response
description: >
  A system can automatically shed or throttle its own load to survive a
  spike without crashing, as long as it detects the overload itself rather
  than trusting a signal an attacker or a dependency could spoof.
sources:
  - title: "Building Secure and Reliable Systems"
    resource: "Building Secure and Reliable Systems (Google), ch. 8"
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Dekker), ch. 5"
---

# Self-Healing Overload Response

Overload handling is a concrete, common case of a self-healing pattern: a
component detects that it's approaching its own capacity and automatically
changes its own behavior to survive, without waiting for a human or an
external controller to intervene. Two mechanisms do this:

- **Load shedding** — return errors for excess requests instead of trying
  to serve everything and crashing. A component that crashes loses *all*
  of its capacity, not just the capacity for the requests that pushed it
  over; shedding trades a controlled, partial failure for an uncontrolled,
  total one. Deciding what to shed needs a policy driven by request
  priority and request cost, not shed-everything-equally.
- **Throttling** — delay responses (or delay accepting new requests)
  instead of rejecting them outright, reducing the rate the client
  receives service without an outright failure.

Both work best as **self-contained detection**: a server that determines
*for itself* that it can't serve some class of requests, rather than one
that waits for an external signal telling it to degrade. This matters
because an external signal is something an attacker (or a buggy upstream
dependency) can spoof or corrupt — self-detection means the automation's
self-preservation doesn't depend on trusting the same channel that might be
the thing attacking it.

At larger scale, these per-component decisions get coordinated by a central
policy service that translates business priorities into shedding/throttling
rules and distributes them to servers in near real time — but the
self-contained fallback stays in place underneath that coordination, so a
component doesn't lose its ability to protect itself if the central service
is unreachable.

Whatever triggers degradation, record it: the level of degradation a
component is running at is diagnostic information you need both during the
incident (to know remaining system capacity) and after it (to evaluate
whether the mechanism worked). This is the same instinct behind
[safeguards against runaway automation](safeguards-against-runaway-automation.md)
applied to self-protective behavior instead of destructive automation:
bound the damage, and make the bound visible while it's active.

Self-healing that relies on automatic process restart has a specific blind
spot worth designing around: a component that crashes and restarts cleanly
every few minutes produces no outage and pages nobody, which means the bug
causing it can recur indefinitely unnoticed. See [exception collection as
an automation health signal](exception-collection-as-automation-health-signal.md)
for the mechanism that keeps a self-healing restart from silently hiding a
recurring failure, and [crash-loop escalation
thresholds](crash-loop-escalation-threshold.md) for what stops the same
restart mechanism from looping forever on a process that can never actually
recover. A related but distinct blind spot applies to gradual, continuous
self-correction rather than discrete restarts — see [silent correction
masking a growing failure](silent-correction-masks-growing-failure.md).

Load shedding and throttling are narrow, tactical instances of a broader
design goal: resilience engineering frames genuine resilience as a
*capability*, not a static property, made of four distinct abilities a
self-healing system (or the team operating it) needs — recognizing when it
is approaching the boundary of safe operation, steering back from that
boundary in a controlled way before crossing it, recovering from an actual
loss of control if it does cross, and detecting when its own margins are
being quietly eroded over time in the first place. Load shedding and
throttling only cover the second of these (steering back); the fourth
(detecting eroding margin) is exactly what the recording-and-visibility
practice above is for, and is the harder one to get right, since a margin
being spent gracefully looks identical to a healthy system until the
moment it runs out — see [normalization of deviance via
decrementalism](normalization-of-deviance-via-decrementalism.md) for how
that erosion typically happens unnoticed. Removing a live instance from service safely — before
restarting, replacing, or scaling it down — also depends on [lame-duck mode
draining](lame-duck-mode-draining.md) so self-healing doesn't drop
in-flight requests as a side effect of protecting the rest of the fleet.
