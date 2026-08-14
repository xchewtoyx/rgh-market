---
type: concept
title: Database Sandbox
description: >
  An isolated database instance dedicated to a single developer or automated
  test runner, so schema migrations and test scenarios can execute
  independently without cross-contaminating other work in progress.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 12"
---

# Database Sandbox

A database sandbox extends
[ephemeral test environments](ephemeral-test-environments.md) to the data
tier specifically: rather than sharing one test database across every
developer and pipeline run — where one run's schema migration or test data
setup can corrupt another's results — each developer or automated test runner
gets its own instance, provisioned and torn down like any other ephemeral
environment.

This is what makes it safe to test
[database migration scripts](database-migration-scripts.md) in isolation
before they run anywhere shared: a migration can be applied, verified, and
discarded in a sandbox without any risk to a colleague's in-progress work or
to a shared pipeline stage's state.
