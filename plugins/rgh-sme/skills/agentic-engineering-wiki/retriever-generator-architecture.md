---
type: concept
title: Retriever Generator Architecture
description: >
  Split a dense (or hybrid) retriever from a seq2seq generator, with optional
  query-encoder finetuning while keeping the document index fixed.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    resource: "RAG (Lewis et al.), §2; §4.5–§6"
---

A [RAG](retrieval-augmented-generation.md) system has a **retriever**
\(p_\eta(z|x)\) (index + query against non-parametric memory) and a
**generator** \(p_\theta(y|x,z,\ldots)\) (parametric memory). Classic Lewis et
al. RAG uses a DPR bi-encoder — \(p_\eta(z|x) \propto \exp(d(z)^\top q(x))\)
with BERT document and query encoders — and a BART seq2seq generator that
concatenates \(x\) with retrieved \(z\). Top-\(k\) retrieval is approximate
MIPS.

Production systems usually compose off-the-shelf pieces; early work jointly
trained without document-level supervision by maximizing marginal likelihood
of \(y\). Updating the document encoder forces periodic index rebuilds, so a
common compromise **freezes** \(\text{BERT}_d\) and the index while finetuning
only the query encoder and generator. How you marginalize latents —
[RAG-Sequence vs RAG-Token](rag-sequence-vs-token.md) — changes decoding.
Ablations: **learned** query-encoder retrieval beats a frozen retriever on
most tasks; dense DPR beats BM25 except on entity-overlap-heavy FEVER; test-
time \(k\) is flexible after training (Sequence often likes more docs on NQ;
Token may peak earlier). Raw-text memory stays human-readable and writable —
the interpretability/editability win over embedding-only stores.

Indexing depends on the retrieval algorithm: term indexes versus embedding
indexes in a vector store. Long documents are [chunked](chunking-strategy.md)
before indexing. At query time, fetch top chunks, join with the user prompt
(light post-processing), and generate. Treat "document" as either whole source
or chunk per IR convention. Null-document tricks are often unnecessary —
models can learn to retrieve a harmless set when retrieval would not help.

For agents, the retriever is one tool among many; tabular flows add text-to-SQL
and execution tools under [tabular retrieval tools](tabular-retrieval-tools.md).
Hot-swap the index under
[retrieval-augmented generation](retrieval-augmented-generation.md) when facts
change rather than waiting on weight updates.
