---
type: concept
title: Read Replicas for Analytics Offload
description: >
  Using a synchronously replicated copy of a production database to absorb
  batch scans and CDC queries so they don't compete with live application
  traffic.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 7"
---

A synchronous read replica is a full copy of a production database, kept in
sync in real time with the primary, that can serve reads identical to the
primary and support zero-data-loss failover. Because it's built for exactly
this, it's a natural place to route work that would otherwise compete with
production application traffic on the primary: large batch export scans, or
timestamp-based [batch CDC](change-data-capture.md) queries run several
times a day.

This is the practical mitigation for the tension
[source system evaluation](source-system-evaluation.md) flags — "will reads
impact source performance?" — without needing to negotiate a maintenance
window or accept degraded application latency every time a pipeline needs to
read a large slice of the source. It's most valuable exactly where the
alternative (querying the primary directly) is riskiest: high-frequency
batch scans against a database that's also serving latency-sensitive
production traffic.

The trade-off is operational cost (running and keeping a second full replica
in sync) against the risk it removes — for a source queried rarely or
lightly, a read replica is usually overkill; for one queried heavily enough
to threaten production performance, it's close to a prerequisite.

**A replica also buys freedom to modify, not just capacity to offload.**
Because it's a separate copy, extraction-friendly indexes can be added to
the replica specifically to speed up a pipeline's own scan or CDC query
pattern, without paying that index's write-side maintenance cost on the
primary — an index that would slow down every production write if added
there costs nothing extra on a replica whose only job is being read from.
The same applies to lighter-weight schema changes (renamed columns, a
narrower subset of tables mirrored) made purely to simplify the extraction
job, changes that would be far riskier to make directly on a live
production schema other applications depend on.

For the equivalent isolation pattern on a log-based streaming platform
rather than a database, see
[streaming analytics replica cluster](streaming-analytics-replica-cluster.md).

**A "synchronous" replica still isn't guaranteed instantaneously
consistent.** Even under strong replication protocols, there's an
irreducible gap between the primary committing a write and every replica
having applied it — the caveat matters concretely for a pipeline step that
writes to the primary (a status flag, a checkpoint row) and then immediately
reads it back from a replica expecting to see its own write: that read can
land on a replica that hasn't caught up yet and silently miss the update.
Where a pipeline genuinely needs to observe its own just-written value, read
that specific check back from the primary rather than a replica, or confirm
the tooling being used offers an explicit read-your-writes guarantee (a
returned commit token or timestamp the subsequent read can wait on) rather
than assuming any replica is always current.
