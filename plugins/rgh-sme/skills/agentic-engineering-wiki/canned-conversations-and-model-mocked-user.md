---
type: concept
title: Canned Conversations and Model-Mocked User
description: >
  Two ways to define a test "example" for a multi-call conversational loop —
  replay a scripted transcript, or have a model play the user's side too.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 10"
---

For a simple, single-call loop, an [example](example-suite.md) problem is one
instance of the context that goes into that call's prompt, and the example
solution is the processed output — straightforward to define. For complex,
multi-call, interdependent architectures, especially conversational ones
under [conversational agent context](conversational-agent-context.md),
defining what counts as one "example" is harder. Two approaches:

- **Canned conversations** — write out a full scripted conversation ahead of
  time. Evaluate the model pass by pass on how well it performs at each step,
  and regardless of what the model actually answered at a given step, test the
  *next* step by substituting the scripted (canned) answer instead of the
  model's real one. This isolates each step's quality from compounding
  [errors](compound-mistake-amplification.md) earlier in the same run, at the
  cost of never testing how the model recovers from its own actual mistakes.
- **Model-mocked user** — have a model play the user's side of the
  conversation too, guided by a user profile the way an actor follows
  improv-theater instructions. This tests the whole loop end to end, but bakes
  in whatever shortfalls the mocking model itself has — domain
  misunderstandings, behavioral assumptions about users — into the test
  itself. Imperfect, but often the best available option when no real user
  transcripts exist yet.

Choosing between them is a tradeoff between isolating individual steps
(canned conversations) and testing realistic end-to-end behavior at the cost
of a biased proxy for the user (model-mocked user) — the same
per-step-versus-whole-loop tradeoff [eval test granularity](eval-test-granularity.md)
makes generally, applied specifically to how the *input side* of a
conversational test gets constructed.
