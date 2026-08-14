---
type: concept
title: Multi-Table Conditional Insert
description: >
  Fanning one source read out into several target tables in a single pass,
  each with its own insert condition, instead of scanning the source once
  per target.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Gershkovich), ch. 17"
---

A single incoming source record often needs to feed more than one target
table at once — a [Data Vault](data-vault-load-mechanics.md) load routing one
order record into a hub, a link, and a satellite simultaneously is the
clearest case, but the same shape shows up anywhere a load needs to
conditionally split one read across multiple destinations. Reading the
source once and evaluating a per-target condition against it — rather than
running a separate pass over the source for each target — is both cheaper
and keeps the targets' insert decisions consistent with each other, since
they're evaluated from the exact same source row at the exact same moment.

The general shape: for each target, check whether this record already
exists there (by key, or by key-plus-[hash-diff](hash-based-change-detection.md)
for a target that also needs change detection), and insert into that target
only if the check comes back empty — with either "evaluate every matching
condition" or "stop at the first matching condition" semantics available
depending on whether a record should be able to land in more than one target
at once.

This same fan-out-with-a-condition mechanic is useful well outside Data
Vault as a [data quality](data-quality-dimensions.md) technique: when an
anomaly type is known in advance (an out-of-range value, a disallowed
combination), the same single pass can route anomalous rows to a
[quarantine table](dead-letter-queue.md) for review while letting the rest
of the batch load normally to its intended target — one read, two
destinations, one condition deciding which row goes where.
