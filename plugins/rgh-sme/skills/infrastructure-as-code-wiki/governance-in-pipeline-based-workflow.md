---
type: concept
title: Governance in a Pipeline-Based Workflow
description: How defining infrastructure as code and testing it continuously lets organizations replace up-front review gates with automated, shift-left compliance checks embedded in the delivery pipeline.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 20"
---

Governance — making sure infrastructure changes meet an organization's security, legal, architectural, and cost-control policies — doesn't have to mean a manual review gate for every change. [Defining infrastructure as code](define-everything-as-code.md) and testing it [continuously](progressive-testing-for-infrastructure.md) opens up ways to reshuffle who's involved and when: code that's already been designed, reviewed, and reused doesn't need a fresh design review every time it's applied again; people can review and decide against *working* code and example infrastructure rather than diagrams; and testing and reviewing consistently-built infrastructure early gives faster, more accurate feedback than reviewing it once, late, in production.

This enables **shift left**: instead of a heavyweight review just before production, governance specialists focus on building tools and tests that catch their concerns automatically, early, during implementation — a security team might provide scanning tools and write automated policy tests that run in every pipeline, rather than personally reviewing every change. Once these automated checks exist, someone without deep specialist expertise can make a change to sensitive infrastructure (networking, security policy) with reasonable confidence, because the specialist's judgment has effectively been encoded into the pipeline's tests; the specialist still reviews and approves the riskiest changes, but does so by reading code, test reports, and a live test instance rather than a document.

An **emergency change process** that's meaningfully faster than the normal one is itself a governance smell: any step that's safe to skip under emergency pressure was probably never actually necessary, and should be removed from the normal process too; any step that genuinely can't be skipped safely needs to be made efficient enough to always do, not routed around when convenient — having two different processes ("dual value streams") is itself an antipattern worth fixing.
