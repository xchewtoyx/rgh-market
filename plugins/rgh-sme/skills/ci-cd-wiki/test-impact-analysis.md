---
type: concept
title: Test Impact Analysis
description: >
  Running only tests downstream of a change in the dependency graph instead of
  the full suite, trading complete coverage per run for faster feedback and
  lower resource use.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Test Impact Analysis

At monorepo scale — billions of lines, tens of millions of lines changed
weekly, almost every dependency built from source at head — running every
test on every change is infeasible without selective execution. Google's Test
Automated Platform (TAP) and related CI manage billions of test runs and
tens of thousands of binary builds weekly alongside
[continuous build and green head](continuous-build-and-green-head.md).

**Test impact analysis** uses a live dependency graph (from
[artifact-based build systems](artifact-based-build-systems.md) like Blaze/Bazel)
to select the **minimal downstream test set** affected by a change. Changes
triggering fewer tests can be scheduled sooner than large blast-radius
changes — incentivizing smaller, targeted edits.

When batched runs fail, culprit finding splits batches and reruns tests per
change, or developers binary-search a batch. Flakes and infrastructure issues
complicate attribution — see [CI as alerting](ci-as-alerting.md).

Impact analysis complements [presubmit vs. postsubmit testing](presubmit-vs-postsubmit-testing.md):
presubmit runs a fast subset; postsubmit runs the expanded impacted set on
[continuous build](continuous-build-and-green-head.md). Execution often uses
[remote build cache and execution](remote-build-cache-and-execution.md) for
parallelism.
