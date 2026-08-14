---
type: concept
title: Perplexity-Based Prompt Compression
description: >
  Drop the lowest-perplexity tokens from a prompt using a small reference
  model, trading human readability for compression ratio since only the
  target LLM, not a person, needs to parse the result.
sources:
  - title: "LLMLingua: Compressing Prompts for Large Language Models"
    resource: "LLMLingua (Jiang et al.), Abstract, §1"
---

Natural language is redundant — a token an LLM (or any predictive language
model) assigns high probability to given its preceding context contributes
little additional information toward comprehension, since the reader
(human or model) could largely have predicted it anyway. **Perplexity-based
compression** exploits this directly: score each token or unit's
[perplexity](logprobs-fundamentals.md) under a small reference LM, and drop
the lowest-perplexity ones first, on the premise that a target LLM can
reconstruct the intended meaning from what's left — evidence for this
premise includes LLMs successfully reconstructing source code from
compressed natural-language descriptions.

**The audience for the compressed text is the LLM, not a human.** This is
the load-bearing difference from prompt-shrinking techniques aimed at
[last-minute context trimming](last-minute-context-trimming.md) (eliding or
summarizing while preserving readable, coherent prose per the
[Little Red Riding Hood principle](little-red-riding-hood-principle.md)):
perplexity-based compression accepts visibly garbled, fragmented output — a
human skimming it would struggle to parse it as English — as the cost of a
far higher compression ratio (up to ~20x with reported little task
performance loss), because the only downstream reader that matters is a
capable LLM, which tolerates far noisier input than a human does. Reach for
this technique specifically when the compressed prompt never needs human
review, and reach for readability-preserving trimming when it does.

**Why prompt-side, not model-side, compression.** Standard model-compression
levers — quantization, distillation, pruning — require access to the model's
weights. When the target is only reachable through an API (a black-box
LLM), none of those levers apply, so compression has to happen to the prompt
text itself before it's sent, rather than to the model that reads it.

**Distribution alignment.** A small reference model's own notion of which
tokens are "surprising" doesn't automatically match what the target black-box
LLM would find informative — the two models were trained on different data
and objectives, so perplexity computed under the small model is only a
useful proxy for the target's needs if the two are calibrated to agree.
Instruction-tuning the small compressor model specifically to align its
output distribution with the target LLM's is what makes its perplexity
scores a trustworthy signal for what the *target* can safely lose, rather
than just what the *small model* itself finds redundant.

See [selection-based vs generation-based compression](selection-vs-generation-compression.md)
for why dropping tokens this way beats asking a model to rewrite the prompt
shorter. See [prompt compression budget allocation](prompt-compression-budget-allocation.md)
for how compression ratio is allocated unevenly across prompt roles
(instruction, demonstrations, question) before this token-level pruning is
even applied within each role's surviving text. Scoring every token's
perplexity independently against the original, uncompressed context is
itself a simplification worth questioning — see
[iterative token-level compression](iterative-token-level-compression.md)
for why conditioning on what's already been compressed produces more
accurate keep/drop decisions than independent scoring does.
