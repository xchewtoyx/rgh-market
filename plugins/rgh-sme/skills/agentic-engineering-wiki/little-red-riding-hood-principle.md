---
type: concept
title: Little Red Riding Hood Principle
description: >
  Don't stray far from documents resembling the model's training data — the
  closer a prompt matches a familiar document type, the more stable the output.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 4"
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 7"
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

Named for the fairy tale where straying from the forest path leads to
disaster: don't stray far from the path upon which the model was trained. The
more a prompt resembles a familiar document type from training data, the more
predictable and stable the resulting completion — this is the first of the
[criteria for converting a user problem into the model domain](prompt-conversion-criteria.md),
and it recurs across nearly every other prompt-engineering technique in this
domain, because most techniques are really just different ways of making a
prompt look like something the model has plausibly seen before.

Since model providers rarely document their training data composition in
detail (partly to avoid handing out a jailbreaking cheat sheet), the practical
way to discover a familiar document type is to just ask the model — e.g. "What
types of formal documents are useful for specifying financial information
about a company?" — then have it generate an example and check whether the
format fits your need. The [document-completion prediction
heuristic](document-completion-prediction-heuristic.md) is the diagnostic
counterpart: given a candidate prompt, imagine the training-set document it
most resembles to predict how it will actually complete.

For completion models, mimic any recognizable document type or motif:
programs, news articles, tweets, markdown documents, transcripts. For chat
models, the overall document (ChatML) is fixed by the provider, but the
principle still applies *within* a user message — using common markdown
conventions (`#` for sections, backticks for code, `*` for list items) works
because these are motifs the model recognizes, not because markdown is
inherently better structured. Choosing the right document archetype — an
[advice conversation](advice-conversation-document.md),
[analytic report](analytic-report-document.md), or
[structured document](structured-document-format.md) — and matching
[snippet formatting](snippet-formatting-by-document-type.md) are the concrete
mechanisms for staying on the path, and
[prompt assembly algorithms](prompt-assembly-algorithms.md)
should preserve an ordering that still reads like a plausible training
document rather than scrambling it for machine convenience.

Three common document archetypes put this principle into practice:
[advice conversation](advice-conversation-document.md),
[analytic report](analytic-report-document.md), and
[structured document](structured-document-format.md) — each trained-on
heavily enough that mimicking it makes the completion easy to anticipate.

A [fine-tuned model](fine-tuning-decision.md) complicates the principle: it
now has two paths a completion could follow — the original pretraining path
(still there, if "slightly overgrown") and the new fine-tuned path. If a
prompt looks like it could follow the old path, the model will follow it,
effectively forgetting the fine-tuning it received. The modified guidance for
a fine-tuned model — elaborated in
[fine-tuning as prompt continuation](fine-tuning-as-prompt-continuation.md) —
is two-part: make the prompt look like the beginning of one of the documents
it was fine-tuned on, and be very sure it doesn't also look like one of the
original pretraining documents — an ambiguous prompt that resembles both
risks the model reverting to pretraining behavior right when the fine-tuning
was needed most.
