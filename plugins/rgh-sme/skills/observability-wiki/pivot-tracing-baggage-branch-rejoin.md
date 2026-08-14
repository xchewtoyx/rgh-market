---
type: concept
title: Pivot Tracing Baggage Branch and Rejoin
description: When request execution branches and rejoins across threads or async boundaries, baggage uses interval tree clock versioning so happened-before joins remain correct — dividing IDs on branch and merging instances on rejoin.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §5"
---

[Pivot Tracing baggage](pivot-tracing-baggage.md) must preserve the [happened-before relation](happened-before-join.md) correctly when execution **branches and rejoins** — parallel threads, fork/join patterns, async callbacks. The implementation uses **interval tree clock** versioning:

Baggage maintains one or more versioned instances, each with a globally unique interval-tree ID. Only one versioned instance is "active" for any given branch.

- **On branch:** the active instance's interval-tree ID is divided into two globally unique, non-overlapping IDs; each branch receives one; each side gets a copy of the baggage and creates a new active instance using its half of the divided ID.
- **On pack:** a tuple is placed into the active instance for its branch. To unpack from baggage with multiple instances, tuples are unpacked from each instance and combined according to the query's logic.
- **On rejoin:** a new active instance merges contents from each side's active instances; the new ID joins the IDs from each side; inactive instances from each branch are copied over and duplicates discarded.

The baggage API exposes `split()` for branching and `join(b1, b2)` for rejoining. Storage uses thread-local variables with lazy protocol-buffer serialization — baggage is only deserialized when an application actually packs or unpacks, minimizing overhead for applications that don't participate in a given query. Developers must implement baggage propagation at thread, process, and async execution boundaries — typically by adding a baggage field to existing request contexts and RPC headers. See [context propagation](context-propagation.md) for the general intraprocess/interprocess propagation problem this addresses.
