---
type: concept
title: Idempotent and Replayable Jobs
description: >
  Designing a pipeline job so running it twice on the same input produces
  the same result, which is what makes safe retry and backfill possible.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 4"
  - title: "Kafka: a Distributed Messaging System for Log Processing"
    resource: "Kafka: a Distributed Messaging System for Log Processing (Kreps, Narkhede, Rao), §3.1"
---

A job is idempotent if running it more than once with the same input leaves
the target in the same state as running it once — no duplicated rows, no
double-counted aggregates, no compounding side effects. This is what makes it
safe to retry a failed job, replay a historical period for a backfill, or
reprocess data after a bug fix, without first having to manually undo
whatever the previous partial or erroneous run already did.

Idempotency is the property that turns
[pipeline granularity](pipeline-granularity-and-blast-radius.md) into a real
recovery mechanism: a small, well-bounded task is only safe to retry
automatically if rerunning it doesn't corrupt output that a previous attempt
already wrote. Common techniques: writing to a new partition/table version
and swapping it in atomically rather than appending in place; upserting on a
natural or surrogate key instead of blindly inserting; and making
aggregations recompute a full window from source rather than incrementing a
running total in place.

**A batch job reading from a [log-based broker](log-based-message-broker.md)
gets this almost for free by committing its output data and its consumer
offset together, atomically, only on job success.** A MapReduce-style job
loading from Kafka into HDFS, for instance, writes both the loaded data and
the offset it read up to in the same successful-completion step; a task that
fails partway through simply never advances its offset, so a retry re-reads
and re-writes the same range rather than silently skipping or duplicating
it. This works cleanly specifically because the broker itself is stateless
about per-consumer progress — offsets live with the consumer, not the
broker — so retrying a failed load is indistinguishable from running it for
the first time.

**Checkpoint the offset of the oldest unflushed message, not the offset of
the most recently received one, whenever a consumer buffers before
writing.** A consumer that only periodically flushes buffered data to its
actual persistent store (a batch indexer, say) and naively advances its
committed offset as soon as each message is *received* creates a gap: if the
consumer crashes before its next flush, everything sitting in the buffer at
crash time is lost, because the broker has already been told the consumer
is done with it. Tracking and committing the offset of the oldest message
still waiting to be flushed instead closes that gap — on restart, the
consumer resumes exactly from the oldest genuinely-unpersisted message
rather than from wherever it happened to last acknowledge receipt.

This property is also the precondition for backfill and reprocessing: a
pipeline that isn't idempotent can't be safely re-run over a historical date
range to fix bad output, because doing so risks corrupting whatever the
first, flawed run already produced. Idempotency alone isn't sufficient,
though — reprocessing also needs the original input still available, which is
why [archiving staged extracts](extract-archival-for-reprocessing.md) matters
as much as idempotent job logic does.

**Scope a corrupt-data recovery to exactly what was affected, not the whole
pipeline.** Once corrupt data has been found and the source of new corrupt
writes has been stopped, the natural instinct is a full end-to-end reprocess
— but idempotent, well-[granular](pipeline-granularity-and-blast-radius.md)
jobs make it possible to instead restore from the last known-good checkpoint
and selectively reprocess only the affected accounts or the affected time
window. This is faster, lower-risk (a narrower blast radius for the fix
itself to introduce a new bug), and only available at all because the job's
granularity and idempotency already made "rerun just this slice" a
well-defined operation rather than an all-or-nothing choice.

**The end-to-end argument for idempotency**: a delivery guarantee or retry
mechanism enforced at any single hop — a message broker's at-least-once
semantics, a database transaction — cannot by itself guarantee the whole
pipeline behaves idempotently end to end. A client can successfully commit a
write, then lose the network connection before receiving the acknowledgment,
retry the same logical request, and produce a duplicate — even though every
individual hop along the way honored its own guarantee correctly. The fix has
to span the whole chain: generate a unique operation ID once, at the point a
logical request originates, and carry that same ID through every hop the
request passes through, enforcing a uniqueness constraint on it wherever the
request is finally applied. A guarantee stitched together correctly at every
individual hop still isn't the same thing as a guarantee that holds
end to end — the ID has to be threaded through deliberately, not assumed to
survive by default.
