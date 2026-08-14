---
type: concept
title: Contextual Chunk Augmentation
description: >
  Prepend metadata or model-generated situating text to each chunk before
  indexing so retrieval works when the chunk alone lacks standalone meaning.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
---

Chunks often lack standalone context after [chunking](chunking-strategy.md).
Augment before indexing:

- Metadata — tags, keywords, titles, captions, extracted entities (preserves
  exact-match terms embeddings may blur).
- Questions the chunk can answer — organizing as Q&A improves match to user
  phrasing.
- Model-generated situating context — given the whole document and chunk, ask
  for a short (50–100 token) explanation of how the chunk fits the document,
  prepend it, then index (Anthropic-style contextual retrieval).

Augmentation raises index cost and tokens per hit but improves retrievability for
[RAG](retrieval-augmented-generation.md) agents that otherwise fetch orphaned
fragments under [lost in the middle](lost-in-the-middle.md) pressure.
