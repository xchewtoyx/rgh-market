---
type: concept
title: Branch Gated Deploy Workflow
description: >
  Wire deployment as a separate pipeline job that requires tests to pass
  and restricts to an approved branch, enabling optional continuous deployment.
sources:
  - title: "Serverless Design Patterns and Best Practices"
    resource: "Serverless Design Patterns and Best Practices (Zambrano), ch. 9"
---

# Branch Gated Deploy Workflow

A complete delivery pipeline often splits **build** (test, coverage, artifacts)
from **deploy** (promote to production). The deploy job should:

1. **Require build success** — `deploy` depends on `build` passing; failed
   tests never reach production.
2. **Filter by branch** — deploy runs only when commits land on a designated
   branch (e.g., `production`), not on every feature branch or mainline
   commit used for integration.

That yields **continuous deployment on the production branch only**: merge
to the gated branch after review and CI green triggers automated deploy;
other branches get test feedback without production exposure.

Whether to enable step-two continuous deployment is a team choice; the
pipeline should still be built so deployment *is possible* when the team
opts in — see [continuous deployment vs. continuous
delivery](continuous-deployment-vs-continuous-delivery.md). Serverless
frameworks often supply deploy tooling; the workflow definition (branch
filters, job dependencies) remains the team's safety design.

Pair with [peer review as change control](peer-review-as-change-control.md)
so merges to the deploy branch aren't solo-authored changes.
