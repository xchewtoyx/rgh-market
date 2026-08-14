---
type: concept
title: Tokenization Fundamentals
description: >
  LLMs process text as deterministic multicharacter tokens, not letters, which
  makes token count — not character count — the real unit of prompt length.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 2"
---

An LLM does not read text character by character. Input is first broken into
**tokens** — multiletter chunks, typically 3-4 characters, with longer tokens
available for common words or sequences — by a **tokenizer** specific to that
model; the full set of tokens a model can use is its **vocabulary**. The
tokenizer converts text to a token sequence before the model sees it, and
converts the model's output tokens back to text afterward. Tokenizers are
fixed per model: you cannot mix and match a tokenizer with a different model,
and it's worth inspecting a model's actual tokenizer (e.g. via Hugging Face or
`tiktoken`) rather than assuming.

**Deterministic mapping, unlike human reading.** Humans map letters to words
fuzzily — the "inner autocorrect" that lets a typo pass unnoticed because
letters get grouped into whole words early in processing. Tokenizers are
deterministic instead, which makes a typo stand out sharply from the inside:
in a common GPT tokenizer, "ghost" is a single token, but the typo "gohst"
splits into three (`g`-`oh`-`st`) — a completely different token sequence,
not a near-miss of the same one. LLMs are nonetheless fairly typo-resilient in
practice simply because typos are common in training data, so the model has
seen the pattern before even though it can't casually round a typo back to
the intended word the way a human does.

**Why token count matters.** Token count, not character count, is the real
measure of prompt "length," because it drives several practical constraints
at once:

- Reading time scales roughly linearly with prompt token count; generation
  time scales roughly linearly with completion token count — and [reading is
  much faster than generating](autoregressive-generation.md).
- Computational cost scales with length in both directions, which is why
  model-as-a-service providers typically charge per token processed and
  produced.
- Token count determines the **context window** — the total prompt-plus-
  completion length a model can handle in one call, typically measured in
  thousands of tokens. Context windows keep growing, but application authors
  are consistently tempted to fill and overfill them regardless, which is why
  counting still matters in practice — see [prompt element
  importance](prompt-element-importance.md) for prioritizing what actually
  earns a place in a tight budget.

There's no universal character-to-token formula — it depends on both the text
and the tokenizer. Rough figures for a common GPT tokenizer: about 4
characters per token for typical English prose (most tokenizers are optimized
for English and are less efficient on other languages); a little over 2
characters per token for random digit strings; under 2 characters per token
for random alphanumeric strings such as cryptographic keys. Strings with rare
characters are least efficient of all — a single emoji can cost 2 tokens by
itself. Most vocabularies also include an **end-of-text** special token,
appended to every training document so the model learns where a document
ends; when the model emits this token during inference, the completion is cut
off there.

[Token boundary inertness](token-boundary-inertness.md) covers a sharper,
composition-time consequence of this same tokenizer determinism: token counts
computed on prompt pieces in isolation don't sum correctly once those pieces
are concatenated. [Subtoken task avoidance](subtoken-task-avoidance.md) covers
what the model can and can't do given that it only ever sees these
multicharacter chunks, never individual letters.
