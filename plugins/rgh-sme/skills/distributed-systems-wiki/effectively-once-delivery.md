---
type: concept
title: Effectively-Once Delivery
description: >
  "Exactly-once" semantics in stream processing: faults cause reprocessing,
  but atomic offset+state+output commits or idempotent writes make the net
  effect appear once.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 11"
  - title: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale"
    resource: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale (Akidau et al.), §6.1.2–6.1.3"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 6"
---

# Effectively-Once Delivery

Exactly-once *delivery* is impossible on an
[unreliable network](unreliable-networks.md) — a consumer crash after
processing but before acknowledging always forces redelivery. What systems
actually provide is **effectively once**: messages may be *processed* more
than once, but the *net effect* equals a single processing.

## Accuracy versus completeness

**Accuracy** means no record is dropped or duplicated in the processed
output. **Completeness** means every record that should be included actually
is — including late-arriving data up to a configured wait boundary. A
streaming system can be accurate while deliberately dropping records that
arrive after a lateness deadline; that is a completeness knob, not an
accuracy failure. Batch jobs have the same gap: a nightly job over
"yesterday's data" is accurate for its window but incomplete for anything
collected after the cutoff.

The historical **Lambda Architecture** (fast streaming layer plus slower
batch recomputation) traded accuracy for complexity: two pipelines with
different semantics, unpredictable divergence between them, and latency high
enough that users stopped trusting the stream. End-to-end accurate streaming
collapses this into one codebase when technically feasible.

## User code and side effects are out of scope

Frameworks that guarantee at-least-once (or better) **do not guarantee user
transform code runs only once per record**. Under worker failure, the same
record may be executed multiple times or concurrently on different workers;
the framework ensures only one invocation's output **wins** downstream. No
known at-least-once system executes arbitrary user code exactly once.

Consequence: **non-idempotent side effects** (calling an external API,
sending email) are not covered by the framework's exactly-once claim. There
is no general way to atomically commit internal pipeline state with an
external side effect. Sinks must restructure work into idempotent operations
or insert a stabilizing shuffle before the side-effect step (below).

Stream jobs are infinite, so fault tolerance can't be "restart from
scratch". The recovery mechanisms:

- **Microbatching** (Spark Streaming): chop the stream into small batches
  and reuse batch retry semantics per batch.
- **Checkpointing** (Flink): barrier markers flow through the stream;
  operators periodically snapshot their state durably and roll back to the
  last checkpoint on failure.

Both guarantee *internal* state is consistent after replay, but anything
already sent to the outside world during the replayed interval happens
twice. Closing that gap needs one of:

- **Atomic commit:** the state update, the input offset advance, and the
  downstream output are committed together as one transaction (Kafka
  transactions, VoltDB export streams) — a scoped, homogeneous cousin of
  [distributed atomic commit](two-phase-commit.md) kept cheap by staying
  inside one framework.
- **[Idempotent writes](idempotency.md):** tag external effects with the
  input's [log offset](log-based-messaging.md) so a replayed write
  overwrites rather than duplicates — pushing deduplication to the
  destination.

When integrating systems, ask which side carries the guarantee: a pipeline
is effectively-once only if *every* external effect is inside the
transaction or idempotent — one naked side effect (an email, a
non-idempotent API call) breaks the property end-to-end.

## Shuffle exactly-once transport

Stream pipelines shuffle keyed records so all events for a key land on one
worker ([partitioning](partitioning.md) at the transport layer). Shuffle
uses RPCs on an [unreliable network](unreliable-networks.md): **upstream
backup** retries until a positive ack, including across sender crashes —
at-least-once delivery. Ambiguous failure (timeout while the receiver
actually succeeded) creates duplicates; only a successful status is fully
trusted.

Dedup: tag every sent message with a unique ID; receivers drop IDs already
in a durable catalog. User transforms may be **nondeterministic** (external
lookups, wall clock, randomness, late data changing aggregations) — rerunning
them on retry could produce different output. **Checkpointing** writes each
transform's output to stable storage keyed by message ID *before* delivery
downstream; shuffle retries replay the checkpoint instead of re-executing
user code. Only one checkpointed output wins.

Naive per-record catalog lookups hurt throughput. Mitigations:

- **Graph fusion** — chain logical steps in-process, skipping cross-step
  exactly-once state.
- **Combiner lifting** — partial aggregate locally before shuffle, cutting
  message volume.
- **[Bloom filters](idempotency.md)** on seen IDs — no false negatives; a
  "not seen" result skips the expensive catalog lookup; "maybe seen" falls
  through to the authoritative store.

Catalog entries are garbage-collected using a processing-time watermark
(bounded buckets, e.g. ten-minute ranges) — distinct from event-time
[watermarks](stream-processing-watermarks.md). Remnant messages arriving
after GC for their bucket are necessarily duplicates and are ignored safely.

## Sources and sinks

**Deterministic sources** (files with byte offsets, Kafka partitions with
fixed order) need no extra dedup — rereads yield the same record IDs.
**Nondeterministic sources** (Pub/Sub-style fan-out to competing subscribers)
must supply stable record IDs via the source API so the runner can dedupe;
publisher retries that mint new IDs bypass source-level dedup unless the
publisher reuses its own idempotency key.

**Sinks** are side effects. Built-in idempotent sinks (file rename,
BigQuery insert with stable per-record UUID) follow a common pattern: a
nondeterministic step prepares output, then a **`GroupByKey` / reshuffle**
stabilizes the bundle so the side-effect step always receives the same input
on retry, and the external operation itself is idempotent (overwrite, not
append). Without the shuffle, a window that fires twice after failure may
send different element sets even if the sink API is idempotent per call.

## Atomic commit's hidden latency cost: coupled pipeline stages

Committing a downstream production atomically with its triggering state
update (MillWheel calls this a **strong production** — checkpoint the
outgoing record in the same atomic write as the state change, *before*
sending it) is what makes non-idempotent operator logic behave as if it
were idempotent to the framework's own retries. But paying that atomic-write
cost on every hop through a multi-stage pipeline creates a coupling
problem distinct from raw overhead: skipping the checkpoint (a **weak
production** — broadcast optimistically, persist after) forces each stage
to wait for its downstream ACK before it can safely ACK *its own* upstream
sender, chaining every stage's completion time to the slowest stage below
it. Combined with ordinary machine failure rates, this coupling makes
latency degrade sharply with pipeline depth — even a modest per-minute
failure probability compounds across a handful of chained stages into a
non-trivial chance that *some* production in the chain is delayed by a
recovery. The general fix does not require choosing one extreme for an
entire pipeline: checkpoint (pay the atomic-write cost) only for
productions that are actually straggling — e.g. after a short delay with no
downstream ACK yet — so a slow stage can ACK its own upstream sender and
free those resources without forcing every hop to pay commit-time
durability cost unconditionally. This is the same kind of trade MillWheel
also makes explicit at the framework level: strong productions and
exactly-once deduplication can both be disabled per-computation when a
stage is already naturally idempotent (a stateless filter is the clean
example — reprocessing it is a correctness no-op), since paying the
durability cost there buys nothing.

[Timers](stream-processing-timers.md) get the identical guarantee when they
fire: a timer callback is just another piece of computation logic subject to
the same replay-and-dedupe machinery as processing an input record.
