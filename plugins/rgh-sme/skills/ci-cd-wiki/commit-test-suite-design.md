---
type: concept
title: Commit Test Suite Design Principles
description: >
  Tests in the commit stage must run entirely in memory, be independent of
  execution order, be deterministic, and exclude anything slow — with slower
  integration tests moved to a downstream stage instead.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 7"
---

# Commit Test Suite Design Principles

The commit test suite is what makes the [commit stage](commit-stage.md)'s
5–10 minute budget achievable, and what gives it a high enough
signal-to-noise ratio that a failure reliably means "there is a real bug,"
not "the environment was flaky." Four design rules:

- **Speed and isolation**: tests run entirely in memory. Disk I/O, database
  access, network connections, web servers, and third-party APIs are mocked
  or stubbed out — anything that touches the outside world is both slow and a
  source of nondeterminism.
- **Test independence**: every test is self-contained. No test depends on
  execution order or shares mutable global state with another; a test suite
  that only passes in one order is not actually testing independent units.
- **Deterministic execution**: a test passes or fails consistently regardless
  of CPU speed, OS, or time of day. Timing-based waits (`sleep()`) are replaced
  with explicit assertions or polling/latches, because a `sleep()`-based test
  is a coin flip under different machine load.
- **Separate slow tests out**: integration tests that need a real database or
  filesystem access do not belong in the commit suite — move them to a
  downstream pipeline stage (or run them in parallel to the commit stage) so
  they can't blow the commit stage's speed budget.

A commit stage that ignores these rules degrades into exactly the failure mode
[continuous integration](continuous-integration.md) depends on avoiding:
developers stop trusting (and stop waiting for) a slow or flaky commit-stage
result, which reopens the door to
[integration hell](integration-hell.md).
