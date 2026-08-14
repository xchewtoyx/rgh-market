---
type: concept
title: Commit Stage
description: >
  The first, fastest stage of the deployment pipeline, triggered by every
  version-control commit, that compiles, runs fast unit tests, performs static
  analysis, and packages a binary artifact within minutes.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 3, 5, 7"
---

# Commit Stage

The commit stage is the entry point of the [deployment pipeline](deployment-pipeline.md):
it runs automatically on every commit and is the automation behind
[continuous integration](continuous-integration.md)'s "single command build."

## What it does

- Compiles the source code.
- Runs the fast unit-test suite.
- Runs static code analysis (linting, style checks).
- Packages the binary artifact and publishes it to the
  [artifact repository](artifact-repository.md), per
  [build once, deploy everywhere](build-once-deploy-everywhere.md).

## Speed target

Under 5–10 minutes. This is the tightest feedback loop in the pipeline, so its
speed budget is the strictest — everything in it must be fast enough that
developers wait for the result rather than context-switching away, which is
what keeps [fixing a broken build immediately](continuous-integration.md)
practical.

## Test suite design

The commit test suite (the tests that actually run in this stage) has its own
design discipline — see
[commit test suite design principles](commit-test-suite-design.md). A stage
that runs enough tests and static inspections to catch the bulk of routine
defects, while staying inside the speed budget, is doing its job; a stage that
either runs too little to catch real bugs or too much to stay fast has failed
at the core trade-off the commit stage exists to strike.

## Deliverables

A successful run produces: a versioned binary artifact stamped with a
build/commit ID and published to the
[artifact repository](artifact-repository.md); test, coverage, and
static-analysis reports; verification that database migration scripts at
least compile against a clean local database; and a trigger that
automatically starts the downstream acceptance test stage.

## Enforcement mechanism

Some teams enforce "never push on a broken build" structurally rather than
relying on discipline alone — see
[pre-tested commit](pre-tested-commit.md).

## Downstream relationship

Only a commit-stage pass produces a [release candidate](release-candidate.md)
eligible to proceed to the acceptance test gate and beyond. A commit-stage
failure stops the pipeline immediately — see
[fail-fast pipeline design](fail-fast-pipeline.md). If a developer breaks the
commit stage and can't fix it within about 10 minutes, the commit must be
reverted from version control to keep mainline green for the rest of the team.
