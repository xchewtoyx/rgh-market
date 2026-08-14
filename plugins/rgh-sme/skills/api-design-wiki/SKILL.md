---
name: api-design-wiki
description: "Retrieve api design wiki concepts. Use when the question is about api design: Resource and endpoint modelling; Wire-contract naming, typing, and identification; Message and parameter structure; Operation semantics for async and bulk work; Reliability-facing contract mechanics; Response shaping and transfer efficiency; API evolution and lifecycle governance; API-as-product decisions. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# api design wiki

This skill retrieves atomic concept notes for **api-design**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Resource and endpoint modelling: resource orientation versus RPC; the standard-method contract (get/list/create/update/delete/replace) and its idempotency and side-effect discipline; custom methods; endpoint roles (processing versus information-holder resources; operational, master, and reference data holders); resource hierarchy versus cross-reference; association resources and add/remove methods; polymorphic resources.
- Wire-contract naming, typing, and identification: naming grammar, context, and units for wire-visible names; primitive and collection data types with explicit missing-versus-null and default-value policy; identifier design — format, checksums, permanence, uniqueness scope, UUID trade-offs.
- Message and parameter structure: request/response structural patterns (atomic parameter, parameter list, tree, forest); element stereotypes (data, metadata, ID, link); field masks for partial retrieval and update; context representation; error-report shape.
- Operation semantics for async and bulk work: long-running operations, rerunnable jobs, singleton sub-resources, batch operations, criteria-based deletion, anonymous writes, import/export as contract-level data movement.
- Reliability-facing contract mechanics: request deduplication and idempotency keys, request validation (`validateOnly`), resource revisions, retry guidance in the contract (backoff expectations, `Retry-After`), and the authentication surface of the message (API keys as elements, request-fingerprint signing) — the wire-visible mechanism, not the theory behind it.
- Response shaping and transfer efficiency: pagination, filtering, wish lists/templates, embedded entity versus linked information holder, conditional requests, request bundles.
- API evolution and lifecycle governance: versioning strategy (perpetual stability, agile instability, semantic versioning) and an explicit backward-compatibility definition; deprecation and decommissioning patterns (two in production, limited lifetime guarantee, aggressive obsolescence, experimental preview); soft deletion as an evolution-safety pattern.
- API-as-product decisions: visibility (public/community/solution-internal), frontend versus backend integration, what an API description must document, pricing plans, rate limits, and service-level agreements as the published contract's governance layer; developer experience as a design objective.

Boundaries:

- Also retrieve from `software-design-wiki` for module- and code-level interface design (deep versus shallow modules, error-handling design inside a codebase, code-level compatible evolution)
- Also retrieve from `change-engineering-wiki` for rollout mechanics of a version change (deploy sequencing, canary, migration execution, compatibility windows during rollout)
- Also retrieve from `distributed-systems-wiki` for general distribution failure semantics (why retries are unsafe, delivery guarantees, partial failure)
- Also retrieve from `security-engineering-wiki` for threat modelling, credential lifecycle, and identity architecture
- Also retrieve from `requirements-architecture-wiki` for ADR and design-doc practice
- Also retrieve from `technical-communication-wiki` for general writing craft
- Also retrieve from `agentic-engineering-wiki` for tool/function contracts shaped for LLM consumption (ACI design)

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
