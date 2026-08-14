---
type: concept
title: Fail-Fast Pipeline Design
description: >
  A deployment pipeline should reject a build at the earliest stage that can
  detect a problem, stopping its progress immediately rather than letting it
  continue into slower, more expensive downstream stages.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 5"
---

# Fail-Fast Pipeline Design

Pipeline stages are ordered from fast/cheap to slow/expensive precisely so
that fail-fast is effective: the [commit stage](commit-stage.md) (minutes)
runs before the acceptance test gate (an hour or two), which runs before
capacity/nonfunctional testing (potentially longer). If a build is going to
fail, catching it at the cheapest stage that can detect the problem saves the
cost of running every later stage against code that was already broken.

When any stage fails, the pipeline stops that build's progress entirely —
there is no partial promotion of a build that failed a gate. The team's
priority becomes fixing whatever broke ("stop the line") before accepting new
work, the same discipline
[continuous integration](continuous-integration.md) applies to the commit
stage specifically, generalized to every stage of the pipeline.
