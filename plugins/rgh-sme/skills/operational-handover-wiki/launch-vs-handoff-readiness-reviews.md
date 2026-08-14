---
type: concept
title: Launch vs. Handoff Readiness Reviews
description: Comparing self-managed launch readiness reviews with the more stringent handoff readiness reviews used when transferring service management to operations.
sources:
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook (Kim et al.), ch. 16"
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 7"
---

When introducing new services or transitioning their operational ownership, organizations separate the initial product launch from the official handoff to dedicated operations or SRE teams. This is managed through two distinct gating processes:

## Launch Readiness Review (LRR)

An LRR is completed before a new service goes live to customers. 
- **Ownership**: Typically self-reported and executed by the product development team.
- **Goal**: Verifies that the service is functional, has basic monitoring, and does not pose immediate risks to customers.
- **Engagement**: SRE or Operations engineers act in a consulting role to help teams prepare.

## Handoff Readiness Review (HRR)

An HRR is performed when transitioning the service from a developer-managed state to an SRE- or Operations-managed state. This usually occurs at least six months after the initial launch, once the service has proven its baseline stability under real traffic.
- **Ownership**: Conducted by the receiving Operations or SRE team.
- **Goal**: Evaluates the service against much more stringent operational standards, including:
  - Pager alert frequency and signal-to-noise ratios
  - Loose architectural coupling and deployment predictability
  - Production hygiene (e.g., access controls, secret rotation)
  - Regulatory and compliance exposure (e.g., SOX, PCI-DSS, HIPAA) — see [Compliance in Spirit vs. Ceremonial Documentation](compliance-in-spirit-vs-ceremonial-documentation.md) for satisfying these without duplicating documentation effort

## Key Success Factors

- **Organizational Memory**: The checklists used during LRRs and HRRs function as a repository of historical postmortem lessons, preventing teams from repeating past launch failures.
- **Early Engagement**: The most successful handovers occur when development teams engage operations engineers early in the service design phase rather than treating handoff as a late-stage box-ticking exercise.
- **Single Named Owner**: A checklist this long is easy to let stall as "everyone's job, so no one's." Naming one launch lead — who works the checklist, delegates individual items, files gap tickets, and tracks everything through to sign-off — is what actually gets a long readiness checklist completed, rather than each item quietly waiting on whichever team happens to notice it.

For transitioning services back to development if they fail to maintain these standards over time, see [Service Handback Mechanism](service-handback-mechanism.md). For the mirror-image process at the other end of a service's life, see [Service Decommissioning Checklist](service-decommissioning-checklist.md).
