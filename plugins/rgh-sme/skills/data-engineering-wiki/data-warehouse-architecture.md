---
type: concept
title: Data Warehouse Architecture
description: >
  The organizational pattern (OLAP/OLTP separation, centralization via
  ETL/ELT, department-level data marts) that defines a data warehouse,
  independent of its underlying technical implementation.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 3"
---

Bill Inmon's definition, still the reference point: a data warehouse is "a
subject-oriented, integrated, nonvolatile, and time-variant collection of data
in support of management's decisions."

It's useful to separate the warehouse's **organizational** architecture from
its **technical** implementation — the two have coevolved but are logically
independent (you can have warehouse organization without MPP, or MPP without
warehouse organization). Organizationally, a data warehouse:

1. **Separates [OLAP from OLTP](oltp-vs-olap.md)** — analytical query load is moved off
   production transactional databases, so heavy reporting queries don't
   compete with the application traffic those databases actually serve.
2. **Centralizes and organizes data**, traditionally via [ETL or ELT](etl-vs-elt.md):
   data is pulled from sources, cleaned and modeled, and loaded into the
   warehouse — often further split into per-department **data marts**, a
   warehouse subset serving one line of business. Data marts exist for two
   reasons: they make data easier for analysts and report developers in that
   department to work with, and they add a transformation stage that
   precomputes joins and aggregations to speed up that department's reporting
   queries. How marts relate to the warehouse behind them — derived from one
   central physical repository, or independently built and held consistent
   through shared conformed dimensions — is itself an architectural choice;
   see [Kimball bus vs. Inmon CIF](kimball-bus-vs-inmon-cif-architecture.md).

Technically, warehouses have historically run on **massively parallel
processing (MPP)** engines — first appearing in the late 1970s, popularized
through the 1980s — which support standard SQL semantics while optimizing for
parallel scanning of large data volumes. Modern MPP systems, especially cloud
warehouses, have shifted from row-based to columnar storage, and increasingly
rely on [compute/storage separation](compute-storage-separation.md) rather
than a fixed on-premises cluster.

The warehouse pattern is one point on a spectrum with
[data lake architecture](data-lake-architecture.md) and
[the lakehouse](data-lakehouse.md); modern cloud platforms increasingly blur
the distinction (see [pipeline metadata categories](pipeline-metadata-categories.md)
for how schema is tracked differently across these). Calling something a
warehouse doesn't make it one — see
[relational warehouse anti-patterns](relational-warehouse-anti-patterns.md)
for the recurring ways a build skips the modeling work this pattern actually
depends on.
