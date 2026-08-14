---
name: resilience-engineering-wiki
description: "Retrieve resilience engineering wiki concepts. Use when the question is about resilience engineering: Accident causation models; Safety-I versus Safety-II; Human factors of failure; Safety culture and organisation; The human-factors critique of procedures. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# resilience engineering wiki

This skill retrieves atomic concept notes for **resilience-engineering**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Accident causation models: root-cause fallacy versus contributing factors, chain-of-events versus systemic models, drift into failure, normalisation of deviance, Rasmussen's safety-boundary migration model, control-theoretic models (STAMP).
- Safety-I versus Safety-II: performance variability as normal work, why success and failure share the same sources, graceful extensibility and adaptive capacity, anticipation/monitoring/responding/learning.
- Human factors of failure: local rationality, hindsight and outcome biases as they apply to accident analysis (the general bias mechanisms and their effect on forecast feedback belong to `judgment-calibration`), error as symptom rather than cause, sharp end versus blunt end, plan-continuation bias, decontextualisation traps.
- Safety culture and organisation: just culture (retributive versus restorative), Westrum's typology, chronic unease, safety bureaucracy and safety clutter, blame's effect on reporting and learning — as safety science for high-risk systems (psychological safety and learning culture as general knowledge-work constructs belong to `organizational-learning`).
- The human-factors critique of procedures: work-as-imagined versus work-as-done, procedural drift, work-to-rule, why compliance and safety are not the same thing.

Boundaries:

- Also retrieve from `incident-management-wiki` for incident response and learning practice
- Also retrieve from `reliability-engineering-wiki` for technical resilience patterns (circuit breaking, graceful degradation, load shedding, cascading-failure prevention)
- Also retrieve from `automation-engineering-wiki` for ironies of automation and human-automation interaction
- Also retrieve from `operational-handover-wiki` for writing runbooks and procedures that survive real operating conditions

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
