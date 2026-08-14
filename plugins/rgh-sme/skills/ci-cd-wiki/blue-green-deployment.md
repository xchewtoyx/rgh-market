---
type: concept
title: Blue-Green Deployment
description: >
  Maintaining two identical production environments, deploying a new release
  to the idle one, verifying it, then switching live traffic to it — giving
  zero-downtime deploys and an instantaneous rollback path.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 10"
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd ed. (Nygard), ch. 13"
---

# Blue-Green Deployment

Two identical production environments exist at all times: **Blue** (currently
serving live traffic) and **Green** (idle). To release:

1. Deploy the new [release candidate](release-candidate.md) to Green.
2. Run automated [smoke tests](smoke-test.md) and verification against Green
   while it carries no live traffic.
3. Switch the router/load balancer from Blue to Green. Green becomes live;
   Blue becomes idle.

**Rollback** is the traffic switch in reverse — instantaneous, since Blue is
still running the previous known-good version and hasn't been torn down.

Trade-off: running two full production environments simultaneously costs
double the infrastructure during the switch window, and anything stateful
(especially the database) has to either be shared between Blue and Green or
handled via a compatible migration — see
[backward-compatible schema migration](backward-compatible-schema-migration.md)
when the schema changes but the database instance itself doesn't, or
[dual-write datastore migration](dual-write-datastore-migration.md) when the
whole stateful instance is being replaced. Compare with
[canary release](canary-release.md), which verifies a new version against a
fraction of real traffic instead of switching all traffic at once.
