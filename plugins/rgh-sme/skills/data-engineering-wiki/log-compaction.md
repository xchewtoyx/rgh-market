---
type: concept
title: Log Compaction
description: >
  Retaining only the latest message per key in a streaming log so the topic
  itself can serve as a rebuildable snapshot, not just a transient feed.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 11"
---

A [log-based message broker](log-based-message-broker.md) can run a
background process that discards obsolete messages for the same key,
keeping only the most recent one (and eventually removing **tombstones** —
explicit "this key was deleted" markers — once consumers have had a chance to
see them). This is log compaction, and it changes what the log is for: an
uncompacted topic is a pure event feed, but a compacted topic can be read from
offset 0 to reconstruct a complete current snapshot of every key's latest
value, because every superseded intermediate write has already been dropped.

This makes a compacted topic usable as a durable, replayable substitute for a
keyed table: a new consumer that needs the current state of every key doesn't
need a separate bulk-load step — it just replays the compacted topic from the
start, which is far cheaper than replaying an uncompacted full history. It's
the concrete mechanism that lets [change data capture](change-data-capture.md)
streams double as a rebuildable copy of the source table's current state, not
only a feed of individual changes, and it's what makes
[stream replay for reprocessing](stream-replay-for-reprocessing.md) practical
at scale for state-reconstruction use cases specifically — replaying an
uncompacted history from the start of retention would otherwise mean
processing every historical write a key ever had, not just its current value.

The cost is on the write side: compaction is a background housekeeping
process, and a pipeline relying on it must tolerate eventual (not instant)
removal of superseded messages, plus the added storage and I/O the compaction
process itself consumes.
