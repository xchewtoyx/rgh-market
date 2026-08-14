---
type: concept
title: Production Readiness Review
description: A structured framework to audit and improve service architecture and operational readiness before launching or handing over a service.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Beyer et al.), ch. 32"
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 7"
---

The Production Readiness Review (PRR) is a key mechanism for operational handover. It is used to ensure a service meets reliability standards before it is launched or transitioned to a dedicated support team (e.g., Site Reliability Engineering).

## The PRR Lifecycle

The PRR framework consists of four sequential stages:

1. **Engagement**: The development team requests a PRR engagement prior to a major launch or handoff.
2. **Analysis**: SRE/Operations audits the system architecture against established reliability standards. This audit covers critical areas such as:
   - Monitoring and telemetry
   - Service Level Objectives (SLOs) and error budgets
   - Capacity planning
   - Backup and restore procedures
   - Failover and disaster recovery mechanisms
   - Dependencies: a full dependency diagram, plus evidence that rate limits with each dependency have actually been negotiated and acknowledged, not just assumed
   - Oncall readiness: a schedule already staffed months ahead, and an estimated per-shift alert volume kept under a set threshold
   - Documentation completeness: a full playbook reviewed by an assigned reviewer, and an open-documentation-bug count kept under a threshold rather than merely "some docs exist"
   - Business sign-offs: security, privacy, and (where relevant) marketing/legal approval, tracked as explicit gates alongside the technical ones
3. **Improvements & Refactoring**: The development team addresses and refactors any deficiencies or risks identified during the audit stage.
4. **Onboarding**: The operations team signs off on the production launch or officially accepts on-call responsibilities.

For services undergoing initial customer launch versus long-term operational handoff, see [Launch vs. Handoff Readiness Reviews](launch-vs-handoff-readiness-reviews.md). When a service's operational health degrades post-onboarding, a [Service Handback Mechanism](service-handback-mechanism.md) can be used to return responsibility to development.
