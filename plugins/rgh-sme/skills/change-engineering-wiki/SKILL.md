---
name: change-engineering-wiki
description: "Retrieve change engineering wiki concepts. Use when the question is about change engineering: Progressive delivery; Rollback engineering; Release verification; CI/CD as a safety system; Change risk management; Delivery metrics (DORA-style) as they inform delivery safety. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# change engineering wiki

This skill retrieves atomic concept notes for **change-engineering**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Progressive delivery: canary releases, blue-green deployment, rolling updates, traffic shifting, feature flags and their lifecycle.
- Rollback engineering: designing for rollback, roll-forward vs roll-back, data/schema migration safety, backwards compatibility windows.
- Release verification: canary analysis, automated release gating, pre-production fidelity limits, testing in production.
- CI/CD as a safety system: pipeline design, deployment frequency, batch size, lead time, and their relationship to change failure rate.
- Change risk management: change review, freeze windows and their pathologies, coordinating changes across services.
- Delivery metrics (DORA-style) as they inform delivery safety.

Boundaries:

- Also retrieve from `reliability-engineering-wiki` for error budgets that gate releases
- Also retrieve from `incident-management-wiki` for responding to a bad change once it becomes an incident
- Also retrieve from `automation-engineering-wiki` for general operational automation and tooling
- Also retrieve from `observability-wiki` for canary _metric analysis_ techniques
- Also retrieve from `api-design-wiki` for API versioning strategy and the compatibility contract itself

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
