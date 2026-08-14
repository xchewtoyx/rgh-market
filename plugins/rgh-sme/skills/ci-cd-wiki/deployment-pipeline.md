---
type: concept
title: Deployment Pipeline
description: >
  An automated, end-to-end sequence of gated stages that takes every version-control
  commit from build through testing to production, providing fast, precise feedback
  and increasing confidence at each step.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 1, 5"
---

# Deployment Pipeline

The deployment pipeline is the automated manifestation of the software delivery
process: every commit to version control is a potential [release candidate](release-candidate.md),
and the pipeline orchestrates building, testing, provisioning, and deploying it
through a series of automated gates.

## Purpose

- **Feedback loop**: the pipeline's core purpose is to give developers and
  stakeholders rapid, precise feedback on the quality, compliance, performance,
  and stability of every change.
- **Fail fast**: see [fail-fast pipeline design](fail-fast-pipeline.md) — reject a
  build as early as possible so effort is not wasted running later, more
  expensive stages against code that is already broken.
- **Layered risk coverage**: see the [Swiss cheese testing
  model](swiss-cheese-testing-model.md) for how to decide what each stage
  should check — no single stage needs to catch every risk, as long as every
  risk is caught by some stage.

## Typical stage structure

1. **[Commit stage](commit-stage.md)** (< 5–10 min): compiles source, runs fast
   unit tests, runs static analysis, packages binaries, publishes to the
   [artifact repository](artifact-repository.md).
2. **Automated acceptance test gate** (< 1–2 hrs): provisions a clean QA
   environment, deploys the candidate binary, runs the automated acceptance
   suite against business requirements.
3. **Subsequent gates (parallel/on-demand)**: manual/exploratory testing gate,
   and a capacity/nonfunctional test gate (performance, load, security) run
   against a production-like environment.
4. **Release stage**: manually triggered (Continuous Delivery) or automatically
   triggered (Continuous Deployment) zero-downtime production deployment,
   followed by a [smoke test](smoke-test.md).

Each stage only runs once the previous stage has passed, and a failure at any
stage stops the candidate from progressing further — the same binary either
keeps advancing or is rejected; it is never patched mid-pipeline.

## Key pipeline practices

- Only build binaries once, in the commit stage — see
  [build once, deploy everywhere](build-once-deploy-everywhere.md).
- Use the exact same deployment mechanism for every environment (dev, test,
  staging, production) — see
  [repeatable deployment process](repeatable-deployment-process.md).
- Deploy to a clean copy of the target environment, provisioned automatically
  from scratch or reset to a known-good baseline, so environment state cannot
  bias the result — see [ephemeral test environments](ephemeral-test-environments.md).
- Smoke-test every deployment immediately after it lands.

## Metrics

- **Cycle time / lead time**: total duration from commit to production release
  — see [cycle time](cycle-time.md).
- Process time vs. queue time: how much of cycle time is actual execution
  versus waiting between stages.
- Build pass/failure rate per stage.
- Mean time to recovery (MTTR): time to restore the pipeline to green after a
  failure.
