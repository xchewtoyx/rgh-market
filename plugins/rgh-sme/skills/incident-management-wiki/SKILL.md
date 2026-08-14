---
name: incident-management-wiki
description: "Retrieve incident management wiki concepts. Use when the question is about incident management: Incident response structure; On-call design; Postmortems and learning from incidents; Preparedness. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# incident management wiki

This skill retrieves atomic concept notes for **incident-management**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Incident response structure: roles (incident command), escalation, communication during incidents, severity classification.
- On-call design: rotation structure, pager load, handoffs, compensation and sustainability.
- Postmortems and learning from incidents: blameless practice, contributing factors over root cause, action-item quality, incident reviews.
- Preparedness: game days, chaos experiments as organisational practice, runbooks and their limits.

Boundaries:

- Also retrieve from `resilience-engineering-wiki` for safety science and resilience-engineering theory
- Also retrieve from `observability-wiki` for the telemetry and query techniques used during diagnosis
- Also retrieve from `reliability-engineering-wiki` for error-budget policy
- Also retrieve from `change-engineering-wiki` for rollback and change-related remediation mechanics
- Also retrieve from `automation-engineering-wiki` for automation that prevents or auto-remediates incidents

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
