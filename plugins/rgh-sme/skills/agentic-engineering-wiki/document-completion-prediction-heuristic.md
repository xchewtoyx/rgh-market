---
type: concept
title: Document-Completion Prediction Heuristic
description: >
  Predict a completion by imagining a random training-set document that
  happens to start with the prompt, not by asking how a reasonable person
  would reply.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 2"
---

To predict what a given prompt will complete to, don't ask "how would a
reasonable person reply to this?" Ask instead: pick a document from the
training set at random; all you know about it is that it starts with this
exact prompt; what is the statistically most likely way it continues? That's
the expected LLM output, because the model is a [document-completion engine
that mimics its training data](little-red-riding-hood-principle.md), not a
reasoning agent answering as a person would.

The gap between these two framings is often the gap between a surprising
model output and an unsurprising one. A prompt ending "...at all. For a text
that starts like that, what's the statistically most likely completion?"
resolves very differently depending on whether the training set leans
narrative prose (a line about reading a book) or advice/customer-service
transcripts (troubleshooting instructions) — the "reasonable person" framing
gives no way to choose between these, while the "random training document"
framing forces you to actually think about what kind of document the prompt
resembles. The better you know a model's training-data composition, the
sharper this heuristic gets; providers rarely publish exact composition, but
a reasonable sense of the kinds of documents involved is usually formable.

This heuristic is the diagnostic counterpart to the [Little Red Riding Hood
principle](little-red-riding-hood-principle.md): where that principle
prescribes shaping a prompt to resemble a familiar document type, this
heuristic is how to check, before sending a prompt, what a model conditioned
on that training data is actually likely to produce from it.
