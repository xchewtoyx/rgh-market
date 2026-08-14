---
name: automation-engineering-wiki
description: "Retrieve automation engineering wiki concepts. Use when the question is about automation engineering: Toil; The automation maturity path; Designing safe automation; Operational software engineering; Ironies of automation; Self-healing and auto-remediation patterns and their risks. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# automation engineering wiki

This skill retrieves atomic concept notes for **automation-engineering**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Toil: definition, measurement, budgets, and the engineering case for elimination.
- The automation maturity path: documented procedure → script → tool → self-service platform → autonomous system.
- Designing safe automation: idempotency, dry-run modes, blast-radius limits, rate limiting, safeguards against runaway automation.
- Operational software engineering: building internal tools and platforms with software-engineering rigour, treating operations as a software problem.
- Ironies of automation: skill atrophy, automation surprises, when humans must take over from automation.
- Self-healing and auto-remediation patterns and their risks.

Boundaries:

- Also retrieve from `ci-cd-wiki` for CI/CD pipelines and deployment automation
- Also retrieve from `incident-management-wiki` for automation failures as incident contributors
- Also retrieve from `capacity-performance-wiki`

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
