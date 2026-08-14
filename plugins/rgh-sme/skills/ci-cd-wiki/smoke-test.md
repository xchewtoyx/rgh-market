---
type: concept
title: Smoke Test
description: >
  A fast, automated post-deployment check — application starts, core services
  respond, database connectivity works — run immediately after any deployment
  to confirm the deploy itself succeeded before trusting further testing or traffic.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 5"
---

# Smoke Test

A smoke test answers one narrow question: did the deployment work at all? It
checks application startup, core service availability, and database
connectivity — not business correctness. Every stage of the
[deployment pipeline](deployment-pipeline.md) that deploys a build (to a QA
environment, a UAT environment, or production) should run a smoke test
immediately afterward, before running the stage's actual test suite or
routing real traffic to it.

This exists because deployment itself is a step that can fail independently
of the software being deployed — bad configuration injection, an unreachable
dependency, insufficient resources. Without a smoke test, a slow or flaky
result from the acceptance suite could actually be masking a broken
deployment rather than a genuine application defect, wasting time diagnosing
the wrong layer.
