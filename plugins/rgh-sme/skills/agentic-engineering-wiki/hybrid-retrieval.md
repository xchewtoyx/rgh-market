---
type: concept
title: Hybrid Retrieval
description: >
  Combine term-based and embedding-based retrieval — sequentially via reranking
  or in parallel via rank fusion — to catch both keywords and semantics.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 5"
---

Term-based retrieval ([TF-IDF, BM25](lexical-similarity-scoring.md),
Jaccard-style overlap, inverted indexes) is fast, cheap, and strong on exact
keywords (error codes, product names) but blind to semantics — and may need
stop-wording/stemming. Simple overlap scores treat common and rare word
matches equally; BM25/TF-IDF weight rarer terms higher when corpus statistics
exist. Embedding-based retrieval ranks by meaning in vector space but is
costlier, can obscure exact strings, and is harder to debug when an expected
hit is missing. Hybrid search combines both for
[RAG](retrieval-augmented-generation.md).

The two have different debuggability, too: when an embedding-based miss
happens, the query and document vectors are opaque, so there's little you can
do to directly diagnose or fix why an expected match didn't show up. A
term-based miss is explainable (query tokens didn't match document tokens) and
fixable (adjust stemming, add synonyms) — lexical stacks also benefit from
mature, well-understood tooling (Elasticsearch, Algolia). Term-based
retrieval also lets you tune relevance to match user expectations directly —
e.g. boosting title matches over description matches — where the nearest
embedding-based equivalent is retraining the embedding model with that notion
of relevance baked in and reindexing the whole corpus, a much heavier lift.
Embedding retrieval's own core advantage is matching on ideas rather than
words, so documents using completely different vocabulary for the same
concept, or even different languages or modalities mapped into a shared
embedding space, can still match.

Two patterns:

- **Sequential reranking** — cheap retriever fetches candidates; a more precise
  (often embedding) stage reranks within the context budget.
- **Parallel ensemble** — run retrievers together and fuse rankings (for
  example reciprocal rank fusion scoring 1/(k + rank) per list).

Choose hybrid when agents must find both semantic matches and brittle tokens.
Evaluate retrieval quality *and* end-to-end answer quality; better nearest
neighbors are worthless if the generator still fails or falls for the
[Chekhov's gun retrieval fallacy](chekhovs-gun-retrieval-fallacy.md).
