---
type: concept
title: API Design Pattern
description: >
  A reusable interface blueprint for recurring API problems, documented with
  motivation through trade-offs, chosen early because public contracts resist change.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 2"
---

A **design pattern** is a repeatable structure adjusted per problem — a blueprint,
not a shipped library. **API design patterns** apply that idea to the **interface**:
most describe wire shape and behavior obligations, not server implementation.

Patterns mix and match (pagination plus [long-running operation](long-running-operation.md)
plus [import and export as contract](import-export-as-contract.md)) rather than
 prescribing whole systems.

## Why patterns matter for APIs

APIs are **rigid** (computers break on renames) and often **public** (large unknown
audience) — the hardest cell in the flexibility×visibility matrix. Internal GUIs
and private modules iterate cheaply; [web API characteristics](web-api-characteristics.md)
force immediate consumer impact. Proven patterns reduce late **breaking** structural
changes — for example adding [pagination](pagination.md) after launch silently truncates
datasets for old clients computing aggregates on "full" results.

Catalog entries follow a fixed shape: name, motivation, overview, implementation
(with example definitions), trade-offs.

## Pattern versus ad hoc growth

Ad hoc designs that "return everything" or a single download URI can look close
to pattern-based designs until requirements arrive (destinations, compression,
progress). Retrofitting then breaks consumers; pattern-first shapes ([operation resource shape](operation-resource-shape.md),
polymorphic config objects) absorb extension via optional fields and new subtypes
under [backward compatibility policy](backward-compatibility-policy.md).

Naming, resource layout, and data types are foundational topics that are not always
full patterns themselves but feed every pattern application — see [good API design qualities](good-api-design-qualities.md)
and [resource orientation versus RPC](resource-orientation-vs-rpc.md).
