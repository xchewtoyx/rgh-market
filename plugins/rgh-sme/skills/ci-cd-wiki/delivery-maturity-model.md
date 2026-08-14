---
type: concept
title: Continuous Delivery Maturity Model
description: >
  A five-dimension assessment framework — build/CI, environment/deployment,
  testing, data, and release management — for locating which part of a
  delivery pipeline is least mature and most worth investing in next.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 15"
---

# Continuous Delivery Maturity Model

A structured way to diagnose where a delivery pipeline is weakest, rather than
improving whichever part happens to be most visible. Each dimension
progresses from ad hoc/manual toward fully automated:

1. **Build management & CI**: manual local builds -> single-command automated
   builds -> automated commit-stage test suite ->
   [trunk-based development](trunk-based-development.md).
2. **Environment & deployment management**: manual server tweaks -> fully
   automated infrastructure provisioning ->
   [idempotent provisioning](idempotent-provisioning.md) -> zero-downtime
   releases.
3. **Testing strategy**: manual regression testing -> automated unit,
   component, [acceptance](automated-acceptance-testing.md), and
   [nonfunctional](nonfunctional-test-gate.md) testing integrated into the
   pipeline.
4. **Data management**: manual SQL changes ->
   [version-controlled migrations](database-migration-scripts.md) ->
   automated schema rollback -> sanitized, automated test data generation.
5. **Release management**: high-risk manual release runbooks -> automated
   push-button deployment -> [continuous deployment](continuous-deployment.md).

Because each dimension is independent, a team can be advanced in one (e.g.
build/CI) and still ad hoc in another (e.g. data management) — the model's
value is surfacing exactly that kind of imbalance, since the pipeline's
overall risk and [cycle time](cycle-time.md) are usually dominated by
whichever dimension lags furthest behind, not by the average maturity across
all five.

Treat this staged framing as a diagnostic tool, not a destination — see
[capability model vs. maturity model](capability-model-vs-maturity-model.md)
for why "reaching the top level" is the wrong goal to optimize for.
