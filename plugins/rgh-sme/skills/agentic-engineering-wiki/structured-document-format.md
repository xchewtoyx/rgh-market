---
type: concept
title: Structured Document Format
description: >
  Write a prompt as a formally specified document — XML, YAML, or JSON — to
  make strong assumptions about completion shape and ease parsing.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

Structured documents follow a formal specification, letting an application
make strong assumptions about completion form and easing parsing of complex
output — the third
[document archetype](advice-conversation-document.md) alongside the advice
conversation and [analytic report](analytic-report-document.md). A worked
example: Anthropic's Artifacts feature prompts the model with XML tags
delineating interaction pieces — an `artifacts_info` block explains how
Artifacts work, with example `user_query`/`assistant_response` pairs; inside a
response, an `antThinking` block lets the model reason about whether the
request warrants an Artifact, and if so an `antArtifact` block (with
`identifier`, `type`, `language`, `title` attributes) holds the actual
Artifact content. This makes response parsing straightforward: the
`antThinking` block is extracted and hidden from the user, and `antArtifact`
is extracted into its own rendering pane under its title.

Per the [Little Red Riding Hood principle](little-red-riding-hood-principle.md),
prefer formats common in training data — XML and YAML are both frequent in
precision-oriented technical documents across many domains, and both organize
a document hierarchically into named elements with subelements:

- **XML** — tags opened and closed, may carry attributes, content may contain
  nested subtags. Works well when elements are relatively short, or multiline
  where indentation doesn't matter. Watch for five escape sequences:
  `&quot;`, `&apos;`, `&lt;`, `&gt;`, `&amp;`. Supports HTML-style comments
  (`<!-- ... -->`), occasionally useful as editorial hints to the model.
- **YAML** — named fields or unnamed bullet points, with hierarchy tracked by
  indentation. Indentation must be exact for standard parsers, which makes it
  fiddly, but it's helpful precisely where indentation matters, such as code
  or other formatted text — a field opened with `fieldname: |2` preserves
  indentation in a multiline value without needing any escaping, ending at
  the first line whose indentation is smaller than the field's own baseline.
- **JSON** (or JSON Lines) — historically discouraged for prompts as
  escape-heavy and less readable than XML or YAML, but providers that have
  invested heavily in accurate JSON generation for their function-calling
  APIs make JSON a reasonably good choice specifically for those models.

Structured formats reduce ambiguity at the cost of more scaffolding tokens per
element than a [markerless transcript](transcript-format-selection.md) would
need — the same tradeoff [tool definition internal representation](tool-definition-internal-representation.md)
makes when it renders tool calls with explicit argument names instead of a
positional format.

Choosing a well-formed prompt-side format is only half of getting reliable
structured completions — it makes a conforming output *likely*, not
*guaranteed*. See [structured output generation](structured-output-generation.md)
for the harness-side techniques (defensive post-processing, constrained
decoding, fine-tuning) that close that remaining gap.
