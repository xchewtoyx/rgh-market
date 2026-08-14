---
type: concept
title: Build Once, Promote the Artifact
description: >
  Compile and package a release candidate exactly once, then move that
  identical binary unchanged through every subsequent environment, so what
  was verified is provably what ships.
sources:
  - title: "Continuous Delivery"
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 1, ch. 5"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Build Once, Promote the Artifact

A **release candidate (RC)** is a cohesive, deployable unit created by an
automated process — code, configuration, and other dependencies that have
passed continuous build — assembled for promotion through test environments
and possibly to production.

A deployment pipeline should compile and package a release candidate
exactly once, at the earliest stage, and store it in an artifact
repository. Every later stage — acceptance testing, staging, production —
deploys that same versioned binary unchanged; nothing is recompiled
per-environment.

Rebuilding per environment (even from identical source) breaks the
guarantee that matters most: that the artifact which passed every test is
the artifact running in production. A different compiler flag, dependency
resolution, or build-time environment variable between two builds from the
same commit can produce a binary with different behavior — silently
invalidating everything the pipeline verified. Environment-specific
behavior belongs in configuration injected at deploy time or read at
runtime, never baked in by rebuilding.

**Configuration belongs in the RC.** Static configuration should be
promoted alongside its corresponding code so it undergoes testing together
— a large fraction of production bugs stem from configuration problems.
Prefer dynamic configuration, experiments, and feature flags where
appropriate rather than compiling config into binaries; whatever static
config exists should live in version control with the code and pass the
same review. [Version skew during rollout](version-skew-during-rollout.md)
is often caught during RC promotion when config and code are assembled as
one unit.

This makes the artifact repository, not the source repository, the
authoritative record of "what is deployable right now," and it's what
makes [rollback vs. roll-forward](rollback-vs-roll-forward.md) simple to
reason about — a rollback re-deploys a specific prior artifact rather than
re-running a build against an old commit and hoping it reproduces.

It is also the load-bearing precondition for [deployment pipeline
traceability](deployment-pipeline-traceability.md): tracing a running
artifact back to the exact commit, dependencies, and test results that
produced it only works if that artifact was never silently rebuilt along
the way. As an RC progresses through environments, its artifacts
(binaries, containers) ideally are not recompiled — container images and
orchestration consistency enforce the same bits from early testing through
production, yielding higher-fidelity earlier signal and fewer surprises.
See [release candidate regression testing](release-candidate-regression-testing.md)
for why the assembled RC still gets a comprehensive test pass even after
per-commit continuous build.
