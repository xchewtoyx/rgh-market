---
type: concept
title: Explicit Instruction Design
description: >
  Ambiguity-free task wording, personas, examples, and explicit output formats
  that tell the model exactly what success looks like.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 5"
---

Clear [prompt engineering](prompt-engineering.md) starts with unambiguous
instructions: define scales, decide what uncertain cases should return, and
forbid unwanted formats (for example fractional scores). Ask the model to adopt
a persona when perspective matters — the same essay scores differently for a
first-grade teacher than for a generic grader. Prefer stating **dos** over
bare don'ts, give a reason that bolsters the command, and soften brittle
absolutes; still place hard rules in the
[system prompt](system-prompt-architecture.md) when the API trains obedience
there ([static vs dynamic prompt content](static-vs-dynamic-prompt-content.md)).

Provide examples to reduce ambiguity
([in-context learning](in-context-learning.md)). Specify output format
explicitly, including exact strings (e.g. "N/A", "Unknown") if you want them
to appear in inputs so the model emits structured output instead of appending to
the input. These tactics are the baseline before clever tricks that rot as models
improve.

This kind of always-applicable instruction is
[static content](static-vs-dynamic-prompt-content.md): clarification baked into the
app for every request, distinct from the dynamic context that varies per
instance. Explicit clarification matters more than it seems, for two reasons:
programmatic queries get none of the quick back-and-forth repair humans use to
fix miscommunication, so a misunderstanding here causes outright failure
rather than a follow-up question; and clarity produces **consistency** —
similar inputs get processed the same way — which in turn enables
optimization, helps users learn what the app can do, and builds trust.

Three rules of thumb for writing the instructions themselves: state positives
instead of negatives (say what to do, not just what to avoid); bolster
commands with a reason, since a stated rationale is followed more reliably
than a bare command; and avoid absolutes where the underlying rule genuinely
has exceptions ("kill only rarely, and make sure it's really appropriate" is
more robust than "never kill," which the model may follow inconsistently
regardless of good intentions). For chat-API models specifically, put explicit
instructions in the [system prompt](system-prompt-architecture.md) — it is
trained specifically to be obeyed — but no model follows instructions with
perfect reliability, explicit or otherwise.
