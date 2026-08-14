---
type: concept
title: Hybrid Clock
description: >
  A (wall-clock time, tick counter) timestamp that is monotonic and
  causality-preserving like a Lamport timestamp, but stays anchored to real
  date-time so versions can be queried "as of" an actual moment.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 23, Hybrid Clock"
---

# Hybrid Clock

A plain [Lamport timestamp](lamport-timestamps.md) counter orders writes
correctly but is an opaque integer — a client can't ask a store for "the
value as of 2020-01-01" against a bare counter. A hybrid logical clock fixes
this by keeping a two-part timestamp, `(wallClockTime, ticks)`, compared by
wall-clock time first and tick count as tiebreaker: monotonically increasing
like a Lamport timestamp, but anchored to a real calendar time.

On a local action, the clock reads the system clock; if wall-clock time
hasn't advanced past what this clock last recorded — a stall, or NTP
stepping the clock backward — it instead bumps only the tick counter on the
existing wall-clock value, which is exactly how it stays monotonic through a
wall-clock hiccup. On receiving a message carrying a timestamp, it takes
`max(local reading, current value, received timestamp)` and always adds one
tick to that maximum — the identical causal-ordering guarantee a [Lamport
timestamp](lamport-timestamps.md) gives, just expressed with a wall-clock
anchor.

## What the timestamp anchor buys

Because the version *is* a real timestamp, a client can query "as of" an
actual date-time directly — CockroachDB's
`AS OF SYSTEM TIME '2016-10-03 12:45:00'` constructs exactly this kind of
timestamp and does an ordinary floor-lookup against it, the same lookup
mechanism [versioned value](versioned-value.md) uses for point-in-time
reads.

## Assigning one timestamp across a distributed transaction

Combines directly with [two-phase commit](two-phase-commit.md): at commit
time, every participant's write must land at the *same* timestamp, even
though each participant's own clock may be running ahead. The coordinator
collects the write-timestamp each participant actually used during prepare
and takes the maximum across all of them as the single commit timestamp —
the same "pick the max reported by any prepare response" mechanism, carried
out over hybrid timestamps instead of plain integers, and folded into the
prepare phase that's already collecting responses from every participant.

Hybrid clocks still only give a **partial order**: two writes on
independent nodes with no causal link between them can't be ordered by
timestamp alone, and a read served by a node whose clock lags can miss a
genuinely earlier write. Closing that gap needs an explicit wait for clock
uncertainty to resolve — see [clock-bound wait](clock-bound-wait.md).
MongoDB, CockroachDB, and YugabyteDB all use hybrid clock variants for MVCC
storage versions and cross-transaction causality.
