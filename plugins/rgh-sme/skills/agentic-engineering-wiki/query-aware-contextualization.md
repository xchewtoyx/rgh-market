---
type: concept
title: Query-Aware Contextualization
description: >
  Place the question or lookup key both before and after long retrieved
  material so mid-context items can attend to the query while encoding.
sources:
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    resource: "Lost in the Middle (Liu et al.), pp. 1–18 (§4)"
---

Default long-context prompts often put the query **after** a stack of
documents or key–value pairs. Decoder-only models then cannot condition
earlier tokens on the query while encoding them. **Query-aware
contextualization** sandwiches the data between a leading and trailing
copy of the question/key so each item can be read with the retrieval goal
in mind.

On synthetic UUID [key–value](lost-in-the-middle.md) retrieval this is
dramatic: models that failed mid-list (for example GPT-3.5-Turbo-16K worst
case ~45.6% at 300 pairs) become near-perfect across lengths. On
multi-document QA the same trick barely changes the U-curve — exact-match
lookup is fixed far more than reasoning over natural-language passages.

Use as a cheap [context engineering](context-engineering.md) lever before
assuming you need a larger window or an encoder–decoder. Encoder–decoder
models can be more position-robust *inside* their training lengths
(bidirectional future context for relative importance) but still develop
U-curves once prompts exceed that length. Instruction/chat fine-tuning
raises absolute accuracy and can shrink best–worst gaps slightly without
removing the U-shape; small base models may show **only** recency until
scale brings primacy back. Pair with
[sandwich technique](sandwich-technique.md) for instruction refocus and
with ranked truncation when open-domain readers already saturate.
