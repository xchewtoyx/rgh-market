---
type: concept
title: Function-Call Chaining
description: >
  Let the model request immediate follow-up inference after a tool result so
  multi-step retrieval or edits can run without waiting for a new user turn.
sources:
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §2.3"
---

Function-call chaining extends the usual [function calling](function-calling.md)
loop: after the harness executes a validated call and feeds the result back,
the model may signal that another inference cycle should run immediately —
MemGPT's `request_heartbeat=true` argument is one concrete keyword for that
intent. Without chaining, multi-step memory search or staged edits stall until
the next user message; with it, the agent can page through recall, refine
queries, and assemble an answer in one user-visible turn.

Harness requirements: parse the chain signal separately from user-facing prose,
bound the number of heartbeats to limit
[compound mistake amplification](compound-mistake-amplification.md) and cost,
and keep each tool result within the context budget (paginate large retrievals).
Chaining is especially valuable with
[self-directed memory management](self-directed-memory-management.md), where
answering often needs several store reads and writes before a final reply.
