---
type: concept
title: Paxos
description: >
  The two-phase (prepare, accept) protocol for reaching agreement on a single
  value without a stable leader, and why real systems build a replicated log
  on top of it rather than run it directly.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 8, Paxos"
---

# Paxos

[Leader and followers](leader-election.md) solves agreement cheaply once a
stable leader exists — it just decides and pushes the decision out. Paxos,
published by Leslie Lamport in "The Part-Time Parliament," solves the harder
case: reaching agreement on a single value with **no** stable leader, where
competing nodes independently try to gather a quorum for their own proposed
value, and any node can crash or disconnect mid-protocol — even after
already achieving a quorum but before telling anyone.

## The protocol

Three phases, run by a **proposer** against a set of **acceptors**:

1. **Prepare** — the proposer picks a [generation](generation-clock.md)
   number (combining a counter with a node id for tie-breaking, e.g.
   `[2,a] > [1,e] > [1,a]`) and asks a quorum of acceptors to promise not to
   accept anything from an earlier generation, discovering in the responses
   any value an acceptor has *already* accepted in an earlier round.
2. **Accept** — if a quorum promises, the proposer sends its proposed value
   for that generation; acceptors accept unless they've since promised a
   higher generation to someone else.
3. **Commit** — once a quorum accepts, the proposer tells everyone the value
   is chosen. (The original 1998 paper omits this phase — proving a single
   value is chosen is sufficient for the safety proof — but real systems need
   it so every node actually learns the outcome.)

**Flexible Paxos** (Heidi Howard) later showed the true requirement is not
that both quorums be *majorities*, only that the prepare and accept quorums
*overlap*.

## The rule that makes it converge

If a proposer's prepare responses include a value some acceptor already
accepted at an earlier generation, the proposer **must** re-propose that
value — even if its own client wanted something else — always preferring the
highest-generation previously-accepted value seen. Because any successful
prepare quorum is guaranteed to overlap with any earlier accept quorum, at
least one acceptor in a fresh round always knows about the highest-generation
value chosen so far, and is forced to surface it. This is what lets the
protocol converge on one value even when proposers crash mid-round, get
raced by other proposers, or never learn the outcome themselves — a later,
completely unrelated node running its own prepare phase for an unrelated
client request can still be forced to discover and re-commit an
already-chosen value. Explicit rejection of stale prepare/accept messages is
only a performance optimization (it lets a stale proposer learn faster and
retry); an acceptor could just as safely ignore them and the protocol still
converges.

## Fundamental limits

Two competing proposers can indefinitely leapfrog each other's generation
numbers without either completing an accept round — the FLP impossibility
result proves even a single slow or faulty node can prevent a cluster from
ever choosing a value. The standard mitigation (not a fix) is a random
back-off delay before retrying with a new generation, making one proposer
likely to finish first. The trade-off is unavoidable and explicit: **Paxos
guarantees safety, not liveness** — exactly one value is ever chosen and,
once chosen, never overwritten, but *when* (or whether) that happens is not
guaranteed.

## Why real systems don't run bare Paxos

Basic ("single-decree") Paxos is proven for agreeing on exactly *one* value.
Reusing it for a stream of writes needs extra machinery outside the formal
protocol (resetting per-key acceptor state after each commit, which has known
correctness pitfalls unless committed values are tracked and consulted during
prepare) — and reads are not free, either: because only the prepare phase can
surface an already-chosen value, a `get` has to run the full protocol too (a
no-op proposal). This is exactly why production systems build a
[replicated log](state-machine-replication.md) instead — Multi-Paxos or Raft
— running the agreement protocol once per log position rather than once per
independent value, reusing an established leader across many decisions
instead of paying the two-phase cost on every one. A middle ground exists:
running one independent Paxos instance per key (Cassandra's lightweight
transactions) avoids needing a leader at all, at the cost of the
per-operation two-phase overhead and the read-is-a-write wrinkle above.

Raft and other consensus algorithms reuse Paxos's core ideas — a two-phase
shape, [quorums](truth-defined-by-majority.md), and a
[generation clock](generation-clock.md) — structured differently to make the
common case (an established, stable leader) cheap.
