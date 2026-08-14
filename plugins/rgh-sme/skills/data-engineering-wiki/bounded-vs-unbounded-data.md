---
type: concept
title: Bounded vs. Unbounded Data
description: >
  Why all data is fundamentally an ongoing stream, and batch is only ever a
  convenient artificial boundary imposed on it.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 7"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 2"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 7"
---

Unbounded data exists the way it does in reality: an ongoing, continuous or
sporadic sequence of events with no natural end. Bounded data is a
convenient bucketing of that same stream across some boundary, most commonly
time. The framing to hold onto: **all data is unbounded until it's bounded**
— true of the overwhelming majority of business data (an online retailer's
transactions keep happening continuously; a batch cut of "yesterday's
orders" is an artificial boundary businesses have long imposed on that
stream, not a property of the data itself).

This reframes [batch vs. streaming ingestion](batch-vs-streaming-ingestion.md):
streaming ingestion isn't a fundamentally different kind of data, it's simply
a tool for preserving data's true unbounded nature so later pipeline stages
can also process it continuously, instead of forcing an artificial boundary
onto it earlier than necessary. Choosing batch is choosing where to draw that
boundary — a decision with real consequences, since once data crosses into a
batch, that batch's cadence becomes a hard downstream latency floor for
everything after it.

Two orthogonal dimensions further define dataset shape:

- **Cardinality** — **bounded** (finite) vs. **unbounded** (infinite, at
  least theoretically). Unbounded datasets impose additional burdens on
  consuming frameworks.
- **Constitution** — **table** (holistic view at a point in time; SQL's
  native form) vs. **stream** (element-by-element evolution over time;
  MapReduce lineage). Pipeline developers interact with streams directly;
  the [streams-and-tables duality](streams-and-tables-duality.md) unifies both
  views — batch pipelines are repeated cycles of table→stream reads,
  stream→stream transforms, and stream→table groupings.

A **streaming system** in the narrow sense is a processing engine designed
with infinite datasets in mind — including
[micro-batch implementations](micro-batch-vs-true-streaming.md) that repeatedly
execute a batch engine on unbounded input. Low latency, approximate results,
and speculative output are separate properties, not definitional to streaming.
