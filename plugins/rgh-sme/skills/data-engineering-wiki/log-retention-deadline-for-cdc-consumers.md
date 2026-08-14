---
type: concept
title: Log Retention Sets a Hard Deadline for CDC Consumers
description: >
  Why log-based change data capture has a real consumption deadline, not
  just a performance target, because the source's write-ahead log is never
  retained forever.
sources:
  - title: "Patterns of Distributed Systems"
    resource: "Patterns of Distributed Systems (Joshi), ch. 3-5"
---

[Log-based CDC](change-data-capture.md) works by tailing a source's
write-ahead log — the append-only record every database and log-backed
system (Kafka included) already keeps for its own durability. That log is
never kept indefinitely: it's split into segments as it grows, and old
segments get deleted once they fall behind a **low-water mark**, computed
one of two ways depending on the system:

- **Snapshot-based retention** (Zookeeper, Raft/etcd-style systems): the
  system periodically snapshots its full current state, records which log
  index that snapshot reflects, and anything before that index is safe to
  delete because the snapshot itself already captures it.
- **Time-based retention** (Kafka and similar systems where the log isn't
  the thing reconstructing state): segments are dropped purely by age — a
  fixed retention window (Kafka commonly defaults on the order of a week),
  regardless of whether every consumer has actually read them yet.

The consequence for a CDC consumer is concrete and unforgiving: **falling
behind the source's retention window doesn't degrade the pipeline, it loses
data permanently.** Under time-based retention in particular, nothing stops
a segment from being deleted just because a downstream consumer hasn't
caught up — retention is governed entirely by elapsed time, not by whether
every subscriber has consumed it. This turns "keep the CDC consumer's lag
under control" from a performance nice-to-have into a correctness
requirement: a pipeline reading log-based CDC needs to monitor its own
consumer lag against the source's actual retention window and alert well
before the gap closes, not just track throughput.

This is also the concrete reason [log scraping is called the messiest CDC
technique](change-data-capture.md): a shared production log's retention
policy is set by whoever owns that system for their own durability needs,
not for the pipeline's convenience, and a storage-pressured DBA rotating or
shrinking that retention window can silently shorten a CDC consumer's grace
period with no warning to the pipeline team.
