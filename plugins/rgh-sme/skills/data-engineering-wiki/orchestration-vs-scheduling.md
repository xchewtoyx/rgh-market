---
type: concept
title: Orchestration vs. Plain Scheduling
description: >
  Why a dependency-aware DAG orchestrator is a different thing from a
  time-based scheduler like cron, and what capability that difference buys.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

A scheduler (cron being the archetype) is aware only of time: run this at
this hour — and a single-host scheduler is also a
[reliability single point of failure](distributed-scheduler-reliability.md)
in its own right, independent of whatever it's actually scheduling. An
**orchestration engine** additionally understands
job-dependency metadata, typically represented as a **directed acyclic graph
(DAG)**, and runs jobs once their upstream dependencies have actually
completed — not just once the clock says it's time.

A production orchestration engine is assumed to run highly available and
always-on: it senses and monitors without human intervention, kicks off new
tasks as DAG dependencies complete, watches external systems and
data-arrival criteria, and alerts when something is out of bounds — e.g., an
overnight pipeline expected to finish by 10 a.m. that hasn't. More advanced
engines add job history, visualization, alerting, DAG/task backfilling, and
time-range dependencies (a monthly report job that waits for a full month of
upstream loads to land).

Orchestration as commonly built is strictly a batch concept. The streaming
analogue — a "streaming DAG" — is harder to build and maintain, since the
dependency-completion model that makes batch orchestration tractable doesn't
map cleanly onto an unbounded stream.

Maturity in this area tends to follow a recognizable path: ad hoc cron jobs →
operational fragility as pipeline count grows (instance failures, job
overruns causing stale downstream data, engineers finding out from analysts
rather than from monitoring) → adopting a dependency-aware orchestrator →
further pain from manual/untested deployment of pipeline definitions →
automated, tested deployment with guardrails against shipping a broken
pipeline definition. Treating orchestrator job definitions as versioned,
tested code — not one-off scripts — is what closes that last gap; see
[pipelines as code](pipelines-as-code.md).
