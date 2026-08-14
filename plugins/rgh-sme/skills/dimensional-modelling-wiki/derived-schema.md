---
type: concept
title: Derived Schema
description: A star or cube built by restructuring data already loaded into other dimensional structures, rather than sourced from operational systems, to move cost from query time to load time.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 14"
---

A derived schema is a star or [olap-cube](olap-cube.md) whose data is copied and restructured from other, already-loaded dimensional structures rather than sourced fresh from operational systems — it piggybacks on existing stars instead of drawing from the source of record. This is a second layer on top of the ordinary dimensional architecture, and it is redundant by definition — but redundancy is not inherently a problem in dimensional design; it is a deliberate trade, moving cost out of the query and reporting process and into ETL.

## Why build one

- **Query performance**: any single design serves most needs well but performs poorly on some minority of queries. A derived schema reorganizes data into the shape a specific class of hard query needs, paid for once at load time instead of on every run.
- **Report complexity**: some questions are technically answerable against the original schema but require parsing results, layering conditional logic, or transposing data — real development cost, requiring skilled developers, independent of whether performance is actually a problem. A derived schema can make such answers accessible to less-skilled report authors.
- **Schema scope**: when only a subset of a schema's data is actually needed somewhere (a region's data at a regional office, a role's permitted data for security, a bounded data set for a mobile deployment), a derived schema holding just that subset serves the need without touching the original.
- **Cubes**: when a cube supplements relational storage rather than serving as the primary store, it is a derived schema by definition, and can mirror any of the derivation techniques below, each targeted at a specific class of business question.

Three patterns already amount to derived schemas even though they're usually discussed on their own terms: a [periodic snapshot fact table](periodic-snapshot-fact-table.md) is typically derived from a transaction star (though not always — some status measurements have no underlying transactions to derive from, or the transactions are too voluminous to retain); an [accumulating snapshot fact table](accumulating-snapshot-fact-table.md) is usually derived by correlating activities across one or more other stars in advance so the correlation doesn't have to happen at query time; and a [supertype/subtype schema](supertype-subtype-schema.md)'s core fact table is often derived as a union of common facts from the type-specific custom fact tables.

Four further derivation techniques are common enough to name individually: a [consolidated fact table](consolidated-fact-table.md) (also called a merged or drill-across fact table) combines facts from multiple business processes at a shared grain; a [pivoted fact table](pivoted-fact-table.md) transposes data between row-wise and column-wise orientation; a [sliced fact table](sliced-fact-table.md) holds only a row-subset of an existing star; and a [set operation fact table](set-operation-fact-table.md) precomputes a union, intersection, or difference between two stars.

## Cost

Every derived schema adds a table to design, load, and maintain; ETL routines to build, test, and deploy; dependencies on an already-contended load window; and processing resources at load time. It also creates a usability cost distinct from the ETL cost: the same business process now has multiple representations (a snapshot alongside its source transactions, a core star alongside its custom variants, a process-specific star alongside a merged one), and report developers must learn which one answers a given question. Two mitigations are typical: restrict the derived schema to power users and trained developers while the original stays generally available, or provide multiple clearly named, well-documented query environments so people pick the right one up front. Whether a specific derived schema is worth its cost is best decided with input from report developers, ETL developers, DBAs, and end users together, not by the schema designer alone.
