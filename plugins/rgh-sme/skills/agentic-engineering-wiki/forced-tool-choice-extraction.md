---
type: concept
title: Forced Tool-Choice Extraction
description: >
  Extract structured content from free-form input by defining a tool shaped
  like the target structure and forcing the model to call it.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
---

For a workflow task that extracts structured content from free-form input
(e.g. scraping a restaurant's name, address, and phone number out of raw
HTML), define a tool whose arguments are exactly the structure to extract, and
force the model to call it rather than leaving tool choice open. Example:
system message "Your job is to extract content about restaurants and save
them to the database," a `saveRestaurantDataToDatabase` tool with
`name`/`address`/`phoneNumber` properties, and a user message containing the
raw HTML. Providers that support forcing a specific tool (OpenAI's
`tool_choice` set to name the function) guarantee this call happens.

It doesn't matter that no real database exists behind the tool — the tool call
is only a vehicle to convince the model to emit the structured information it
read out of the input, which the workflow then passes to the downstream task
as structured [function calling](function-calling.md) output rather than text
to be parsed. Structured-output features that constrain function-call
arguments to a schema further guarantee the parsed shape matches what's
needed. This is one of several [structured output generation](structured-output-generation.md)
techniques — the tool-calling-specific way to get a schema guarantee, as
opposed to relying on plain-text JSON-mode prompting or a grammar-constrained
decoder.

When this approach struggles, two likely causes, each with a different fix:

1. **Extraction is genuinely hard from the source document** — sanity check by
   asking whether a human could pick out this content; if not, the model can't
   either, and the fix is to clean up or simplify the input rather than the
   tool definition.
2. **The target structure is overly complex** — many keys, nested objects or
   lists, possibly-null fields. Fix by breaking the structure into smaller
   pieces tackled one at a time
   ([task decomposition prompting](task-decomposition-prompting.md)), per
   [tool definition design](tool-definition-design.md)
   on keeping arguments few and simple; this also lets you give more specific
   per-field instructions, which further improves results.

Prefer this over free-text parsing when downstream tasks need reliable keys;
prefer a [templated prompt task](templated-prompt-task.md) when the product
is prose whose exact shape is softer.
