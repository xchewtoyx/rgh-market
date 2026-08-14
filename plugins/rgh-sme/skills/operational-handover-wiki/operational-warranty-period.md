---
type: concept
title: Operational Warranty Period
description: Requiring development teams to support a new service in production for a set period before handoff to ensure operational stability.
sources:
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook (Kim et al.), ch. 16"
---

To prevent the "throw it over the wall" anti-pattern, where newly written features or services are immediately handed over to an operations team that has no context on the codebase, organizations implement an **Operational Warranty Period**.

## Definition of Done and Warranty

An operational warranty period is a predefined timeframe (ranging from two weeks to six months depending on system complexity) during which the development team retains full operational responsibility for a new service in production.
- **Warranty Rule**: A service is not considered complete (or "done" in Agile terms) simply because it was deployed. It is only "done" when it runs reliably in production without excessive interventions, manual workarounds, or page volume for the duration of the warranty.
- **Shared Pager Duty**: During the warranty period, developers, development managers, and system architects share or own the on-call pager rotation. Waking up the engineers who wrote the code at 2:00 AM for production failures ensures that bugs and defects are prioritized and fixed immediately.

## Key Benefits

- **Immediate Feedback Loop**: Developers observe real-world performance, edge cases, and non-functional gaps (like deployment friction or poor error messages) in the production environment.
- **Calibrated Operational Cost**: It forces development teams to pay down technical debt before handing over the service, ensuring the receiving operations team is not burdened with a fragile system.

For details on the formal gating processes that occur before and after the warranty period, see [Launch vs. Handoff Readiness Reviews](launch-vs-handoff-readiness-reviews.md) and [Production Readiness Review](production-readiness-review.md).
