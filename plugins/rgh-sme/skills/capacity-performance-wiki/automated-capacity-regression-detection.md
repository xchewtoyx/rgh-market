---
type: concept
title: Automated Capacity Regression Detection
description: Running capacity tests automatically against a stored performance baseline so that latency or resource-consumption regressions are caught as build failures rather than discovered in production.
sources:
  - title: "Continuous Delivery"
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Jez Humble, David Farley), ch. 9"
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook (Gene Kim, Jez Humble, Patrick Debois, John Willis, Nicole Forsgren), ch. 10"
---

Manual, occasional capacity testing catches capacity problems too late to act on cheaply — by the time someone runs a one-off load test, several changes have usually landed since the system was last known to be within budget, making the regression hard to isolate. **Automated capacity regression detection** runs a [capacity test](capacity-test-types.md) as a routine, automated step and compares its results against a stored historical baseline, failing the build the same way a functional test failure would.

## What Gets Compared

Two distinct kinds of regression are worth checking automatically, because a system can degrade in either without the other moving:

*   **Latency/throughput regression:** the tracked percentile (e.g., p95 latency) degrades by more than a set threshold (e.g., 5-10%) relative to the historical baseline, at the same offered load.
*   **Resource-consumption regression:** CPU, memory, disk I/O, or database connection usage increases for an *identical* throughput level, even if latency and throughput targets are still met. This catches efficiency regressions — a change that silently makes the system more expensive to run at the same load — before they show up as a capacity or cost problem later. See [utilization targets](utilization-law.md) for why rising resource consumption at constant load erodes headroom even when nothing has visibly broken yet.

## Why Compare Against a Baseline, Not a Fixed Threshold

A single fixed pass/fail threshold (e.g., "p95 must be under 200ms") only catches regressions large enough to cross that line. Comparing against a rolling historical baseline instead catches smaller, incremental regressions — the kind that individually stay under any reasonable fixed threshold but compound over many changes into a real problem. This requires the capacity test to run against a stable, [representative environment](scaled-capacity-test-environment.md) on every run, since baseline comparisons are meaningless if the environment's own capacity is inconsistent from run to run. The comparison threshold can be tight — one reported convention fails the build if a run's results deviate more than 2% from the immediately preceding run, rather than the wider 5-10% band used for looser baselines; the right threshold depends on how much natural run-to-run variance the test environment has.

## Sourcing Load Without a Dedicated Tool

A pipeline-integrated capacity test doesn't necessarily need a purpose-built load-generation tool: existing parallelizable acceptance tests can double as load generators by running many instances of them concurrently against the build (e.g., firing hundreds of parallel "search" or "checkout" acceptance-test scenarios at an e-commerce build). This reuses test assets that already encode realistic request shapes instead of building and maintaining a separate synthetic workload generator — though see [load generator bottlenecks](load-generator-bottlenecks.md) for the limits of any harness pressed into this role.

## Boundary

The result of this comparison is a signal about system capacity; the pipeline mechanics that gate a release on that signal (build stages, deployment gates) are a delivery-pipeline concern, not a capacity-engineering one.
