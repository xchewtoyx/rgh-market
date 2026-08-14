---
type: concept
title: Adaptive Liveness Detection vs. Fixed Timeouts
description: A fixed heartbeat timeout forces a single trade-off between detection speed and false positives across every environment, while accrual-style detectors (e.g. Phi Accrual, SWIM) score suspicion continuously from the historical heartbeat-interval distribution, giving callers a tunable confidence level instead of a hard-coded cutoff.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 7, HeartBeat"
---

The simplest liveness check declares a node down once its heartbeat is more than a fixed interval late (`Timeout Interval > Request Interval > network RTT`). This forces one static trade-off for the whole system: shrink the timeout and false positives rise (a slow GC pause or a jittery network gets misread as a crash); grow it and real failures take longer to notice. This is the same shape of problem as [fixed-threshold alerting on non-Gaussian metrics](statistical-threshold-alerting-limits.md) — a single hard-coded cutoff can't fit a signal whose normal variance changes by environment or over time.

**Accrual failure detectors** (Phi Accrual, used by Akka and Cassandra; SWIM with Lifeguard, used by Consul) replace the binary threshold with a continuously computed suspicion level derived from the actual historical distribution of heartbeat arrival gaps for that specific peer. Instead of asking "has more than X ms elapsed?", the detector asks "how surprising is this elapsed time, given how this peer has actually behaved?" and emits a graded suspicion value. Callers then pick their own action threshold on that continuous value rather than the detector hard-coding one universal cutoff — a component that wants fast, false-positive-tolerant detection can act on a low suspicion level, while one that needs high confidence before taking a disruptive action (e.g. reassigning ownership of data) can wait for a much higher one.

This distinction matters for observability work in two ways: first, when instrumenting or evaluating a health-check subsystem, a fixed timeout that "works in staging but flaps in production" is a symptom of exactly this trade-off, not a tuning bug to keep nudging — the fix is a detector that adapts to the peer's own historical variance. Second, at very large scale, all-to-all fixed-interval heartbeating doesn't fit an observed-signal budget (bounded messages per node, bounded total bandwidth), which is why large clusters combine failure detection with a gossip-style dissemination protocol instead of direct heartbeats between every pair of nodes — favoring eventually-correct detection over fastest-possible detection once the blast radius of a false positive (e.g. triggering wholesale data movement) is high.

A local-pause artifact worth instrumenting for directly: if a process's own heartbeat-processing loop resumes after an unexpectedly long gap (its own thread was paused, not the peer's), that cycle's suspicion computation is unreliable and should be treated as suspect rather than acted on immediately — the delay was self-inflicted, not evidence of the peer's failure.

Heartbeat is one entry in a broader [runtime fault-detection instrumentation taxonomy](runtime-fault-detection-instrumentation-taxonomy.md) — ping/echo, watchdogs, condition monitoring, and voting each catch a different class of fault that a heartbeat alone cannot.
