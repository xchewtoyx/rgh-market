---
type: concept
title: Security Telemetry Visibility
description: >
  Displaying live attack telemetry where every engineer sees it, not just
  security specialists, turns abstract threat models into a felt reality
  that changes how people write code.
sources:
  - title: The DevOps Handbook
    resource:
      "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 22"
---

# Security Telemetry Visibility

[Security log design](security-log-design.md) is about capturing enough
to investigate an incident after the fact. This is a different use of the
same underlying signal: surfacing security telemetry — failed logins,
database syntax errors, SQL-injection attempts, abnormal process
terminations — as live, visible metrics alongside the ordinary
performance and reliability dashboards every engineer already watches,
rather than routing it exclusively to a security team's own tooling.

The reasoning is that most breaches sit undetected for a long time
precisely because no one outside a small specialist team is regularly
looking at the signal at all. Folding security telemetry into the same
visible infrastructure the whole engineering organization already uses
means an active attack is something the team notices as it happens, not
something discovered months later by an external party. Documented
examples of what to surface: application-level signals (failed vs.
successful login ratio as an early brute-force indicator, password and
credential-reset volume), and environment-level signals (security-group
and access-control changes, malformed-query rates, error-rate spikes on
public endpoints).

**The effect compounds with [shift-left security](shift-left-security.md):
seeing your own code under live attack changes how you write the next
line of it.** One documented case treated a database-syntax-error rate as
a zero-tolerance signal — such errors both enable and indicate injection
attempts — and put a running graph of attempted injections against
production in front of every developer. The reported effect was not just
faster detection: developers who could see their own code being probed in
real time started reasoning about attacker behavior while still writing
the code, which is the design-time payoff shift-left security is after,
produced here by visibility rather than by process.

This does not replace [security postmortems](security-postmortem.md) or
forensic-grade [audit logging](audit-log-design.md) — a live dashboard is
built for ambient awareness and fast anomaly recognition, not for the
retention depth or [nonrepudiation](nonrepudiation.md) guarantees an
investigation needs.
