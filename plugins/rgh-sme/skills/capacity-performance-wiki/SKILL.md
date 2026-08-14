---
name: capacity-performance-wiki
description: "Retrieve capacity performance wiki concepts. Use when the question is about capacity performance: Capacity planning; Performance analysis methodology; Load characterisation and testing; Latency engineering; Efficiency and cost; Scalability patterns as they affect capacity. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# capacity performance wiki

This skill retrieves atomic concept notes for **capacity-performance**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Capacity planning: demand forecasting, organic vs inorganic growth, headroom, N+M redundancy, capacity models.
- Performance analysis methodology: USE method, latency percentiles and their pitfalls, queueing theory basics, utilisation vs saturation vs errors.
- Load characterisation and testing: load generation, stress vs soak, finding saturation points, capacity limits per resource.
- Latency engineering: tail latency, amplification in fan-out systems, latency budgets across call chains.
- Efficiency and cost: utilisation targets, overprovisioning trade-offs, cost as an engineering signal, rightsizing.
- Scalability patterns as they affect capacity: horizontal vs vertical scaling limits, per-resource bottleneck analysis.

Boundaries:

- Also retrieve from `observability-wiki` for the instrumentation that produces performance telemetry
- Also retrieve from `reliability-engineering-wiki` for latency _SLO targets_
- Also retrieve from `automation-engineering-wiki` for autoscaling implementation
- Also retrieve from `incident-management-wiki` for load-related incident response

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
