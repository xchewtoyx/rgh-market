---
type: concept
title: Distributed Cron
description: >
  Making periodic job scheduling fault-tolerant: consensus-elected leader,
  replicated schedule state, decoupled execution, and idempotent jobs to
  absorb duplicates and catch-ups.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer et al.), ch. 24"
---

# Distributed Cron

Single-host cron is a single point of failure: if the host dies, jobs
silently don't run. Distributing it is a compact case study in applying
consensus machinery, because a scheduler must be highly available *and* must
not double-launch:

- **One active scheduler via leader election:** a
  [consensus](consensus.md)-backed [lock/lease](distributed-locks.md)
  (Chubby, in Google's design) elects a single leader daemon;
  lease-based leadership prevents [split-brain](split-brain.md) dual
  launches.
- **Replicated state:** job definitions, schedules, and execution history
  live in Paxos-backed replicated storage
  ([state machine replication](state-machine-replication.md)), so a new
  leader inherits exact knowledge of what ran.
- **Decoupled execution:** the leader schedules but doesn't execute — it
  dispatches to a worker pool (Borg), keeping the consensus-critical
  component small.
- **Failover semantics per job:** after a leader failure, the new leader
  reads the execution log and must decide, for each missed or ambiguous run,
  whether to launch (at-least-once — risking a duplicate if the old leader
  had launched before dying) or skip (at-most-once — risking a missed run).
  There is no universal right answer; the job's semantics decide.
- **Idempotency as the escape hatch:** because "did it run?" is sometimes
  [unknowable](unreliable-networks.md), jobs should be
  [idempotent](idempotency.md) so the safe default is to re-run.

The pattern generalizes to any "exactly one instance of this must be active"
component: singleton consumers, cluster janitors, report generators — same
election, same replicated state, same duplicate-vs-missed trade-off.
