---
type: concept
title: Pipeline Metadata Categories
description: >
  The four kinds of metadata (business, technical, operational, reference) a
  pipeline generates or depends on, and why operational metadata is usually
  the most scattered.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

DAMA's DMBOK splits metadata — "data about data" — into four categories, all
of which a pipeline touches:

- **Business metadata**: business definitions, rules, and ownership — e.g.,
  what precisely counts as a "customer" for a given analysis. This is where
  ambiguity in a pipeline's output usually traces back to.
- **Technical metadata**: schema, [lineage](data-lineage.md), field mappings,
  and pipeline/workflow definitions from the orchestration layer. Note that
  object stores don't manage schema internally and need an external
  metastore, while cloud warehouses manage schema internally.
- **Operational metadata**: job IDs, runtime logs, process statistics, error
  logs. This category is often scattered across many separate systems (the
  orchestrator, the compute engine, individual job logs) — that scatter is a
  major reason next-generation orchestration and metadata tooling exists, and
  a pipeline that doesn't consolidate it will struggle to answer basic
  "what actually happened on that run?" questions during an incident.
- **Reference metadata**: lookup/classification data such as geographic codes,
  units of measurement, or internal calendar standards. It changes slowly and
  is sometimes sourced externally, but a pipeline that inlines it ad hoc
  instead of treating it as a managed reference dataset will drift out of sync
  across jobs.

Metadata capture is an investment in a pipeline's own future discoverability
and debuggability, not overhead — a pipeline that emits none of the four
categories is opaque to the next engineer (or the same engineer, six months
later) who has to reason about what it did.
