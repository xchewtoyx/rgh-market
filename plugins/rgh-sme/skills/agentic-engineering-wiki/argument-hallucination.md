---
type: concept
title: Argument Hallucination
description: >
  A model may invent plausible-looking placeholder values for tool arguments
  never mentioned in the conversation, producing schema-valid but
  semantically wrong calls, rather than asking for them.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
---

Under [function calling](function-calling.md), providers may constrain *which*
tools and parameter names appear, but argument values remain generative. Given
a tool argument the conversation never supplied a value for, a model may
invent a plausible-looking placeholder (e.g. `"my-org"`, `"my-repo"`) rather
than flagging that the value is unknown. This is [hallucination](hallucination.md)
specialized to tool-call arguments, and a specific case of
[valid tool, incorrect parameter values](agent-planning-failure-modes.md) — the
call is well-formed and passes schema validation, but the value is fabricated.

No silver bullet exists, but mitigations help, mostly falling under
[tool definition design](tool-definition-design.md):

- **Drop the argument from the tool definition when the application already
  knows the value** — supply it directly at call time instead of asking the
  model to fill it in, or give it a default the application can detect and
  handle specially.
- **Instruct the model to ask when unsure** — unreliable on its own, but
  improving across model generations.
- **Log every parameter set and inspect actual values** rather than trusting
  that a valid-looking call used a real one, treating this the same way you
  treat any other [function calling](function-calling.md) output; require
  [plan-validate-execute](plan-validate-execute.md) or
  [human approval gates](human-approval-gates.md) when a wrong value would be
  costly.
