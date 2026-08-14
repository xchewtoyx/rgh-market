---
type: concept
title: Emergency Response Triage
description: The principle of prioritizing rapid user-service mitigation over long-term root-cause diagnosis during an active incident.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 13"
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook (Gene Kim, Jez Humble, Patrick Debois, John Willis, Nicole Forsgren), ch. 19"
  - title: "The Site Reliability Workbook"
    resource:
      "The Site Reliability Workbook: Practical Ways to Implement SRE (Betsy
      Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen
      Thorne), Appendix C"
---

During an active outage, the primary objective is **triage first**—restoring user service as quickly as possible. Investigators must not delay mitigation to diagnose the underlying code bugs or root causes.

Tactical mitigation strategies include:
* **Traffic Shedding / Load Dropping**: Dropping low-priority requests or background features to preserve core user workflows.
* **Graceful Degradation / Fallbacks / Feature Removal**: Falling back to static or cached content, or dropping slow features rather than degrading the entire page (e.g., Netflix showing non-personalized video lists during traffic surges).
* **Traffic Redirection / Failover**: Routing traffic away from degraded systems to healthy regions.
* **Rollbacks**: Reverting recent deployments or configuration changes — a high-value first check, since analysis of thousands of postmortems found binary pushes and configuration pushes together responsible for roughly two-thirds of outage triggers.
* **Continuous Fault Injection**: Running tools like Chaos Monkey to constantly and randomly kill production servers during normal hours, forcing services to automatically recover and making failure mitigation routine.
* **Fail Fast**: Enforcing aggressive timeouts and **circuit breakers** to prevent failing components from cascading and stalling the whole system.

First responders execute these steps using pre-written runbooks to minimize cognitive load. Mitigation strategies and crisis communication are structured via the [incident command system](incident-command-system.md), and practiced in [preparedness drills](preparedness-drills.md).

### Mitigate on a possible cause, not a confirmed one

The recommended incident sequence is: assess impact, mitigate impact,
find root cause, then fix and hold a postmortem — in that order. Generic
mitigations (rolling back to a known-good state, redirecting load away from
a suspect component) should be applied as soon as a *possible* cause or
location is known, well before the team has full root-cause understanding.
Waiting for certainty before mitigating prolongs user pain for no benefit —
prioritizing mitigation over full diagnosis is the core discipline here, not
an exception to it. This is easiest to execute quickly if mitigation tooling
(rollback tools, traffic-redirection controls) is built and pre-staged
*before* an incident happens, informed by what previous
[blameless postmortems](blameless-postmortems.md) revealed was missing.
