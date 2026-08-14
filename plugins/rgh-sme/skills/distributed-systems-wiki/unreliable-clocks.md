---
type: concept
title: Unreliable Clocks
description: >
  Each node's quartz clock drifts and jumps; wall-clock timestamps cannot
  order events across nodes, and a clock reading is really an uncertainty
  interval.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 8"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer et al.), ch. 23"
  - title: "Time, Clocks, and the Ordering of Events in a Distributed System"
    resource: "Time, Clocks, and the Ordering of Events in a Distributed System (Lamport), \"Physical Clocks\""
---

# Unreliable Clocks

Every node keeps time with its own quartz oscillator, which drifts with
temperature — Google assumes 200 ppm, about 17 seconds/day without correction.
NTP synchronization is limited by network round-trip time over an [unreliable
network](unreliable-networks.md) and can step a clock abruptly.

## Two kinds of clock — never confuse them

- **Time-of-day (wall-clock):** `CLOCK_REALTIME`,
  `System.currentTimeMillis()`. Returns calendar time (UTC). Can jump
  forward or *backward* when NTP resets it or on leap-second handling.
  **Unsuitable for measuring elapsed time** — a negative duration is possible.
- **Monotonic:** `CLOCK_MONOTONIC`, `System.nanoTime()`. Always moves
  forward at a near-constant rate; its absolute value is meaningless and not
  comparable across machines. The right clock for timeouts and duration
  measurement.

## Consequences for distributed ordering

- Ordering events across nodes by wall-clock timestamp is wrong: a causally
  later write on a node with a lagging clock gets an earlier timestamp, and
  [last-write-wins](last-write-wins.md) then silently discards the newer data.
  Causal order needs **logical clocks** — [Lamport
  timestamps](lamport-timestamps.md), [hybrid clocks](hybrid-clock.md), and
  [version vectors](version-vectors.md) — not physical time.
- A clock reading should be treated as an **uncertainty interval**
  [t − ε, t + ε], not a point. Most systems ignore this; Google Spanner's
  TrueTime API exposes it explicitly ([earliest, latest], ε ≈ 7 ms via GPS
  and atomic clocks per datacenter) and **waits out the interval** ("commit
  wait") before committing a transaction, so transaction timestamps are
  guaranteed non-overlapping — making timestamps usable for globally
  consistent snapshots and externally consistent (strictly
  [serializable](serializability.md)) transactions across continents. See
  [clock-bound wait](clock-bound-wait.md) for the mechanics of commit-wait
  and its cheaper read-side alternative, read restart.
- Leases and any logic of the form "check the clock, then act" are further
  undermined by [process pauses](process-pauses.md): the clock may be right
  and the process still acts on stale knowledge.

Clock problems are insidious because a slightly-wrong clock mostly works —
data is silently lost rather than anything crashing. If clock accuracy
matters, monitor clock offsets between nodes and evict bad clocks like any
other failed component.

## Why ε is bounded at all: drift plus periodic resync

The uncertainty bound ε isn't a hardware constant handed down from nowhere —
it falls out of two facts about ordinary clocks: each clock's rate is only
*approximately* correct (a bounded drift rate, historically around
10⁻⁶ for crystal oscillators — 200 ppm is the modern SRE-cited figure above,
same idea), and independent clocks left alone drift apart from each other
over time regardless of how tightly they started synchronized. Keeping any
two clocks within ε of each other therefore requires **periodic
resynchronization** — messages that carry a sender's clock reading and
nudge the receiver forward — sent often enough that drift between
resyncs never exceeds the target ε. This is the underlying reason NTP
polls regularly rather than syncing once at boot, and why a wider
resync interval (or a network too congested to deliver resync messages
promptly) directly widens the achievable ε: less frequent correction gives
drift more time to accumulate before it's caught. It's also why a
resynchronization round trip after a long outage or a suspected clock jump
is fast: a single message relayed through the cluster is often enough to
pull every clock back inside bounds, rather than waiting out a full drift
cycle.

This is also the deeper reason [Lamport (logical)
timestamps](lamport-timestamps.md) exist as a *separate* mechanism from
physical clocks rather than a replacement for them: no amount of resync
frequency makes physical clocks capture causality that never passed through
an observed message (see [causal ordering's limits](causal-ordering.md)) —
physical-clock synchronization bounds *drift*, logical clocks capture
*causation*, and they solve different problems that happen to both be
called "clocks."
