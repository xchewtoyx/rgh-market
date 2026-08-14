---
type: concept
title: Information Holder Resource
description: >
  A data-oriented endpoint representing a domain entity with coordinated
  create/read/update/delete and search operations hiding implementation detail.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 3"
---

An **information holder resource** exposes domain data while hiding storage
layout, coordinating concurrent access in the implementation. Standard
create/read/update/delete and search map naturally here — but naive one-field-
one-endpoint CRUD tends toward chatty, tightly coupled APIs.

Refine by data lifetime and changeability:

- [Operational data holder](operational-data-holder.md) — short-lived
  transactional entities, frequent change, many outgoing relations.
- [Master data holder](master-data-holder.md) — long-lived parties and things,
  widely referenced, infrequent change; deletes are special updates.
- [Reference data holder](reference-data-holder.md) — immutable shared codes;
  read-only.
- [Data transfer resource](data-transfer-resource.md) — shared drop box for
  decoupled participants in time and location.
- [Link lookup resource](link-lookup-resource.md) — resolves current addresses
  for [link elements](link-element.md).

Design around well-scoped aggregates or business capabilities rather than
anemic one-table-per-endpoint mappings. Pair with
[retrieval operations](retrieval-operation.md) using [pagination](pagination.md)
for large collections.

Sample trade-off: expressive CRUD on customer contact data couples the channel
to the customer backend — acceptable when a consolidated cross-system view is
the goal if performance and availability are engineered.
