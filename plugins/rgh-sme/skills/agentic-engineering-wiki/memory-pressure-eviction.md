---
type: concept
title: Memory Pressure Eviction
description: >
  Warn the model before the window fills, then flush oldest in-context messages
  into durable recall while rebuilding a recursive summary.
sources:
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §2.2"
---

Memory pressure eviction softens blind [FIFO context eviction](fifo-context-eviction.md)
with two thresholds. At a **warning** token count (for example 70% of the
window), the harness inserts a system message that impending queue eviction is
near — a memory-pressure signal — so the model can use
[self-directed memory management](self-directed-memory-management.md) tools to
copy important FIFO contents into working context or archival storage *before*
loss. At a **flush** token count (full window), the queue manager evicts a
configured slice (for example half the window) and rebuilds a
[recursive summary](memory-summarization.md) from the prior summary plus the
evicted messages.

Evicted messages leave the in-context FIFO immediately but remain readable from
recall storage via memory tools. Retrieved recall messages re-enter at the
**back** of the FIFO so they become visible again without rewriting history
order semantics. This pairs management (what leaves the window) with retrieval
(what returns) under [memory management](memory-management.md): durable loss is
optional; in-context visibility is not.
