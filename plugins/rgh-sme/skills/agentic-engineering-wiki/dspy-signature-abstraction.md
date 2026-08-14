---
type: concept
title: DSPy Signature Abstraction
description: >
  Declare what a text transformation needs to do — typed input/output field
  names, not a hand-written prompt string — so a compiler can generate and
  refine the actual prompting strategy.
sources:
  - title: "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines"
    resource: "DSPy (Khattab et al.), §1, §3"
---

Hand-written prompt templates hard-code both *what* a step should do and *how*
to get a model to do it in the same string, which is why they generalize
poorly across models, domains, or even individual inputs — closer to
hand-tuning classifier weights than to programming. A **signature** separates
the two: it declares only *what* a text transformation needs to do — a tuple
of named input fields and output fields, plus an optional instruction — and
leaves *how* to prompt for it to a compiler.

Shorthand notation makes a complete signature as short as `question ->
answer`, or `english_document -> french_translation` for translation; DSPy
expands field names into meaningful LM instructions automatically, inferring
each field's semantic role from its name (`question` is treated differently
from `answer`). When more control is needed, a signature can instead be
declared as an explicit Python class with per-field descriptions and (as a
richer variant) typed output fields (`bool`, `int`, `list`, `dict`), trading
the shorthand's brevity for reduced brittle string-parsing.

The payoff of separating declaration from prompting strategy: the same
signature compiles into different concrete prompts depending on which
[module](dspy-module-parameterization.md) implements it and what a
[teleprompter](dspy-compiler-three-stages.md) discovers works best for the
current model and data — one declarative spec, several possible executions —
and structured field parsing replaces ad hoc string manipulation on both the
input and output sides. This is the DSPy-specific instance of a broader
pattern in [prompt optimization tooling](prompt-optimization-tooling.md):
separate *what a step must accomplish* from *the literal prompt text*, so the
text becomes something a search process owns rather than something written
once by hand.
