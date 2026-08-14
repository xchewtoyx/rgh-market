---
type: concept
title: Exception Collector as a Rollout Health Signal
description: Centrally collecting every program-exiting exception, rather than letting an auto-restart mechanism silently absorb crashes, turns crash volume into an aggregate health signal that can gate a rollout in progress, not just a post-hoc debugging aid.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 2"
---

Severe, program-exiting errors should be captured by a central exception-collector framework rather than left to an automatic-restart mechanism, which otherwise hides them entirely — a process that crashes and restarts cleanly every few minutes can look perfectly healthy on an uptime or request-success dashboard while quietly failing constantly underneath. Centralizing exception collection turns this invisible failure mode into three distinct uses: it makes otherwise-masked crashes visible at all; it functions as a real-time aggregate health signal, where a spike in exception volume during a rollout is itself a stop-the-rollout condition, independent of whether any user-facing metric has moved yet; and it supports trend analysis across releases, distinguishing a genuinely improving system (exception rate trending down release over release) from a worsening one.

The general principle for observability is that crash/restart counts deserve the same first-class treatment as latency and error-rate metrics in a deployment pipeline — a canary or progressive rollout that only watches request success rate can miss a component that's failing fast and restarting fast enough to never actually drop a request, right up until the restart budget or the underlying resource leak catches up with it. See [deployment markers and settling period](deployment-markers-and-settling-period.md) for the related practice of correlating a metric's behavior against the timing of a specific release, and [centralized crash report and coredump collection](centralized-crash-report-and-coredump-collection.md) for what to actually capture per crash so the aggregate signal is backed by debuggable detail, not just a bare count.
