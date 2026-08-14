---
type: concept
title: Completion Preamble Types
description: >
  A completion's leading text is boilerplate, reasoning, or fluff — only one
  of which is worth paying tokens for, and each needs a different fix.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 7"
---

The **preamble** is the part of a generated completion that precedes the main
content — whatever the model emits before the main answer. Whether it's
wasteful depends on which of three types it is:

- **Structural boilerplate** — text between the end of the prompt and the
  start of the actual content. With a completion model this can often be
  eliminated entirely by moving the deterministic boilerplate into the prompt
  instead (an application of [prompt transition](prompt-transition.md),
  sometimes called inception), which is more efficient — it keeps the model
  adhering to the desired format and is faster and cheaper — and doubles as a
  clean prompt-to-completion transition point.
- **Reasoning** — many chat models mirror an interpreted version of the
  question before answering, which helps inference by focusing the model on
  key aspects of the prompt. [Chain-of-thought](chain-of-thought-prompting.md)
  preambles are a virtue here, not a vice, even when much longer than the
  final answer: a long reasoning preamble can produce a correct answer where
  a short one produces an incorrect one. Plan for it in token budgets rather
  than treating length as waste.
- **Fluff** — RLHF-trained models tend toward verbose, polite responses that
  hurt programmatic use, and even non-RLHF models occasionally produce it.
  Mitigations: [few-shot examples](few-shot-example-formatting.md) paired
  with explicit instructions, or reformatting the prompt to separate the main
  answer from commentary (asking for the main answer first, extra
  commentary after, aids downstream parsing) — though enforcing this can cost
  extra tokens or an extra pass, and is better isolated with
  [completion boundary markers](completion-boundary-markers.md) plus
  [stop sequences](stop-sequences.md). [Structured document formats](structured-document-format.md)
  tend to keep the model honest; free-form contexts are where fluff creeps in
  most. Which fluff to worry about (comments, disclaimers, background,
  explanation) depends on the specific model and question type, and even
  explicit instructions to push fluff after the answer can still leak a short
  introduction before, say, the first item of a numbered list.

Distinguishing these matters because the fix differs by type: eliminate
boilerplate, embrace reasoning, and fight fluff — treating all three the same
way (e.g. trying to prompt reasoning away along with fluff) throws away real
accuracy gains. Classify before optimizing.
