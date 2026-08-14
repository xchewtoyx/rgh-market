---
type: concept
title: Spurious Pattern Extrapolation
description: >
  A model extrapolates whatever pattern its few-shot examples happen to
  exhibit, including accidental ones like ordering, not just the intended one.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 5"
---

Models are good at picking up and continuing patterns from
[few-shot examples](few-shot-example-formatting.md) — but not always the
pattern the prompt engineer intended. An accidental pattern, such as examples
happening to be presented in ascending versus descending numeric order,
gets picked up and continued too: the same example set in ascending order
versus descending order has been shown to produce opposite predictions for
the next item.

The risk is not hypothetical at typical example counts: with only 3 examples
there's roughly a 17% chance they land in perfect ascending order by accident
(and another 17% for descending); at 10 examples the odds of an accidental
perfect ordering become vanishingly small. But examples aren't drawn randomly
unless deliberately shuffled — systematically working through cases tends to
produce a "happy path first, then unhappy path" ordering, which can bias the
model toward unwarranted pessimism about later cases (an ordered prompt has
made a model wrongly claim "no solution" to a puzzle that a shuffled version
of the same prompt solved, albeit still incorrectly, since the underlying
problem still needed genuine [chain-of-thought](chain-of-thought-prompting.md)
reasoning to solve).

Mitigation: shuffle or subset your examples and evaluate which selection and
ordering actually improves results, rather than assuming the order you
happened to write them in is neutral. Emerging prompt-optimization approaches
systematically select and order few-shot examples against a predefined metric
instead of leaving the choice to intuition — see
[prompt optimization tooling](prompt-optimization-tooling.md).
