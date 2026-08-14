---
type: concept
title: Prompt Optimization Tooling
description: >
  Automated search and AI-assisted rewriting can explore the prompt space, but
  multiply API calls and hide template mistakes unless you inspect outputs.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), ch. 3 §3.3"
---

Manual [prompt engineering](prompt-engineering.md) is slow because the search
space is infinite. Tools such as OpenPrompt and DSPy search for prompts or
chains given I/O format, metrics, and eval data — DSPy specifically does this
by separating *what* a step does
([signatures](dspy-signature-abstraction.md)) from *how* it's prompted
([parameterized modules](dspy-module-parameterization.md) a
[teleprompter](dspy-compiler-three-stages.md) can search over). Evolutionary and gradient-like
optimizers (Promptbreeder, TextGrad) mutate prompts with model help. Structured-
output helpers (Guidance, Outlines, Instructor) constrain generations.

These tools need per-task I/O example data to search over, so start collecting
it as soon as a task's [I/O schema is defined](task-io-schema-design.md) —
well before optimization begins. The same data doubles as an offline test
harness: [per-task offline harness tests](per-task-offline-harness-tests.md)
exercise each task's prompt against recorded examples and check the
completions still match expected behavior before shipping a prompt change, so
changes can be made confidently without silent quality regressions — those
same I/O examples are the fuel the optimizers need.

Choose the optimization surface deliberately:
[instruction vs demonstration optimization](instruction-vs-demonstration-optimization.md)
(system-prompt rewrite vs few-shot bootstrap) and, when cost matters,
[strong-to-weak prompt optimization](strong-to-weak-prompt-optimization.md)
(stronger feedback model, cheaper deployed reasoner). Frameworks such as
TextGrad cast the system as a computation graph and search with
[textual gradients](textual-gradients.md) /
[textual gradient descent](textual-gradient-descent.md), covering both
[instance vs prompt optimization](instance-vs-prompt-optimization.md).
Validate each candidate prompt on a held-out split before keeping it.

Risks: hidden API-call multiplication across variants and scoring steps;
tool-developer mistakes (wrong [chat templates](system-prompt-architecture.md),
token mishandling, typos in default critiques); silent default-prompt changes
upstream. Start by writing prompts yourself to learn the model and requirements;
when adopting tools, always inspect the prompts they emit and track call volume.

**Adopting a pre-packaged agent/RAG framework doesn't itself escape hand-
written prompts.** A framework that ships ready-made chains, agents, and
retrieval pipelines (LangChain, LlamaIndex) is solving a different problem
than a search-based optimizer: it gives an application developer
pre-assembled *components*, but those components are typically implemented
internally via the same manually engineered prompt strings the developer was
trying to avoid writing — a long hand-tuned few-shot template inside a
"batteries-included" SQL chain is still a hand-tuned few-shot template. An
informal audit of one such codebase found dozens of large (1000+ character)
hand-written prompt strings and files dedicated to prompt templating, versus
none in a signature/module-based framework covering comparable tasks at
similar quality. The lesson for harness design: judge a framework by whether
its *internals* are searchable/compilable parameters or hard-coded strings,
not by whether the *surface API* you write against looks declarative.
