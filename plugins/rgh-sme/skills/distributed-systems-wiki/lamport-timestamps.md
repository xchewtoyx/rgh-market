---
type: concept
title: Lamport Timestamps
description: >
  A (counter, node ID) pair maintained by max-and-increment on every message,
  giving a total order of events consistent with causality — but only after
  the fact.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 9"
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 22, Lamport Clock"
  - title: "Time, Clocks, and the Ordering of Events in a Distributed System"
    resource: "Time, Clocks, and the Ordering of Events in a Distributed System (Lamport), \"Logical Clocks\"; \"Ordering the Events Totally\""
---

# Lamport Timestamps

Naive ways to order events across nodes fail causality: per-node even/odd or
block-allocated sequence numbers drift with load, and
[physical timestamps](unreliable-clocks.md) suffer clock skew. Lamport
timestamps generate a total order that *respects*
[causality](causal-ordering.md) with almost no machinery:

- Each node keeps a counter and its unique node ID; a timestamp is the pair
  **(counter, node ID)** — compared by counter first, node ID as tiebreak.
- Every node and client attaches its maximum counter seen to every message;
  a recipient with a smaller counter jumps its own to
  `max(local, received) + 1`.

Because every causal chain passes the maximum along, if A happened before B
then A's timestamp is smaller. Concurrent operations get ordered too
(arbitrarily but consistently) — unlike
[version vectors](version-vectors.md), Lamport timestamps are more compact but
**cannot distinguish concurrency from causal dependency**.

Lamport's original terms for this: the **Clock Condition** is the
requirement "a happened-before b implies C(a) < C(b)" (the converse need not
hold — concurrent events may still land on different timestamps). It follows
from two local rules — increment between any two events on the same process,
and on receiving a message, jump to `max(local, received) + 1` — which is
exactly the counter behavior above; the paper's original names for these are
IR1 and IR2. Timestamps alone give a *partial* order matching causality; the
counter-then-node-id comparison above additionally makes that order *total*
(any two timestamps, even from unrelated events, are comparable), which is
what "arbitrarily but consistently" means above — the tiebreak is arbitrary,
but every node applies the same tiebreak and so agrees on the resulting
order.

In a data store, the "events" being ordered are value writes, so a Lamport
timestamp naturally becomes the version number in [versioned
value](versioned-value.md) — but the extra machinery (accepting a
request-carried counter and taking the max) is only needed once *multiple
independently-writable* nodes are in play. If a single [leader](leader-election.md)
is always responsible for all writes to a value, as in ordinary
[single-leader replication](single-leader-replication.md), a plain
incrementing counter suffices with no message-carried max needed — only the
leader ever increments it, and followers simply adopt the same numbers via
replication. [Generation clock](generation-clock.md) is itself a direct
application of this same technique to leadership changes rather than to
value writes.

The deeper limitation: the total order only materializes **after the fact**.
A node cannot decide "is this username claim safe to accept *right now*?"
because another node may be concurrently issuing a lower-timestamped claim it
hasn't heard about — knowing for sure means checking with every node, which
stalls on any node failure. Making the order known *at decision time* is
exactly what [total order broadcast](total-order-broadcast.md) adds.
