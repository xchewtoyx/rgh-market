---
type: concept
title: Model Router
description: >
  Classify intent and send each query to the right model, human, FAQ, or tool
  path so simple work stays cheap and out-of-scope work is declined early.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 10"
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
---

A router sends different query types to different solutions: specialized models
for narrow tasks, cheaper models for easy queries, humans or static FAQs when
appropriate. It usually builds on
[intent classification for routing](intent-classification-for-routing.md):
decline out-of-scope politely, ask for clarification on ambiguity, and help
agents choose the next tool or [memory tier](agent-memory-tiers.md).

Routers are often small LMs or dedicated classifiers so several can run per
query cheaply. Common pattern: route → retrieve → generate → score, with
additional routing before retrieval (in scope?) and after (escalate to human?).
If a routed action returns more context than the chosen model's limit, truncate
or re-route to a larger-context model under
[progressive agent architecture](progressive-agent-architecture.md).

Within a single [workflow](workflow-build-process.md), the same idea applies as
**model tiering** at the task level rather than the query level: a lightweight,
cheap, self-hosted model for easy tasks; a large, expensive frontier model for
hard tasks; an in-house fine-tuned specialist for highly customized tasks; and
traditional software or classical classifiers when an LLM is unnecessary at all
([generality–strength tradeoff](generality-strength-tradeoff.md)). Each
[task](task-io-schema-design.md) picks the tier it actually needs rather than
every task defaulting to the strongest available model.
