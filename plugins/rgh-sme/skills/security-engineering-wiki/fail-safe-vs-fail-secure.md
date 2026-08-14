---
type: concept
title: Fail Safe Versus Fail Secure
description: >
  Reliability wants failure to leave the system open and operable; security
  wants failure to leave it closed to an adversary — the same failure mode
  demands opposite defaults depending on who might exploit it.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), chs. 1, 8"
  - title: Software Architecture in Practice, 4th Edition
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), chs. 10, 11"
---

# Fail Safe Versus Fail Secure

Absent an adversary, systems are designed to fail *safe* (open): an
electronic door lock releases on power failure so people can exit safely.
But fail-open behaviour is an obvious vulnerability to an adversary who
can *cause* the failure — cutting power becomes an unlock. Defending
against that means designing the door to fail *secure* (closed) when
unpowered.

There is no universally right default. The choice per failure mode is a
question about the [presence of an
adversary](security-reliability-intersection.md): who is harmed if this
fails open, and who benefits? Safety-of-life pushes toward open;
confidentiality and integrity push toward closed. Many real designs mix
both: the lock fails secure but accepts a physical key.

The software statement of the dilemma: if ACLs fail to load, a system
optimized for availability assumes "allow all" and keeps serving; a system
optimized for security assumes "deny all" and locks down, because a system
that cannot verify its own integrity — whether a failed disk ate the
config or an attacker changed it — can't be trusted to operate. (ACL-based
systems must fail closed, with access explicitly granted by entries.)

**Resolving the tension**: first determine your minimal nonnegotiable
security posture, then engineer the *reliability of the security services
themselves* so that posture survives failure — e.g. tag security-oriented
RPC traffic with special QoS so it isn't dropped with low-priority
packets, and shield security RPC servers from CPU starvation by workload
schedulers. Security-critical operations must not fail open, or an
attacker can degrade your security using a DoS alone; if they must
degrade, degrade to a *stronger* cheaper control (see
[graceful degradation](graceful-degradation.md)).

**The redundancy corollary**: that physical-key override, like a fire
escape, is redundancy — and redundancy that increases reliability also
increases attack surface. Each redundant path is another way in, and the
adversary needs a vulnerability in only *one* path. Every fallback,
override, and emergency mechanism added for reliability (including
[breakglass](breakglass.md) access) must be threat-modelled as an attack
surface in its own right, not exempted as "the emergency path."

The same tension appears at system scale in
[degrading gracefully under attack](dos-defense-in-depth.md) and in
deciding how an [authorization system behaves when it is itself
broken](breakglass.md).

**The kinship with safety engineering is structural, not just analogical.**
A safety "barrier" tactic (e.g. a firewall stopping a fault from
propagating between subsystems) is the same mechanism as a security
[compartment](compartmentalization.md) boundary — both block spread, one
of accidental failure, one of adversarial action, and the same boundary
often needs to do both jobs at once. Safety-critical engineering also
grades required assurance effort by failure severity (e.g. avionics'
Design Assurance Levels, DO-178C) — the same "spend proportionate to risk"
logic as [access classification by risk](access-classification-by-risk.md),
applied to how much validation a component needs rather than how much
access it gets.
