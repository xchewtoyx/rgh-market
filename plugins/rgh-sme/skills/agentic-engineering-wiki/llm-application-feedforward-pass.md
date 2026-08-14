---
type: concept
title: LLM Application Feedforward Pass
description: >
  Convert a user's problem into a model-ready prompt in four steps — retrieve
  context, snippetize it, score and prioritize it, then assemble the prompt.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 4"
---

The feedforward pass is the half of the
[LLM application loop](llm-application-loop.md) that converts the user's
problem into the model's domain, built from four steps:

1. **Context retrieval** — gather the raw material the prompt will draw on,
   at varying [directness](context-directness-spectrum.md) from the user's
   own words. The runtime, per-instance side of this step is
   [dynamic context gathering](dynamic-context-gathering.md), constrained by
   urgency, preparability, and scored usefulness.
2. **Snippetizing context** — break retrieved context into the chunks most
   relevant to the prompt, needed whenever raw retrieval returns more than
   fits the token budget. See [chunking strategy](chunking-strategy.md) for
   how sources get split, and note that snippetizing can also mean format
   conversion — transcribing voice to text for a phone assistant, or turning
   a raw JSON API response into natural language so the model doesn't
   incorporate raw JSON fragments into its own output. Format the result to
   match the prompt's [document type](snippet-formatting-by-document-type.md).
3. **Scoring and prioritizing snippets** — decide which snippets actually make
   it into the prompt. Large context windows have made running out of raw
   space less common, but trimming still matters: irrelevant text confuses
   the model and degrades completions regardless of how much room is left.
   See [prompt element importance](prompt-element-importance.md) for the two
   mechanisms (priority tiers and finer-grained scores) used to rank
   candidates against each other.
4. **Prompt assembly** — pack the best supporting context around the user's
   problem without exceeding the token budget (exceeding it yields only an
   error, not a degraded response). This needs "accounting": fit the
   boilerplate instructions and the user's request first, then fill the
   remaining space with context via a
   [prompt assembly algorithm](prompt-assembly-algorithms.md), in a final
   ordering that still reads like a plausible document per the
   [Little Red Riding Hood principle](little-red-riding-hood-principle.md).
   When space is still tight, [trim what's already selected](last-minute-context-trimming.md)
   rather than dropping whole snippets.

This is the operational pipeline behind
[context engineering](context-engineering.md) that runs before the model
call; the outbound transform back to the user domain happens after the
completion returns.
