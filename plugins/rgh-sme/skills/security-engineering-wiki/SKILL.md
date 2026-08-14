---
name: security-engineering-wiki
description: "Retrieve security engineering wiki concepts. Use when the question is about security engineering: Threat modelling; Secure-design principles; Identity, authentication and authorisation as design concepts; Vulnerability classes as concepts; Security and reliability as related system properties; Security assurance practice; Machine-agent identity and delegated authority; The LLM/agent threat surface as a vulnerability-class family. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# security engineering wiki

This skill retrieves atomic concept notes for **security-engineering**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Threat modelling: assets, adversaries and their capabilities, attack surfaces, trust boundaries, structured enumeration (STRIDE-style), abuse cases alongside use cases.
- Secure-design principles: least privilege, defence in depth, secure defaults, minimising blast radius, separation of duties, designing for auditability, zero-trust reasoning.
- Identity, authentication and authorisation as design concepts: credential lifecycle, secrets management, session semantics, service-to-service identity.
- Vulnerability classes as concepts: injection, memory safety, confused deputy, supply-chain compromise — the pattern and its structural defence, not exploit technique.
- Security and reliability as related system properties: failing safe versus failing secure, recovery and incident containment design, insider risk, the cost of security controls on operability.
- Security assurance practice: security design review, red-team findings as evidence, proportionate control selection.
- Machine-agent identity and delegated authority: how autonomous and LLM-driven agents acquire, scope, attenuate, rotate, and audit credentials; per-user authorization flowing through tool calls; safe-proxy / attenuated-authority patterns; trust and review burden scaled to the actor's capability and autonomy.
- The LLM/agent threat surface as a vulnerability-class family: direct and indirect prompt injection as the injection pattern's natural-language instance, model-as-confused-deputy, agent-memory and retrieval-corpus poisoning, system-prompt extraction — the pattern and its structural defence, not exploit technique.

Boundaries:

- Also retrieve from `ci-cd-wiki` for supply-chain enforcement in delivery pipelines (provenance, signing, admission policy)
- Also retrieve from `infrastructure-as-code-wiki` for policy-as-code and compliance controls on infrastructure
- Also retrieve from `incident-management-wiki` for incident response structure
- Also retrieve from `reliability-engineering-wiki` for reliability patterns and error budgets
- Also retrieve from `agentic-engineering-wiki` for harness enforcement mechanics

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
