---
type: concept
title: Surrogate Key
description: A meaningless, sequentially assigned integer used as a dimension table's primary key instead of the operational system's natural key.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 5"
---

A [dimension-table](dimension-table.md)'s primary key should be a surrogate key, not the operational system's identifier (its natural key). Surrogate keys — also called meaningless, non-natural, artificial, or synthetic keys — are simple, sequentially assigned integers (1, 2, 3, ...) with no business significance, existing purely to join a dimension to its [fact-table](fact-table.md)s. The DW/BI system must claim control of dimension primary keys rather than depend on operational code structure. Column names ending in "Key" conventionally denote a surrogate key throughout dimensional modeling literature.

## Why not use the natural key directly

Any assumptions embedded in an "intelligent" operational key eventually get invalidated, and queries or applications should never build in a dependency on key structure. Reasons to insist on a surrogate:

- **Buffer from operational changes** — the warehouse retains history for years, while operational systems may recycle or reassign codes (e.g., an inactive account number reused after 12 months of dormancy), and surrogate keys protect against key collisions from acquisitions or system consolidation.
- **Integration of multiple source systems** — a back-room cross-reference table can map several inconsistent natural keys to one common surrogate.
- **Performance** — a surrogate key is the smallest integer that comfortably covers a dimension's cardinality, versus bulkier alphanumeric operational codes; smaller keys shrink fact tables and their indexes.
- **Handling null/unknown conditions** — a surrogate key value can represent "No Promotion," an anonymous customer, or a to-be-determined date, none of which SQL natively supports. See [null handling in dimensional models](null-handling-in-dimensional-models.md).
- **Supporting change tracking** — surrogate keys are foundational to representing multiple historical profiles for one real-world entity; see [slowly changing dimension](slowly-changing-dimension.md). This is considered one of the most important reasons to use them.

A pseudo-surrogate built by gluing a natural key to a timestamp is "perilous," and multi-column ("double-barreled") joins between dimension and fact tables should be avoided for both performance and usability reasons.

## Hash-based surrogate keys

An alternative generation technique, common in Data Vault-style designs, derives the surrogate key by hashing the natural key (and, for a [type 2](slowly-changing-dimension-type-2.md) row, the effective-from date) rather than drawing from a central sequence — for example `MD5(customer_id || from_date)`. This sacrifices the smallest-possible-integer performance benefit above, but lets keys be generated independently and in parallel by any load process without coordinating through one shared sequence generator, which matters more in highly parallelized or distributed ETL than in a traditional single-threaded warehouse load.

## Exception: the date dimension

The [date dimension](date-dimension.md) is the one dimension permitted a more "intelligent" primary key (e.g., a `yyyymmdd`-formatted integer), because calendar dates are fixed and predetermined — there are no deletions and no unexpected new dates. Even so, a special key value must still be reserved for "date unknown at load time."

## A numbering convention for special rows

A simple convention keeps [special-case dimension row](special-case-dimension-row.md)s consistent and easy for ETL to reason about across every dimension in the warehouse: reserve surrogate key `0` for the default "Missing" row (holding whatever missing-value labels stakeholders defined for each attribute), use negative integers for other special-case rows ("Unknown," "Not Applicable," "Error"), and leave all positive integers for ordinary dimension members. ETL and query logic can then test for special rows with a single, uniform `SK <= 0` check rather than tracking special values per dimension.

## Referential integrity: procedural, not DBMS-enforced

A fact table's foreign keys must always resolve to a matching dimension row — an unmatched foreign key ("bent needle") is expensive to even detect after the fact, since searching billions of fact rows for orphaned keys with `NOT IN` is prohibitively slow. In practice this referential integrity is guaranteed procedurally rather than by the database: ETL is already performing an in-memory lookup to translate each incoming natural key into its surrogate key, so a natural key with no matching dimension row is caught at that translation step, before the fact row is ever written — this is often called "free" referential integrity, since it falls out of the load process ETL needs to do anyway rather than requiring separate enforcement. DBMS-enforced foreign key constraints are typically too slow for warehouse load volumes, so the common practice is to define them as *unenforced* (so the query optimizer can still use them for hints) rather than drop them outright, keeping them fully enforced only during ETL development and initial data loads as a belt-and-braces check while the ETL's own key-lookup logic is being proven correct.

## Degenerate and fact table surrogate keys

Surrogate keys aren't typically assigned to [degenerate dimension](degenerate-dimension.md)s, but should be considered when the natural transaction control number isn't unique across locations, gets reused or wrapped, is bulky, or the BI tool requires a real dimension table to drill across on it. Once modeled this way, the number is no longer degenerate by definition.

The [fact-table](fact-table.md) itself can also carry its own simple, sequential surrogate key — a back-room ETL convenience rather than a business necessity — used as a single-column primary key, an immediate row identifier during ETL, a way to back out or resume an interrupted bulk load, or a way to decompose an update into a safer insert-then-delete pair. It also serves as the parent key exposed to a lower-grain child fact table in a header/line schema (see [allocated facts](allocated-facts.md)); a fact-to-fact join across foreign keys directly should still be avoided (see [drilling across](drilling-across.md)).
