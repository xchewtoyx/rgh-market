---
type: concept
title: Context Mind Mapping
description: >
  Vary the target question's individual words and aspects to surface what
  context would help answer it, before checking what's actually obtainable.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 5"
---

One technique for discovering what dynamic context an application needs:
write the target question in the middle of a mind map and vary individual
words or aspects of it, spawning follow-up questions. For example, "What book
shall I read next?" varied on "I" and on removing "next" leads to "What have
I read last?" and then "And how did I like that?" — each variation surfaces a
piece of context that would help answer the original question, whether or not
it's actually obtainable yet.

This is the inverse of starting from
[what's obtainable by proximity and stability](context-source-proximity-and-stability.md)
and asking what's relevant — mind mapping starts from what would be useful and
works backward toward whether it's feasible to obtain. Actually gathering some
of the surfaced context may be infeasible, or worth postponing to a later
version of the application; the technique's value is in generating the full
candidate list before triaging it, rather than only ever considering context
that was already easy to think of.

A recommended combined approach: mind-map what the model might want to know,
separately list what the application can actually find out, implement the
most obvious overlapping sources first, then extend to more exotic sources as
the project matures.
