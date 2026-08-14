---
type: concept
title: Selection-Based vs Generation-Based Prompt Compression
description: >
  Prefer dropping low-value tokens over asking a model to rewrite a prompt
  shorter — generation-based compression can't hit a target ratio reliably,
  costs more, and tends to lose the reasoning path.
sources:
  - title: "LLMLingua: Compressing Prompts for Large Language Models"
    resource: "LLMLingua (Jiang et al.), §5.5"
---

A prompt can be shortened two structurally different ways: **selection**
(score existing tokens or segments and drop the low-value ones, as in
[perplexity-based prompt compression](perplexity-based-prompt-compression.md))
or **generation** (ask a model to rewrite/paraphrase/summarize the prompt
into a shorter version). Generation looks more natural — it's just
summarization — but has three concrete disadvantages against selection for
this specific job:

- **Uncontrollable output.** A generated rewrite's length and content are
  unpredictable: hitting an exact target compression ratio needs repeated
  regeneration attempts, and uncontrolled content risks low overlap with the
  original — especially costly for prompts that encode a multi-step
  reasoning path (worked examples, chain-of-thought demonstrations), where a
  paraphrase can silently drop or garble the reasoning steps a selection
  method would have kept as literal surviving tokens.
- **Higher computational cost.** A small model can't reliably perform
  complex rewriting, and using a large, capable model to do the compression
  itself adds substantial overhead — defeating much of the point of
  compressing in the first place. (This mirrors why perplexity scoring
  itself uses a small reference model rather than the target LLM: the
  compression step should stay cheap relative to what it saves.)
- **Lower achievable compression ratio.** Generated text has to remain a
  complete, grammatical, continuous passage, which structurally caps how much
  it can shrink. Selection-based dropping isn't bound by grammaticality —
  see [perplexity-based compression](perplexity-based-prompt-compression.md)
  on trading human readability away entirely when the compressed prompt's
  only reader is the target LLM — which is what lets it reach far higher
  ratios (up to ~20x) than a fluent rewrite ever could.

The general principle: when the compressed prompt only has to remain
*machine-legible*, not human-readable, selection-based methods dominate
generation-based ones on every axis that matters for compression — ratio
control, cost, and reasoning-path fidelity — because they don't pay the
overhead of reconstructing fluent prose as a byproduct of shrinking.
