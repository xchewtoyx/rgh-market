---
type: concept
title: Causal Ordering
description: >
  The consistency model in which all observers see causes before effects — a
  partial order over operations, and the strongest model that stays available
  and fast under network partitions.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 9"
  - title: "Time, Clocks, and the Ordering of Events in a Distributed System"
    resource: "Time, Clocks, and the Ordering of Events in a Distributed System (Lamport), \"Anomalous Behavior\""
---

# Causal Ordering

Causal consistency guarantees that operations related by
[happens-before](happens-before-and-concurrency.md) are observed in that order
by every replica: nobody sees the answer before the question, the effect
before the cause. Operations that are *concurrent* may be observed in
different orders by different replicas — that's permitted and harmless.

The structural distinction from [linearizability](linearizability.md):

- Causality defines a **partial order** — causally related operations are
  ordered, concurrent ones are incomparable. Branching and merging timelines
  (as in version control) are the mental model.
- Linearizability imposes a **total order** — one global timeline, no
  concurrency at all. Linearizability therefore implies causal consistency.

Why it matters practically: **causal consistency is the strongest model that
does not become unavailable under network partitions and does not pay the
latency-proportional-to-network-uncertainty cost** of linearizability
(see [CAP](cap-theorem.md)). Many systems that "need linearizability"
actually only need causality — [consistent prefix
reads](consistent-prefix-reads.md) is exactly a causal-ordering demand, and
snapshot isolation's [consistent snapshots](snapshot-isolation.md) are causal.

Implementing it requires tracking what a client knew when it wrote —
[version vectors](version-vectors.md) generalize this, and
[Lamport timestamps](lamport-timestamps.md) provide a compact total order
consistent with causality. What causality alone cannot give you: deciding
*right now* between two concurrent claims (e.g. a unique username) — that
requires forcing an order, i.e. [total order
broadcast](total-order-broadcast.md) or [consensus](consensus.md).

## What causality can't see: out-of-band causal links

Every causal-consistency mechanism only tracks causality it can *observe* —
messages and dependencies that actually pass through the system. Lamport's
original illustration: person A issues a request through the system, then
phones a friend out-of-band, who issues a second, causally later request.
Nothing in the system carries the phone call, so the two requests can be
timestamped in either order — the system genuinely cannot know A's request
came first, because the only evidence of that precedence lived entirely
outside the events it tracks. No algorithm reasoning solely over its own
visible events can close this gap; the two available fixes both step
outside pure event-tracking:

- **Push the ordering burden onto the user**: expose the first operation's
  timestamp/token so a client can explicitly request "anything after this"
  on the second operation — [causality tokens](read-your-writes-consistency.md)
  are exactly this pattern, just scoped to a single client's own writes
  rather than an arbitrary out-of-band channel.
- **Use physical clocks synchronized tightly enough** to bound real-world
  ordering directly, rather than relying on message-observed causality at
  all — the motivating case for [clock-bound wait](clock-bound-wait.md) and
  TrueTime-style [uncertainty intervals](unreliable-clocks.md): a
  sufficiently synchronized physical clock can order two events correctly
  even when no message ever linked them.

This is a structural limit, not an implementation bug — it is why systems
that must respect *all* real-world precedence (not just precedence their own
messages reveal) reach for synchronized physical time instead of purely
logical causality tracking.
