---
type: concept
title: Fencing Tokens
description: >
  Monotonically increasing tokens issued with each lease or lock grant, letting
  the protected resource itself reject writes from deposed zombie leaders.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 8"
  - title: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale"
    resource: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale (Akidau et al.), §6.2"
---

# Fencing Tokens

A client holding a lease or [distributed lock](distributed-locks.md) can never
be sure it still holds it — a [pause](process-pauses.md) or network delay may
have let it expire and pass to another node. Asking the client to check is
useless (the answer is stale immediately); the fix is to make the **protected
resource** enforce ordering:

1. The lock service (e.g. ZooKeeper, whose transaction id `zxid` serves this
   role) issues a **monotonically increasing fencing token** with every grant.
2. The client includes the token in every request to the protected resource
   (storage service, etc.).
3. The resource remembers the highest token it has processed and **rejects any
   request with an older token**.

A zombie leader resuming from a pause presents its stale token and is turned
away; the write that would have corrupted data becomes a visible error. Note
the requirement this places on the resource itself: it must participate by
checking tokens — a lock protocol whose safety depends purely on client
good behavior is broken under pauses and delays. This is the robust form of
the crude STONITH approach to [split-brain](split-brain.md), and it assumes
nodes are honest-but-unreliable; deliberately lying nodes are the
[Byzantine](byzantine-faults.md) realm.

## Per-key fencing without a dedicated lock service

The same pattern applies below the level of a whole leader election: a
stream processor that shifts a given key's work between machines (rebalance
or failure) needs exactly one worker able to write that key's state at a
time, and no ordinary transaction guarantees this by itself — a
transaction only protects against concurrent writers *it* knows about, not
a "zombie" from a superseded worker whose write is simply delayed on the
wire. MillWheel attaches a **sequencer token** to every state write for a
key; a new worker taking over that key invalidates the previous sequencer
before doing anything else, and the backing store's write path rejects any
write presenting an already-invalidated sequencer. This closes the exact
race fencing tokens are for: a successor worker rebuilding its in-memory
state from the store, followed by a stale writer's delayed write landing
*after* that rebuild completed, would otherwise silently corrupt soft
state the successor believes is authoritative — a hazard transactions alone
cannot prevent, because the successor's read and the zombie's write are
each individually valid; only sequencing them against each other closes
the gap.
