---
type: concept
title: Chat vs. Completion Tradeoffs
description: >
  Chat models buy unambiguous turn-taking and instruction compliance at the
  cost of alignment tax, excess chattiness, and loss of expressive range.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 3"
---

[ChatML](chatml-format.md)'s chat models solve the ambiguity of instruct
prompting, but the switch away from raw completion isn't free:

1. **Alignment tax** — specializing a model for assistant behavior risks
   degraded performance elsewhere; some evidence points to frontier chat
   models becoming progressively less capable at certain tasks over time as
   assistant-alignment work continues.
2. **Reduced control and excess chattiness** — RLHF-trained chat models
   remain "chatty" and often resist returning just an answer (a bare code
   snippet, say) without added commentary. A raw completion prompt like "The
   following is a program that implements quicksort in python: ```python"
   lets you rely on the completion starting exactly with the code, with a
   [stop sequence](completion-stop-condition-design.md) on the closing
   fence so there's nothing extra to parse out — a chat API can't guarantee
   this as reliably, even as it improves. See
   [completion preamble types](completion-preamble-types.md) for the general
   shape of this problem.
3. **Loss of the breadth of human diversity** — RLHF finetuning makes models
   uniform and polite by design, whereas raw training data (and so the base
   model) reflects the internet's full range of human expression, including
   its vulgar, biased, or rude corners. Sometimes that raw signal is genuinely
   useful — generating unfiltered natural-language sample data, or letting a
   domain expert brainstorm options without being redirected to "seek
   professional help." This still needs the same care against casual misuse
   that motivates safety training in the first place; the tradeoff is real in
   both directions, not a reason to discard alignment.

None of this argues chat models are worse — it argues the choice between chat
and completion access is itself a design decision with real costs on both
sides, not a default to make unreflectively.
