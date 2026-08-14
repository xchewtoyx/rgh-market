---
name: dimensional-modelling-wiki
description: "Retrieve dimensional modelling wiki concepts. Use when the question is about dimensional modelling: Dimensional modelling technique; Fact table types (transaction, periodic snapshot, accumulating snapshot, factless), additivity, degenerate dimensions; Dimension design; The bus architecture, bus matrix, and enterprise conformance, including the business-led governance process that…; The dimensional design process; Physical implementation of a dimensional model; Schema patterns that absorb operational/timing realities; Trade-offs versus other modelling styles (Inmon's Corporate Information Factory, stand-alone data marts, Data Vault…. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# dimensional modelling wiki

This skill retrieves atomic concept notes for **dimensional-modelling**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Dimensional modelling technique: facts, dimensions, star and snowflake schemas, grain declaration, surrogate keys.
- Fact table types (transaction, periodic snapshot, accumulating snapshot, factless), additivity, degenerate dimensions.
- Dimension design: slowly changing dimensions, conformed dimensions, role-playing, junk and outrigger dimensions, hierarchies, bridge tables.
- The bus architecture, bus matrix, and enterprise conformance, including the business-led governance process that produces conformed definitions.
- The dimensional design process: gathering business requirements, identifying business processes, grain-first design.
- Physical implementation of a dimensional model: relational star/snowflake schema and multidimensional OLAP cube as co-equal targets.
- Schema patterns that absorb operational/timing realities: late-arriving facts and dimensions, real-time fact tables, audit dimensions, error event schemas — own the pattern itself, not the pipeline that implements it.
- Trade-offs versus other modelling styles (Inmon's Corporate Information Factory, stand-alone data marts, Data Vault, wide tables) as they affect dimensional design decisions.

Boundaries:

- Also retrieve from `observability-wiki` for telemetry "dimensions"/cardinality in monitoring systems
- Also retrieve from `capacity-performance-wiki` for warehouse capacity, query performance tuning, and cost
- Also retrieve from `automation-engineering-wiki` for ETL/ELT pipeline operability and deployment
- Also retrieve from `change-engineering-wiki`
- Also retrieve from `decision-alignment-wiki` for cross-departmental stakeholder consensus on conformed definitions

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
