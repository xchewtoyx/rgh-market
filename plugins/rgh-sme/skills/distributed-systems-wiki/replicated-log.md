---
type: concept
title: Replicated Log
description: >
  Keeping every node's state identical by agreeing on a write-ahead log
  entry-by-entry and applying entries in that same order everywhere — the
  concrete mechanics Raft and Multi-Paxos use in steady state.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 9, Replicated Log"
---

# Replicated Log

[State machine replication](state-machine-replication.md) states the
principle: replicas that start identical and apply the same operations in
the same order stay identical. A replicated log is how that's actually built
on top of [leader and followers](leader-election.md): nodes maintain a
[write-ahead log](write-ahead-log.md) where every entry carries both the user
request and consensus metadata (a [generation](generation-clock.md) number),
they agree on that log entry-by-entry, and they execute strictly in log
order.

Running a full two-phase agreement (establish a generation, discover
prior-quorum entries, then replicate) on *every single request* is wasteful.
In practice a leader is elected once — which does the "establish generation"
work as part of the election itself — and thereafter the stable leader alone
drives replication for every subsequent request, reducing steady-state
consensus to one phase per write. This is exactly why Raft and Multi-Paxos
outperform running bare [Paxos](paxos.md) repeatedly.

## Steady-state mechanics (Raft)

- **Append and replicate.** The leader appends to its own log, then sends the
  entry to every follower. A follower appends any new entries it doesn't
  already have and replies with its own latest log index and current
  generation.
- **Full-replication catch-up.** Every replication request also carries the
  index and generation of the entry immediately *preceding* the new ones. If
  a follower's log doesn't match at that position — missing entries, or a
  generation mismatch showing a conflicting entry — it rejects the request;
  the leader responds by retrying at a progressively lower index until the
  follower accepts. This single mechanism both detects gaps (follower log too
  short) and repairs conflicts (follower truncates a stale-generation entry
  at that position), and guarantees every node eventually receives the
  leader's full log even after being disconnected. Heartbeats are folded into
  this same mechanism as empty replication requests carrying the current
  [high water mark](high-water-mark.md), rather than a separate message type.
- **Stale-leader rejection.** A follower rejects any replication request
  whose generation is lower than what it already knows, signaling the sender
  to step down — the same check [generation clock](generation-clock.md)
  describes generically.

## The cross-generation commit rule

A subtle safety hazard: a newly elected leader can replicate an
*old-generation* entry (one appended by a previous leader before it was
deposed) to a fresh quorum. It is tempting to consider that entry committed
once a quorum has it — but Raft never rewrites the generation stamped on
existing entries, so some currently-unreachable server could still hold a
*different* entry at that same index carrying a *higher* generation, which
would later override it once that server reconnects. The rule that closes
this hole: **a new leader must commit at least one entry from its own
current generation before it can safely treat anything from a prior
generation as committed.** This is why Raft implementations append a no-op
entry immediately after election and withhold client service until that
no-op itself is committed (see [high water mark](high-water-mark.md) for the
matching startup hazard this solves).

## Fault model

Crash faults (a faulty node simply stops) are the assumption behind Raft,
Paxos, and essentially all production consensus systems — see [system
models](system-models.md). Byzantine fault tolerance needs the same
log-based shape but three message phases instead of two and a quorum of
`3f + 1` instead of a simple majority to tolerate `f` faults; see [Byzantine
faults](byzantine-faults.md) for why this is rarely worth paying for inside a
single organization's datacenter.

## Push versus pull, and what goes in the log

Raft as usually described has the leader *push* entries to followers;
Kafka's Raft implementation (KRaft) instead has followers *pull*. What goes
in the log is deliberately general — key-value mutations, lease grants,
blockchain blocks, arbitrary database mutations — the rule is simply that
every state-changing request goes through it. Strict cluster-wide ordering
also isn't always required: a key-value store may only need ordering *per
key*, allowing one independent consensus instance per key with no
cluster-wide leader at all (EPaxos), or one replicated log per
[partition](partitioning.md) (MongoDB), ordered within a partition but not
across partitions.

See [stale-leader reads](stale-leader-reads.md) for the hazard that shows up
when reads bypass this log entirely to avoid its latency cost, and
[idempotency](idempotency.md) for how duplicate client requests are handled
on top of a replicated log.
