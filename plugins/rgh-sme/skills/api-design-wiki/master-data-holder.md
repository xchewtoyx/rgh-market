---
type: concept
title: Master Data Holder
description: >
  An information holder for long-lived, widely referenced entities with
  infrequent change, strong quality requirements, and careful delete semantics.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 3, ch. 5"
---

A **master data holder** is an [information holder resource](information-holder-resource.md)
for **master data** — parties (customers, employees, suppliers) and things
(products, materials, vehicles) and places. Long-lived, frequently referenced,
relatively stable.

Operations must preserve consistency and reference integrity across systems.
Treat delete as a special update ([soft deletion](soft-deletion.md) or status
change) rather than hard removal when references exist.

Drivers: data quality, protection from breach, cross-organizational ownership.
Consolidating master data in one API creates a bottleneck and single point of
failure unless scaled and cached deliberately.

Avoid chatty per-attribute CRUD; model rich aggregates. Often paired with
[reference data holders](reference-data-holder.md) for codes and
[link lookup resources](link-lookup-resource.md) for dynamic references.
