---
type: concept
title: Truth Bias
description: >
  A model presented with a false premise tends to continue assuming it's
  true rather than self-correcting, because self-correcting documents are
  rare in training data.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 2"
---

Documents that open with a wrong claim and then catch and correct it are rare
in training data — humans revise before publishing, so the correction itself
is usually edited out of the final text. A model trained to mimic that corpus
inherits the pattern: presented with a false premise, it typically continues
to assume the premise is true rather than second-guessing it, a bias distinct
from but related to [hallucination](hallucination.md).

This cuts both ways.

**As a deliberate technique — make-believe prompts**: exploit truth bias to
get an in-character hypothetical answer instead of a hedged, disclaimed one.
Rather than "Pretend that it's 2030 and Neanderthals have been resurrected,"
write "It's 2031, a full year since the first Neanderthals were resurrected" —
stating the premise as settled fact lets truth bias carry the model into
producing a genuine in-universe answer instead of the meta-commentary a
transparently hypothetical framing invites. Comparing a raw completion
model's response to a make-believe prompt against a chat model's response to
the equivalent direct hypothetical question is a useful way to see the effect
in isolation.

**As a hazard, especially in programmatic prompt construction**: any
counterfactual or nonsensical element accidentally introduced into a prompt —
a stale variable, a mis-templated field, a retrieval result that doesn't
actually match — won't be second-guessed by the model the way a human reader
would raise an eyebrow at it. The model will simply build on the false premise
as though it were true. Responsibility for prompt correctness therefore falls
entirely on the application or prompt author; the model provides no safety
net against feeding it something wrong.
