---
name: requirements-architecture-wiki
description: "Retrieve requirements architecture wiki concepts. Use when the question is about requirements architecture: Requirements practice; Architecture documentation; Constraints and trade-offs; Rationale capture; Traceability; Requirements for machine consumers. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# requirements architecture wiki

This skill retrieves atomic concept notes for **requirements-architecture**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Requirements practice: eliciting and specifying functional and non-functional requirements, distinguishing requirements from solutions, scoping, prioritisation, acceptance criteria.
- Architecture documentation: design docs, architecture decision records (ADRs), system-context and component diagrams, documenting interfaces and boundaries.
- Constraints and trade-offs: capturing the forces that shaped a design (technical, organisational, cost, timeline), documenting options considered and why one was chosen or rejected.
- Rationale capture: writing the "why", not just the "what" — so a design can be understood, challenged, and revisited later without reconstructing context from scratch.
- Traceability: linking requirements through to design decisions and back, keeping documentation current as a system evolves, deprecating stale design docs.
- Requirements for machine consumers: specifying work an autonomous or LLM-driven agent will implement — acceptance criteria precise enough to guard against literal-genie interpretation and specification gaming, requirements-versus-solutions hygiene when the reader optimises what is written rather than what was meant, and stating the intent and constraints a machine reader cannot infer from shared context.

Boundaries:

- Also retrieve from `evidence-verification-wiki` for whether the requirements/architecture claims are adequately evidenced and independently reviewable
- Also retrieve from `technical-communication-wiki` for general writing clarity and structuring for the reader
- Also retrieve from `decision-alignment-wiki` for choosing between architecture options and getting stakeholders aligned on the choice
- Also retrieve from `operational-handover-wiki` for documenting how to operate, maintain, or troubleshoot the resulting system
- Also retrieve from `agentic-engineering-wiki` for how a requirements artifact moves through an agent harness (task decomposition, prompt and task-IO schema design, handoff mechanics)

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
