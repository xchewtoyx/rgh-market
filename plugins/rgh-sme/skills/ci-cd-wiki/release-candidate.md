---
type: concept
title: Release Candidate
description: >
  Every commit to version control produces a potential release candidate, whose
  fitness for production is established only by passing every gate in the
  deployment pipeline.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 1"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Release Candidate

In continuous delivery, there is no separate "release build" produced late in a
cycle: every commit that passes the [commit stage](commit-stage.md) yields a
binary artifact that is, by construction, a candidate for release. Whether it
actually reaches production is a question the [deployment pipeline](deployment-pipeline.md)
answers progressively, gate by gate — not a special activity performed after
the fact.

This is what makes [build once, deploy everywhere](build-once-deploy-everywhere.md)
possible: because the artifact under test is never rebuilt, "this build passed
all pipeline stages" and "this exact binary is safe to deploy to production"
are the same statement.

## Google-style RC assembly

A release candidate is a **cohesive, deployable unit** assembled by automation
from code, configuration, and dependencies that passed
[continuous build](continuous-build-and-green-head.md) — usually from green
head, not necessarily every intermediate true-head commit. **Configuration
belongs in the RC** even when values differ per environment during promotion:
static configuration should be versioned with code and reviewed together, since
a large fraction of production bugs are "silly" configuration problems.
[Version skew during rollout](version-skew-during-rollout.md) is often caught
during RC promotion.

Re-run comprehensive suites against the RC even when postsubmit already ran
them, for: sanity after cut/recompile, auditability (RC-scoped results),
[cherry-pick](hotfix-through-pipeline.md) divergence from latest CB, and
emergency cuts from true head with a minimal test set.

As an RC progresses through environments, artifacts ideally are not
recompiled — [build once, deploy everywhere](build-once-deploy-everywhere.md)
via containers and orchestration enforces consistency and higher-fidelity early
testing.
