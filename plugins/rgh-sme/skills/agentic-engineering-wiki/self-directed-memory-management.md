---
type: concept
title: Self-Directed Memory Management
description: >
  Let the agent call memory tools itself — guided by hierarchy docs and
  pressure signals — rather than only a fixed external eviction policy.
sources:
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §2"
---

Self-directed memory management makes overflow handling part of the agent's
[function calling](function-calling.md) loop: the model decides when to move
items between [agent memory tiers](agent-memory-tiers.md), edit working state,
or search durable stores. The harness still owns parsing, validation, and
execution; the *policy* of what to keep in-window is model-generated from
current context.

Two prompt ingredients make this workable: a detailed description of the memory
hierarchy and each store's utility, and a function schema (with natural-language
docs) for access and mutation. Feed execution results — including capacity
errors — back into the next turn so the agent can adjust. [Memory pressure
eviction](memory-pressure-eviction.md) warnings teach awareness of context
limits; without them, autonomous edits often arrive too late.

Use when conversation or task state outlives a single window and a fixed
[FIFO](fifo-context-eviction.md) or summary policy would drop the wrong facts.
Pair with [function-call chaining](function-call-chaining.md) for multi-step
retrieval, and keep retrieval results page-sized so tools cannot blow the
budget the agent is trying to manage. Document QA is the stress case:
paginated archival search lets the agent iterate when top-\(K\) misses gold —
but only if the model actually continues paging instead of answering early
([OS-inspired agent memory](os-inspired-agent-memory.md)). Encode that
obligation as an
[exhaustive archival search instruction](exhaustive-archival-search-instruction.md)
in the persona/system layer, not only in tool docs.
