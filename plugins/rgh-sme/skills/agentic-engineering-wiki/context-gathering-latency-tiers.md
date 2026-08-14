---
type: concept
title: Context Gathering Latency Tiers
description: >
  How urgently a request needs a response bounds how context can be gathered
  for it — and drives how much of that context should be prepared in advance.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 5"
---

Unlike [static content](static-vs-dynamic-prompt-content.md), which can be authored
once in advance, dynamic context has to be gathered while the application is
running — so how urgently a response is needed bounds what gathering strategy
is even feasible. Urgency is generally driven by what triggers the
[feedforward pass](llm-application-feedforward-pass.md):

- **Low urgency** — a non-user trigger while the user is inactive, or a
  fire-and-forget action (e.g. an email-summarization assistant). No one is
  watching, so context gathering can afford to be slow.
- **Medium urgency** — an on-demand action (e.g. a book-recommendation
  assistant). Users tolerate some wait but not too much, so a multi-LLM-pass
  gathering pipeline is likely infeasible.
- **High urgency** — an automatic response to the user's current, ongoing
  action (e.g. a completion assistant while typing). Every millisecond of
  context lookup risks the user invalidating the request by acting again
  before it returns, so complex retrieval strategies that can't be
  precomputed are likely off the table entirely.

**Preparability** is the direct response to this constraint: ask, for each
piece of context, whether it can be prepared in advance rather than fetched at
request time. Some context changes rarely or never for a given user and can
be precomputed once; if latency matters, prepare whatever can be prepared
ahead of the request. For the most latency-critical applications, it can even
be worth *speculatively* preparing context that might turn out to be needed,
since there won't be time to retrieve it once the request actually arrives.
