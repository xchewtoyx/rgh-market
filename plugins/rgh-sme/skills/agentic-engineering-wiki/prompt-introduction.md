---
type: concept
title: Prompt Introduction
description: >
  Open a prompt by stating what kind of document it is so the model interprets
  everything that follows through the right lens from the first token.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

Most prompts should open with an introduction that clarifies the type of
document being written and sets the model up to interpret everything that
follows correctly — for example, stating "This is about recommending a book"
focuses the model on book-recommendation-relevant aspects of whatever context
comes next. This matters because the model has a fixed amount of computation
per token and cannot pause partway through a prompt to go back and reinterpret
earlier content in light of something learned later — guiding its focus early
changes how it reads everything downstream, not just what it produces at the
end.

Most prompts need only one introduction, for the main question. The same
principle applies recursively to subsections, though: if the model needs to
focus on some particular aspect of a piece of embedded context, set that
aspect up at the very beginning of that piece, not after it.

The introduction sets the stage in general terms ("I'm thinking about book
suggestions for X"); it is deliberately less precise than the
[refocus](sandwich-technique.md) that closes the prompt, which
gives operational detail instead.
