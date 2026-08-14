---
type: concept
title: Pipeline Workflow Gating
description: >
  Expressing deploy jobs as workflow steps that require prior jobs to pass and
  apply branch filters so production deployment fires only on approved branches.
sources:
  - title: Serverless Design Patterns and Best Practices
    resource: "Serverless Design Patterns and Best Practices (Brian Zambrano), ch. 9"
---

# Pipeline Workflow Gating

A [deployment pipeline](deployment-pipeline.md) should separate **build/test**
jobs from **deploy** jobs and wire them with explicit dependencies:

1. Build job: checkout, restore cache, install dependencies, run unit tests,
   publish artifacts (coverage reports, binaries).
2. Deploy job: runs only when the build job succeeds **and** the commit sits
   on an allowed branch (e.g. `production` rather than every feature branch).

Workflow engines express this as `requires: [build]` plus branch `filters`.
That makes [continuous deployment](continuous-deployment.md) a toggle: the
pipeline is built so automatic production deploy is *possible*, but the branch
filter decides whether every merge triggers it. Teams often use a dedicated
production branch when `main` receives frequent non-shipping commits (docs,
experiments, multi-track monorepos).

Keep CI configuration thin by delegating install, test, and deploy commands to
the same [single-command build](single-command-build.md) / Makefile targets
used locally — one definition of "how to test" and "how to deploy," invoked
from developer laptops and the CI runner alike.

Pair with [secrets management in pipelines](secrets-management-in-pipelines.md):
non-secret configuration can live in tracked pipeline YAML; credentials and
production passwords stay in the CI provider's secret store, injected at runtime
into deployment tooling (e.g. `${env:CUPPING_DB_PASSWORD}` in infrastructure
templates).
