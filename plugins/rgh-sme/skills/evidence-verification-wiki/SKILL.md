---
name: evidence-verification-wiki
description: "Retrieve evidence verification wiki concepts. Use when the question is about evidence verification: Substantiating claims; Verification method; Review process; Review workflows; Common failure modes. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# evidence verification wiki

This skill retrieves atomic concept notes for **evidence-verification**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Substantiating claims: sourcing and citing evidence, distinguishing fact from opinion/assumption, flagging unsupported assertions, calibrating confidence language to the strength of the evidence behind it.
- Verification method: reproducibility, cross-checking against source data or a second source, fact-checking practice, distinguishing verified from claimed.
- Review process: structuring a document so an independent reviewer can actually check it (showing work, making assumptions explicit, providing the data/reasoning a claim rests on, not just the conclusion).
- Review workflows: peer review and technical review practice, review checklists, review comment conventions, sign-off/approval trails, audit trails for what was reviewed and by whom.
- Common failure modes: circular sourcing, stale evidence, cherry-picking, confusing correlation with causation, and how document structure guards against them.

Boundaries:

- Also retrieve from `technical-communication-wiki` for general prose clarity and document structure for readability
- Also retrieve from `requirements-architecture-wiki` for requirements and architecture documents are a _type_ of document that needs this discipline applied to it, but the content of what a requirements/design doc should capture
- Also retrieve from `decision-alignment-wiki` for turning verified evidence into a recommendation and getting stakeholders to agree
- Also retrieve from `operational-handover-wiki` for verifying that operational/handover documentation is accurate belongs at the boundary with
- Also retrieve from `judgment-calibration-wiki` for the psychology of miscalibrated judgment and forward-looking probability calibration (bias mechanisms, forecast scoring, debiasing technique)

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
