---
type: concept
title: Iterative Token-Level Compression
description: >
  Estimate each segment's token perplexity conditioned on the already-
  compressed version of prior segments, not the full original text, so
  earlier compression decisions correctly influence later ones.
sources:
  - title: "LLMLingua: Compressing Prompts for Large Language Models"
    resource: "LLMLingua (Jiang et al.), §4.2"
---

Naive [perplexity-based token pruning](perplexity-based-prompt-compression.md)
scores every token or unit's informativeness independently — each token's
perplexity is computed against the full *original* context, as if every
other token's keep/drop decision were unrelated to this one. That's an
inaccurate independence assumption: whether a token is safe to drop actually
depends on what else around it survives compression, not on the uncompressed
original. Estimating probabilities without conditioning on what's
simultaneously being kept or dropped systematically mis-scores tokens, the
same class of error masked-language-model-style scoring is known for
(estimating a token from full bidirectional context rather than from what an
autoregressive read would actually see).

**Iterative token-level compression fixes this by making later decisions
depend on earlier ones.** Split the prompt into segments and process them in
order; when scoring a segment's tokens, condition the perplexity estimate on
the *already-compressed* version of every prior segment, not on those
segments' original uncompressed text. Each segment's decisions are made in
light of what will actually be present in the final compressed prompt up to
that point, not what used to be there before compression started — this is
what makes the algorithm genuinely iterative rather than one independent
scoring pass per unit.

Within each segment, compression rate is converted into a per-segment
perplexity threshold, and any token whose perplexity clears that threshold
is kept (higher perplexity meaning less predictable, hence more informative)
while everything below it is dropped. The per-segment target rate comes from
whichever role that segment belongs to under
[prompt compression budget allocation](prompt-compression-budget-allocation.md)
— instruction, demonstration, or question — so the coarse role-level budget
from that stage and this segment-level conditioning compose: role decides
*how much* budget a segment gets, iterative conditioning decides *which*
tokens within it actually survive, correctly accounting for what neighboring
segments already lost.
