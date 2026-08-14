---
type: concept
title: Pipeline Secret Injection
description: >
  Store deployment secrets in the CI platform's secret store, never in
  version control, and inject them into deploy jobs at runtime.
sources:
  - title: "Serverless Design Patterns and Best Practices"
    resource: "Serverless Design Patterns and Best Practices (Zambrano), ch. 9"
---

# Pipeline Secret Injection

Non-sensitive configuration (test database host, usernames, environment
names) can live in tracked pipeline config. **Secrets** — production
database passwords, cloud API keys — must be set via the CI platform's
secret or environment-variable UI (or sealed secret mechanism), never
committed to the repository.

Deploy jobs reference secrets by name; the platform injects values at
runtime so infrastructure-as-code templates can bind `${env:SECRET_NAME}`
without the value appearing in git history. Cloud provider credentials for
deployment attach the same way (e.g., IAM access keys configured once in
CI permissions, picked up automatically by deploy tooling).

This is a delivery-safety prerequisite for [segregation of duties via
pipeline audit trail](segregation-of-duties-via-pipeline-audit-trail.md)
and [provenance-based deployment policy](provenance-based-deployment-policy.md):
the pipeline is the controlled path to production, and secrets must not
leak through the same channel that stores application source.

Non-critical test secrets may still differ by environment — detect CI via
platform-injected markers (e.g., `CIRCLECI`) and override hosts so linked
service containers resolve correctly in build jobs vs local development.
