---
type: concept
title: Component Reliability Tiers
description: >
  High-capacity, high-availability, and low-dependency versions of
  critical components trade features and freshness for survivability, with
  failover rules that must not let an attacker push you to a weaker
  option.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 8"
---

# Component Reliability Tiers

When [failure domains](failure-domains.md) aren't enough — a root cause
can still fail every copy — resilience comes from alternative components
with *different* reliability and security properties:

- **High-capacity**: the normal serving fleet; absorbs user spikes and DoS
  traffic until mitigation or [degradation](graceful-degradation.md) kicks
  in. Invest in capacity planning and rollout hygiene here first.
- **High-availability**: copies with provably lower outage probability —
  fewer dependencies (local cached data instead of a remote database) and
  a limited rate of change (older code and configs, dodging recent bugs).
  Low operational overhead, but resource costs scale with fleet size;
  serving the full user base vs. a fraction is a cost/benefit call.
- **Low-dependency**: an alternative implementation whose *entire*
  dependency chain is minimal — often meaning fewer features and a
  simplified serving stack (the layered platforms that make high-capacity
  scaling easy also stack up error budgets). Expensive and rarely used;
  justified when high-availability failure is unacceptable. Redundancy
  succeeds in inverse proportion to the probability of a shared root
  cause, so the alternative must not share failure domains with the
  primary. Examples: a home security system with a local server
  implementing the same APIs (local log writes, cached emergency numbers,
  landline backup); a minimal alternative production network sharing no
  links, switches, routers, or SDN software with the main one, supporting
  only the most critical features at a fraction of bandwidth.

**Failover control.** Systems needing different reliability behaviors
should use *distinct sets of interchangeable backends* selected by
explicit logic (flags) — not an RPC parameter asking a high-availability
backend to please act low-dependency (if the runtime dependency is also a
startup dependency, you're one restart from disaster). Tune separate
shedding/throttling policies for the alternative's smaller capacity, and
make failback disableable.

**Pitfalls**:

- Quietly relying on the alternative for normal operation — dependents
  then overload it during a real outage, turning your backup into a DoS.
- The opposite: never using it, so it rots and surprises you when needed.
  Exercise emergency components in normal workflows
  ([continuous validation](continuous-validation.md)).
- Unchecked growth of dependencies and resource needs, eroding the tier's
  defining property; monitor intended operating constraints continuously.
- **Security regressions on failover**: failover must not compromise
  integrity or security. Attackers can exploit differences between
  redundant paths by pushing you toward the weaker option — whereas if
  the low-dependency alternative has *stronger* security, wearing down
  your system becomes a disincentive. Judgment calls are situational: an
  intentionally six-week-stale high-availability service needing an
  urgent security fix; storing private keys locally to remove a
  key-service startup dependency (acceptable with faster
  [rotation](credential-rotation.md)?); slowing updates of ACLs/CRLs to
  save resources versus giving attacker changes longer to persist.
- **Wrong-time autorecovery**: if automation throttled, automation may
  unthrottle; but never let automation override a *manual* failover — the
  drained system may be quarantined for a security vulnerability or held
  down to stop a cascading failure.
