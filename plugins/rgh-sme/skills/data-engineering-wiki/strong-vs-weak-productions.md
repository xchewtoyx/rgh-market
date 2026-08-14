---
type: concept
title: Strong vs. Weak Productions
description: >
  Whether a streaming computation checkpoints a downstream record before or
  after emitting it, and the correctness-versus-latency tradeoff that choice
  controls.
sources:
  - title: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale"
    resource: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale (Akidau et al.), §6.1"
---

When a streaming computation both updates its own state and emits a
downstream record for the same input, the order it does those two things in
is a real design decision, not an implementation detail — MillWheel names
the two options **strong** and **weak productions**.

**Strong productions**: checkpoint the record to be produced in the *same
atomic write* as the state modification, before sending it downstream. If
the computation crashes after checkpointing but before the send completes,
it replays the checkpointed production on restart instead of re-running the
user code that generated it — so a downstream consumer never sees two
bit-wise-different records for what is logically the same output (e.g., two
different partial counts for the same aggregation window because a restart
recomputed the aggregate from a slightly different set of inputs). This is
the same
[atomic state-plus-output commit](stream-processing-fault-tolerance.md)
that genuine exactly-once processing requires; "strong productions" is
MillWheel's name for implementing it via checkpoint-before-send specifically.

**Weak productions**: broadcast the downstream record optimistically,
*before* persisting state, and only checkpoint afterward. This removes the
extra write from the hot path, but couples each stage's completion time to
waiting on its downstream ACK — combined with the baseline chance of any
one machine failing in a given interval, the probability of *some* stage in
the chain stalling on a failure grows with pipeline depth. A back-of-envelope
estimate at a 1%-per-minute per-machine failure rate puts a 5-stage pipeline
at nearly 5% odds of hitting a failure-induced stall in any given minute —
a cost that compounds specifically because weak productions serialize each
stage's ACK on the next stage's liveness.

**Mitigation**: rather than choosing one mode pipeline-wide, checkpoint a
small percentage of pending weak productions that have been waiting an
unusually long time for their downstream ACK (e.g., after a fixed delay like
one second) — this releases the upstream sender's resources for the slow
production without paying the strong-production write cost on the common,
fast-ACKing case. This turns strong vs. weak productions into a per-record,
adaptive choice instead of a single global setting.

Both strong and weak productions carry a resource and latency cost beyond
plain [at-least-once delivery](delivery-guarantees-exactly-once-vs-at-least-once.md);
a pipeline stage that is already idempotent regardless of retries (a
stateless filter, for example) gets no correctness benefit from either mode
and can reasonably disable both.
