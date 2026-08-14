---
name: ci-cd-wiki
description: "Retrieve ci cd wiki concepts. Use when the question is about ci cd: Continuous integration, build automation, artifact management, and commit-stage feedback; Deployment pipelines, release orchestration, environment promotion, and automated rollback execution; Automated acceptance, integration, and non-functional testing as delivery gates; Software supply chain security; Evolutionary database schema migrations, database sandboxing, and zero-downtime schema deployment patterns; Pipeline design for repeatability, fast feedback, traceability, and safe change flow; Versioning, branching, dependency management, and release coordination; On-demand, self-service provisioning of ephemeral test environments within delivery pipelines; Delivery metrics and pipeline bottleneck diagnosis when they guide pipeline improvement; Delivery of LLM/agent artifacts. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# ci cd wiki

This skill retrieves atomic concept notes for **ci-cd**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Continuous integration, build automation, artifact management, and commit-stage feedback.
- Deployment pipelines, release orchestration, environment promotion, and automated rollback execution.
- Automated acceptance, integration, and non-functional testing as delivery gates.
- Software supply chain security: hermetic builds, binary provenance, artifact signing, and policy enforcement at deployment choke points.
- Evolutionary database schema migrations, database sandboxing, and zero-downtime schema deployment patterns.
- Pipeline design for repeatability, fast feedback, traceability, and safe change flow.
- Versioning, branching, dependency management, and release coordination.
- On-demand, self-service provisioning of ephemeral test environments within delivery pipelines.
- Delivery metrics and pipeline bottleneck diagnosis when they guide pipeline improvement.
- Delivery of LLM/agent artifacts: prompts, tool and harness definitions, eval suites, and model pins as versioned, pipeline-managed artifacts; eval regression suites as delivery gates alongside conventional tests; rollback and traceability for changes — including provider model swaps — that alter behaviour without a code diff.

Boundaries:

- Also retrieve from `change-engineering-wiki` for broader change-risk policy, rollout strategy, and organizational change practice
- Also retrieve from `infrastructure-as-code-wiki` for declarative infrastructure design, state, modules, and policy-as-code
- Also retrieve from `automation-engineering-wiki` for operational automation and auto-remediation
- Also retrieve from `incident-management-wiki` for incident response, postmortems, and live-service recovery
- Also retrieve from `agentic-engineering-wiki` for the design of the prompts, harnesses, and offline eval content being delivered
- Also retrieve from `observability-wiki`

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
