---
type: concept
title: Embedding-Plus-LLM Memory Linking
description: >
  Filter candidate memory connections cheaply with embedding similarity, then
  let an LLM judge which of those candidates are genuinely related — neither
  step alone finds good links at scale.
sources:
  - title: "A-Mem: Agentic Memory for LLM Agents"
    resource: "A-Mem (Xu et al.), §3.2, §4.4-4.6"
---

Connecting a new memory note to relevant existing ones without a predefined
schema (see [Zettelkasten agent memory notes](zettelkasten-agent-memory-notes.md))
needs a way to find candidates that scales past exhaustive comparison, and a
way to judge relatedness that goes beyond surface similarity. Neither an
embedding search alone nor an LLM comparing every pair alone is the right
tool — combine them in two stages:

1. **Cheap filter, embedding similarity.** Compute cosine similarity between
   the new note's embedding and every existing note's embedding; take the
   top-k nearest neighbors as the candidate set. This scales to a large memory
   collection because it never requires an LLM call per existing note.
2. **Nuanced judgment, LLM over the narrowed set.** Prompt an LLM with the new
   note and its nearest-neighbor candidates to decide which candidates are
   actually related and why, based on shared attributes — subtle patterns,
   causal relationships, conceptual connections that embedding similarity
   alone cannot detect (two notes can be semantically close in embedding space
   without being causally or conceptually linked, and vice versa). The LLM's
   output becomes the new note's link set.

The result is a link network that emerges from each memory's actual content
and context rather than a predefined graph schema — the closest fit to
Zettelkasten's flexible-linking principle achievable at LLM scale. Use the
embedding stage purely to bound the LLM's workload to a manageable candidate
set, not as the relatedness judgment itself; treat the LLM stage as the one
that actually decides whether a link exists.

**Retrieval depth (top-k) needs tuning, not maximizing.** Increasing how
many notes the embedding-similarity stage returns generally helps up to a
point, then plateaus and can start reversing — a richer set of candidate
memories also means more noise for the LLM stage to sort through and a
longer context for it to process, the same [lost in the
middle](lost-in-the-middle.md) tension that shows up in document retrieval
generally. Treat top-k as a value to sweep per task category rather than a
knob to turn up by default; the optimal depth differs by how much
cross-memory synthesis a task category actually needs.

**The richer structure doesn't have to cost scalability.** Compared against
simpler memory baselines at matched store sizes from a thousand entries up
to a million, one system reported the same linear, O(N) storage growth as
its simpler competitors — the added link and evolution metadata introduced
no extra storage overhead — and retrieval time grew only modestly (roughly
12x latency for a 1000x increase in store size), staying close to a
baseline with no linking or evolution at all. A design that adds structure
at write time is not automatically trading away retrieval-time or storage
scalability to get it; that tradeoff has to be demonstrated for a given
implementation, not assumed.

**Of the two mechanisms layered on top of a note store — this linking step
and [memory evolution](memory-evolution-on-retrieval.md) — linking is the
more load-bearing one.** An ablation removing both dropped performance
substantially on multi-hop and open-domain questions; removing evolution
alone while keeping linking recovered most of that loss, leaving only a
smaller residual gap to the full system. Read this as a priority order for
implementation effort under constraints, not as evolution being optional:
build reliable linking first — without connections between notes there is no
network for evolution to refine — and treat evolution as the mechanism that
sharpens an already-connected graph rather than the one that makes multi-hop
retrieval possible in the first place.
