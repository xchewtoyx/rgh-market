---
type: concept
title: Failure Scenario Mapping
description: A structured workshop technique for brainstorming plausible infrastructure failure scenarios and planning mitigations for each of their causes, failure mode, detection, and correction.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 21"
---

Since failures are inevitable even with strong prevention, teams benefit from deliberately mapping out plausible failure scenarios and planning for each one, rather than discovering their gaps only when a failure actually occurs. A team runs a workshop to brainstorm scenarios, rates each by likelihood and potential impact, and works through four questions for each:

- **Causes and prevention** — what situations lead to this failure, and what reduces their likelihood? (A server running out of disk space under a usage spike might be addressed by right-sizing based on usage analysis, by predictive alerting, or eventually by automatically expanding capacity as usage grows.)
- **Failure mode** — what actually happens when the failure occurs, and can the consequence be reduced without a human needing to intervene? Teams often don't actually know the answer until they investigate; ideally the system stays operational in a degraded way (a load balancer stops sending traffic to an unresponsive instance) rather than failing destructively.
- **Detection** — how will you know the failure has happened, and can you detect it earlier — ideally before it fully manifests, rather than after a customer notices?
- **Correction** — what has to happen to recover? In the best case this is fully automatic (destroy and rebuild an unresponsive instance, per [continuous disaster recovery](continuous-disaster-recovery.md)); if a system does self-correct automatically, it's worth also asking why the failure happened at all, so a recurring root cause doesn't hide behind a well-functioning auto-heal.

The resulting mitigations become an explicit, prioritized backlog rather than an unbounded, unrealistic goal of handling every conceivable failure gracefully — few teams have the resources to build even half of an idealized resilience wishlist, so ranking by likelihood, impact, and cost to implement matters. Any planned mitigation should eventually be backed by an automated check that actually exercises the scenario — in a [pipeline stage](infrastructure-delivery-pipeline.md) or as a chaos experiment — rather than being trusted on the strength of the design alone. Failure planning is continuous: any incident, including ones in development or test environments, is a prompt to ask whether it represents a new scenario worth adding to the map. For a specific high-stakes change already planned rather than the system's standing failure surface, see [premortem for infrastructure changes](premortem-for-infrastructure-changes.md) — a narrower, faster technique aimed squarely at the overconfidence a team develops in a plan it just finished building.
