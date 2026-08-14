---
type: concept
title: Distributed Scheduler Reliability
description: >
  Why a single cron host is a scheduling single point of failure, and the
  leader-election and lease mechanisms a distributed scheduler uses to avoid
  duplicate or dropped runs across a failover.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 24"
---

A single host running cron is a scheduling single point of failure: if that
host goes down, every job depending on it simply doesn't run, silently,
until someone notices the missing output. A distributed scheduler removes
that SPOF by running the scheduling role itself as a fault-tolerant service
rather than a single machine's local cron table.

The standard shape: a **leader election** mechanism (a consensus protocol
backed by replicated storage, such as Paxos-backed Chubby) selects exactly
one active scheduler at a time from a pool of candidates, and job
definitions, schedule state, and execution history persist in that same
replicated store rather than on the leader's local disk — so a leader that
crashes leaves nothing lost for its replacement to pick up. The leader
itself typically doesn't execute jobs directly; it dispatches execution
requests to a separate worker pool, decoupling the (comparatively rare,
low-throughput) scheduling decision from the (frequent, resource-heavy) job
execution.

Two failure modes this design has to solve explicitly, both direct instances
of concerns [orchestration](orchestration-vs-scheduling.md) has to answer for
any dependency-aware pipeline runner, not just a plain time-based scheduler:

- **Duplicate execution during failover**: if a leader fails mid-dispatch and
  a new leader is elected, both the dying leader and its replacement must
  never be allowed to believe they're each the sole active scheduler at the
  same time (a split-brain condition) — this is what a **lease**, granted and
  renewed only through the same consensus mechanism used for leader election,
  prevents: only the current lease holder may dispatch, and a lease expires
  cleanly rather than being contested.
- **Missed schedules after a failover**: when a new leader takes over, it has
  to decide, per job, whether a schedule that should have fired during the
  gap actually ran. It answers this by inspecting the persisted execution
  log rather than guessing — and even once that answer is known, the newly
  elected leader still has to make an explicit policy call about whether to
  run the missed occurrence late ("catch up") or let it go ("skip"), since
  neither choice is universally correct: catching up matters for a job whose
  output every downstream consumer depends on, while skipping is often
  better for a job whose next scheduled run will produce an equivalent or
  superseding result anyway.

Because a dispatch can still be redelivered despite lease protection — a
worker crash after starting a job but before the scheduler recorded
completion looks identical to a job that never started — every job a
distributed scheduler dispatches still has to be
[idempotent](idempotent-and-replayable-jobs.md) on its own terms. The
scheduler's leader-election and lease machinery reduces how often a
duplicate dispatch happens; it does not eliminate the need for the job
itself to tolerate one.
