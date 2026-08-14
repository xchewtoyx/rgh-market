---
type: concept
title: Graceful Degradation
description: >
  Deliberately designing which features to disable or throttle under
  overload or failure, so the system breaks at chosen breakpoints instead
  of collapsing where it happens to be weakest.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 8"
  - title: Site Reliability Engineering
    resource:
      "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 21"
---

# Graceful Degradation

When load exceeds capacity — from failures shrinking the resource pool, a
traffic spike, misconfiguration, or a [DoS attack](dos-defense-in-depth.md)
— response degrades and can collapse entirely. Unplanned, the break happens
where the system is *weakest*, not where it's safest. Controlled
degradation chooses in advance which properties to disable or adjust,
giving the system deliberate breakpoints instead of chaotic collapse, and
buying incident responders time. Make the hard choices before the
incident, not under pressure during it.

Mechanisms:

- **Disable low-value/high-cost features** to free resources for critical
  ones (e.g. drop RSA support and serve only cheaper ECC when
  resource-constrained; Gmail's simple-HTML mode). This requires knowing
  each feature's criticality, cost, and interdependencies — and ranking
  *security functions* among the critical ones (a region's network
  security monitoring may outrank even degraded user features).
- **Fail early and cheaply.** Measure where in each operation cost is
  incurred, then move error checks ahead of expensive work: validate
  access before allocating memory or doing I/O; SYN cookies avoid
  allocating memory for spoofed TCP connections; CAPTCHAs shield the most
  expensive operations from automated abuse. Aggressive client retries
  multiply the cost of late failure into cascading failure.
- **Load shedding** — serve errors for excess requests rather than crash
  (a crash loses *all* capacity and shifts load elsewhere, cascading).
  Requires notions of request priority (security-critical functions rank
  high) and request cost comparable to utilization measures. A concrete
  implementation: sort incoming requests into a small number of fixed
  priority tiers (e.g. critical production traffic down to sheddable
  batch work) and drop the lowest tiers first under overload; pair this
  with propagating each request's remaining deadline so a server can
  drop a request outright once it has no time left to be useful instead
  of processing it anyway, and prefer serving newest-first when queued
  past capacity, since older queued requests are the ones most likely to
  already be past their caller's deadline.
- **Throttling** — delay processing or responses to slow client request
  rates, targeted at offending clients or applied generally.
- **Lame-duck mode** — a server that detects declining health keeps
  serving but signals callers to back off, giving the environment signal
  to adapt rather than silently burning resources on errors.

**Degraded UX**: tell users what's broken, keep functional parts usable,
communicate staleness and risk, and *explicitly disable features no longer
safe to use*. Anti-pattern: a GUI frozen because one backend RPC timed
out, or a mobile app that can't even show cached content without
connectivity — which also turns backend reachability into a critical
dependency with a client-rollout-speed recovery time. Avoid putting
critical failure points in components you can't update quickly.

**Automate, responsibly.** Automation reacts faster than humans and juggles
more variables, so preprogram safe response measures (central policy
services can translate business priorities into shedding/throttling
policies distributed in near real time). Prefer *self-contained* failure
detection — don't let external signals an attacker could simulate force
your fleet into shedding. But keep a human foothold:

- Automation must never disable the services employees need to recover the
  infrastructure — emergency access must survive even DoS (a SYN flood
  must not prevent a responder's SSH session); maintain and continuously
  validate low-dependency alternatives
  ([component reliability tiers](component-reliability-tiers.md)).
- Cap unsupervised automated action with **change budgets**: no automatic
  change of large magnitude (one server shedding *all* RPCs) or scope
  (*all* servers shedding some RPC) — when the budget is exhausted, a
  human must extend it or decide otherwise.

**Security tradeoff**: security-critical operations must not fail open, or
an attacker could degrade your security with a DoS alone (see
[fail safe versus fail secure](fail-safe-vs-fail-secure.md)). Decide
explicitly how much added risk degradation may carry — is login without
2FA acceptable during a 2FA outage, or does the bank prefer full outage to
unauthorized access? Degradation *can* still apply to security controls if
the fallback is a *stronger* cheaper control — then attacking the regular
control becomes counterproductive.

Record and report actual degradation levels (self-imposed or directed):
you need them to judge remaining capacity, user impact, bugs versus
attacks, and — afterwards — whether the mechanisms worked. Validate the
whole apparatus regularly via
[continuous validation](continuous-validation.md).
