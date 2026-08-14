---
type: concept
title: Prompt Assembly Algorithms
description: >
  Assembling a final prompt is an optimization problem — pick the
  highest-value elements that fit the token budget and respect dependencies.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

Once content has been turned into prompt elements carrying
[position](prompt-element-position.md),
[importance](prompt-element-importance.md), and
[dependency](prompt-element-dependency.md) properties, creating the
final prompt means solving an optimization problem: which elements to include
to maximize overall value, subject to two constraints:

- **Dependency structure** — respect every requirement and incompatibility
  between elements.
- **Prompt length** — stay within a limit, typically the context window size
  minus tokens needed for the model's response. With very large context
  windows, a softer token budget based on available compute — and to avoid
  diluting the prompt with irrelevant context, per the
  [Chekhov's gun retrieval fallacy](chekhovs-gun-retrieval-fallacy.md) — can
  substitute for a hard limit.

Once the included elements are decided, arrange them by position to form the
final prompt. The problem resembles linear programming or the 0-1 knapsack
problem (decide whether to include each element), though standard knapsack
formulations don't account for dependencies between items the way this
problem needs. No standard off-the-shelf tool solves this directly, so a
custom solution tailored to your requirements is generally needed — fast
assembly for interactive apps, or handling specific dependency patterns (code
snippets that need a specific postfix, for example, in a code-completion
tool).

Two families of algorithm cover most cases in practice, in order of
increasing sophistication:
[the minimal prompt crafter](minimal-prompt-crafter.md) — keep as much as
possible from the *end* of the content list until the budget fills, suited to
chat and documents where the recent suffix matters most, with no explicit
prioritization — for a fast starting point; and
[greedy prompt assembly](greedy-prompt-assembly.md) — additive (start empty,
repeatedly add the highest-value feasible element) or subtractive (start with
everything, drop the least valuable or unmet-dependency items, well suited to
[elastic snippets](elastic-snippets.md)) — once the application has matured
past simple suffix-filling. Both are meant as basic prototypes — expect to
move beyond them as your specific requirements become clear while refining
the application. This completes the
[feedforward pass](llm-application-feedforward-pass.md): a coherent prompt has
been constructed for the model to complete.
