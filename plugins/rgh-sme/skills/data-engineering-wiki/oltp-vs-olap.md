---
type: concept
title: OLTP vs. OLAP
description: >
  Why transactional application databases and analytical query engines are
  built for opposite workloads, and why that mismatch is the reason
  pipelines exist at all.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 5"
---

**OLTP** (online transaction processing) systems read and write individual
records at high rate, low latency, and high concurrency — an RDBMS can
select or update a single row in under a millisecond and handle thousands of
operations per second. This is what application backends need. It is *not*
what large analytical scans need: an OLTP system is poorly suited to queries
that touch huge data volumes, and running analytics directly against one
works only until the analytical load contends with, or exceeds, the
production transactional load it was actually built to serve.

**OLAP** (online analytical processing) systems are built for the opposite
workload: large scans across huge data volumes, inefficient at individual-record
lookup. Modern column databases scan without indexes at all, typically in
blocks of 100 MB or more per query — doing thousands of individual-record
lookups per second on such a system, without a caching layer in front, would
overwhelm it just as badly as the reverse mismatch.

This structural mismatch — not organizational preference — is the reason
[data warehouse architecture](data-warehouse-architecture.md) exists as a
pattern: moving analytical query load off the OLTP system and onto a
purpose-built OLAP system is the whole point of building a pipeline between
them, not an optional nicety. An OLAP system is also frequently read *from*
as a source in its own right further downstream — e.g., a warehouse feeding
ML training data or a [reverse ETL](reverse-etl.md) flow back into an
operational system.
