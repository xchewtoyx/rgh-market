---
type: concept
title: Delivery Guarantees (Exactly-Once vs. At-Least-Once)
description: >
  The two realistic message-delivery guarantees a pipeline can build against,
  and why idempotency — not the guarantee itself — is what actually protects
  correctness.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 5"
  - title: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale"
    resource: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale (Akidau et al.), §6.1"
  - title: "Kafka: a Distributed Messaging System for Log Processing"
    resource: "Kafka: a Distributed Messaging System for Log Processing (Kreps, Narkhede, Rao), §2"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 6"
---

Message queues and streaming platforms offer one of two delivery guarantees:

- **At-least-once**: a message may be delivered to a subscriber more than
  once, or to more than one subscriber. Fine when duplication doesn't change
  the outcome.
- **Exactly-once**: a message is delivered, and removed, exactly one time.
  In the strict sense this is debated as technically impossible to guarantee
  in a distributed system (see the Two Generals Problem) — real "exactly-once"
  systems are closer to at-least-once delivery plus deduplication.

**Match the guarantee's strength to how much the data can actually
tolerate losing, rather than defaulting to the strongest option
available.** Traditional enterprise messaging systems (IBM WebSphere MQ,
JMS-based brokers) offer transactional, multi-queue-atomic delivery — real
capability, but overkill and a genuine complexity cost for data where an
occasional dropped record is a non-event, such as high-volume pageview or
click logs. Paying for guarantees stronger than the data needs isn't free:
it shows up as reduced throughput (no easy way to batch messages into one
request when every message has to be individually transactional) and a
larger API and implementation surface than the pipeline actually uses. The
right default is set by the data's own tolerance for loss or duplication,
not by reaching for the strongest guarantee a platform happens to offer.

Distributed queues also rarely guarantee strict ordering: most offer only
best-effort ("fuzzy") ordering, with strict-FIFO variants available at extra
overhead where a technology explicitly supports them (e.g., Amazon SQS
standard vs. FIFO queues). The safe default assumption for pipeline design is
that messages may arrive out of order and may be delivered more than once,
unless the specific technology in use explicitly guarantees otherwise.

Because even an "exactly-once" guarantee can't rule out a consumer crashing
after processing a message but before acknowledging it — which forces a
redelivery — the same gap shows up inside a long-running stream job's own
[recovery from failure](stream-processing-fault-tolerance.md), not only at
the queue's delivery boundary. The real correctness property a pipeline needs
is
[idempotency](idempotent-and-replayable-jobs.md): processing the same message
twice should produce the same result as processing it once. Idempotent
processing absorbs both delivery guarantees equally well, which is why it
matters more than which guarantee the underlying platform advertises.

**The concrete mechanism most "exactly-once" platforms use to deduplicate**
is worth recognizing when evaluating one: the sender is assigned a durable
identity plus a monotonically increasing request number per message, and the
receiver caches the response for each (sender, request number) pair it has
already processed. A retried request whose number the receiver has already
seen returns the cached result instead of reprocessing — this is exactly
what Kafka's idempotent producer feature does under the hood. Two practical
limits worth expecting from any implementation of this pattern: it only
catches duplicates from a *live* sender retrying after a lost
acknowledgment — a sender that crashes and restarts gets a fresh identity and
no protection against re-sending what it already sent before crashing — and
it has no visibility into duplicates the sending application itself creates
by mistake (issuing two logically-identical requests under two different
request numbers). Both gaps still have to be closed by [idempotent,
replayable job design](idempotent-and-replayable-jobs.md) on the pipeline's
own side, not assumed away by the platform's guarantee.

**Two optimizations worth expecting from a framework-level implementation of
this mechanism**, illustrated by MillWheel: since the full set of
already-seen record IDs can outgrow memory, a **Bloom filter** of known
record fingerprints gives a fast path for records provably never seen
before, falling back to a read against the durable dedup store only on a
filter miss (a false positive) — most records never pay that read. And
because record IDs can't be discarded the instant they're processed (a
retry might still be in flight, and an injector delivering
[late-arriving data](late-arriving-data.md) may retry much later), garbage
collecting old record IDs waits for a **slack value** — typically hours —
past the point processing completed, rather than deleting dedup state
immediately.

**A framework's exactly-once guarantee is scoped to what the framework
itself manages, and stops at its own boundary.** MillWheel states this
explicitly: internal state updates are atomically checkpointed and records
are delivered exactly once *within* the framework, but that guarantee does
not extend to any external system a computation's user code happens to
contact. If a computation calls out to an external API, writes to a store
the framework doesn't manage, or otherwise has a side effect outside the
framework's own state, making that specific side effect idempotent is the
user code's responsibility — the framework's guarantee, however strong,
provides no help there. This is worth checking explicitly for any
"exactly-once" streaming platform: exactly-once *within the platform's own
state* and exactly-once *for every side effect a job produces* are two
different claims, and only the narrower one is usually what's actually
guaranteed.

**Exactly-once concerns accuracy, not completeness.** Accuracy means no
record is ever dropped or duplicated in the pipeline's own processing;
completeness means the pipeline waited long enough to see every record it
should. A streaming engine can process every in-time record exactly once
while still dropping records that arrive after a configured
[allowed-lateness](allowed-lateness-horizon.md) deadline — that is a
completeness knob, not an accuracy failure. Batch pipelines have the same
split: a nightly job over "yesterday's data" is accurate for what it saw but
not complete relative to records that landed after the cutoff.

**User transform code may run more than once even under exactly-once
shuffle.** Frameworks like Cloud Dataflow guarantee that only one invocation's
*output* wins downstream — not that the user's ParDo runs once per record.
Retries after worker failure, simultaneous execution on multiple workers, and
nondeterministic user code (external lookups, wall-clock time, randomness,
or even deterministic code fed by
[late-arriving data](late-arriving-data.md)) all mean user code can execute
multiple times. The standard fix is **checkpointing**: each transform output
is written to durable storage keyed by a unique record ID before delivery to
the next stage, so shuffle retries replay the checkpoint rather than
re-running user code. This is the same
[strong-production](strong-vs-weak-productions.md) pattern — checkpoint
before emit — applied at every shuffle boundary.

**Closing the sink gap: stable input before an idempotent write.** Sinks are
side effects outside the framework's state, so exactly-once delivery through
shuffle alone is not enough. The practical pattern: insert a reshuffle
(`GroupByKey` / `Reshuffle`) between the step that *prepares* output and
the step that *performs* the side effect. The framework guarantees only one
version of shuffled output crosses that boundary, so the sink always sees the
same deterministic bundle on retry; the sink operation itself must still be
[idempotent](idempotent-and-replayable-jobs.md) (overwrite/set, not append).
File sinks follow this literally — nondeterministic temp-file writes grouped
and finalized with an idempotent rename; BigQuery streaming inserts get a UUID
per record with a reshuffle immediately after generation so retries reuse
the same ID rather than minting a new one. Nondeterministic sources (Pub/Sub)
expose stable record IDs through the source API so the framework can dedup;
deterministic sources (Kafka partitions, file byte offsets) need no extra
dedup layer.
