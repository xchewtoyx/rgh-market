---
type: concept
title: RAG-Sequence vs RAG-Token
description: >
  Marginalize retrieved documents once per answer sequence, or per generated
  token, trading single-doc coherence against multi-doc mixing.
sources:
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    resource: "RAG (Lewis et al.), §2"
---

Classic RAG treats the retrieved passage \(z\) as a latent variable and
approximates the marginal over the retriever's top-\(k\) hits in two ways
(Lewis et al.):

- **RAG-Sequence** — one document conditions the **entire** output sequence;
  \(p(y|x) \approx \sum_z p_\eta(z|x)\, p_\theta(y|x,z)\). Coherent when the
  answer should come from a single source.
- **RAG-Token** — a (possibly different) document may influence **each**
  token; \(p(y|x) \approx \prod_i \sum_z p_\eta(z|x)\, p_\theta(y_i|x,z,y_{<i})\).
  Lets the generator mix facts across passages — empirically stronger on
  Jeopardy-style question generation that combines two facts from different
  docs, where document posteriors peak on different passages mid-sequence.
  For length-one classification targets the two coincide.

Decoding differs: token marginals plug into ordinary beam search; sequence
marginals need per-document beams then combine (thorough) or approximate by
ignoring hypotheses never proposed for a document (fast). In a modern
[retriever–generator architecture](retriever-generator-architecture.md) you
usually concatenate top chunks into one prompt rather than explicit latent
marginalization — still choose whether the harness expects
single-source answers or multi-source synthesis, and place those chunks with
[lost in the middle](lost-in-the-middle.md) in mind under
[retrieval-augmented generation](retrieval-augmented-generation.md).
