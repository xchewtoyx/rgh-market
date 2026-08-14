---
name: data-visualization-wiki
description: "Retrieve data visualization wiki concepts. Use when the question is about data visualization: Matching visual form to analytical question; Perceptual foundations; Dashboard design; Graphical integrity; Analytical interaction. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# data visualization wiki

This skill retrieves atomic concept notes for **data-visualization**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Matching visual form to analytical question: comparison, trend, distribution, part-to-whole, correlation, deviation — and when a table beats a chart.
- Perceptual foundations: preattentive attributes, effectiveness ordering of visual encodings, Gestalt grouping, colour use and its pitfalls, data-ink and decluttering.
- Dashboard design: composition and layout for at-a-glance comprehension, information density, context for numbers (targets, ranges, prior periods), monitoring displays versus exploratory analysis displays.
- Graphical integrity: honest axes, scales, baselines and aggregation choices; forms that mislead (truncated bars, dual axes, 3-D effects) and honest alternatives.
- Analytical interaction: drill-down, filtering, linked views, and progressive disclosure as consumption design.

Boundaries:

- Also retrieve from `evidence-verification-wiki` for detecting misleading statistics and quantitative claims
- Also retrieve from `technical-communication-wiki` for prose, document structure, and audience adaptation around a figure
- Also retrieve from `dimensional-modelling-wiki` for the analytical data model behind a dashboard
- Also retrieve from `observability-wiki` for monitoring-display design as applied to telemetry

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
