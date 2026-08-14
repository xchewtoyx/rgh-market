---
name: observability-wiki
description: "Retrieve observability wiki concepts. Use when the question is about observability: Telemetry types and their trade-offs; Instrumentation practice; Debugging methodology; AI agent & LLM observability; Observability data systems; Sociotechnical & developer feedback loops. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# observability wiki

This skill retrieves atomic concept notes for **observability**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Telemetry types and their trade-offs: metrics, logs, traces, structured wide events, continuous profiling (flame graphs), and eBPF kernel tracing.
- Instrumentation practice: OpenTelemetry semantic conventions, context propagation, high cardinality/dimensionality, sampling strategies (head/tail/target-rate), and telemetry pipeline architecture (OTel Collector).
- Debugging methodology: hypothesis-driven exploration, Core Analysis Loops, known-unknowns vs unknown-unknowns, automated anomaly diffing (BubbleUp), and change correlation.
- AI agent & LLM observability: evals-as-telemetry, tracing nondeterministic execution at episode/trajectory scale as the primary unit of analysis (request-scale APM as a secondary lens), runtime invariant assertions, and prompt/token/cost tracking.
- Observability data systems: columnar storage architectures (ClickHouse MergeTree, Retriever), unaggregated wide-event preservation vs pre-aggregation, and high-cardinality query mechanics.
- Sociotechnical & developer feedback loops: Observability-Driven Development (ODD), telemetry cost visibility, and explorable interfaces (de-emphasizing static wall-of-graphs anti-patterns).

Boundaries:

- Also retrieve from `reliability-engineering-wiki` for choosing SLIs and setting SLOs/error budgets
- Also retrieve from `incident-management-wiki` for using telemetry during incident response (who looks at what, when)
- Also retrieve from `capacity-performance-wiki` for load and saturation analysis methodology (USE, queueing behaviour)
- Also retrieve from `dimensional-modelling-wiki` for analytical/warehouse data modelling

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
