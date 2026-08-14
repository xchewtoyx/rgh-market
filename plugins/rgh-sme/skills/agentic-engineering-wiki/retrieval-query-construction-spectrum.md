---
type: concept
title: Retrieval Query Construction Spectrum
description: >
  Build a retrieval query directly from the user's text, via an LLM-generated
  rewrite, or by letting the model decide when and what to search at all.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 4"
---

Constructing the search query for
[retrieval-augmented generation](retrieval-augmented-generation.md) spans a
spectrum of sophistication:

- **Simplest** — use the user's request directly as the search query. Risky
  when the request is a long, run-on message with extraneous content, since
  the noise can cause spurious matches.
- **LLM-assisted query** — ask the model what a good search query would be
  given the request, and search the index with its response text instead of
  the raw request. This is a lighter-weight relative of
  [query rewriting](query-rewriting.md), which specifically resolves
  conversational underspecification rather than just cleaning up a query.
- **Tool-based** — in long conversations, it isn't always obvious that search
  is even warranted for a given turn (searching on every comment is wasteful
  if the user is still discussing the prior topic). Give the model a search
  tool via [function calling](function-calling.md) and let it decide when to
  search and what to search for, rather than deciding on its behalf. This is
  the point where retrieval and general
  [agent tool categories](agent-tool-categories.md) overlap: a retriever
  exposed as a tool is architecturally no different from any other
  knowledge-augmentation tool in the inventory.

Higher sophistication costs an extra model call (or an extra decision baked
into an existing one) in exchange for a better-targeted query — the same
cost/precision tradeoff that runs through retrieval design generally.

A scripted middle ground between the LLM-assisted and tool-based ends: fix the
number of query-generation rounds in advance rather than letting the model
decide when to stop, generating each round's query from the context
accumulated so far. See
[iterative multi-hop retrieval](iterative-multi-hop-retrieval.md).
