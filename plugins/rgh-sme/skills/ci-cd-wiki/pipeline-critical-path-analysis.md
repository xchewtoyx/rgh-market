---
type: concept
title: Pipeline Critical Path Analysis
description: >
  Diagnosing pipeline latency by modeling stages as a dependency graph and
  finding the critical path through it, because optimizing a stage off the
  critical path yields zero improvement in what a developer actually waits
  for.
sources:
  - title: Observability Engineering
    resource: "Observability Engineering (Majors, Fong-Jones, Miranda), ch. 18"
---

# Pipeline Critical Path Analysis

A [deployment pipeline](deployment-pipeline.md)'s stages aren't a flat list
even when a dashboard displays them as one — they form a directed graph, with
some stages running in parallel and others gated behind a shared dependency
(a prebuilt base image, a shared test fixture). A developer waiting on the
pipeline waits for the whole graph to resolve, not for any individual stage,
which means the stage worth optimizing is whichever one currently sits on
the graph's **critical path** — the longest dependency chain from start to
finish — and no other stage.

This has a specific, easy-to-miss failure mode: speeding up a stage that
isn't on the critical path produces a faster individual stage and zero
improvement in overall [cycle time](cycle-time.md), because the pipeline was
never waiting on that stage in the first place. Diagnosing this requires
actually tracing the pipeline's stage dependencies and durations (mapping
each pipeline run as a trace, each stage as a span) rather than guessing from
which stage feels slowest in isolation — the stage that's slowest on its own
is not necessarily the one gating the whole run.

## What the trace reveals once you have it

- **Resource-bound vs. genuinely slow**: a stage's wall-clock duration alone
  doesn't say why it's slow — correlating stage traces with host-level
  resource metrics (CPU, memory, I/O, network) distinguishes "this step is
  compute-bound and needs more parallelism" from "this step is
  bandwidth-bound and more compute won't help at all."
- **Unused parallelism**: some toolchains parallelize automatically across
  available cores; others need explicit configuration to do so, and silently
  run single-threaded until someone notices via a trace that added compute
  produced no speedup.
- **Contention showing up as tail latency, not median latency**: packing
  more parallel work onto shared build infrastructure can leave the typical
  (p50) run time roughly unchanged while pushing p90/p99 up sharply, as
  contention-driven retries and flakiness hit an unlucky fraction of runs —
  a p50-only view of pipeline health can miss this entirely.

## Why full instrumentation is worth it here specifically

Pipeline observability has an unusually strong cost/benefit case compared to
instrumenting a high-traffic production system: pipeline run volume is
naturally bounded (roughly one run per pull request, not one per user
request), so full instrumentation of every run is cheap, while every run has
a specific developer (or agent) idle and waiting on it — making the payoff
per instrumented run far higher than in a system where most individual
requests don't matter enough to examine individually.
