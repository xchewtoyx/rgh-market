---
type: concept
title: Leader Failover
description: >
  Promoting a follower to leader after the leader fails — a process riddled
  with pitfalls: lost writes, reused primary keys, and split-brain.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 10"
---

# Leader Failover

When the leader in a [single-leader](single-leader-replication.md) system dies,
some node must take over. Automatic failover runs three steps:

1. **Detect the failure** — usually a heartbeat timeout. There is no reliable
   way to distinguish a dead leader from a slow one (see [unreliable
   networks](unreliable-networks.md)), so the timeout is a judgment call:
   too short causes unnecessary failovers under load, too long extends the
   outage.
2. **Elect a new leader** — ideally the replica with the most up-to-date data,
   chosen by an election (a [consensus](consensus.md) problem; see [leader
   election mechanics](leader-election.md) for how the vote or external-store
   handoff actually runs).
3. **Reconfigure** — clients route writes to the new leader; if the old leader
   returns, it must be forced to become a follower.

## Why failover goes wrong

- **Discarded writes.** With [asynchronous
  replication](synchronous-vs-asynchronous-replication.md), the new leader may
  not have all of the old leader's writes. When the old leader rejoins, its
  un-replicated writes are usually discarded — confirmed writes silently
  vanish, violating durability.
- **Cascading corruption from reused identifiers.** In a GitHub incident, an
  out-of-date MySQL follower was promoted and reused auto-increment primary
  keys already assigned by the old leader; those keys were also in a Redis
  cache, so rows were disclosed to the wrong users. Discarded writes are
  especially dangerous when other systems have observed them.
- **[Split-brain](split-brain.md).** Two nodes both believe they are leader and
  both accept writes. Without conflict resolution, data is lost or corrupted.
- **Trigger-happy timeouts.** Under high load, a slow leader can be declared
  dead, and the failover itself adds load — a self-inflicted cascade.

These pitfalls are why some operations teams prefer manual failover, and why
correct automatic failover needs the machinery of [consensus](consensus.md) and
[fencing](fencing-tokens.md) rather than ad-hoc scripts.

**Planned failover** (maintenance, upgrades) is the tame variant and worth
distinguishing: pick the candidate, pre-configure it, briefly pause writes so
[asynchronous replication](synchronous-vs-asynchronous-replication.md)
catches up fully, then repoint clients — no data loss, because the handover
happens with lag at zero. Every step of the *unplanned* flow (detect, select
most-caught-up replica, reattach the other followers, repoint clients,
rebuild a replacement) is an inflection point that can fail; rehearse it, and
verify candidates aren't [silently divergent](monitoring-replication-health.md)
before you need them.
