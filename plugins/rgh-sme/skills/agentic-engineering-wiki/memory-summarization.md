---
type: concept
title: Memory Summarization
description: >
  Compress redundant short-term history into running summaries, merges, or
  reflection-driven updates to free context without discarding task state.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §2.2"
---

Human language is redundant for clarity; stripping redundancy shrinks the
short-term footprint. Common approaches under
[memory management](memory-management.md):

- **Running summarization** — same or separate model summarizes the
  conversation, often with named-entity tracking.
- **Pairwise keep/merge decisions** — after summarizing, a classifier chooses
  for each (memory sentence, summary sentence) pair whether to keep one, both,
  or neither, recovering facts a summary alone would drop.
- **Reflection-based updates** — after each action, reflect on new information
  and decide insert, merge, or replace when older facts are outdated
  (compatible with [reflection and error correction](reflection-and-error-correction.md)).

Contradiction handling is use-case dependent: default to newer facts, or let a
judge choose; sometimes keeping multiple perspectives is useful. Summarization
beats naive [FIFO context eviction](fifo-context-eviction.md) when early goals
must survive. Under [memory pressure eviction](memory-pressure-eviction.md),
flush can rebuild a **recursive summary** from the existing summary plus the
just-evicted messages so goals survive after the FIFO shrinks. For bulk
corpora outside the chat queue, use
[hierarchical summarization](hierarchical-summarization.md) and decide whether
summaries should be general or
[task-specific](task-specific-summarization.md).
