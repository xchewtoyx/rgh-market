---
type: concept
title: Repeatable Deployment Process
description: >
  Deployments must use the exact same automated mechanism regardless of target
  environment, so that a deployment to production exercises a path already
  proven by every earlier deployment to test and staging environments.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 1, 5"
---

# Repeatable Deployment Process

If dev, test, staging, and production are deployed to using different scripts
or manual procedures, then every deployment before production is exercising a
different — and therefore untrustworthy — path. Using identical deployment
automation for every environment means that by the time a build reaches
production, its deployment mechanism has already been run successfully dozens
or hundreds of times against earlier environments in the
[deployment pipeline](deployment-pipeline.md), so the production deployment
itself carries little incremental risk.

This depends on [configuration injection](configuration-injection.md) to
supply the environment-specific values the identical script needs, and pairs
with [smoke testing](smoke-test.md) every such deployment to catch the cases
where an environment difference still causes a problem despite the shared
mechanism.
