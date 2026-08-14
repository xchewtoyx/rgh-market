---
type: concept
title: Read Replica Selection
description: >
  After metadata lookup returns candidate replicas, how the client picks
  which copy to read — local preference, rack locality, and randomization
  among ties determine load spread.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing (Mace, Roelke, Fonseca), §6.1"
---

# Read Replica Selection

Replicated storage separates **where replicas exist** (metadata lookup) from
**which replica serves this read** (client selection). HDFS illustrates a
common policy chain:

1. Prefer a **local replica** on the same host as the client if one exists.
2. Else prefer a **rack-local** replica (same network switch / failure
   domain).
3. Else choose among remaining replicas — typically **uniformly at random**.

Each step trades latency (local is cheapest) against **load balance** across
DataNodes. Randomizing among rack-local ties matters: if every client picks
the same tie-break rule on a list returned in fixed order, load concentrates
on whichever host sorts first even when replica *sets* are fair.

A production bug paired **non-randomized NameNode ordering** of rack-local
replicas with a client that always took the **first** list entry. Non-local
reads should have spread evenly; instead they followed a static global
precedence (host A whenever it held a replica, else D, and so on). Clients
and per-file distributions looked uniform; only cross-tier tracing
(client → NameNode `GetBlockLocations` → DataNode actually serving)
revealed the skew — backend-only metrics showed *that* load was uneven, not
*why*.

## Narrowing routing-induced skew

When per-node counters show skew but [partition keys look
fair](hot-spots-and-skew.md), eliminate causes in order before blaming hot
keys:

1. **Client access pattern** — is each client reading uniformly over keys or
   files? Skew here is a key-level problem, not replica selection.
2. **Replica placement** — does metadata return near-uniform replica sets
   per client? If not, placement or replication policy is the issue.
3. **Actual serving node** — given fair placement, which replica served each
   read? Skew here isolates selection policy, not data distribution.
4. **Ordering versus randomization** — strip out reads satisfied by a local
   replica (they legitimately follow host locality), then check whether
   remaining reads always take the first entry in the metadata server's
   returned list.

The HDFS case study followed exactly this ladder: uniform file reads and
fair replica sets, yet DataNode throughput ranged from ~150 to ~25 ops/sec
on identical hardware — only step 4 exposed static list ordering combined
with a client that never shuffled rack-local ties (~39% of reads were local,
explaining part of the host-diagonal, not the rest).

Design checks:

- Randomize or shuffle tie-breaking among equally good replicas.
- Do not assume symmetric behavior from symmetric replica sets — ordering
  bugs create [hot spots](hot-spots-and-skew.md) without hot keys.
- When diagnosing skew on shared storage, trace through [request
  routing](request-routing.md) decisions, not just per-node counters.

The fix class (HDFS-6268) improved sort randomization when no local replica
exists — both metadata ordering and client selection must cooperate for fair
spread.
