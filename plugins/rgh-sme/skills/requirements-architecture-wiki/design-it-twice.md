---
type: concept
title: Design It Twice
description: >
  Deliberately sketching a second, radically different candidate design
  before committing to the first idea — even a weak one — surfaces what
  actually makes either alternative good or bad.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 11"
---

A first-draft design is rarely the best one, and the discipline for
catching that is simple to state and easy to skip under time pressure:
for each significant design decision, sketch more than one candidate
before committing. The candidates should be **radically different** from
each other, not minor variations — comparing two nearly-identical options
teaches little, while comparing genuinely different approaches (worked
example: a text-storage interface sketched as line-oriented,
character-oriented, and range-oriented) exposes trade-offs that a single
design never surfaces at all. Even when one option feels obviously right,
sketching a second, deliberately weaker one and articulating specifically
why it's worse sharpens the case for the first far more than simply
asserting it.

Evaluate candidates primarily on how easy each one is for the code that
will actually use it, then on secondary questions: is one simpler, more
general-purpose, or more efficient to implement than the others? Often
the best result isn't picking one candidate outright but noticing a
shared weakness across all of them (in the worked example, both initial
interfaces forced extra work onto every caller) and using that specific
weakness as the design driver for a new, better candidate.

This generalizes across levels: apply it once to choose a module's
interface and again, separately, to choose its implementation — the
evaluation criteria differ at each level (interface comparisons favor
ease of use and generality; implementation comparisons favor simplicity
and performance) — and it applies well above the module level too, to
choosing between whole system decompositions or major UI approaches. The
cost is genuinely cheap relative to the payoff: an hour or two of
comparative sketching against days or weeks of implementation, which is
why it belongs in the same category as [documenting
trade-offs](documenting-trade-offs.md) and [design concept
selection](design-concept-selection.md) as a low-cost way to make a design
decision's rationale defensible before it's locked in, rather than only
after something has gone wrong with it.
