---
type: concept
title: Structured Agent Memory
description: >
  Store tables, queues, and other structured state outside raw prompt text so
  the agent can rely on shape the context window alone cannot preserve.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
---

Dumping structured data into the prompt as line-by-line text does not guarantee
the model treats it as a table or queue. A memory system that keeps structured
stores — spreadsheets of leads, queues of pending actions, typed tool results —
preserves structural integrity the flat context window cannot.

This is a long-term tier benefit in [agent memory tiers](agent-memory-tiers.md):
persistence plus shape. Agents then retrieve or query structured state through
tools rather than hoping [context engineering](context-engineering.md) alone
reconstructs schema. Pair with [memory management](memory-management.md) so
overflow leaves the window without losing typed records.
