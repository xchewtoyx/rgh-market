---
name: software-design-wiki
description: "Retrieve software design wiki concepts. Use when the question is about software design: Module design; Complexity management; Interface and API design; Public API surface as a product; Refactoring; Test design at the code level; Code-level readability. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# software design wiki

This skill retrieves atomic concept notes for **software-design**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Module design: coupling and cohesion, information hiding, deep versus shallow modules, abstraction layering, when to split and when to merge.
- Complexity management: change amplification, cognitive load, obscurity; strategic versus tactical programming; designing it twice; managing technical debt as a design decision.
- Interface and API design: contracts, error-handling design (exceptions versus results, defining errors out of existence), general-purpose versus special-purpose interfaces, backwards-compatible evolution.
- Public API surface as a product: designing library and SDK interfaces for consumers you cannot refactor — versioning and deprecation policy toward external consumers, semantic-versioning contracts, and client-facing ergonomics (network/service contract surface has its full treatment in `api-design`).
- Refactoring: behaviour-preserving transformation, code smells as signals, seams and dependency-breaking techniques, characterization tests, working safely in legacy code without full understanding.
- Test design at the code level: what makes a unit test valuable, test doubles and their costs, testability as a design property, tests as design feedback.
- Code-level readability: naming, comments that carry design intent, consistency and idiom as engineered properties.

Boundaries:

- Also retrieve from `ci-cd-wiki` for tests as pipeline gates, suite architecture, and delivery-stage design
- Also retrieve from `requirements-architecture-wiki` for system- and service-level architecture (views, quality attributes, ADRs)
- Also retrieve from `automation-engineering-wiki` for software-engineering rigour for operational tooling
- Also retrieve from `change-engineering-wiki` for API versioning and compatibility during rollout
- Also retrieve from `api-design-wiki` for network-facing API contract design (resource modelling, wire naming and typing, versioning policy, API governance)

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
