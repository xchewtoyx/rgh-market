---
type: concept
title: Operational Responsibility Transition
description: Safely transferring operational ownership of systems between product and operations teams to avoid communication gaps and operational degradation.
sources:
  - title: "Site Reliability Workbook"
    resource: "Site Reliability Workbook (Beyer et al.), ch. 18, 20"
---

Transferring operational responsibility for a system—whether during the initial handoff to a new operations team or when ending an engagement—is a high-risk transition. If managed poorly, it can result in a loss of tacit knowledge, silent technical debt accumulation, and critical communication breakdowns.

## Core Transition Guidelines

To mitigate these risks, organizations follow structured guidelines when shifting system ownership:

### 1. Phased Engagement and Slow Handover
- **No Day-One Handovers**: When a new team is tasked with taking over a service, they must not assume full operational responsibility immediately. The product development team must retain primary support during the initial phase.
- **Design-Stage Collaboration**: Operations teams should engage as early as the design and architecture phases, rather than receiving the system as a finished product.
- **Slow On-Call Cuts**: When splitting or shifting on-call rotations, transition responsibilities slowly. Maintain dual support or keep members on-call for prior systems during a 3-to-6-month transition period to build familiarity.

### 2. Guardrails for Team Capacity
- **Limit Trainee Ratios**: When a team is taking over new systems while onboarding members, cap new hires at under a third of the team. This ensures that training responsibilities do not overwhelm the veterans and degrade the team's operational capability.
- **Engage Incrementally**: When onboarding a large project with multiple microservices, the receiving team should take over exactly one service first. Expand scope only after that service's operations have stabilized.

### 3. Maintaining Alignment Post-Handoff
- **Retain Development Toeholds**: Even after a successful handoff, developers should retain a small, permanent operational footprint (e.g., placing one developer in the on-call rotation). This keeps the development team grounded in the system's operational realities.
- **Name and Reset Tensions**: If a shared support model causes a communication breakdown (e.g., SREs managing a legacy system while developers focus exclusively on the rewrite), teams must be willing to reset. This can involve temporarily returning the system to development via the [Service Handback Mechanism](service-handback-mechanism.md) or merging functions into a single team to align priorities.

For the structured training curriculum needed to prepare teams for this transition, see [On-Call Onboarding and Training](on-call-onboarding-and-training.md).

This structured process addresses handing a *live* system between teams; a different, quieter failure mode occurs when there was never a formal transition at all because a system's survival depended on one individual's personal advocacy — see [Champion-Dependent Projects](champion-dependent-projects.md).
