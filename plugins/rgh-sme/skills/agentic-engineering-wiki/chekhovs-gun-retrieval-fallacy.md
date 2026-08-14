---
type: concept
title: Chekhov's Gun Retrieval Fallacy
description: >
  A model tends to treat any retrieved snippet as meaningfully relevant and
  feels compelled to use it, so irrelevant hits actively mislead the answer.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 5"
---

Irrelevant retrieved snippets in a [RAG](retrieval-augmented-generation.md)
prompt don't just waste space — they can actively crowd out more useful
context and mislead the model, because the model tends to treat any
information it's given as meaningfully relevant and feels compelled to make
use of it. The name comes from Chekhov's dramatic principle that a gun hung on
the wall in act one must be fired by the end of the play: put a snippet in
front of the model, and it will try to make it matter to the answer, whether
or not it actually does.

The only sure mitigation is retrieving the *right* snippets in the first
place — there is no reliable way to instruct the model to ignore irrelevant
context once it's included. Frame retrieval explicitly as a search problem: a
search string against a document collection — treat that string like a
mini-prompt under [query rewriting](query-rewriting.md) — aiming to surface
the snippets most closely related to it, ideally with a relevance score from
[hybrid retrieval](hybrid-retrieval.md), rather than pulling in everything
even loosely on-topic. [Context grounding](context-grounding.md) instructions
help the model lean on what's actually relevant but cannot undo a prompt
already stuffed with misleading "guns." This compounds with
[lost in the middle](lost-in-the-middle.md) pressure — a low-relevance snippet
is doubly costly if it also lands where the model attends to it poorly, since
it wastes both attention and prompt budget for no benefit.
