---
type: concept
title: Task-Specific Summarization
description: >
  Summarize source text for a fixed downstream question so retained details
  match the later prompt — trading reusability for relevance.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 5"
---

General summaries keep what seems “central” and drop asides — often exactly
the asides a later app needs (a vacation post’s book mention for a
recommendation agent). **Task-specific summarization** states the downstream
use in the summarizer prompt (few-shot notes of what to jot vs `N/A`) so
lossy compression keeps app-relevant signal.

Tradeoff: powerful when the [feedforward](llm-application-feedforward-pass.md) question is
stable across instances; if the question changes, re-summarize from scratch.
General summaries are reusable across apps and models. Prefer task-specific
inside [dynamic context gathering](dynamic-context-gathering.md) when you know
the ask; use [hierarchical summarization](hierarchical-summarization.md) first
when the raw corpus will not fit even one summarizer call.
