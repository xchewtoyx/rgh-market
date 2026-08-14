---
type: concept
title: Generation Over Extractive Retrieval
description: >
  Prefer generative readers when answers need synthesis across clue-bearing
  passages or parametric fallback — extractive spans score zero if the string
  never appears.
sources:
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    resource: "RAG (Lewis et al.), §3–4.4"
---

Classic open-domain QA often extracts answer **spans** from retrieved docs.
[RAG](retrieval-augmented-generation.md)-style generators instead emit free
text conditioned on top-\(k\) passages. Empirically that wins when:

- Documents contain **clues** but not the verbatim answer — marginalization
  still contributes probability mass.
- The answer is in **no** retrieved document — generators can fall back on
  parametric memory (Lewis et al. report non-zero accuracy on such NQ cases;
  extractive systems score 0%).
- Outputs must combine facts from **different** docs (Jeopardy-style QGen) —
  favor [RAG-Token](rag-sequence-vs-token.md) so document posteriors can shift
  mid-sequence; non-parametric hits also **guide** which parametric titles or
  facts get drawn out.

Abstractive and verification tasks follow the same lesson: fewer hallucinations
and higher factuality/specificity than generator-only baselines, and strong
FEVER accuracy **without** supervised evidence labels when the retriever
proposes its own support. Keep extractive readers when answers are guaranteed
spans and latency is tight; otherwise design the harness as generative RAG
under [context grounding](context-grounding.md).
