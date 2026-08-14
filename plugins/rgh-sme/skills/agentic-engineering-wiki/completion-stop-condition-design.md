---
type: concept
title: Completion Stop-Condition Design
description: >
  Engineer how and where a completion-model generation halts, since nothing
  in the API tells a completion model a turn has naturally ended.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 4"
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 7"
---

Chat models handle stopping mostly for free: fine-tuned stop behavior ends
generation after the assistant's message, though the model may still need
instruction to limit chattiness. Completion models have no such built-in
signal, so stopping has to be engineered — usually one of two ways:

- **Build an expectation of a natural end into the instructional text**, so
  the model's own sense of "this response is complete" triggers the stop.
- **Engineer a predictable opening pattern for whatever comes next**, and use
  the API's `stop` parameter to halt generation exactly when that pattern
  begins — for example, if every section of a document starts with `##`, a
  stop string of `\n#` reliably halts generation right as a new section would
  begin, before the model can confabulate content that doesn't belong.

A cautionary anecdote for why this matters: a misconfigured early chat model
once had its end-of-turn stop token suppressed, so it never learned to stop —
completions that had already produced an intelligible answer would spiral
into repeated sign-offs ("Hope you have a nice day!" … "…a wonderful day!" …
"…a festive day!" …) until hitting the hard token limit, because the model had
no way to naturally terminate on its own.

This is [criterion 4](prompt-conversion-criteria.md) of turning a user problem
into a working prompt, and it interacts with the
[transition](prompt-transition.md): a good transition gets the model producing
the answer; a good stop condition keeps it from continuing past the answer
once it's done.

Once [recognizable completion boundaries](recognizable-completion-boundaries.md)
are known, model-as-a-service APIs offer two mechanisms to actually cut
generation off there instead of just filtering after the fact (self-hosted
models already have full freedom to stop wherever the caller likes):

- **Stop sequences** — many APIs accept a `stop` argument: a list of
  sequences that halt generation server-side the moment one is reached, at no
  further time, compute, or money cost. Stop sequences often should begin
  with a newline character (e.g. `\n#` for a markdown header) — omitting the
  newline risks stopping erroneously mid-phrase, such as inside a comment or
  a phone number that happens to contain the stop string.
- **Streaming with cancellation** — tokens or small batches arrive
  incrementally; recognizing the end while streaming lets the caller stop
  consuming without waiting for the rest, and if the model supports
  cancellation, some compute and money can be saved too — though less
  reliably than with stop sequences, since network delay means a cancellation
  signal doesn't land instantly. More models support stop sequences than
  support streaming plus cancellation, and stop sequences are slightly more
  effective when both are available; but since stop sequences are limited to
  specific literal strings, cancelling a stream is sometimes the only option
  for a boundary that can't be expressed as one. Streaming cancellation can be
  strengthened by also treating common-but-not-exhaustive continuation
  markers as stop points — e.g. when generating a Python class body, `\nclass`,
  `\ndef`, and `\nif` at column zero are common signals the class definition
  has ended, since the class's own methods appear indented (`\n\tdef`) rather
  than at that same zero indentation.
