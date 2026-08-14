---
type: concept
title: Acceptance Test Data Management
description: >
  Every acceptance test scenario must set up and tear down its own test data,
  using builders or database resets rather than a shared, persistently dirty
  database, to prevent inter-test dependency and flakiness.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 8"
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 4"
---

# Acceptance Test Data Management

A common cause of flaky [automated acceptance tests](automated-acceptance-testing.md)
is shared, accumulating test data: one scenario's leftover data changes the
outcome of another scenario run later, and failures become order-dependent
and hard to reproduce. Two practices prevent this:

- **Data builder pattern**: generate the exact test data a scenario needs
  programmatically, through domain-object builders that call the
  application's own APIs or inject directly into the database, rather than
  relying on data that "happens to already be there."
- **Database teardown**: reset the test database to a clean, known baseline
  before each test run — via transactional rollback or re-running migration
  scripts — instead of running tests against a shared, long-lived database
  whose state has drifted from whatever earlier tests left behind.

This is the acceptance-testing analogue of
[commit test suite design](commit-test-suite-design.md)'s test-independence
rule, applied to a layer where the "shared mutable state" in question is a
database rather than in-process globals.

## On-demand generation, not blocking

High-performing teams specifically ensure test data can be generated on
demand, without blocking on a cross-team dependency or requiring a full
database clone. A data-provisioning step that has to wait on another team or
a slow full-clone operation reintroduces exactly the queuing delay
[capacity utilization and lead time](capacity-utilization-antipattern.md)
warns against, just relocated into the test-setup phase of the pipeline.
