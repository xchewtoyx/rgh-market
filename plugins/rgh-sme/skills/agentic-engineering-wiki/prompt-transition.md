---
type: concept
title: Prompt Transition
description: >
  End a prompt by firmly pivoting from explaining the problem to solving it,
  so the model completes an answer instead of adding more framing.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

The final part of a prompt should firmly pivot from explaining the problem to
solving it — this is the part the model is meant to complete, and it should
not just add more (possibly fabricated) context of its own.

In chat interfaces this can be as simple as ending on a question mark; RLHF
training has taught such models to answer the last stated, or even implied,
question. Some commercial chat platforms auto-signal via the API when the
assistant should begin responding, removing the need to engineer this
explicitly.

Completion models need more explicit guidance, since nothing in the API tells
them a turn has ended. The most common technique, sometimes called
**inception**, is to shift from problem-poser to problem-solver directly in
the prompt text: begin writing the answer yourself and let the model continue
it as if it had authored the opening — even a trailing opening quotation mark
can serve this purpose. Beyond driving the transition itself, inception
improves instruction compliance, eases downstream parsing, and removes
ambiguity about how the response should open. The
[refocus / sandwich technique](sandwich-technique.md) and the transition can
often be merged: write the beginning of the answer as a restatement or
summary of the
problem, and let the model supply the actual answer from that point. This
pairs with [templated prompt tasks](templated-prompt-task.md), which use
prefix/suffix framing to force extractable completions.
