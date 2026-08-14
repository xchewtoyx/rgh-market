---
type: concept
title: Read-Your-Writes Consistency
description: >
  The guarantee that a user who submits a write will see that write on
  subsequent reads, despite reading from lagging replicas.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
---

# Read-Your-Writes Consistency

Also called read-after-write consistency. Under [replication
lag](replication-lag.md), a user can submit data, reload the page from a stale
follower, and conclude their data was lost. Read-your-writes guarantees each
user always sees *their own* updates (it promises nothing about other users'
writes).

Implementation techniques:

- **Route by ownership:** read anything the user may have modified from the
  leader (e.g. a user's own profile), everything else from followers. Works
  when user-editable data is a known small subset.
- **Time-based routing:** after any write, route that user's reads to the
  leader for a window (e.g. one minute); also stop reading from any follower
  more than a threshold behind.
- **Causality tokens:** the client remembers the timestamp or log position
  (LSN) of its last write; a follower serving the read must have applied
  writes up to that position, or the read waits/goes elsewhere — see
  [follower reads](follower-reads.md) for the concrete
  [versioned-value](versioned-value.md)-based mechanism.
- **Cross-device:** the same user on phone and laptop expects to see writes
  made on either — the write timestamp must be centralized rather than kept in
  device-local state, and different devices may route to different datacenters,
  complicating "read from the leader".

This is a session guarantee: cheap to provide per-user without global
coordination, far cheaper than [linearizability](linearizability.md).

Whichever technique is chosen, classify queries into "must be fresh" versus
"can be stale" **when the query is first written**, not as a later
retrofit — auditing an existing codebase query-by-query to sort this out
afterward is expensive, so if it's cheap now to route through a dedicated
read-vs-write connection even with zero replicas today, that discipline pays
off when replicas are added later. A cautionary shape this failure mode
takes in practice: a component doing occasional "read soon after write"
against a follower keeps seeing stale data, so as a quick fix its reads (and
writes) both get pinned to the leader — reasonable while the component runs
rarely, but the ad hoc fix has no capacity accounting behind it, and as the
component's usage grows toward continuous traffic the leader silently
absorbs load nobody planned for, until it overloads and forces the proper
fix under outage pressure instead of by design.
