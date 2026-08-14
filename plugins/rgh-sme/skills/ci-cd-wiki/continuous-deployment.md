---
type: concept
title: Continuous Delivery vs. Continuous Deployment
description: >
  Continuous delivery keeps every passing change releasable but triggers
  production deployment manually; continuous deployment removes that manual
  trigger and deploys every passing change to production automatically.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 10"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 12"
  - title: Serverless Design Patterns and Best Practices
    resource: "Serverless Design Patterns and Best Practices (Brian Zambrano), ch. 9"
---

# Continuous Delivery vs. Continuous Deployment

Both practices depend on the same underlying
[deployment pipeline](deployment-pipeline.md): every change is built, tested,
and pushed through every automated gate. They differ only in what happens once
a change has passed every gate:

- **Continuous delivery**: the change sits ready, provably releasable, and a
  human triggers the actual production deployment as a business decision.
- **Continuous deployment**: the pipeline itself triggers production
  deployment automatically the moment every gate passes — no human step in
  between.

Continuous deployment is a strict superset of continuous delivery's technical
requirements: a pipeline not trustworthy enough to deploy automatically isn't
trustworthy enough to hand a human a "yes, ship this" signal either. The
difference is entirely about whether that last trigger is manual, not about
pipeline design. See [deploy vs. release](deploy-vs-release.md) for how a team
can deploy continuously (in either mode) while still controlling exposure
separately via feature toggles.

## Optional at the last step

Continuous deployment is a **team choice**, not an automatic consequence of
good pipeline design. Continuous delivery means fixing a bug and getting that
fix safely to production is fast and easy to hand off — the pipeline should
be built so automatic deploy *could* run, via [pipeline workflow gating](pipeline-workflow-gating.md),
even when the team keeps a manual approval or a production-branch filter on
the final step. Serverless frameworks often ship opinionated deploy commands;
non-serverless stacks usually assemble the same capability from
[deployment script design principles](deployment-script-design.md) and CI
integration.

## Precise ordering

Jez Humble's later clarification makes the layering explicit:
[continuous integration](continuous-integration.md) (small-batch trunk work,
always releasable) is the prerequisite for continuous delivery (release on
demand at the push of a button during normal business hours), which is in
turn the prerequisite for continuous deployment (regularly and automatically
deploying good builds to production — commonly at least once per day per
developer, sometimes on every commit). Continuous deployment fits online web
services particularly well; continuous delivery is the broadly applicable
target for anything wanting fast, low-risk, predictable releases, including
embedded systems, mobile apps, and other contexts where deploying on every
commit isn't practical or desirable.
