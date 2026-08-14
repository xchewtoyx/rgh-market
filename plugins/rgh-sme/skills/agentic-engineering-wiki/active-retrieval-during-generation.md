---
type: concept
title: Active Retrieval During Generation
description: >
  Let the model decide when and what to retrieve mid-generation — paging
  external memory as a tool call rather than a single upfront top-K dump.
sources:
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §4"
---

Classic [RAG](retrieval-augmented-generation.md) often retrieves once before
generation. **Active retrieval** (FLARE-style and interleaved CoT+retrieve)
lets the LM choose *when* and *what* to fetch while producing the answer —
overlapping [OS-inspired agent memory](os-inspired-agent-memory.md) paging and
[ReAct](react-loop.md) tool use. Long-context window scaling enlarges **main
memory** capacity; hierarchical external stores still matter for durable user
history and corpora that outlive any window.

Design the harness so retrieval is a first-class function with
[function-call chaining](function-call-chaining.md) for multi-hop needs, not
only a preprocessor. MemGPT’s emphasis is long-term memory of **user inputs**
via tiers, not only interactive-environment agent benchmarks — keep that
product focus when choosing between paging tools and pure context expansion.
