---
type: concept
title: Change Data Capture (CDC)
description: >
  Three mechanisms for propagating source-row changes into a pipeline, and
  the push/pull and load-on-source trade-offs between them.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

Change data capture is how a pipeline learns that a row in a stateful source
changed, without re-reading the whole table. Three common patterns:

1. **Trigger-based CDC**: a row change fires a database trigger that pushes a
   message onto a queue. Push model, source-driven.
2. **Log-based CDC**: the ingestion system tails the database's binary/write-
   ahead log, which the database is already writing for its own durability.
   This adds little or no extra read load on the source — effectively a push,
   since the source was going to produce that log regardless. The resulting
   change stream is often published through a
   [log-based message broker](log-based-message-broker.md), and if that
   broker applies [log compaction](log-compaction.md) to the topic, a new
   consumer can replay it from the start to reconstruct the source table's
   current state, not just observe individual future changes.
3. **Timestamp-based batch CDC**: the ingestion system periodically queries the
   source for rows changed since the last run (e.g., `updated_at > last_run`).
   This is a pull model, and it does add read load to the source on every
   poll.

A related but weaker technique when a source table is already **range-
partitioned along a date key** (e.g., an orders table partitioned by day):
the partition boundary itself identifies "today's" or "yesterday's" rows
without needing a separate timestamp column or CDC mechanism. It only works
for append-heavy tables where the partition key reliably correlates with
when a row changed, and it can't distinguish an update to an old row from a
genuinely new one the way a `Last Modified` timestamp or a CDC stream can.

These map onto the broader [push vs. pull ingestion](batch-vs-streaming-ingestion.md)
distinction: log-based and trigger-based CDC are push-oriented and
comparatively cheap for the source; timestamp-based batch CDC is pull-oriented
and simpler to build but scales worse and can miss changes between polls
depending on how it's implemented.

Log-based CDC is generally the least invasive option for a source system that
already writes a durable log, which is why it's the default choice for
incremental loading against OLTP databases feeding a warehouse. When a source
system's own writer needs to guarantee an event exists for every change (not
just a queryable log to poll), pairing log-based CDC with a
[transactional outbox](transactional-outbox-pattern.md) on the source avoids
the dual-write problem of persisting state and publishing an event as two
separate, driftable operations.

Each pattern has a specific, well-known failure mode worth checking for
before relying on it:

- **Trigger/audit-column CDC** breaks silently when a source-populated
  `date_modified`-style column is left NULL, or when back-end scripts write
  to the table directly and bypass the application layer (and its triggers)
  entirely — rows changed that way never get marked as changed at all.
  Deletions in particular are often not captured by an audit column at all,
  since there's no row left to stamp.
- **Timestamp-based batch CDC**, if implemented naively as "select rows where
  the date field equals yesterday" rather than "greater than the last
  successful run," silently drops an entire day of data if one run is
  skipped or fails, and produces duplicate rows if a run is retried after a
  partial failure.
- **Log scraping** (reading a database's redo/transaction log, either by
  snapshotting it or polling it live) is the messiest technique: production
  DBAs may rotate or empty the log under storage pressure, permanently
  losing any transactions the pipeline hadn't yet consumed. If a source
  system's log is used this way, get a dedicated log stream carved out for
  the pipeline rather than sharing the DBA's operational log. See [log
  retention as a hard CDC deadline](log-retention-deadline-for-cdc-consumers.md)
  for why this isn't just a reliability nice-to-have.
- **Message queue monitoring** is low-overhead when a message bus already
  exists, but most queues have no replay feature — a dropped consumer
  connection means the messages in flight during the outage are gone for
  good, not merely delayed.

A related technique when none of the above is available: **full diff
compare** — retaining the prior full extract and comparing it record-by-record
against the current one. It's thorough (it catches every change, including
ones a flawed audit column or log stream would miss) but resource-intensive;
run the comparison on the source machine when possible rather than
transferring the whole table first, and use a checksum (e.g. CRC) over each
row's tracked columns to detect a change with one comparison instead of
comparing every field — the same idea generalized further in
[hash-based change detection](hash-based-change-detection.md).

**Batch CDC's hidden information loss**: timestamp-based batch CDC captures
which rows changed since the last query, not every individual change applied
to them during that window. A bank account table polled every 24 hours will
show only the last recorded balance for an account that had five debit-card
withdrawals that day — the four intermediate transactions are silently lost,
even though the final state is technically correct. Where the intermediate
history itself matters (not just the latest value), mitigate with an
[insert-only history pattern](insert-only-history-pattern.md) at the source
so every individual change becomes its own row, or move to continuous
log-based CDC, which captures every write as its own event.

**Filter to changed rows as early in the pipeline as possible** — ideally
before the bulk data transfer, not after. Applying a CDC filter late, once
the full volume has already been extracted and partially transformed, throws
away most of the benefit CDC exists to provide: the extraction and transfer
cost is paid regardless, and only the (usually cheap) filtering step gets
skipped.

**CDC has a real cost on the source**: reading a database's log, or running
repeated timestamp-filtered queries, consumes the source's memory, disk
bandwidth, storage, CPU, and network bandwidth — CDC is never free just
because it's less invasive than a full scan. Test any new CDC or replication
setup with the team that owns the production system before enabling it, and
consider a [read replica](read-replicas-for-analytics-offload.md) to isolate
that cost from production traffic entirely.
