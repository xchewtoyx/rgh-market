---
type: concept
title: Non-LLM Task Implementation
description: >
  Not every workflow task needs an LLM — mechanical, retrieval, and
  classification tasks are usually cheaper and more dependable without one.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
---

Before implementing any [workflow task](task-io-schema-design.md) with an
LLM, check whether it needs one at all:

- **Purely mechanical or retrieval tasks** — crawling a site's content,
  saving content to a database — should just use traditional software. An
  LLM adds cost, latency, and nondeterminism for zero benefit over code that
  already does the job reliably.
- **Where classification suffices, use a dedicated classifier** (e.g. a
  BERT-based model) rather than an LLM. A classifier is more dependable — it
  won't "make commentary" instead of classifying — and is faster and cheaper
  to run per item.

This is the task-level instance of the same principle
[progressive agent architecture](progressive-agent-architecture.md) applies at
the system level: don't reach for the more general, more expensive tool when
a narrower one already solves the problem. Reserve
[templated-prompt](templated-prompt-task.md) and
[tool-based](forced-tool-choice-extraction.md) task implementations for the
tasks that genuinely need an LLM's language understanding or generation.
