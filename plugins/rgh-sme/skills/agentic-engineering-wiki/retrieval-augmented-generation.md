---
type: concept
title: Retrieval-Augmented Generation
description: >
  Retrieve the most relevant external knowledge per query and feed it to the
  generator — context construction that treats the retriever as an agent tool.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 5"
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    resource: "RAG (Lewis et al.), Abstract; §1–§2"
---

RAG retrieves relevant information from external stores and joins it with the
user prompt so a generator answers with grounded context. It is feature
engineering for foundation models: give the model the facts it needs for this
input. Benefits include denser answers, fewer hallucinations, and per-user
data scoping. Without retrieval, models may refuse unknown facts or — worse —
hallucinate convincing ungrounded answers. Retrieving *irrelevant* snippets is
not neutral either — see the
[Chekhov's gun retrieval fallacy](chekhovs-gun-retrieval-fallacy.md) for why
padding context with loosely-related hits actively hurts answers rather than
just wasting space.

Lewis et al. frame RAG as a **hybrid memory** recipe: **parametric** memory
(pretrained generator weights) plus **non-parametric** memory (a dense index
queried by a retriever). The non-parametric side is why knowledge can be
inspected for provenance, expanded without retraining, and **replaced** when
the world changes — problems parametric-only models handle poorly. Both
components arrive pretrained (for example BART + DPR over Wikipedia), so
knowledge access is present without training memory networks from scratch for
each task. **Index hot-swapping** is the operational form of that claim:
rebuild or swap the Wikipedia dump (for example 2016 vs 2018) and leader-
identity questions flip to the matched year's answers (~70% correct) while
mismatched indices collapse (~4–12%) — world knowledge updated with **no**
generator retraining.

Long context does not obsolete RAG: data volume grows faster than windows, and
models often use long prompts poorly ([lost in the middle](lost-in-the-middle.md))
while every token costs latency. Small knowledge bases may still fit whole in
prompt; larger ones need retrieval. Prefer precise hits over volume, per the
Chekhov's gun retrieval fallacy above. Pair retrieved material with
[context grounding](context-grounding.md) so the generator actually uses the
passages rather than drifting back to parametric guesses.

Retrieval query construction spans using the raw user text (risky for long
noisy requests), asking the model for a search string
([query rewriting](query-rewriting.md)), or giving the agent a search tool so
it decides when to retrieve — the overlap of RAG and
[function calling](function-calling.md). Architecturally RAG is a special case
of an [LLM agent](llm-agent.md) where the retriever is a tool, and the
agentic pattern generalizes further with richer
[tool inventories](tool-inventory.md); see
[agent memory tiers](agent-memory-tiers.md) for how retrieved material enters
short-term context. Classic latent-document formulations choose between
[RAG-Sequence and RAG-Token](rag-sequence-vs-token.md) marginalization inside a
[retriever–generator architecture](retriever-generator-architecture.md);
prompted systems usually approximate that by concatenating top chunks instead.
Prefer [generation over extractive retrieval](generation-over-extractive-retrieval.md)
when answers need synthesis, clue-bearing passages, or parametric fallback.
