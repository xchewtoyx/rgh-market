---
type: concept
title: Membership Services
description: >
  Agreeing on which nodes are currently alive members of a cluster — a
  consensus decision, because failure detection alone cannot produce an
  agreed answer.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 9"
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §4.8"
---

# Membership Services

A cluster must know which nodes are currently members — to assign work,
place replicas, count [quorums](truth-defined-by-majority.md), and elect
leaders. But on an [unreliable network](unreliable-networks.md),
[failure detection](timeouts-and-failure-detection.md) is guesswork: a node
declared dead by one observer looks alive to another.

A membership service resolves this by coupling failure detection with
[consensus](consensus.md): nodes *agree* on the current membership list, so
even a wrong verdict (declaring a live-but-slow node dead) is at least a
*consistent* verdict everyone acts on. It matters less that the answer is
occasionally wrong than that the cluster doesn't split over it.

In practice membership is usually delegated to a
[coordination service](coordination-services.md): each node holds an
ephemeral entry tied to its heartbeat session, and watchers see a single
agreed view of who is in. Downstream decisions — which node owns which
[partition](partitioning.md), who is eligible for
[leader election](leader-failover.md) — key off that agreed list.

## The AP alternative: no agreed membership at all

An [AP](cap-theorem.md) system that never needs a single leader can opt out
of this problem entirely rather than solve it: Dynamo treats *permanent*
membership change (a node genuinely joining or leaving) as an **explicit,
administrator-driven** action rather than something automatically inferred
from failure detection — an operator issues the join/remove, the receiving
node persists it with a timestamp, and the change then spreads via
[gossip](gossip-dissemination.md) (reconciling each node's local membership
*history*, since a node can be removed and re-added more than once) rather
than through consensus. A handful of designated **seed nodes**, discoverable
by all members through an external mechanism, exist purely so that two
independently-bootstrapped parts of the ring reliably reconcile with each
other — without them, joining node A and joining node B could each believe
themselves full members while remaining unaware of one another, a logical
partition of the membership view itself.

*Transient* failure, by contrast, is deliberately left **local and
un-agreed**: node A considers node B down simply because B stopped
responding to A's own messages — even if B is answering C's just fine — and
routes B's share of requests elsewhere until B responds again. No global
failure-state view is constructed or needed, because the only thing a
transient-failure verdict controls is which node *this* observer tries
next, not a cluster-wide decision like "who is allowed to be leader." This
is the same distinction [truth defined by the
majority](truth-defined-by-majority.md) draws for authority-bearing
decisions — an individual node's private view is never trustworthy for
*those* — but it doesn't apply here, because a leaderless system has no
authority-bearing role riding on the answer. The trade-off is real: Dynamo's
own design keeps every node aware of every other node's placement (full
membership, propagated as one gossiped table), and that table's size grows
with cluster size in a way that stops scaling gracefully into the tens of
thousands of nodes — the cost an agreed, consensus-backed membership list
avoids by keeping a much smaller ensemble authoritative instead.
