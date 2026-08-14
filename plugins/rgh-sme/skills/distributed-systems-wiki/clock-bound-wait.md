---
type: concept
title: Clock-Bound Wait
description: >
  Waiting out the assumed maximum clock skew across a cluster before
  exposing a write (or, cheaper, restarting a read that lands in the
  uncertainty window) so timestamp order matches real-time order everywhere.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 24, Clock-Bound Wait"
---

# Clock-Bound Wait

A [hybrid clock](hybrid-clock.md) gives each node a monotonically
increasing, causally consistent timestamp — but only a **partial** order.
Two writes on independent nodes with no causal link between them still
can't be ordered by timestamp alone, and concretely: a read served by a node
whose clock lags can miss a genuinely earlier write that landed at a
timestamp beyond what that node's clock has reached yet. Two clients
comparing notes after reading from different nodes can then observe results
that flatly contradict each other — a violation of external consistency
(see [linearizability](linearizability.md)).

## Commit-wait: pay the cost on the write

Given an assumed maximum clock offset across the cluster (a conservative
configured constant, since there's no reliable commodity way to measure
actual cross-node clock difference — commonly 200–500 ms for
cross-datacenter drift), a write assigned timestamp `t` waits until local
wall-clock time reaches `t + maxOffset` before the value is stored or made
visible. This guarantees every other node's clock has since passed `t`, so
no read anywhere can land before it in real time yet after it in timestamp
order. Google Spanner's **TrueTime** and AWS's **Time Sync Service /
ClockBound** do this properly: instead of a single point-in-time reading,
they expose an explicit `[earliest, latest]` uncertainty interval with two
guarantees — bounds overlap across nodes at any real instant, and bounds
for two real-time instants `t1 < t2` never cross. A write then picks the
interval's `latest` as its timestamp and waits only until its *own* current
`earliest` bound has passed that timestamp — shorter than waiting a flat
worst-case constant, and it directly rewards better clock hardware (tighter
bounds mean shorter waits).

## Read Restart: pay the cost only on affected reads

A flat commit-wait (hundreds of milliseconds per write) is too costly to
pay unconditionally. CockroachDB and YugabyteDB instead push the check to
the read path: on read, check whether any version exists inside the
uncertainty window `(readTimestamp, readTimestamp + maxOffset]`. If one
does, the reader's clock might simply be lagging relative to whoever wrote
it — rather than silently returning a possibly-stale answer, the server
throws a restart signal telling the client to retry the read at the later
timestamp instead. Under this scheme writes never wait; only reads that
actually land inside a genuinely concurrent write's uncertainty window pay
an occasional retry round trip. The trade-off is explicit: the configured
max-clock-drift value is an assumption, not a guarantee — a node whose
drift exceeds it can still violate the guarantee undetected (a real
YugabyteDB causal-consistency bug is cited as evidence this isn't purely
theoretical), whereas TrueTime/ClockBound-based commit-wait is backed by an
actual hardware-enforced bound rather than a configured guess.

## Read-Wait, for symmetric snapshot correctness

The read-side counterpart to commit-wait: a reader picks its own clock
bound's *latest* value as the read timestamp; if that's ahead of what the
serving node's clock currently shows, the node waits for its own clock to
catch up, and separately waits for any pending writes at or below that
timestamp to finish committing before answering. This combination is what
guarantees [snapshot isolation](snapshot-isolation.md) across nodes: once a
read response is returned at a given timestamp, no value will ever later be
written at that timestamp or below it, cluster-wide — the same
readers-never-block-writers property snapshot isolation gives on a single
node, extended across clock uncertainty.
