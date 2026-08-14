---
type: concept
title: Low Water Mark
description: >
  The log index below which a write-ahead log's entries are safe to discard,
  computed either from a durable state snapshot or from an age-based
  retention window.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 5, Low-Water Mark"
---

# Low Water Mark

[Segmenting](segmented-log.md) a [write-ahead log](write-ahead-log.md) makes
individual files manageable, but total disk usage still grows unboundedly
unless something actively reclaims space. The low water mark is the lowest
log index before which entries are known to be safe to delete; a background
task periodically recomputes it and deletes any closed segment that falls
entirely below it.

Two ways systems compute it:

- **Snapshot-based.** The mechanism used by most consensus implementations
  (ZooKeeper, etcd/Raft): the storage engine periodically takes a full
  snapshot of its state and records, alongside it, the log index that
  snapshot reflects. Once the snapshot is itself durably persisted, that
  index becomes the low water mark — any segment whose last entry falls
  below it is redundant, because a restart can reconstruct at least that much
  state from the snapshot instead of replaying the log. This only works
  because the log is the *sole* source the snapshot needs to reproduce state
  from (see [state machine replication](state-machine-replication.md)).
- **Time-based.** Used where the log is not the mechanism that reconstructs
  system state at all — Kafka being the canonical example. Segments are
  dropped purely by age once a configured retention window (e.g. seven
  weeks) has passed, with no coordination against any other subsystem about
  a "safe" index. This only works because Kafka's log *is* the durable
  record consumers rely on for a bounded window, not a recovery aid for
  some other store.

The choice tracks a broader distinction: a snapshot-based low water mark
assumes the log is disposable once its effect is captured elsewhere (crash
recovery use, as in a plain [write-ahead log](write-ahead-log.md)); a
time-based one assumes the log itself is the thing being consumed
(integration-backbone use, as in [log-based
messaging](log-based-messaging.md)) and is retained for its own read window
rather than for recovery.
