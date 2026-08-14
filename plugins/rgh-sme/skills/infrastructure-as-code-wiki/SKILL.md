---
name: infrastructure-as-code-wiki
description: "Retrieve infrastructure as code wiki concepts. Use when the question is about infrastructure as code: Infrastructure expressed as version-controlled, reviewable declarations; Resource, module, component, and stack design; State management, drift detection, import, migration, and reconciliation; Safe live-infrastructure change; Infrastructure testing, validation, policy-as-code, and compliance controls; Cost governance embedded in infrastructure code and its pipeline; Reusable infrastructure interfaces, environment promotion, and team workflows; Tooling choices and trade-offs for provisioning and configuration systems. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# infrastructure as code wiki

This skill retrieves atomic concept notes for **infrastructure-as-code**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Infrastructure expressed as version-controlled, reviewable declarations.
- Resource, module, component, and stack design; composition and dependencies.
- State management, drift detection, import, migration, and reconciliation.
- Safe live-infrastructure change: blue-green/canary cutover, expand-and-contract, feature toggles, rolling updates, and roll-forward recovery for stateless and stateful (data-bearing) infrastructure.
- Infrastructure testing, validation, policy-as-code, and compliance controls.
- Cost governance embedded in infrastructure code and its pipeline: sizing/budget policy gates, automated cost estimation, and cost-attribution tagging.
- Reusable infrastructure interfaces, environment promotion, and team workflows.
- Tooling choices and trade-offs for provisioning and configuration systems.

Boundaries:

- Also retrieve from `ci-cd-wiki` for CI/CD pipeline mechanics, artifact flow, and application release orchestration
- Also retrieve from `automation-engineering-wiki` for operational runbooks, remediation automation, and self-healing systems
- Also retrieve from `capacity-performance-wiki` for capacity models, workload sizing, and performance diagnosis

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
