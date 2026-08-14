---
type: concept
title: Actionable Alert Philosophy
description: >
  Alerts should correspond to real, urgent, user-impacting problems that a
  human can actually act on, with severity tiered by how urgently a human
  needs to respond, and the whole alert corpus needs ongoing curation.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 1"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 8"
  - title: "Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations"
    resource: "Accelerate (Forsgren, Humble, Kim), ch. 13"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 10"
---

Three precepts underpin sustainable alerting: alerts should correspond to
real, urgent problems, since human attention is a scarce, easily-exhausted
resource prone to pager fatigue and [burnout](sustainable-on-call-and-burnout.md); every alert received should be something a human can actually act
on; and multiple kinds of alerts can coexist in one corpus, but that corpus
needs intentional, ongoing curation — it doesn't stay healthy on its own.

A standard three-way severity split, tied to how urgently a response is
needed:

- **Pages** — require immediate human intervention because of active or
  imminent user impact.
- **Tickets** — require human action within hours or days; no active user
  outage.
- **Logs/dashboards** — diagnostic information retained for historical
  review and post-hoc troubleshooting, not routed to a person at all.

For example, during a denial-of-service (DoS) attack or sudden traffic spike, a team should not page on the mere presence of attack traffic if the system's automated defenses are successfully absorbing or mitigating it. An alert is only warranted if demand actually exceeds capacity or if a critical resource (such as egress link bandwidth) is saturated, causing user-visible degradation.

Grounding this severity split in real user impact — rather than in whatever
internal signal happens to be easy to alert on — is what
[user-centric SLI selection](user-centric-sli-selection.md) is for, advocating
for [symptom-based alerting](symptom-based-alerting.md) rather than paging
on internal system causes. This is the property
[why simple threshold alerting fails](why-simple-threshold-alerting-fails.md)
identifies as the recurring failure of alerting built on internal proxies
instead. [Multiwindow multi-burn-rate alerting](multiwindow-multi-burn-rate-alerting.md)
is the concrete mechanism that best satisfies "real, urgent, actionable" at
scale, by tying severity directly to how fast the error budget is actually
burning rather than to an arbitrary internal metric threshold.

## Proactive Alerting vs. Reactive Notifications

Sustainable operational practices require that alerting be proactive (system-driven) rather than reactive (customer-driven). Psychometric research validates this distinction:
*   **Reactive notifications** (relying on customer complaints or manual Operations Center calls) do not predict software delivery performance.
*   **Proactive system notifications** (relying on automated monitoring, telemetry, and early warning thresholds) directly predict higher delivery performance and organizational outcomes.

Because individual telemetry signals (such as CPU utilization or network latency) are imperfect proxies for underlying system health, relying on a single metric creates vulnerability to instrument failure or false signals. A robust alerting philosophy leverages multiple correlated signals (or structured SLIs/SLOs) to construct a reliable, multi-dimensional view of service health before failures impact users.
