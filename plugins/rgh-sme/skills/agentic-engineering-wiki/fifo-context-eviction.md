---
type: concept
title: FIFO Context Eviction
description: >
  Drop the oldest short-term messages first when the window fills — simple, but
  often deletes the purpose-setting turns that matter most.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §2.2"
---

FIFO (first in, first out) evicts the earliest short-term memory to external
storage when context is full. Many APIs and frameworks implement "retain last N
messages/tokens" this way. It assumes early messages matter less.

That assumption can be fatally wrong: opening turns often state the
conversation's purpose and carry the densest instructions. Blind FIFO is easy
to ship and easy to break agent coherence. Prefer pairing or replacing it with
[memory summarization](memory-summarization.md) that preserves goals, entities,
and constraints under [memory management](memory-management.md). A stronger
variant is [memory pressure eviction](memory-pressure-eviction.md): warn the
model before flush so [self-directed memory management](self-directed-memory-management.md)
can rescue important queue contents, then summarize what leaves.
