---
type: concept
title: Monitoring Replication Health
description: >
  Measuring lag and detecting silent replica divergence — replication can
  break without erroring, so freshness and consistency must be actively
  verified.
sources:
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 10"
---

# Monitoring Replication Health

Replication fails in two distinct ways, needing separate detection:

## Lag (freshness)

Measure [replication lag](replication-lag.md) end-to-end with a **heartbeat
row**: insert a timestamped row on the leader periodically, poll for it on
each follower, and report the difference. Beware that comparing wall-clock
timestamps across nodes inherits [clock drift](unreliable-clocks.md) — NTP
issues can fake or hide lag. For synchronous/semi-synchronous setups, also
track the write-latency impact replication adds on the leader. In
quorum-based clusters, monitor headroom to losing
[quorum](quorum-reads-and-writes.md) (e.g. replication factor 3 needing 2
responsive replicas), not just node-up counts.

## Silent divergence (consistency)

Replicas can diverge **without any error**: statement-based
[replication log](replication-log-implementations.md) nondeterminism or
schema mismatch, stray writes made directly on a follower, permission
changes, storage exhaustion, partial corruption. Nothing in the replication
stream flags this — detection requires comparing data: checksums are cheap
for append-only/insert-only tables; for mutable data, an async job computing
per-chunk or per-transaction hashes on leader and followers and flagging
mismatches. Assume divergence will eventually happen and make it visible;
discovering it during [failover](leader-failover.md) is the worst case,
because the "up-to-date" promotion candidate may be silently wrong.

Also trend the operational scaling numbers — dataset size, replica rebuild
duration, resync time — to predict when building a new replica takes longer
than your recovery objectives allow.
