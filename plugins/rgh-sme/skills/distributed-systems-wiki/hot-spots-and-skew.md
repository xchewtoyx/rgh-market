---
type: concept
title: Hot Spots and Skew
description: >
  Disproportionate load on one partition or node — from key ordering, unfair
  splits, or single hot keys — which collapses a cluster's throughput to that
  of one node.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 6"
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing (Mace, Roelke, Fonseca), §6.1"
---

# Hot Spots and Skew

**Skew** is any unfairness in how data or load spreads across
[partitions](partitioning.md); a partition (or node) with disproportionate
load is a **hot spot**. In the worst case all traffic lands on one partition
and the cluster performs like a single node — paying distribution's
complexity for none of its throughput.

Sources and remedies:

- **Key ordering:** monotonically increasing keys under
  [key-range partitioning](key-range-partitioning.md) send all writes to one
  partition. Fix by [hashing](hash-partitioning.md) or key-prefixing.
- **Uneven partition sizes:** fixed boundaries that no longer match the data
  distribution — a [rebalancing](rebalancing-partitions.md) problem.
- **A single hot key:** a celebrity user's id receives millions of reads and
  writes; hashing doesn't help, since one key maps to one partition. Today
  this is the application's problem: a known technique is **key splitting** —
  append a random two-digit suffix to the hot key so its writes spread over
  100 sub-keys/partitions. Reads must then scatter-gather all 100 sub-keys
  and merge, and bookkeeping must track which keys are split — so apply it
  only to the few provably hot keys.

Skew is why "just add nodes" fails as a scaling answer: partitioning only
scales what it can spread. Detecting emerging hot spots (per-partition load
metrics) matters as much as the initial strategy, because workloads shift.

## Routing bugs masquerading as hot spots

Skew can also come from **request routing**, not partition keys. Per-node
metrics may show one DataNode at 150 ops/sec and another at 25 despite
uniform client access patterns — the keys are fair, but **which replica
serves each read** is not.

A diagnosed HDFS case combined two behaviors: the NameNode returned
rack-local replica locations in a **fixed sort order** (not randomized), and
the client always picked the **first** location in the list instead of
randomizing among rack-local candidates. Locally hosted replicas explain
part of the diagonal (prefer local copy), but non-local reads should spread
evenly; instead a static global precedence (host A beats D beats …)
concentrated load on whichever hosts sorted first.

Per-DataNode throughput metrics alone could not explain *why* — a shared
multi-tenant storage layer sees aggregate load without upstream client
identity or the metadata server's routing decision. Fixing routing-induced
skew requires correlating client → metadata lookup → actual serving node,
not just watching backend counters. See [read replica
selection](read-replica-selection.md).
