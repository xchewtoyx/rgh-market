---
type: concept
title: Partitioning and Clustering for Query Pruning
description: >
  Splitting and sorting stored data so a query engine can skip the segments
  it doesn't need, cutting scan volume beyond what columnar storage alone
  achieves.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 6"
---

Even with columnar storage scanning only the columns a query needs,
reducing the amount of data scanned further still pays off. Two
complementary techniques:

- **Partitioning** splits a table into subtables on a field — date/time
  partitioning is the classic case for analytics workloads that filter on a
  time range, since a query for one day can skip every other day's
  partition entirely.
- **Clustering** sorts or colocates similar values within partitions by one
  or a few fields, which improves filter, sort, and join performance within
  a partition even after partition-level pruning has already happened.

**Pruning** is the payoff: a query engine that knows which partitions or row
groups can't possibly contain matching rows skips reading them at all,
rather than scanning and then discarding non-matching rows. Snowflake's
micro-partitioning is a instructive variant: instead of the engineer naively
partitioning on one designated field, Snowflake automatically groups rows
into small (50–500MB uncompressed) micro-partitions and tracks, per
micro-partition, the row count and value range for each field. A query
filtering on a field with high value-repetition across rows (e.g.,
`WHERE created_date = '2022-01-02'`) lets the engine skip any micro-partition
whose tracked range can't contain that value — functioning like a
lightweight index without the engineer having to declare one.

**Partitioning also affects the write side, not just the query side.** A
naive time-based partition scheme — every row for "today" landing in one
partition — concentrates every incoming write onto that single partition
for the whole day, which becomes a genuine load bottleneck under high
ingest volume even though it's exactly the layout that makes time-range
queries cheap. This is the same
[hotspotting](stream-partition-keys-and-hotspotting.md) failure mode a
streaming partition key runs into, applied to storage partitioning instead
of a stream's parallel partitions: the field that groups data correctly for
downstream queries is not automatically the field that spreads write load
evenly, and a high-throughput ingestion pipeline needs to check both
properties, not just the query-pruning one. Where write concentration is a
real problem, a compound partition key that adds a second, higher-cardinality
field alongside the time field (an entity or shard ID, say) spreads writes
across more partitions while still letting queries prune on the time
component.

Choosing a partitioning field is therefore a pipeline design decision with
real query-cost consequences, not just a storage-layout detail: it should
match the filter conditions the platform's actual downstream queries use
most, not simply whatever field happens to be convenient to partition on at
load time.

When the partitioning field is a date, an ordered, chronologically
meaningful key (e.g. a `yyyymmdd`-formatted integer) makes partition
maintenance itself straightforward — advancing to a new partition is just
incrementing the key's day/month/year components — versus a partitioning
scheme keyed on an opaque surrogate. Some optimizers instead do better with
a true date-typed column for partitioning, since they can then reason
about date-interval semantics (e.g., that 31 days separate March 1 from
April 1, rather than the misleadingly large gap `20130301` to `20130401`
appears to have as raw integers) and produce better query plans — pick
whichever form the platform's own optimizer actually exploits.
