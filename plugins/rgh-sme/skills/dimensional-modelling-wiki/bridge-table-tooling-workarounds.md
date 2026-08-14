---
type: concept
title: Bridge Table Tooling Workarounds
description: How to work around modeling tools and BI SQL generators that assume every join is a strict primary-key/foreign-key relationship and can't represent a bridge table's genuine many-to-many join.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 8"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 9"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 9"
---

Many modeling tools, BI SQL generators, and even some RDBMSes assume every join is a strict primary-key/foreign-key relationship and cannot represent, or will refuse to configure, a genuine many-to-many join like the fact-to-[bridge table](bridge-table.md) relationship. The workaround is to build an **intersect table** exactly as an entity-relationship modeler would: split the bridge into a group table holding only the group key (with a declarable primary key of its own) plus a separate membership table, identical in shape to the original bridge, that actually holds the group-key-to-member-key pairs. The group table this produces is functionally redundant — it exists only to satisfy tooling conventions, not to add real information — but it lets tools that insist on PK/FK joins work with the structure.

A bridge table also structurally resembles a [factless fact table](factless-fact-table.md): mostly foreign keys, no measures. If a bridge is treated as a fact table by tooling, the general caution against ever joining two fact tables directly (see [drilling across](drilling-across.md)) must be relaxed specifically for the bridge-to-real-fact-table join — the Cartesian effect that rule normally warns against is exactly the mechanism a bridge is built to produce, and is intentional there.
