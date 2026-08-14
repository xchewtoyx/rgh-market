---
type: concept
title: Chunking Strategy
description: >
  Split sources into indexable units with size, overlap, and split rules that
  trade retrieval diversity against boundary integrity and index cost.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 5"
---

Documents are split into chunks before indexing in a
[retriever-generator architecture](retriever-generator-architecture.md). Options
include fixed character/word/sentence/paragraph sizes, recursive splits
(section → paragraph → sentence until under limit), and domain splitters (code,
Q&A, language-specific).

**Sizing criteria:** stay under the embedding model's max window; hold about one
main idea (multi-topic chunks yield ambiguous vectors); and produce a unit that
fits usefully into a later prompt. **Moving windows** (size + stride) overlap so
ideas are not cut at boundaries — more overlap means more vectors and storage.
**Natural boundaries** (paragraphs/sections) keep topics whole. Use
[contextual chunk augmentation](contextual-chunk-augmentation.md) when the chunk
alone lacks situating context for a good embedding.

**Overlap** keeps boundary phrases from being cut mid-meaning. Chunk size must
respect generator and embedding context limits; tokenizing with the generator's
tokenizer eases compatibility but forces reindex on tokenizer change.

Smaller chunks pack more diverse hits into context but risk splitting topics and
double embedding/storage/search cost. There is no universal best size — tune for
the task under [context engineering](context-engineering.md) budgets.
