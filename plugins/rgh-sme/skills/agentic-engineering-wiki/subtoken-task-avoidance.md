---
type: concept
title: Subtoken Task Avoidance
description: >
  A model can't examine or manipulate individual letters within its own
  tokens, so any task requiring that should be handled outside the LLM.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 2"
---

Because a model only ever sees the multicharacter chunks produced by
[tokenization](tokenization-fundamentals.md), never individual letters, it has
no native way to slow down and examine a word's spelling the way a human
consciously can. Reasoning about individual characters requires deep
"concentration" the architecture doesn't naturally support — even advanced
models can be fooled by questions like "how many Rs are in 'strawberry'?"

This makes any task with a **subtoken-level component** — one requiring the
model to break apart or reassemble the letters inside a token — much harder
than it looks from the task description alone:

- Reversing the letters within a word reliably fails, because the reversed
  sequence isn't a token the model has ever "seen" as a unit.
- Filtering by a spelling property (e.g. "list countries starting with the
  two-letter prefix 'Sw'") can fail even for well-known answers, if the
  target words happen to be single tokens in that model's vocabulary — the
  model has no native access to a single token's internal spelling.
- **Capitalization** is a concrete, easy-to-hit instance of the same failure:
  tokens containing capital letters are often entirely different tokens from
  their lowercase counterparts, and capitalized and noncapitalized
  tokenizations don't correspond one-to-one (a lowercase phrase might
  tokenize into 4 tokens while its all-caps form tokenizes into 6). Even
  when a model manages a capitalization-transformation task, it spends real
  processing capacity on it that would otherwise go to the actual task —
  capacity better not spent, since case-conversion needs no LLM at all.

**Design pattern**: avoid giving the model subtoken-level tasks where
possible. If a task has a subtoken-level component, handle that component in
pre- or post-processing instead of asking the model to do it. A useful
decomposition for tasks that mix language understanding with a spelling
constraint: use the LLM as an oracle to generate a broad candidate list (its
actual strength), then apply ordinary, non-LLM logic to filter or transform
that list by the spelling property — rather than asking the LLM to do the
whole task, spelling constraint included, end to end. This is the
subtoken-level instance of the broader principle in [non-LLM task
implementation](non-llm-task-implementation.md): don't reach for the model
where a narrower, more reliable tool already does the job.
