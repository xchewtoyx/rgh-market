---
name: operational-handover-wiki
description: "Retrieve operational handover wiki concepts. Use when the question is about operational handover: Runbook and playbook writing; Handover documents; Capturing tacit/tribal knowledge; Maintenance documentation; Troubleshooting guides and onboarding documentation aimed at building independent operating competence, not just…. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# operational handover wiki

This skill retrieves atomic concept notes for **operational-handover**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Runbook and playbook writing: documenting operational procedures so they can be followed correctly under pressure or by an unfamiliar operator.
- Handover documents: transferring ownership of a system, project, or task — what exists, what state it's in, what's unfinished, who to ask.
- Capturing tacit/tribal knowledge: gotchas, non-obvious dependencies, "here be dragons" notes, assumptions a newcomer would otherwise have to rediscover the hard way.
- Maintenance documentation: how to safely change a system after handover — what's safe to touch, what's brittle, where the tests and guardrails are (or aren't).
- Troubleshooting guides and onboarding documentation aimed at building independent operating competence, not just completing one task.

Boundaries:

- Also retrieve from `incident-management-wiki` for incident-response runbooks specifically (what to do _during_ an active incident)
- Also retrieve from `technical-communication-wiki` for general writing clarity and structure
- Also retrieve from `evidence-verification-wiki` for whether a handover document's claims about the system are accurate and verifiable
- Also retrieve from `requirements-architecture-wiki` for documenting why a system was designed the way it was
- Also retrieve from `decision-alignment-wiki` for decisions about who takes ownership and sign-off on a handover
- Also retrieve from `organizational-learning-wiki` for org-wide learning culture, psychological safety, and the social mechanics of knowledge sharing

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
