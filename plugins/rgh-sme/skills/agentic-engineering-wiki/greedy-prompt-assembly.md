---
type: concept
title: Greedy Prompt Assembly
description: >
  Add elements highest-value-first or remove them lowest-value-first to fit
  the token budget, choosing direction based on how elements interact.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

Once a project has matured past the
[minimal prompt crafter](minimal-prompt-crafter.md), a greedy algorithm —
possibly combined with limited exploration of alternatives — is the
recommended approach to [prompt assembly](prompt-assembly-algorithms.md) for
speed. Two variants, chosen based on how elements interact via
[dependency](prompt-element-dependency.md):

- **Additive greedy** — start with an empty prompt and add elements one at a
  time: each step adds the highest-[value](prompt-element-importance.md)
  element that satisfies all its requirements, doesn't conflict with elements
  already included, and fits the remaining length budget; once the budget is
  filled, re-sort the chosen elements by
  [position](prompt-element-position.md). This stays effective even with far
  more candidate elements than could ever fit, since it never has to consider
  most of them. It works best with few cyclical requirements and few cases of
  a high-value element depending on a low-value one. Pre-sorting candidates by
  their requirements and values lets each element be considered only once its
  dependencies are already satisfied, simplifying the implementation.
- **Subtractive greedy** — start by including all elements, then gradually
  remove the least valuable ones, or ones whose dependencies are no longer
  met, until the prompt fits the budget. This works well with a manageable
  total number of elements and few incompatibilities; otherwise it becomes
  cumbersome. It has the mirror-image weakness of the additive approach: a
  high-value element depending on a low-value one can still produce a
  suboptimal result unless the algorithm specifically prioritizes retaining
  high-value dependencies. [Elastic snippets](elastic-snippets.md) are
  normally easier to handle subtractively (progressively shrink a chosen
  version) than additively (guess which size to add first).

Both are basic prototypes, sufficient for many applications but expected to
be outgrown as an application's specific requirements become clear.
