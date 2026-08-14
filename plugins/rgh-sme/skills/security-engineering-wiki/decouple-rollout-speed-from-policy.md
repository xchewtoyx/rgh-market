---
type: concept
title: Decouple Rollout Speed from Policy
description: >
  Build update mechanisms as fast as you could ever need, then constrain
  them with rate policy — so the emergency push system is just the normal
  push system turned up to maximum.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 9"
---

# Decouple Rollout Speed from Policy

To [recover](design-for-recovery.md) from any class of error you must be
able to change system state. Design every update mechanism (software or
firmware rollout, config change management, batch scheduling) to operate
as fast as you can imagine ever needing — then add controls constraining
the rate of change to match current risk policy. Separating the *action
and content* of a change from its *timing and rate* pays off because:

- **Policies change**; a rollout system designed around this month's
  policy needs painful refactoring when the policy does.
- **Risk calculus changes mid-rollout**: a leisurely internal patch
  becomes urgent the moment the vulnerability is public and exploited in
  the wild ([changing landscape](design-for-changing-landscape.md)).
- **Emergencies need a practiced path.** Untested emergency practices
  won't work when needed. If emergency push = regular push with raised
  rate limits, you exercise the emergency system on every normal release,
  maintain one system instead of two, and rollback and rollout share the
  same machinery. Corollary: if a low-dependency methodology works in
  emergencies, make it your standard methodology.

**Isolate the rate limiter.** Build rate limiting as an independent,
single-purpose, rigorously testable microservice that issues short-lived
cryptographic tokens approving each change — the same
[trust segmentation](trust-segmentation.md) pattern as config signing. It
doubles as the audit-log collection point for changes, and its existence
discourages redundant ad hoc rate-limiting code (a smell of unsafe
design).

Case study: Google's fleet OS management evolved from a monthly "golden
image" (policy baked into tooling) to per-package release units over a
clean API, decoupling rollout rate, config store, and rollout actuator.
Result: different velocities per package, test machines on latest builds,
stable fleet-wide defaults — and emergency releases became "adjust some
rate limits and approve," not a separate system. Simpler, more useful,
safer.
