---
type: concept
title: Four Key Delivery and Stability Metrics
description: The DORA Accelerate research's four metrics — lead time, deployment frequency, change fail percentage, and MTTR — used to measure and compare software delivery and operational performance.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 1"
---

DORA's *Accelerate* research identifies four metrics with the strongest correlation to how well an organization meets its goals:

- **Delivery lead time** — elapsed time to implement, test, and deliver a change to production.
- **Deployment frequency** — how often changes are deployed to production.
- **Change fail percentage** — the proportion of changes that cause an impaired service or require a rollback or emergency fix.
- **Mean Time to Restore (MTTR)** — how long it takes to restore service after an unplanned outage or impairment.

Organizations that score well against organizational goals (revenue, share price, or similar) also tend to score well on these four metrics, and vice versa — high performers are good at both speed (lead time, deployment frequency) and stability (change fail percentage, MTTR) simultaneously, contradicting the assumption that they trade off against each other. See [optimizing infrastructure for continuous change](optimizing-infrastructure-for-continuous-change.md) for why this matters for infrastructure design and governance.

The metrics give teams a basis for defining their own [SLIs, SLOs, and SLAs for their infrastructure delivery workflow](team-workflow-effectiveness.md), and for evaluating whether a design decision (such as how to [modularize infrastructure](infrastructure-component-coupling-and-cohesion.md) or [structure a delivery pipeline](infrastructure-delivery-pipeline.md)) is actually helping rather than just moving work around.
