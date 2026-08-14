---
type: concept
title: Truth Defined by the Majority
description: >
  No node can trust its own perception of the system; authoritative decisions
  (node death, leadership) must come from a quorum majority.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 8"
---

# Truth Defined by the Majority

A node experiencing an asymmetric network fault (it can receive but not send),
or resuming from a [long pause](process-pauses.md), holds a confidently wrong
view of the world: it believes it is alive, connected, and perhaps still
leader, while the rest of the cluster has already declared it dead. Its own
perception is not admissible evidence.

Distributed systems therefore vest authority in a **quorum** — a majority of
more than n/2 nodes. If a majority declares a node dead, it is dead by
definition, and the node must comply even though it feels fine. Majorities are
used to declare nodes failed, elect leaders, and commit decisions, because two
disjoint majorities cannot exist simultaneously — the arithmetic that prevents
[split-brain](split-brain.md) and underlies [consensus](consensus.md).

Two operational corollaries:

- Holding a role (leader, lock holder) by majority vote is still not enough to
  *act* safely, because the holder may act on expired authority after a pause
  — enforcement must be receiver-side via
  [fencing tokens](fencing-tokens.md).
- This quorum is about *agreement on decisions*; the similarly named
  [read/write quorums](quorum-reads-and-writes.md) in leaderless replication
  are about replica overlap for data freshness. Related arithmetic, different
  purpose.
