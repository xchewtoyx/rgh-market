---
type: concept
title: Sliced Fact Table
description: A derived fact table holding the same columns as its source star but only a row-subset selected by a dimension attribute value, for scoped deployment or security.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 14"
---

A sliced fact table is a [derived schema](derived-schema.md) identical in structure to its source star but containing only a subset of rows, selected by a specific dimension attribute value — for example, only rows where `region = 'East'`. This is **horizontal partitioning**: every column of the original fact table is kept, but only a subset of rows, with each partition (slice) defined by a dimension value. It contrasts with **vertical partitioning**, which keeps every row but only a subset of columns/facts — the mechanism behind an [aggregate fact table](aggregate-fact-table.md).

## Uses

- **Distributed or regional deployment**: replicate only the relevant subset of fact rows (alongside a full copy of the dimension tables) to a regional office, without sacrificing any detail within that region's data.
- **Mobile applications**: reduce an offline data set's size — a complementary technique to using an [aggregate fact table](aggregate-fact-table.md) for the same purpose.
- **Role-based security**: grant a job function access to only its relevant slice, since table-level access is typically far easier to configure and administer than row-level security on the original, unsliced schema.
- **Limiting cube size**: slicing data before loading it into an [olap-cube](olap-cube.md) keeps the cube to a manageable size, used alongside other derivation and aggregation techniques.

## Deriving the whole from its slices

Going the other direction — building the combined, unsliced fact table out of independently produced slices, as happens when regional fact tables are built in parallel and then combined at the end of a load window — is possible but demands care with the dimensions involved: the slices must not overlap, and every slice must share an identical common dimension set. In practice this forces a strict ETL ordering: process the common dimension tables first, then process the fact table slices (optionally in parallel), and only then derive the combined fact table from the slices. Skipping the shared-dimension step first risks nonconformance, overlapping key values, or inconsistent [slowly changing dimension](slowly-changing-dimension.md) representation across the regions being combined.
