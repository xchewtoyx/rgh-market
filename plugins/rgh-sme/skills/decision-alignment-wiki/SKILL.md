---
name: decision-alignment-wiki
description: "Retrieve decision alignment wiki concepts. Use when the question is about decision alignment: Decision-document genres; Options analysis; Stakeholder alignment; Making decisions defensible; Turning a decision into coordinated action. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# decision alignment wiki

This skill retrieves atomic concept notes for **decision-alignment**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Decision-document genres: decision memos, RFCs used to drive a decision, proposal documents, recommendation writing.
- Options analysis: framing alternatives fairly, articulating trade-offs, making a clear recommendation rather than leaving the reader to infer one.
- Stakeholder alignment: identifying who needs to agree or be informed, sequencing review and sign-off, surfacing disagreement early rather than discovering it after the fact, consensus-building technique.
- Making decisions defensible: recording what was decided, why, by whom, and what would change the decision — so it can be understood and revisited later without re-litigating it from scratch.
- Turning a decision into coordinated action: clear ownership, next steps, and follow-through tracking as part of the document, not a separate afterthought.

Boundaries:

- Also retrieve from `evidence-verification-wiki` for whether the evidence underlying a decision is true and adequately supported
- Also retrieve from `technical-communication-wiki` for clear prose and structure generally
- Also retrieve from `requirements-architecture-wiki` for architecture- and requirements-specific rationale capture (the "why" of a system design)
- Also retrieve from `operational-handover-wiki` for once a decision is made, documenting how to operate or maintain what was built
- Also retrieve from `judgment-calibration-wiki` for the calibration quality of the estimates and forecasts feeding a decision

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
