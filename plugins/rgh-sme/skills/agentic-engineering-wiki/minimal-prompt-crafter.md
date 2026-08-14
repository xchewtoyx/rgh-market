---
type: concept
title: Minimal Prompt Crafter
description: >
  Fill the token budget from the end of the content backward, keeping the
  most recent elements with no scoring or prioritization needed.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

For iterative development, start [prompt assembly](prompt-assembly-algorithms.md)
with a minimal prompt crafter: order the prompt elements, then keep as many as
possible starting from the **end** of the content, filling the token budget
backward from there. No evaluation or prioritization of individual snippets is
needed — position alone decides what survives.

This works because models are trained to handle document suffixes well, so
truncating from the front is a safe default. It suits applications built
around one main text (truncate the oldest parts of a long document) or
chat-like applications where the most recent exchanges are the most relevant,
matching the recency effect behind
[lost in the middle](lost-in-the-middle.md). Reach for
[greedy prompt assembly](greedy-prompt-assembly.md) once elements genuinely
need to be ranked against each other rather than just kept-or-dropped by
recency.
