---
type: concept
title: Quorum Reads and Writes
description: >
  The w + r > n condition ensuring read and write replica sets overlap in at
  least one up-to-date node — and the edge cases where the overlap still
  returns stale data.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §6, §6.1"
---

# Quorum Reads and Writes

In [leaderless replication](leaderless-replication.md) with n replicas per key,
a write must be confirmed by w nodes and a read must collect responses from r
nodes. If **w + r > n**, the set of nodes written and the set of nodes read
must overlap in at least one node, so at least one read response is up to date
(version numbers identify which).

Common configurations: n=3, w=2, r=2 (tolerates one node down); n=5, w=3, r=3
(tolerates two). Tuning trades off: lower w makes writes faster/more available
but reads must cast a wider net; w + r ≤ n is a legitimate choice for
low-latency, high-availability reads that accepts a higher chance of
staleness.

## Why quorum overlap is weaker than it looks

Even with strict w + r > n, stale reads happen:

- **[Sloppy quorums](sloppy-quorum-and-hinted-handoff.md)** put writes on nodes
  outside the home set, destroying the overlap guarantee.
- **Concurrent writes** under [last-write-wins](last-write-wins.md) can drop
  writes due to clock skew.
- **Concurrent read and write:** the read may see the write on some replicas
  only; it is undetermined whether it returns old or new.
- **Partial write failure:** a write succeeding on fewer than w replicas
  reports failure but is *not rolled back* on the replicas that took it —
  later reads may or may not see it.
- **Node restore from a stale replica** can drop the write from a node that
  had it, breaking the overlap arithmetic.

A worked scenario makes the gap concrete: a write lands on one replica only,
a first reader's quorum happens to include that replica and sees the new
value, that replica then goes down, and a second reader's quorum is served
entirely by the stale replicas — a value already observed can "disappear"
from a later read despite w + r > n holding throughout (see [leader election
mechanics](leader-election.md) for the full walkthrough and why routing
through a single leader closes this gap). So quorums provide probabilistic
freshness, not [linearizability](linearizability.md). Staleness can only be
characterized
statistically (e.g. Probabilistically Bounded Staleness), and the session
guarantees ([read-your-writes](read-your-writes-consistency.md),
[monotonic reads](monotonic-reads.md)) are *not* implied.

Note the distinction from consensus quorums: here the quorum is about replica
set *overlap* for data freshness; [consensus](consensus.md) uses majority
quorums for *agreement* on decisions such as leadership.

## Tuning N, R, and W in production (Dynamo)

Client applications tune n, r, and w independently to trade off performance,
availability, durability, and consistency for their own workload — Dynamo
exposes the knobs rather than fixing them:

- **n** sets *durability*: how many copies of the object exist. A typical
  value is n=3.
- **r and w** set *availability and consistency*: w=1 means a write is never
  rejected as long as one node anywhere can take it, but this opens a
  **vulnerability window for durability** — the client is told the write
  succeeded while it sits on only that one node, and a crash there loses it
  before replication catches up.

**Counter-intuitive finding**: durability and availability are usually
assumed to move together, but tuning w drives them in *opposite* directions.
Raising w shrinks the vulnerability window (more replicas must hold the write
before it's acknowledged, so durability improves) but also raises the
probability of rejecting the write outright, since more storage hosts must be
reachable and healthy to reach that count — availability falls. There is no
setting that maximizes both; the choice is a real trade, not a tuning
mistake to be engineered away.

A common production configuration is **(n, r, w) = (3, 2, 2)** — satisfies
w + r > n, so it still gets the overlap guarantee above, while tolerating one
replica being unreachable for either a read or a write. A different extreme
suits **read-heavy, write-light** workloads: **r=1, w=n**, which makes every
read servable by a single replica (minimum read latency, maximum read
availability) at the cost of a write failing unless every replica is up. This
shape fits a store used as an **authoritative persistence cache** in front of
a heavier backing store (e.g. serving a product catalog), where reads
dominate and the data changes rarely.

[Write buffering](write-buffering-for-latency.md) composes with this tuning:
a coordinator can route the durable copy to just one of the w-or-fewer
replicas it waits on, keeping the buffering latency win without giving up
the durability the quorum is meant to provide.
