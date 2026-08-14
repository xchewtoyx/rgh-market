---
type: concept
title: Source System Evaluation
description: >
  The questions a pipeline designer must answer about a source system before
  building ingestion against it.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

A source system (an application database, an IoT device swarm, a message
queue) is the data's origin — one the pipeline consumes but usually doesn't
own. [Data profiling](data-profiling-before-ingestion.md) is the concrete
first step that answers most of the questions below empirically rather than
by asking the source owner. Before designing ingestion, work through:

- What are the data's essential characteristics, and what's its schema? Does
  reading it require joining across tables or systems?
- How is data persisted — long-term or transient — and how is it generated
  (event rate, GB/hour)?
- What consistency, error, duplicate, and late-arrival characteristics does
  the output have? (See [late-arriving data](late-arriving-data.md).)
- How are schema changes communicated downstream? (See
  [schema evolution in source systems](schema-evolution-in-source-systems.md).)
- How frequently should data be pulled, and will reads impact source-system
  performance?
- Can the pipeline connect directly to the source (**online extraction** —
  querying live tables, an intermediate change table, or a transaction log),
  or does the source lack that kind of access entirely (**offline
  extraction** — the source system stages its own extract as a file, e.g. a
  mainframe job dropping CSVs into a filesystem folder, with the pipeline
  only ever touching that staged output)? This determines who initiates the
  extraction and constrains which
  [transfer method](extraction-transfer-method.md) is even available — an
  offline source forces file-based transfer by construction, since there's no
  live connection to stream from.
- For stateful systems: are updates delivered as periodic snapshots or as
  [change data capture](change-data-capture.md) events, and how does the
  source track changes internally?
- Are there upstream dependencies, and are quality checks already in place for
  late or missing data?

Source systems and ingestion — not storage — are typically the most
significant bottlenecks and failure points in a pipeline, precisely because
they're outside the pipeline engineer's direct control and can silently
degrade or stop without an obvious signal downstream.
