---
type: concept
title: Partitioned Secondary Indexes
description: >
  Secondary indexes don't align with primary-key partitions; the choice is
  local indexes (cheap writes, scatter/gather reads) versus global
  term-partitioned indexes (cheap reads, distributed writes).
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 6"
---

# Partitioned Secondary Indexes

A secondary index ("all cars where color = red") doesn't identify records by
the [partitioning](partitioning.md) key, so its entries cut across
partitions. Two architectures:

## Local (document-partitioned) index

Each partition indexes only its own documents, independently.

- **Writes are cheap:** updating a document touches only its own partition's
  index.
- **Reads are scatter/gather:** matching documents for a term may live in any
  partition, so the query goes to *all* partitions and merges results —
  expensive, and prone to [tail latency
  amplification](tail-latency-amplification.md) (the slowest partition gates
  every query). Used by MongoDB, Cassandra, Elasticsearch, SolrCloud,
  VoltDB; vendors advise designing queries to hit a single partition where
  possible. At large partition counts, restructuring the fan-in as an
  [aggregation tree](aggregation-trees.md) rather than one flat
  scatter/gather avoids concentrating all the merge work at a single
  coordinator.

## Global (term-partitioned) index

One index covering all data, itself [partitioned](hash-partitioning.md) by
the indexed *term* (or its hash — trading range scans on terms vs. hot
terms, the same [key-range vs. hash](key-range-partitioning.md) trade-off).

- **Reads are targeted:** a term lookup goes to exactly the partition owning
  that term.
- **Writes fan out:** one document update touches every term it contains —
  index partitions on multiple nodes. Doing that synchronously would need a
  [distributed transaction](two-phase-commit.md), so in practice global index
  updates are **asynchronous**: a read shortly after a write may not see it
  (DynamoDB GSIs behave this way; the index is a
  [derived view](change-data-capture.md) with its own lag).

Rule of thumb: read-heavy on the indexed attribute favors global; write-heavy
or latency-sensitive writes favor local plus disciplined query design.
