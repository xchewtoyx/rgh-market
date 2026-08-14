---
type: concept
title: Generation Clock
description: >
  A monotonically increasing number bumped on every leadership change and
  tagged onto every log entry and request, so nodes can tell which of two
  conflicting entries or leaders is authoritative.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 6, Leader and Followers"
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 8, Paxos"
---

# Generation Clock

Repeated leader crashes can produce genuinely conflicting log entries at the
same log position — one leader accepted client A's request at index 1, a
later leader accepted client B's request at that same index — with no way to
tell which is authoritative from the log content alone. The fix is a
**generation clock** (also called epoch, term, ballot, or view number
depending on the protocol): a number incremented on every leadership change,
tagged onto every log entry and every request a leader issues.

On conflict, the entry or request carrying the higher generation always wins;
a new leader reconciles any uncommitted entries against generation numbers
before serving new writes. This also handles a second failure mode: a leader
that becomes temporarily disconnected and later resumes sending requests gets
those lower-generation requests rejected by nodes that have since elected a
newer leader — the generation clock is a built-in [fencing
token](fencing-tokens.md) for leadership itself, and the same "highest
generation wins, once voted always voted for that generation" rule is what
[Paxos](paxos.md) and [leader election](leader-election.md) protocols use to
guarantee at most one value or one leader is ever chosen per generation.

[Consensus](consensus.md) protocols generically describe this as nodes
electing a leader "for an epoch," with two overlapping majority quorums
guaranteeing a deposed leader's proposals cannot commit under the new one —
the generation clock is the concrete mechanism, carried in every message,
that makes that guarantee checkable locally by any node without a round
trip.

## It is a Lamport timestamp applied to leadership

The technique is a direct application of [Lamport
timestamps](lamport-timestamps.md): each server keeps an integer counter,
bumps it on a leadership-changing action, and piggybacks its value on every
outgoing message; a receiver sets its own counter to `max(own, received)`.
That's enough to order any two causally related leadership changes without a
shared clock. Concretely, the counter must survive a reboot, so it is
persisted with *every* entry in the [write-ahead
log](write-ahead-log.md) — a follower reads its last known generation back
from the log at startup, and the number then flows automatically into
follower logs as part of ordinary replication, because every leader message
and every appended entry carries the leader's current generation. A follower
that sees a request tagged with a lower generation than its own rejects it
and reports its own (higher) generation back; a leader that receives such a
rejection immediately steps down and adopts the higher number, without
needing to ask why.

## Same concept, different names, real systems

- **Raft** calls it **Term**.
- **ZooKeeper (ZAB)** calls it **epoch**, folded into every transaction id so
  every persisted transaction carries a generation marker.
- **Cassandra** stores a generation number bumped on every server *restart*
  (not on leadership change — Cassandra is leaderless) and propagates it via
  [gossip](gossip-dissemination.md): a peer that sees a higher generation
  than it has cached infers the other node restarted, discards its stale
  cached state for that peer, and re-fetches fresh state.
- **Kafka** creates and stores a controller epoch in ZooKeeper each time a
  new Controller is elected, included in every controller-to-broker request;
  a separate per-partition **LeaderEpoch** tracks whether a partition's
  followers are lagging in their own [high water mark](high-water-mark.md).
