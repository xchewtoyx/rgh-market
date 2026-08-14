---
type: concept
title: Stream Processing Fault Tolerance
description: >
  Why a stream job can't restart from scratch after a failure the way a batch
  job can, and the two mechanisms (microbatching, checkpointing) used instead.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 11"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 6"
---

A batch job that fails partway through can usually just be rerun from the
beginning — the input is a bounded, static file or table. A stream job has no
such luxury: its input is unbounded, so "start over from the beginning" isn't
a bounded amount of work, and simply resuming from wherever processing
happened to stop risks either reprocessing already-handled events or skipping
ones that were in flight when the failure occurred. Two mechanisms recover
from this without redoing unbounded work:

- **Microbatching**: break the unbounded stream into a sequence of small,
  discrete batches (Spark Streaming's classic default was one-second
  batches), and reuse ordinary batch-job retry semantics on each one — a
  failed microbatch is simply rerun as a bounded unit. This trades some
  latency (results only land at the microbatch boundary, not truly
  continuously) for being able to fall back on well-understood batch retry
  logic.
- **Checkpointing**: periodically inject a barrier marker into the stream
  that triggers a snapshot of every operator's internal state (Apache Flink's
  approach), written to durable storage. On failure, operators roll back to
  the last completed checkpoint and resume from there — closer to true
  continuous processing than microbatching, at the cost of needing a
  consistent-snapshot mechanism across all operators in the job graph.

A related third mechanism, used by batch dataflow engines (Spark, Flink) more
than pure streaming systems, is **lineage-based recovery**: instead of
snapshotting operator state, the engine tracks the dependency graph that
produced each dataset partition (Spark's Resilient Distributed Dataset
lineage) and, on node failure, recomputes only the lost partition from that
lineage rather than replaying a checkpoint or a whole microbatch. This only
produces a correct result if every operator is deterministic — no reliance
on a random seed that isn't fixed, no dependence on wall-clock time inside
transform logic — since recomputing a partition has to yield output
byte-identical to what was lost, not merely equivalent.

Neither microbatching nor checkpointing is sufficient on its own to prevent
duplicate or missing
output after a restart — replaying a microbatch or rolling back to a
checkpoint can still redeliver events a downstream sink already wrote once.
Genuine
[exactly-once (effectively-once) processing](delivery-guarantees-exactly-once-vs-at-least-once.md)
requires the recovery mechanism to be paired with atomic, all-or-nothing
commits that bundle the operator's state update, its consumer offset advance,
and any downstream write together — so a rollback undoes all three or none of
them, never just some. Where a downstream sink can't participate in such an
atomic commit, the remaining gap has to be closed the same way it always is
in stream processing: making the job's output writes
[idempotent](idempotent-and-replayable-jobs.md), so a redelivered event after
a rollback overwrites state safely instead of duplicating it.

Bundling the state update and the downstream write atomically has a
real cost, and it's possible to relax it deliberately per stage rather than
paying it everywhere — see
[strong vs. weak productions](strong-vs-weak-productions.md) for the
resulting latency/correctness tradeoff and a mitigation that checkpoints only
the stragglers.

**Spark Streaming vs. Flink vs. Dataflow (implementation contrast).**
Spark Streaming's microbatch model treats a stream as a continuous series of
RDDs, each processed with batch shuffle correctness — simple and well
understood, but latency accumulates at every stage in deep pipelines and the
whole operation chain may replay on failure (checkpointing RDDs is primarily
a performance optimization). Flink injects numbered snapshot markers into
source streams; each operator copies state externally on marker receipt and
forwards the marker, producing a progressively built consistent snapshot
(Chandy–Lamport style) without stopping the world. Sinks wait for
`snapshotComplete` before emitting non-idempotent output, adding latency only
at sink boundaries. Flink assumes relatively rare failures and static task
allocation, enabling ordered TCP channels that resume from the last good
sequence number. Dataflow handles constant load-balancing and worker churn
with upstream-backup RPC shuffle (at-least-once transport plus per-record-ID
dedup in durable storage), checkpointing transform outputs before delivery,
and Bloom-filter fast paths to avoid catalog lookups on records provably never
seen before. Each approach pairs its recovery mechanism with
[idempotent or atomic sink patterns](delivery-guarantees-exactly-once-vs-at-least-once.md)
to close the end-to-end gap.

**Flink savepoints** extend checkpointing: restart an entire pipeline from
any chosen past point, extending durable replay from the transport layer to
full pipeline state — among the first practical steps toward graceful
evolution of long-running streaming jobs. See
[streaming platform lineage](streaming-platform-lineage-millwheel-to-beam.md).
