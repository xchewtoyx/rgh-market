---
type: concept
title: Slow Test Accumulation
description: >
  Test suites slow down incrementally as individual tests boot large systems,
  accumulate slow dependencies, or embed fixed sleeps — until engineers run
  them less often or skip them entirely.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 13"
---

# Slow Test Accumulation

Large suites get **slower over time** unless actively managed. Individual
contributions are small; the aggregate blocks the
[deployment pipeline](deployment-pipeline.md):

- Booting large portions of a system, emulators, or heavy datasets per test.
- **Dependency creep** — an integration test with one five-second dependency
  grows to a dozen and five minutes total.
- **`sleep()` / fixed timeouts** embedded in shared utilities — a small wait
  in a widely used helper adds minutes of idle time across every suite run.
  Prefer **high-frequency polling** for state transitions plus a timeout for
  failure — see [developer-owned test suite maintenance](developer-owned-test-maintenance.md).

Parallel execution and faster hardware help but are eventually swamped by
many individually slow tests. When a suite is slow and nondeterministic it
becomes a **roadblock**: engineers work around it, including skipping tests
on submit — a risky practice that happens when the suite causes more harm
than good.

Mitigations:

- [Test size constraints](test-size-constraints.md) and moving slow tests to
  [postsubmit](presubmit-vs-postsubmit-testing.md).
- [Test impact analysis](test-impact-analysis.md) and
  [remote build cache and execution](remote-build-cache-and-execution.md) at
  monorepo scale.
- Performance goals, refactoring marginal tests, and treating tests with the
  same respect as production code — see
  [project health score](project-health-score.md) for tracking test latency.

Without investment, teams eventually decide tests are not worth having — the
opposite of [a few reliable tests beat many unreliable ones](reliable-tests-over-coverage.md).
