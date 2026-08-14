---
type: concept
title: Iterative Multi-Hop Retrieval
description: >
  Generate a search query from accumulated context at each of a fixed number
  of hops, retrieving more passages each time, before answering — a scripted
  alternative to letting an agent decide when to stop searching.
sources:
  - title: "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines"
    resource: "DSPy (Khattab et al.), §7"
---

Single-hop [RAG](retrieval-augmented-generation.md) — retrieve once from the
original question, then answer — bottlenecks on questions whose answer
depends on evidence that doesn't share vocabulary with the question itself
(e.g. "what is the population of the city where X was born?" needs a first
hop to resolve X's birth city before a second hop can find its population).
A single query built from the question alone can't surface that second-hop
evidence, capping recall regardless of how good the retriever is.

**Iterative multi-hop retrieval** fixes this by looping a fixed number of
times: at each hop, generate a search query from the question *and* the
context accumulated so far (typically via
[chain-of-thought prompting](chain-of-thought-prompting.md), e.g. `context,
question -> search_query`), retrieve more passages with that query, and
append them to the accumulated context; after the last hop, a final step
answers from everything accumulated (`context, question -> answer`). Each
hop's query is grounded in what the *previous* hop turned up, so later hops
can chase down entities or facts the original question never mentioned.

This is a **pipeline**, not an agentic loop: hop count is fixed at design
time rather than decided by the model at runtime, which is exactly the
[workflow topology](workflow-topology.md) tradeoff between a scripted
DAG/pipeline and a [ReAct](react-loop.md)-style loop that decides for itself
when it has enough evidence (see the tool-based end of the
[retrieval query construction spectrum](retrieval-query-construction-spectrum.md)).
Prefer a fixed-hop pipeline when the reasoning depth needed is roughly known
in advance (e.g. bounded-hop QA benchmarks) — it's cheaper to compile,
evaluate, and reason about than an open-ended loop, at the cost of not
adapting hop count to question difficulty.
