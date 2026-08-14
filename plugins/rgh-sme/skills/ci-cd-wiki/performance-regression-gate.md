---
type: concept
title: Automated Performance Regression Gate
description: >
  Comparing each build's capacity-test metrics automatically against a
  historical baseline and failing the pipeline on significant degradation, so
  performance regressions are caught the moment they're introduced.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 9"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 10"
  - title: Systems Performance
    resource: "Systems Performance, 2nd ed. (Brendan Gregg), ch. 12"
---

# Automated Performance Regression Gate

Running a [nonfunctional test gate](nonfunctional-test-gate.md) only produces
value if its output is judged against something. The pipeline workflow:

```
[Commit stage pass] -> [Acceptance tests pass] -> [Deploy to capacity environment]
                                                          |
                                                          v
                                             [Execute automated load script]
                                                          |
                                                          v
                                            [Compare metrics vs. baseline]
                                                          |
                                    (fail build if e.g. p95 latency degrades > 5-10%)
```

Two complementary comparisons:

- **Threshold check against baseline**: fail the build automatically if a key
  metric (e.g. p95 latency) degrades beyond a set tolerance versus the
  established [performance baseline](nonfunctional-test-gate.md).
- **Automated trend analysis**: compare resource utilization (CPU, memory,
  disk I/O, DB connections) against historical graphs for the same
  throughput, and alert if it's crept up even without crossing a hard
  threshold — this catches slow regressions that no single build's delta
  would trip.

This is what makes NFR testing a genuine
[deployment-pipeline](deployment-pipeline.md) gate rather than a manual,
after-the-fact performance review: the pass/fail decision is automatic and
tied to the same commit that caused the change, the same way the
[commit stage](commit-stage.md) ties a functional failure back to its commit.

## Reusing acceptance tests as load generators

A practical way to generate realistic load without writing a separate
performance-test suite from scratch: run the existing, already-parallelized
[automated acceptance tests](automated-acceptance-testing.md) concurrently at
volume (e.g. thousands of parallel "search" and "checkout" scenarios for an
e-commerce site) and measure the system's behavior under that concurrency,
rather than authoring load-generation scripts independently of the
functional test suite.

A concrete example threshold: fail the performance tests if results deviate
more than about 2% from the immediately preceding run — tighter than the
5–10% figure above, illustrating that the right tolerance depends on how
noisy a given metric normally is; pick a threshold empirically from the
metric's own historical variance rather than copying one number everywhere.

## Pitfalls that produce a misleading pass or fail

An automated gate is only as trustworthy as the measurement feeding it.
Recurring ways a performance run silently measures the wrong thing:

- **Comparing means instead of percentiles.** An average can look flat while
  p99 latency spikes, because outliers get smoothed away by the mean —
  gate on the percentile that actually matters to users, not the average.
- **Letting the load generator become the bottleneck.** If the client
  driving load runs out of its own CPU, memory, or sockets first, the run
  measures the harness's capacity, not the system under test's — watch the
  generator's own resource usage, not just the target's.
- **Skipping warm-up.** Measuring from the first request includes cold
  caches and JIT warm-up, understating steady-state performance; discard
  the warm-up window before recording results.
- **Ignoring the error rate.** A run that reports high throughput while a
  large fraction of requests are failing fast (which inflates ops/sec) is
  not a pass just because latency looks good — gate on error rate too, not
  latency and throughput alone.
- **Unrepresentative load shape.** A uniform synthetic request distribution
  can hide problems that only appear under the bursty, skewed-key access
  patterns real production traffic has — a
  [nonfunctional test gate](nonfunctional-test-gate.md) built from replayed
  or sampled production traffic is more predictive than one built from an
  evenly distributed synthetic load.
