---
type: concept
title: Lost in the Middle
description: >
  Long-context performance follows a U-curve: primacy and recency beat the
  middle, and longer windows do not by themselves fix position sensitivity.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    resource: "Lost in the Middle (Liu et al.), pp. 1–18 (§2)"
---

Not all prompt positions are equal. Controlled multi-document QA (Natural
Questions with one gold Wikipedia paragraph among \(k-1\) Contriever
distractors) and key-value retrieval show a **U-shaped** curve: models use
relevant information best at the beginning (**primacy**) or end (**recency**)
and degrade when the answer sits in the middle — even for models advertised
with very long windows (Liu et al., 2023). In 20–30 document settings,
mid-context answers for GPT-3.5-class models can fall **below closed-book**
accuracy — adding retrieved distractors can *hurt* if the gold passage is
buried. Extended-context variants often match their short-window siblings
when both fit the same input: a larger maximum length is not evidence of
robust mid-context use. The U-curve survives unambiguous subsets, random
distractors, randomly ordered distractors, and GPT-4 samples. Needle-in-a-
haystack tests reproduce the same finding, and related benchmarks such as
RULER make the same point more broadly: advertised context length is not
uniform usefulness.

**Evaluation bar for long-context claims:** performance should change little
when you move the single relevant item across positions (small best–worst
gap). If quality falls as you add distractors, you are trading more
information against harder reasoning — open-domain QA readers often saturate
long before retriever recall improves (~1–1.5% reader gain past ~20 Contriever
hits while length/latency climb). Prefer **reranking** that pushes likely
answer docs toward the start and **ranked-list truncation** over stuffing
ever-larger \(k\). The U-curve parallels psychology's serial-position effect
even though self-attention can in principle attend anywhere — treat equal
access as a myth for harness design. If quality falls as context grows,
shorten before blaming the model, and do not assume a multi-million-token
window makes placement irrelevant.

For [context engineering](context-engineering.md), put critical instructions
and key facts at the edges, shorten bloated middles, and treat mid-prompt
dumps of [retrieved material](retrieval-augmented-generation.md) as
high-risk. Stacked with a separate recency effect — the closer a piece of
information sits to the *end* of the prompt, the more impact it has on the
completion — the weak band is the [Valley of Meh](valley-of-meh.md): its
depth and exact location vary by model, but some such valley exists in every
model, it is worst in large prompts, and it has no complete fix. Mitigate it
by placing key, high-quality elements outside the valley, by filtering
context to keep the overall prompt as concise as possible, and by countering
deliberately with the [sandwich technique](sandwich-technique.md), which
restates the task at the very end of the prompt where it lands with the most
impact. For lookup keys or questions, use
[query-aware contextualization](query-aware-contextualization.md) (query
before *and* after the data). For agent trajectories, prefer
[collapsed observations](collapsed-observations.md) and edge placement of
task-critical state over stuffing full history into the middle of every turn.

**Minimal retrieval testbed:** synthetic UUID key–value lists (75–300 pairs)
strip linguistic confounders and still show the U-curve for several models —
Claude families can be near-perfect while GPT-3.5 / MPT still fail mid-list.
Middle weakness is therefore not only multi-hop QA difficulty; treat exact
in-prompt lookup as part of long-context eval, not a solved primitive.
