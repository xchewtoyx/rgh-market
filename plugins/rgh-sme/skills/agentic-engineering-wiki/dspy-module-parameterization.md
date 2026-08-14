---
type: concept
title: DSPy Module Parameterization
description: >
  Wrap a signature in a callable module whose LM choice, instructions, and
  demonstrations are explicit parameters a compiler can search over, so
  published prompting techniques become swappable, signature-agnostic
  components.
sources:
  - title: "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines"
    resource: "DSPy (Khattab et al.), §3"
---

A **module** implements a [signature](dspy-signature-abstraction.md) as a
callable: given input fields, it assembles a prompt (including any
demonstrations), calls the LM, and parses the output fields back out. The
base module, `Predict`, holds three explicit **parameters**: which LM to call,
the prompt instructions and each field's string prefix, and — the most
consequential lever in practice — the list of demonstrations used as few-shot
examples (for a frozen LM) or as training data (for finetuning). Making these
ordinary parameters rather than buried string literals is what lets an
optimizer treat prompting as parameter search instead of manual rewriting; see
[instruction vs demonstration optimization](instruction-vs-demonstration-optimization.md)
for which of these two levers tends to matter more in practice.

Built-in modules generalize published prompting techniques into
signature-agnostic, drop-in components implemented as a thin transform over
`Predict`: `ChainOfThought` prepends a rationale output field with a
"let's think step by step" prefix before the real answer field
(implementing [chain-of-thought prompting](chain-of-thought-prompting.md) for
*any* signature with no per-task code); `ProgramOfThought` and
`MultiChainComparison` generalize other published techniques the same way;
`ReAct` implements the [ReAct loop](react-loop.md) as a module. Because a
module only needs to honor its declared signature, swapping `Predict` for
`ChainOfThought` in a one-line program makes the model reason before
committing to an output field with **no other code change** — the technique
becomes an implementation choice, not a rewrite of the surrounding pipeline.

**Tools** are the non-LM counterpart: modules that execute computation instead
of calling an LM — retrieval, SQL, or a sandboxed code interpreter — composed
into a pipeline the same way. A **program** declares the modules it needs
in `__init__` (so a compiler can find and optimize them) and expresses the
pipeline as ordinary imperative code — including `if`, `for`, exceptions — in
a `forward` method, directly modeled on PyTorch/Chainer's define-by-run style.
Because the signature and the module implementing it are separate, changing
only the signature string (e.g. from `"context, question -> answer"` to
`"context, question -> search_query"`) repurposes the same module from an
answerer into a query generator with no structural change to the surrounding
program.
