---
type: concept
title: Star Schema
description: A multi-dimensional schema structure featuring a central fact table surrounded by dimension tables.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 3"
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 1"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 1"
---

The star schema is the standard structural paradigm in dimensional modeling, optimized for simplicity and query performance in Online Analytical Processing ([OLTP vs. OLAP](oltp-vs-olap.md)) workloads. 

The schema is composed of:
*   A central [fact-table](fact-table.md) containing quantitative measurements (facts) and foreign keys referencing surrounding dimensions.
*   A set of surrounding [dimension-table](dimension-table.md)s representing the context (who, what, where, when, why, how) of those measurements.

When visualized, the relationships resemble a star, with the fact table at the center and dimension tables radiating outwards as points. This design simplifies analytical queries and improves query performance on relational databases compared to normalized designs like the [snowflake-schema](snowflake-schema.md), which sub-divide dimensions and require additional SQL joins.

## Why dimensional modeling over 3NF

Dimensional models contain the same information as a fully normalized (3NF) model of the same business process — the difference is degree of normalization, not the underlying facts represented. 3NF suits operational processing well (an update touches the database in only one place), but it is too complex for business intelligence: business users cannot understand, navigate, or remember a schema of potentially hundreds of normalized tables, and unpredictable ad hoc queries overwhelm relational optimizers on deeply normalized schemas. A dimensional model packages the same data in a format that delivers user understandability, query performance, and resilience to change — see [dimensional model extensibility](dimensional-model-extensibility.md).

A 3NF schema is also risky, not just slow, for BI: a query only produces a correct answer if it joins through the *right* path among the many available in a deeply normalized schema, and a wrong-but-plausible join silently returns a meaningless result rather than an error. Star schemas minimize this risk structurally — see "Why it performs well" below — by collapsing the join paths to one hop per dimension.

## Why it performs well

Database optimizers handle a star schema's simple, few-join structure efficiently: they constrain the indexed dimension tables first, then attack the fact table with the Cartesian product of qualifying dimension keys, evaluating arbitrary n-way joins in a single pass through the fact table's index. Every dimension is a symmetrically equal entry point into the fact table, with no built-in bias toward any particular expected query pattern.

## Building a star schema

Every star schema is the product of the [four-step dimensional design process](four-step-dimensional-design-process.md): select the [business process](business-process.md), declare the [grain](grain.md), identify the dimensions, and identify the facts.

## An alternative for less-structured needs

A [wide denormalized table](wide-denormalized-table.md) collapses fact and dimension attributes into one table, trading away conformance and an explicit grain contract for join-free query simplicity — worth considering only where cross-process integration and dimensional discipline aren't actually needed.
