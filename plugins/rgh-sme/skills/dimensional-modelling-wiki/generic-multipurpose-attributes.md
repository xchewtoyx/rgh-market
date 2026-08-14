---
type: concept
title: Generic Multipurpose Attributes
description: A small set of type-agnostic columns whose meaning is resolved per row via a lookup table, trading query accessibility for open-ended storage flexibility.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 13"
---

A dimension (or fact) table can carry a small, fixed set of generic columns — `attribute_1` through `attribute_4`, say — whose actual meaning depends on the row's type and is resolved through an auxiliary mapping table (for example, `facility_attribute_definitions`, keyed by facility type and attribute name, supplying each column's definition for that type). A `facility` dimension spanning factories, warehouses, stores, and offices might use `attribute_3` to mean "has a clean room" for a factory row but "can stock perishables" for a warehouse row. This is one of three techniques for handling attributes that vary by subtype, alongside a single table with every possible attribute and a [supertype/subtype schema](supertype-subtype-schema.md) split into core and custom tables.

Generic attributes are very flexible for **storage** — an arbitrary, open-ended number of subtypes can share the same fixed column set with no schema change as new types appear — but poor for **querying**: constructing a query requires first looking up which generic column carries which meaning for the type in question (`WHERE facility.attribute_3 = 'Has Perishable Storage Facilities'`, `GROUP BY facility.attribute_2`), and ordinary query and reporting tools have no mechanism for that value-dependent column-name translation — they assume one fixed name and definition per column. This makes the technique usable in practice only behind a custom-built application that is itself aware of the definitions table and can dynamically relabel columns and merge or relabel result sets that span multiple types.

A hybrid design captures most of the benefit without giving up standard-tool accessibility: build ordinary [supertype/subtype schema](supertype-subtype-schema.md) core and custom tables for standard query and reporting tools, and separately add generic attribute columns to the core table for exclusive use by the type-aware custom application — hidden from, and simply ignored by, every standard tool that queries the same table.
