---
type: concept
title: Main-Context Sections
description: >
  Split prompt tokens into read-only system instructions, a fixed working
  context block, and a FIFO message queue headed by a recursive summary.
sources:
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §2.1"
---

Under [OS-inspired agent memory](os-inspired-agent-memory.md), main-context
(prompt) tokens are laid out as three contiguous sections:

1. **System instructions** — read-only control flow, how each memory level is
   meant to be used, and how to call memory functions (including retrieving
   out-of-context data). This is privileged
   [system prompt architecture](system-prompt-architecture.md), not user-editable
   chat.
2. **Working context** — a fixed-size read/write unstructured text block,
   mutable only via memory function calls. In conversation, hold key user
   facts, preferences, and agent persona so they survive queue churn —
   required for engaging openers and spontaneous long-range personalization
   under [deep memory retrieval](deep-memory-retrieval.md) criteria, not only
   for answering explicit recall questions.
3. **FIFO queue** — rolling agent/user messages, system warnings, and
   function-call I/O. Index zero commonly holds a system message with the
   [recursive summary](memory-summarization.md) of messages already evicted
   under [memory pressure eviction](memory-pressure-eviction.md).

This is a sharper cut of [conversational agent context](conversational-agent-context.md):
preamble, durable working facts, and transcript are separate budgets with
different write paths. Keep working context updates behind tools so the model
cannot silently overwrite persona by emitting free text into the wrong section.
