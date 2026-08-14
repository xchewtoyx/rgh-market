---
type: concept
title: Streaming Triggers and Panes
description: >
  When in processing time a streaming window materializes output, via repeated
  update triggers, watermark-driven completeness triggers, or both combined.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 2"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 7"
---

In [streams-and-tables](streams-and-tables-duality.md) terms, triggers are
**ungrouping** operations — the complement to grouping. Grouping consumes a
stream and yields an evolving table; a trigger watches that table and puts
selected rows back in motion as a stream, analogous to classic database
triggers evaluated per row as time progresses.

**Triggers** answer "when in processing time are results materialized?" Each
output for a window is a **pane**. Two generally useful trigger families
(used alone or combined):

**Repeated update triggers** — periodically emit updated panes as a window's
contents evolve:

- **Per-record** — fires on every new element. Good for pollable output
  tables; chatty at high volume.
- **Processing-time delay** — two flavors:
  - *Aligned* — slices processing time into fixed regions aligned across all
    keys/windows (Spark Streaming microbatch semantics). Predictable but
    bursty; needs higher peak provisioning.
  - *Unaligned* — delay relative to when data was first observed in the
    window. Same average latency, better load distribution; generally
    preferred at scale.

**Completeness triggers** — materialize only after input for a window is
believed complete. Built on
[watermarks](watermark-computation-and-propagation.md); analogous to batch
semantics scoped to one window rather than the whole dataset. Less common
alone because watermarks can be too slow (delaying all downstream output even
for windows whose data is already complete) or too fast (heuristic
watermarks advancing early produce wrong on-time results).

The key conclusion: you cannot get both low latency and correctness from
completeness alone. Watermark-based completeness is essential for
missing-data use cases (outer joins, absence detection) because unlike a
fixed processing-time delay, it does not silently become wrong when
event-time skew exceeds an assumed constant — skew is inherently variable.

The **early/on-time/late pattern** combines both families
(`AfterWatermark().withEarlyFirings(...).withLateFirings(...)`):

- **Early panes** (zero or more) — speculative repeated-update firings before
  the watermark passes the window end; compensate for watermarks being too
  slow.
- **On-time pane** (exactly one) — watermark-triggered firing when input is
  believed complete; safe to reason about missing data (e.g., emit partial
  outer join).
- **Late panes** (zero or more) — firings for
  [late-arriving data](late-arriving-data.md) after the watermark passed;
  compensate for watermarks being too fast. Zero under a perfect watermark.

This pattern normalizes output shape between perfect and heuristic watermark
implementations and can cut first-output latency dramatically while still
incorporating late corrections. Under a perfect watermark, window state can
drop as soon as the watermark passes the window end; under a heuristic
watermark, state must be retained longer for possible late data — see
[allowed lateness](allowed-lateness-horizon.md).

**Batch triggers** — classic batch has one trigger type: fire when input is
complete. For a source read, all data fires at pipeline launch; for mid-
pipeline table-to-stream steps (e.g., after shuffle), the trigger waits until
the full grouped table is ready. Incremental triggering is what batch lacks
and streaming adds — a latency/throughput tradeoff, not a fundamental
semantic divide.
