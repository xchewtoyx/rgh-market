---
type: concept
title: Developer-Owned Test Suite Maintenance
description: >
  Automated test suites written and maintained by the developers who write
  the code correlate with high delivery performance; suites maintained solely
  by a separate QA team show no such correlation.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 4"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 13"
---

# Developer-Owned Test Suite Maintenance

Empirical finding: it isn't the mere existence of an automated test suite
that predicts delivery performance, it's *who owns it*. Suites written and
maintained by the developers producing the code drive high performance;
functionally equivalent suites maintained exclusively by a separate QA team
or an outsourced vendor show no statistical correlation with performance at
all.

## Why ownership matters

Writing automated tests — especially acceptance tests — forces developers to
write testable code in the first place (the same feedback loop
[test-driven development](continuous-integration.md) relies on), and gives
them direct, immediate incentive to keep the suite healthy, since a flaky or
neglected suite slows down their own work. A suite owned by someone else
removes that feedback loop: the people best positioned to fix a failing or
flaky test aren't the ones who feel the pain of it failing.

This reframes QA's role: rather than owning test suite maintenance, testers
shift toward exploratory testing, usability analysis, and pairing with
developers to shape test scenarios and acceptance criteria — see
[agile testing quadrants](agile-testing-quadrants.md) for where that
exploratory work fits relative to automated testing.

Non-deterministic (flaky) tests destroy trust in the suite regardless of who
owns it, and must be quarantined or deleted immediately rather than tolerated
— see [commit test suite design principles](commit-test-suite-design.md) for
the mechanics of keeping a suite deterministic.

Large tests need explicit [large test ownership](large-test-ownership.md) —
feature owners for cross-service scenarios, not only module authors. Failure
messages must identify the failing scenario clearly; distributed traces (request
IDs across RPC chains) beat stack traces that stop at process boundaries.
Poll/event-driven waits beat fixed sleeps in large tests — sleeps fail together
under fleet load and hide graceful-degradation failures that look like product
bugs. At Google scale, a `sleep()` in a shared utility can add minutes across
every run — see [slow test accumulation](slow-test-accumulation.md).

Treat tests with the same respect as production code: incentivize test quality
(reward rock-solid tests alongside feature launches), set performance goals,
refactor slow or marginal tests, and invest in linters, documentation, and
tooling that make [brittle over-specified tests](brittle-over-specified-tests.md)
harder to write. Fewer supported test frameworks concentrate that investment.
Track regressions via [project health score](project-health-score.md).
