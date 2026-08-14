---
type: concept
title: Consensus
description: >
  Getting nodes to irrevocably agree on a value despite crashes and network
  faults — the primitive behind leader election, atomic commit, and
  replicated logs.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 9"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer et al.), ch. 23"
---

# Consensus

The problem of getting several nodes to **agree on a value** such that the
decision is final, despite node crashes and an [unreliable
network](unreliable-networks.md). Formally, an algorithm must satisfy:

1. **Uniform agreement** — no two nodes decide differently.
2. **Integrity** — no node decides twice.
3. **Validity** — the decided value was actually proposed by some node.
4. **Termination** — every non-crashed node eventually decides (the liveness
   property that distinguishes fault-tolerant consensus from
   [2PC](two-phase-commit.md), which blocks on coordinator failure).

Consensus is the primitive beneath problems that look different but are
equivalent: [leader election](leader-failover.md) (agree who leads, preventing
[split-brain](split-brain.md)), atomic commit (agree commit-or-abort),
linearizable compare-and-set, distributed locks and membership, and
[total order broadcast](total-order-broadcast.md) (repeated consensus on the
next message). Uniqueness/ordering decisions that a single node would make
trivially all reduce to consensus once no single node can be trusted to stay
up.

## FLP impossibility — and why consensus works anyway

Fischer, Lynch, Paterson proved no deterministic algorithm can *guarantee*
termination in a fully asynchronous [system model](system-models.md) if a node
may crash. Practical algorithms escape by assuming **partial synchrony**:
timeouts, randomization, or clocks let them make progress whenever the system
behaves reasonably, while safety holds unconditionally.

## How practical algorithms work: epochs and quorums

[Paxos](paxos.md)/Multi-Paxos, Raft, Zab, and Viewstamped Replication share a
shape:

- Nodes elect a leader for an **epoch** (ballot/view/term — a monotonically
  increasing number; see [generation clock](generation-clock.md) for the
  concrete mechanism). Leadership is only ever *within* an epoch. See [leader
  election mechanics](leader-election.md) for how the vote itself runs, both
  in-cluster and delegated to an external store.
- Both electing a leader and committing each proposal require a **majority
  quorum** (> n/2). The two quorums must overlap, so if a higher epoch has
  started, at least one voter on any proposal knows about it — a deposed
  leader's proposals cannot commit. Epoch comparison is a
  [fencing](fencing-tokens.md) mechanism built into the protocol.
- With 2f + 1 nodes, up to f crashes are tolerated
  ([majority rule](truth-defined-by-majority.md)) — size the ensemble from
  the failures to survive: 3 nodes tolerate 1, 5 tolerate 2.

In practice these algorithms are used not for one-shot decisions but as
[replicated logs](replicated-log.md) — see [state machine
replication](state-machine-replication.md) — and consumed via
[coordination services](coordination-services.md) rather than implemented
in-house.

## Costs

Every decision waits on a majority round-trip; a partitioned minority stalls
(by design — see [CAP](cap-theorem.md)); frequent leader elections under
flaky networks can leave the system voting instead of working. Throughput
degrades faster than cluster size grows — empirically closer to O(1/n²) than
linear, because every additional voter adds a round trip to every write — so
real quorum-based systems overwhelmingly settle on three or five nodes rather
than scaling the ensemble up for extra tolerance: going from 3 to 4 nodes
buys nothing (quorum for both n=3 and n=4 tolerates only 1 failure; reaching
2 requires jumping straight to 5), so an even node count is close to a pure
throughput tax. Use consensus where agreement is genuinely required, not as a
default.
