---
type: concept
title: Query Rewriting
description: >
  Reformulate the user's latest utterance into a standalone retrieval query so
  ambiguous follow-ups resolve against the knowledge store correctly.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 5"
---

Conversational queries are often underspecified ("How about Emily Doe?" after a
question about John Doe). [RAG](retrieval-augmented-generation.md) retrieval
needs a rewritten standalone query that incorporates dialogue state.

AI systems typically prompt a rewriter with recent turns: produce what the user
is actually asking. Rewriting may need identity resolution or external lookup
("his wife"); if that fact is unavailable, the rewriter should mark the query
unsolvable rather than invent a name. Treat the search string itself like a
mini-prompt — clarifying intent and background ("book to read next", "young
backpacker") steers which snippets rank high. Rewritten queries feed the
retriever before [hybrid retrieval](hybrid-retrieval.md) or embedding search,
and sit in short-term [agent memory](agent-memory-tiers.md) with the
conversation.
