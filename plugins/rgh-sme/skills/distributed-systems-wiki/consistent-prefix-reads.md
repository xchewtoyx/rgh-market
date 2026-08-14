---
type: concept
title: Consistent Prefix Reads
description: >
  The guarantee that readers observe writes in an order that respects
  causality — never an answer before its question.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
---

# Consistent Prefix Reads

If a sequence of writes happens in a certain order, anyone reading them should
see them in that order. Violated when an observer sees an effect before its
cause — e.g. sees Mrs. Cake's answer replicated before Mr. Poons's question,
making the conversation nonsensical.

This anomaly is characteristic of **partitioned (sharded) databases**: each
[partition](partitioning.md) replicates independently, so there is no global
ordering of writes across partitions, and a reader may see one partition in a
newer state than another. In a single-leader system without partitioning, the
leader's log provides a total order and the anomaly cannot occur.

Mitigations:

- Route causally related writes to the same partition, so their order is
  preserved by that partition's log — not always efficient.
- Track [causal dependencies](happens-before-and-concurrency.md) explicitly,
  so a replica can delay exposing a write until its causes are visible; this
  is the territory of [causal ordering](causal-ordering.md) rather than a
  per-partition fix.
