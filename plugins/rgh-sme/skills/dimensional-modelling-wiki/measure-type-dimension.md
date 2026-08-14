---
type: concept
title: Measure Type Dimension
description: An anti-pattern that collapses a sparse, wide fact row to one generic fact identified by a measure-type dimension, generally not recommended.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
---

A measure type dimension collapses a long, sparsely populated [fact-table](fact-table.md) row down to a single generic fact column, identified by a foreign key to a dimension enumerating which measure that row represents. This removes empty columns from a sparse row, but multiplies the fact table's row count by the average number of occupied columns per original row, and complicates any computation across measures that now live on different physical rows instead of different columns of the same row.

This technique is generally not recommended, and should be reserved for the rare case where the number of potential facts is extreme (hundreds), with only a few applicable to any given row, and where no arithmetic needs to be computed between the facts (e.g. no ratio or difference between two measures). As a concrete illustration of the row-count cost: a 10-million-row fact table with 6 dimension keys and 4 facts per row becomes roughly 40 million rows with 7 keys and a single fact if normalized this way. Arithmetic between facts that share a row (such as a discount expressed as a percentage of gross) is straightforward in SQL; the same computation across facts that have been split onto different rows requires much more awkward SQL. The pattern is more defensible when the primary BI platform is an [olap-cube](olap-cube.md), since cubes can compute along any dimension, including a measure-type dimension, without the row-based arithmetic problem relational SQL has.
