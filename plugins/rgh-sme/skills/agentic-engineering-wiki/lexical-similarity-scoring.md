---
type: concept
title: Lexical Similarity Scoring
description: >
  Score retrieval candidates by literal word overlap with the query, after
  stripping stop words and stemming, as a fast proxy for relevance.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 5"
---

Term-based retrieval's simplest scoring method: preprocess both the query and
each candidate snippet by removing **stop words** (common, low-meaning words)
and applying **stemming** (walking/walks/walked all reduce to walk), then
compute **Jaccard similarity** — the count of overlapping words divided by the
total count of unique words across snippet and query — giving a score from 0
(no overlap) to 1 (full match).

Jaccard's advantages: trivial to implement, needs no preprocessing or
preindexing of the corpus, has a negligible memory footprint, and is fast when
the search space is small (e.g. searching files currently open in an editor —
why GitHub Copilot uses this style of retrieval). Its weakness is that it
treats a match on a common word (e.g. "go") the same as a match on a specific,
informative word (e.g. "backpacking"), when the latter should count for more.
More sophisticated term-based scoring — TF-IDF or BM25, the same techniques
[hybrid retrieval](hybrid-retrieval.md) pairs against embedding search — weight
matches on rarer words higher, at the cost of needing vocabulary-wide word
occurrence counts precalculated in advance, which isn't always feasible for a
small or rapidly changing corpus.

Treat the search string itself like a mini-prompt: it benefits from the same
clarification and context that improve a normal prompt. Adding "I'm
considering what book to read next" to a query prioritizes story-preference
content in the results; adding background like "the book is about a young
backpacker" prioritizes backpacking-related content. This differs from
[query rewriting](query-rewriting.md), which resolves what a conversational
follow-up is actually asking — this tip is about enriching an already-clear
query so lexical scoring has more to match against.
