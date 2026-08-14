---
type: concept
title: Topic-Shift Context Truncation
description: >
  Drop prior conversation once the topic has moved on, using an inactivity
  threshold or a relevance-judging model to detect the shift.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 8"
---

Prior conversation in [conversational agent context](conversational-agent-context.md)
should not grow unbounded — drop content once the topic has shifted rather than
carrying every past exchange forward. Two ways to detect the shift:

- **Inactivity threshold** — simplest approach: drop all content from prior
  user sessions after some period of inactivity.
- **Model-judged relevance** — use a model to judge whether older turns are
  still relevant to the current request. Likely overkill on cost and latency
  if done with a large model, but feasible with a smaller model trained for
  the purpose.

This is a short-term eviction strategy alongside the others listed under
[memory management](memory-management.md) — it targets conversational
relevance specifically, rather than a fixed window size or a summarize/merge
policy.
