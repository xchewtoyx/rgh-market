---
type: concept
title: Segmented Log
description: >
  Splitting a write-ahead log into multiple size-bounded files instead of one
  unbounded file, so old data can be identified and deleted in whole units.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 4, Segmented Log"
---

# Segmented Log

A single [write-ahead log](write-ahead-log.md) file grows without bound: it
becomes slow to read at startup, and there is no easy way to reclaim space
for old entries out of the middle of one huge file. The fix is to split the
log into **segments** — roll to a new segment file once the currently open
one passes a configured size limit, keeping every earlier segment closed and
immutable.

Segments need a way to map a logical log index (log sequence number) to the
segment file that holds it. Two common approaches:

- Encode the segment's base offset directly into its filename (a well-known
  prefix plus the starting index), so the right file can be found without an
  extra index structure.
- Split each log index into a (file identifier, offset-within-file) pair.

Reads become two-step: given a starting index, first identify which
segment(s) could contain it — by scanning segments from most-recent backward
until finding the first whose base offset is at or below the requested
index — then read forward through those segments in order.

Segmentation is what makes bulk deletion practical: instead of trying to
excise old entries from inside a live file, a whole closed segment is deleted
at once whenever it falls entirely before the [low water
mark](low-water-mark.md). ZooKeeper and Raft/etcd-style consensus logs,
Kafka's storage layer, and conventional database commit logs (including
NoSQL stores) all use a size-based segment-rollover strategy for exactly this
reason.
