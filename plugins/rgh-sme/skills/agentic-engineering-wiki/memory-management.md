---
type: concept
title: Memory Management
description: >
  Decide what enters short-term context versus long-term store, and when to
  add, merge, summarize, or evict so the window stays within budget.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §2"
---

A memory system has two jobs: **management** (what lives in short-term versus
long-term [agent memory tiers](agent-memory-tiers.md)) and **retrieval**
(pulling task-relevant long-term items — mechanically like RAG). Management is
add and delete.

Long-term deletion is often optional because external storage is cheap.
Short-term memory is bound by context limits and needs an explicit strategy.
Reserve a slice of the window for retrieved long-term content (for example 30%);
the rest is short-term budget — when it fills, overflow moves out.

Strategies include [FIFO context eviction](fifo-context-eviction.md),
[memory pressure eviction](memory-pressure-eviction.md),
[memory summarization](memory-summarization.md), reflection-driven insert /
merge / replace, [self-directed memory management](self-directed-memory-management.md)
via memory tools, and contradiction policies (prefer newer, or judge which to
keep). [Zettelkasten agent memory notes](zettelkasten-agent-memory-notes.md)
are a different answer to the add/organize half of this problem: instead of a
developer-predefined store shape, an LLM authors each note's structure at
write time and existing notes can themselves be revised as new ones arrive
([memory evolution on retrieval](memory-evolution-on-retrieval.md)). Usage-based eviction (LFU) is harder because detecting when the model
actually *used* a fact is non-trivial.

For conversational agents specifically,
[topic-shift context truncation](topic-shift-context-truncation.md) drops
prior turns once the conversation has moved on, rather than evicting on a
fixed window or usage signal: inactivity thresholds that clear older sessions
are simple; model-judged relevance is more accurate but adds cost and
latency — often better as a small specialized model than a full-size side
call. Keep enough prior conversation for reference resolution inside
[conversational agent context](conversational-agent-context.md).
