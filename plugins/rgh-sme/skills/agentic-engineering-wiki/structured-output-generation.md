---
type: concept
title: Structured Output Generation
description: >
  Guaranteeing a completion parses into a required schema needs one of four
  techniques, each with a different reliability-versus-effort tradeoff.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 2"
---

Structured output matters whenever a task either inherently produces a
structured result — **semantic parsing**, translating natural language into a
structured or machine-readable format, such as text-to-SQL or classification
into a fixed set of labels — or feeds a downstream step that needs a specific
parsable shape, which is the common case in agentic systems where a model's
output becomes the next step's [tool-call input](task-io-schema-design.md).
"JSON mode" support in an API typically guarantees only *syntactically valid*
JSON, not correct content, and output can still come out truncated or
unparsable if generation stops early (for example by hitting a max-token
limit) — raising the token limit to compensate trades away latency and cost.

Four techniques, in roughly increasing order of reliability and effort:

- **Prompting** — the first line of defense: state the required schema and
  format explicitly. Effectiveness depends entirely on the model's underlying
  instruction-following strength and on prompt clarity, and it comes with no
  format guarantee at all. Adding a validation pass — a second model call
  that checks and, if needed, corrects the format — improves compliance but
  roughly doubles cost and latency per output.
- **Post-processing** — cheap, simple, and surprisingly effective when a
  model's mistakes are small and repetitive, which they usually are, since a
  model (like a student) tends to repeat the same kinds of errors. A
  defensive parser that patches common breakages — for instance, adding a
  missing closing bracket — can push correct-parse rates very high on top of
  imperfect prompting alone. This only works when the errors it needs to fix
  are genuinely easy to fix; it's not a substitute for a model that's
  fundamentally not following the schema.
- **Constrained sampling** — filter the logit vector at every generation step
  to keep only tokens that satisfy a formal grammar for the target format,
  then sample only among the survivors, so an invalid token is structurally
  never chosen. This needs a defined grammar per output format (a JSON
  grammar, for instance, disallows a bare `{` appearing inside a string
  context), and building and integrating one is nontrivial — so it's less
  generalizable than the other techniques and can add generation latency.
  Some practitioners argue the same engineering effort is better spent
  improving the model's general instruction-following instead of building
  grammars for every format needed.
- **Fine-tuning** — the most effective and general technique: fine-tune on
  examples already in the desired output format. This still doesn't
  *guarantee* compliance, but it's far more reliable than prompting alone.
  For genuinely closed-ended tasks like classification, format compliance can
  be architecturally guaranteed rather than merely encouraged, by appending a
  classifier head restricted to the pre-specified classes and training on top
  of it — see [fine-tuning approach comparison](fine-tuning-approach-comparison.md)
  for how this fits among the other fine-tuning options.

[Forced tool-choice extraction](forced-tool-choice-extraction.md) is a
prompting-technique instance of this problem specialized to tool-calling
APIs: instead of relying on a bare JSON-mode prompt, define a tool shaped
exactly like the target structure and force the call, letting the provider's
own function-calling machinery carry the structural guarantee that a
freestanding text prompt can't offer on its own. [Structured document
format](structured-document-format.md) covers the complementary prompt-side
question of which document format (XML, YAML, JSON) to write the prompt in,
as distinct from how to guarantee the completion actually conforms to it.

As instruction-following continues to improve across model generations, the
practical need for the heavier techniques here — constrained sampling and
fine-tuning specifically for format compliance — is expected to shrink, with
plain prompting handling more of the load on its own.
