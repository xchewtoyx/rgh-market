---
type: concept
title: Agent Memory Tiers
description: >
  Internal model knowledge, short-term context, and long-term external stores
  form a hierarchy for what an agent retains and where.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §2"
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    resource: "Generative Agents (Park et al.), pp. 1–22"
---

Memory mechanisms let a model retain and use information beyond a single bare
generation. Three tiers:

1. **Internal knowledge** — weights from training/finetuning; available on every
   query; changes only when the model is updated. Put information essential for
   *all* tasks here.
2. **Short-term memory** — the context window: recent turns, instructions,
   examples, tool inventories, plans, tool outputs, reflections. Fast but
   capacity-limited; reserved for what matters to the *current* task.
3. **Long-term memory** — external stores accessed by retrieval (the durable
   side of RAG-style systems). Persists across tasks; content can be deleted
   without retraining.

RAG and agents routinely overflow context; a memory system extends effective
capability. Choose tier by use frequency. [Memory management](memory-management.md)
moves overflow between short- and long-term stores; retrieval pulls long-term
content back into context under [context engineering](context-engineering.md).
[OS-inspired agent memory](os-inspired-agent-memory.md) makes the short-term
window explicit **main context** and long-term stores **external context**,
with [main-context sections](main-context-sections.md) partitioning what the
processor sees each turn. A [memory stream](memory-stream.md) is another
long-term shape: append-only natural-language experiences retrieved by
recency, importance, and relevance into the short-term prompt.
