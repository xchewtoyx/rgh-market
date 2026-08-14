---
name: agentic-engineering-wiki
description: "Retrieve agentic engineering wiki concepts. Use when the question is about agentic engineering: Prompt and context engineering; Harness and agent-computer interface (ACI) design; Agent loop and orchestration design; External memory and knowledge architecture for agents; Agent failure modes and design-time evaluation; Maintenance and evolution. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# agentic engineering wiki

This skill retrieves atomic concept notes for **agentic-engineering**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Prompt and context engineering: structuring instructions, examples, retrieved material, and working memory for reliable model behaviour; context-window budget and information density; failure modes of poorly structured context.
- Harness and agent-computer interface (ACI) design: tool/function contracts and inventories; action/observation surfaces shaped for LM limits (not human IDE defaults); permission and approval models; sandboxing and blast-radius limits for model-generated write actions; system-prompt / episode-prompt architecture; configurable harness knobs for safe iteration.
- Agent loop and orchestration design: planning/execution loop patterns (including ReAct-style thought/action/observation), subagent dispatch and delegation, multi-agent architectures, task decomposition, control-flow topologies, state and memory management across turns.
- External memory and knowledge architecture for agents: how an agent's durable knowledge store is structured, retrieved, and kept current as a design discipline (this wiki's own onboard/curate pipeline is an instance of the pattern, not the subject — you own the general design knowledge, not this repo's own operation).
- Agent failure modes and design-time evaluation: planning and tool-use failure taxonomies, recovery-oriented guardrails, and offline harness/prompt regression criteria used to iterate the system — not runtime observability practice.
- Maintenance and evolution: prompt and harness versioning, regression testing of agent behaviour, and iterating a harness safely as underlying models change.

Boundaries:

- Also retrieve from `observability-wiki` for evaluating and monitoring agent behaviour at runtime
- Also retrieve from `automation-engineering-wiki` for general safe-automation principles (idempotency, dry-run modes, blast-radius limits as a general operational-safety concept, the automation maturity path)
- Also retrieve from `ci-cd-wiki` for deployment mechanics for prompts and harnesses as software artifacts (pipelines, versioned releases, rollout)
- Also retrieve from `requirements-architecture-wiki` for general architecture-documentation practice (ADRs, design docs, rationale capture)
- Also retrieve from `security-engineering-wiki` for agent identity and credential architecture (how an agent's authority is provisioned, scoped, and audited) and the general LLM threat-model discipline
- This skill does not cover model alignment manufacturing (RLHF / preference training pipelines) and chip-level or generic inference-service optimization

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
