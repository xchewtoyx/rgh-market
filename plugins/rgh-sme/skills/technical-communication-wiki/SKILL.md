---
name: technical-communication-wiki
description: "Retrieve technical communication wiki concepts. Use when the question is about technical communication: Audience analysis; Clarity technique; Document structure; Adapting the same material for different formats and reader types (executive summary vs deep reference vs quickstart)…; Editing practice. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# technical communication wiki

This skill retrieves atomic concept notes for **technical-communication**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Audience analysis: identifying who a document is for, what they already know, what they need to do with it, and writing to that reader rather than to the writer's own understanding.
- Clarity technique: plain language, sentence- and paragraph-level editing, active voice, concrete wording, cutting jargon, defining terms once and consistently.
- Document structure: headings and hierarchy, information ordering (inverted pyramid, most-important-first), skimmability, chunking, use of lists/tables/diagrams to carry structure that prose shouldn't.
- Adapting the same material for different formats and reader types (executive summary vs deep reference vs quickstart), without duplicating source content ad hoc.
- Editing practice: revision passes, self-editing checklists, readability review, style consistency across a document or document set.

Boundaries:

- Also retrieve from `evidence-verification-wiki` for whether the _claims_ in a document are true, supported, and reviewable
- Also retrieve from `requirements-architecture-wiki` for capturing requirements, architecture, and design rationale as content
- Also retrieve from `decision-alignment-wiki` for producing decision memos and driving stakeholder alignment
- Also retrieve from `operational-handover-wiki` for runbooks, playbooks, and handover material

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
