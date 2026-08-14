---
type: concept
title: Fan-Out on Write vs. Fan-Out on Read
description: A capacity trade-off between precomputing a result at write time (cheap reads, expensive/spiky writes) and computing it on demand at read time (cheap writes, expensive reads).
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 1"
---

Many systems that aggregate data from many sources for delivery to a reader (a social feed, a notification inbox, a search index) face a choice about *when* to do the aggregation work: at write time or at read time. This is the **fan-out-on-write vs. fan-out-on-read** trade-off.

## Fan-Out on Read

The system stores raw data normally and computes the aggregate view on demand, at query time (e.g., a relational join across a `follows` table and a `posts` table for every timeline read).

*   **Write cost:** low and constant — a single row insert regardless of how many eventual readers there are.
*   **Read cost:** high and scales with the complexity of the join/aggregation, repeated on every read.
*   Favors workloads where reads are rare relative to writes, or where read latency is not tightly bounded.

## Fan-Out on Write

The system does the aggregation once, at write time, pushing the result into a precomputed per-reader structure (e.g., a "mailbox" or timeline cache written once per follower).

*   **Write cost:** scales with the number of interested readers (the fan-out factor) — one write amplifies into many.
*   **Read cost:** low and constant — a cheap fetch of the precomputed structure.
*   Favors workloads where reads vastly outnumber writes, since it moves the expensive aggregation off the hot read path.

## Worked Example

A timeline service with 4.6k posts/sec but 300k timeline reads/sec: fan-out-on-read would repeat an expensive join 300k times a second, so fan-out-on-write is chosen instead — each post is pushed into every follower's timeline cache once, making the far more frequent read operation cheap.

## The Skew Problem and the Hybrid Pattern

Fan-out on write assumes a bounded fan-out factor per write. Under [heavy-tailed load skew](heavy-tailed-load-skew.md) in the number of interested readers (e.g., a small number of accounts with an extreme number of followers), a single write's fan-out cost can spike by orders of magnitude and blow the write-side latency budget.

The standard mitigation is a **hybrid strategy**: apply fan-out-on-write for the bulk of the distribution (typical entities, bounded fan-out), and fall back to fan-out-on-read for the tail (the small number of entities whose fan-out would otherwise be unbounded), merging the on-demand result with the precomputed cache at read time. This bounds worst-case write cost without giving up the read-side cheapness that fan-out-on-write provides for the common case.

This is the same [read fan-out amplification](tail-latency-amplification.md) concern that shows up in request-serving call chains, applied to a data-propagation problem instead of a request-serving one — either way, an unbounded fan-out factor is the thing that must be capped or segmented.
