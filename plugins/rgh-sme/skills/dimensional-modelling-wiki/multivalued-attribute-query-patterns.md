---
type: concept
title: Multivalued Attribute Query Patterns
description: How to express AND and OR queries against a multivalued dimension attribute modeled through a bridge table, and a delimited-string alternative that sidesteps the bridge entirely.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 8"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 9"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 9"
---

A [bridge table](bridge-table.md) makes an OR query across a multivalued attribute (e.g., "Unix or Linux skill experience") a simple constraint on the value attribute in the bridged sub-table. An AND query (e.g., "Unix *and* Linux experience") is intrinsically harder, because the two conditions must be satisfied by two different *rows* of the bridge, and plain SQL is poor at expressing constraints that span multiple rows of the same join. The standard fix is to generate SQL that UNIONs (for OR) or INTERSECTs (for AND) the results of one subquery per value being searched for, typically hidden behind a purpose-built query interface rather than exposed directly to business users.

When the multivalued attribute's own population is bounded and fairly stable, a [pivoted dimension](pivoted-dimension.md) generated from the bridge turns every AND/NOT combination query into a plain column predicate instead, at the cost of a column-count ceiling and more complex maintenance ETL.

An alternative that sidesteps the bridge table (and the UNION/INTERSECT SQL) entirely for smaller, less-reused value sets is a **delimited text string attribute** directly on the dimension row (or on an outrigger, if the same value list is shared and reused across many rows) — for example `|Unix|C++|`, with the delimiter placed at the start of the string and after every value. Both OR and AND constraints then become simple, structurally identical `LIKE` predicates against that one string column (case-normalized to avoid ambiguity, e.g. `UCase(skill_list) LIKE '%|UNIX|%'`), with the delimiter preventing spurious partial matches (so "SQL" doesn't match inside "NoSQL"). This works on any relational database with no special SQL extensions, at the cost of not being able to count rows by individual value the way a proper bridge table can.
