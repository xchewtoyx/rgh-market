---
type: concept
title: Outcome-Blind Decision Review
description: >
  Evaluate the reasoning behind a decision before revealing how
  it turned out, so the review judges the process instead of
  reverse-engineering a justification for the known result.
sources:
  - title: "Thinking in Bets: Making Smarter Decisions When You Don't Have All the Facts"
    resource: "Thinking in Bets (Annie Duke), ch. 5"
---

Knowing how something turned out changes how people evaluate the
reasoning that led to it, even when they are trying hard to be
objective — researchers analyzing their own physics data show
measurable bias toward confirming the hypothesis they already
believe, which is why fields from particle physics to cosmology
increasingly mask outcomes from the people doing the analysis. The
same distortion applies directly to reviewing a past decision: a
reviewer who already knows the result is not really assessing
"was this reasoning sound" but "does this reasoning justify what I
already know happened" — a different and much easier question that
produces a falsely tidy verdict in both directions, harsh on
good decisions that had bad luck and lenient on bad decisions that
got away with it.

The countermeasure is to describe the decision — the situation,
the options considered, the reasoning applied — without disclosing
the outcome or the presenter's own belief about whether it was
right, and have reviewers assess the reasoning on those terms
alone. This can feel artificial (people used to hearing "how did it
turn out?" find its withholding disorienting), but the discomfort
is the mechanism working: it forces the evaluation to rest on
information that was actually available at decision time, which is
the only fair basis for judging the decision itself (see
[decision-quality-independent-of-outcome](decision-quality-independent-of-outcome.md)).

This is a concrete implementation of
[unfalsifiable-bias-framing](unfalsifiable-bias-framing.md)'s
warning taken to its practical extreme: if a reviewer never learns
the outcome until after judging the reasoning, they cannot
construct a bias explanation that only fits in hindsight, because
hindsight is exactly what's being withheld.
