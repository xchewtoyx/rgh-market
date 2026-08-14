---
name: reliability-engineering-wiki
description: "Retrieve reliability engineering wiki concepts. Use when the question is about reliability engineering: SLI identification; SLO development; Error budgets; Alerting on SLOs; Service-level management practice; Reliability principles; Service-level management for nondeterministic, model-backed services. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# reliability engineering wiki

This skill retrieves atomic concept notes for **reliability-engineering**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- SLI identification: user-journey-based SLIs, SLI specification vs implementation, good/valid-event definitions, measurement points, and data-reliability properties (freshness, completeness, durability, integrity) as a distinct SLI class for data and pipeline services.
- SLO development: target selection, windows, achievable vs aspirational targets, iterating on SLOs.
- Error budgets: computation, burn rate, error-budget policies, using budgets to arbitrate between velocity and stability.
- Alerting on SLOs: burn-rate alerts, multi-window alerting, paging philosophy grounded in user impact.
- Service-level management practice: stakeholder agreement, SLAs vs SLOs, reporting, reliability reviews.
- Reliability principles: embracing risk, the cost of nines, dependency and critical-path reliability, and resilience architecture patterns that prevent cascading failure (graceful degradation, circuit breaking, load shedding).
- Service-level management for nondeterministic, model-backed services: choosing which agent/LLM quality signals (task success, faithfulness, refusal correctness) become user-journey SLIs, setting targets and error budgets that absorb model nondeterminism, and treating model or prompt regressions and drift as budget-consuming events.

Boundaries:

- Also retrieve from `observability-wiki` for instrumentation mechanics and dashboard design
- Also retrieve from `incident-management-wiki` for what happens when an incident occurs (response, postmortems)
- Also retrieve from `change-engineering-wiki` for release gating and progressive-delivery mechanics
- Also retrieve from `capacity-performance-wiki` for capacity headroom and performance targets
- Also retrieve from `automation-engineering-wiki` for toil measurement, self-service tooling, and operational-automation practice
- Also retrieve from `agentic-engineering-wiki` for offline eval design and regression suites for iterating an agent harness

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
