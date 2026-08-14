---
type: concept
title: Stream Processing Watermarks
description: >
  A per-computation bound on the timestamps of records still to arrive,
  defined recursively over the dataflow graph and computed by aggregating
  every worker's in-flight and persisted state through a sharded, journaled
  central authority.
sources:
  - title: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale"
    resource: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale (Akidau et al.), §2, §4.5, 5.2, 7.2"
---

# Stream Processing Watermarks

A stream-processing computation never sees a stream's full input at once, so
it needs a way to answer "have I seen everything up to time T yet?" without
waiting for the (open-ended) stream to end. The **low watermark** answers
this: a bound on the timestamps of records that can still arrive at a
computation. Once the watermark passes T, the computation — and anything
downstream of it — can treat its view of data timestamped before T as
complete.

This matters most for detecting an *absence*. With inputs arriving from all
over a distributed system, generation time and arrival time diverge, so a
gap in the data is ambiguous by itself — is expected traffic merely delayed
on the wire, or did it genuinely never happen (e.g. a region losing network
access)? A raw record stream can't distinguish the two. Once the watermark
for a stage has advanced past a given timestamp without the expected data
showing up, that ambiguity resolves: the data was not merely late, because
the watermark's definition (below) already accounts for everything still
possibly in flight. This is also why the mechanism has to tolerate
out-of-order arrival as the norm rather than the exception — the watermark
is deliberately defined without requiring the *input* stream itself to be
timestamp-sorted.

## Definition

The watermark is defined recursively over the dataflow graph. A
computation's **oldest work** is the timestamp of its oldest unfinished
record — in-flight, stored, or pending delivery. Then:

> low watermark of A = min(oldest work of A, low watermark of C, for every
> computation C that feeds into A)

A computation with no inputs (a source) has its watermark equal to its
oldest work directly. Because the definition takes a minimum over every
upstream source and the computation's own pending work, the watermark can
never claim more completeness than the slowest contributor actually
supports — and the system additionally guarantees it is **monotonic**,
never moving backwards, even when late data arrives.

External data enters through **injectors**, which seed a watermark for the
rest of the pipeline by publishing their own estimate of their oldest
still-outstanding external work (e.g., for a file-reading injector: the
minimum creation time among files not yet fully read). This measurement is
necessarily an estimate — an injector doesn't have perfect knowledge of an
external system's pending work — so late records (arriving behind the
current watermark) are an expected, low-rate occurrence rather than a bug
(one production pipeline measured roughly 0.001% of records arriving late).
An injector distributed across multiple processes can report one aggregate
watermark for the group, robust to individual process failures, by having
the user declare the expected set of injector processes up front. Whether a
late record is dropped (while tracking how much was dropped, for
visibility) or used to retroactively correct an already-emitted aggregate is
an application-level choice, not something the watermark mechanism dictates.

## Aggregation, bottom-up

The recursive definition above is a specification, not an implementation —
computing it in a distributed system requires a **central authority**: a
component that tracks every computation's watermark value and journals it to
persistent state, so a process failure cannot cause it to report an
incorrect (e.g. regressed) value. Each worker reports timestamp information
for all the work it owns —
checkpointed and pending productions, pending timers, persisted state — up to
the central authority. A worker can compute its own contribution cheaply,
straight from its in-memory structures, without querying the backing store
(the same trusted-in-memory-state property [key interval
ownership](key-interval-load-balancing.md) relies on). Because work is
assigned by key interval, watermark updates are bucketed and reported by key
interval too.

The authority assembles these per-interval reports into an **interval map**
covering the whole computation. A gap in that map (an interval that hasn't
reported yet) doesn't stall the watermark: the authority just keeps the last
known value for the missing interval until a fresh report arrives — a
conservative default that can only make the watermark *more* conservative,
never wrong in the unsafe direction. The authority then broadcasts a single
low watermark value per computation.

**Consistency during handoff.** The same [sequencer / fencing
token](fencing-tokens.md) scheme used for key-interval state writes is
attached to watermark updates too, so only the current owner of an interval
can move its watermark forward — a superseded worker's stale report cannot
regress it.

Downstream computations subscribe to their upstream computations' broadcast
watermarks and compute their own **effective input watermark as the minimum
across all of them**. This minimum is deliberately computed by each
*worker*, not by the central authority, so that the authority's own reported
value can never run ahead of what workers actually observe — preserving the
invariant that the watermark is always a safe lower bound, never an
optimistic guess.

**Scale.** The authority itself is sharded across machines, each handling one
or more computations; MillWheel measured this scaling to 500,000 key
intervals with no loss of performance.

## Heuristic (percentile) watermarks

Because the authority holds a global summary of all pending work, it can
optionally strip outliers and report an approximate watermark instead of a
strict one — e.g. a **99% watermark** reflecting the progress of 99% of
record timestamps in the system rather than the very last straggler. A
consumer that only needs approximate results (and would rather not wait on
stragglers at all) can subscribe to this heuristic value for lower latency,
trading completeness for speed on a per-consumer basis.

## Why this holds together

Nothing about this scheme depends on the underlying streams arriving in
strict timestamp order — the watermark is derived from aggregated
in-flight-plus-persisted state, not from observing an already-sorted input.
Routing every update through one global source of truth (the sharded
authority) is what rules out the one failure mode that would make the
watermark useless: its value moving *backwards*, which would falsely tell a
downstream consumer that already-seen data is newly incomplete.

The watermark's main consumer-facing use is triggering [per-key
timers](stream-processing-timers.md) once it passes a value the application
cares about.
