---
name: data-engineering-wiki
description: "Retrieve data engineering wiki concepts. Use when the question is about data engineering: Pipeline design; Loading dimensional and analytical structures; Data quality engineering; Orchestration; Analytical platform architecture; Data lifecycle engineering. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# data engineering wiki

This skill retrieves atomic concept notes for **data-engineering**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Pipeline design: batch and streaming ingestion, ETL versus ELT, incremental loading, backfill and reprocessing strategy, idempotent and replayable jobs.
- Loading dimensional and analytical structures: surrogate-key pipelines, slowly-changing-dimension processing, late-arriving fact and dimension handling — the load mechanics that implement patterns whose design `dimensional-modelling` owns.
- Data quality engineering: validation gates, reconciliation against source systems, audit and lineage trails, data contracts, quarantine and error-row handling.
- Orchestration: dependency graphs, scheduling, retry and recovery semantics, delivery guarantees (exactly-once versus at-least-once) as pipeline correctness concerns.
- Analytical platform architecture: raw/staging/presentation layering, warehouse versus lake versus lakehouse trade-offs, partitioning for load and query, integration and historisation layers (Data Vault and similar).
- Data lifecycle engineering: retention, archival, versioning of datasets, and metadata/governance as pipeline concerns.

Boundaries:

- Also retrieve from `dimensional-modelling-wiki` for dimensional design decisions
- Also retrieve from `ci-cd-wiki` for delivery pipelines for code and infrastructure
- Also retrieve from `reliability-engineering-wiki` for operational reliability of stateful stores (backup/recovery, replication operations) and data-reliability SLIs (freshness, completeness)
- Also retrieve from `capacity-performance-wiki` for resource-level performance of data systems (memory, I/O, query tuning)
- Also retrieve from `observability-wiki` for telemetry pipelines (collectors, sampling, observability data systems)

## How to retrieve

Do not load every note in this folder. Do not load the whole bundle into context.

1. Scan `concepts.json` in this skill folder, beside SKILL.md and the `*.md`
   notes. Match the question against each concept's `description`, `title`,
   and `concept_id`. When the question is broad, prefer higher `pagerank`
   and `concepts[].inbound_link_count` as starting seeds. Do not grep note
   frontmatter. Folded YAML `description: >` breaks line-oriented grep.
2. Read only the matching `*.md` file in this same folder. The filename
   stem is the `concept_id`.
3. Follow basename CommonMark links (`[label](other-note.md)`) hop by hop.
   Read a linked note only when the current note invokes a concept the task
   needs next.
4. Stop when the question is answered. Cite the concept id, title, and the
   note's `sources:` frontmatter.

## Do not

- Do not answer from `fleeting/` literature notes (unatomized, not
  quality-gated). If a concept exists only there, treat it as absent.
- Do not invent wiki notes, index pages, hubs, or tag schemes.
- Do not create `index.md` or README files inside the wiki.
