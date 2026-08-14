---
type: concept
title: Value of Information for Deciding What to Analyze
description: >
  A variable is worth investigating only in proportion to how
  much it could change the decision — and the variables an
  organization already tracks are usually not the ones that
  would.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything (Douglas W. Hubbard), ch. 7"
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Len Bass, Paul Clements, Rick Kazman), ch. 20"
---

The value of resolving uncertainty about some factor is not a
vague notion of "how important it feels" — it is the reduction in
**expected opportunity loss**: the cost of ending up wrong, weighted
by how likely being wrong currently is. A factor whose true value
could flip the recommended choice, and whose current range spans
that flip point, is worth real investigation. A factor whose value
cannot plausibly change what gets recommended — either because its
range never crosses a decision-relevant threshold, or because the
decision would be net-favorable even under its worst plausible
value — is worth approximately nothing, no matter how central it
feels to the topic. Information also loses value on a clock: an
answer that would arrive after the decision window closes is worth
zero, however good it eventually is (solving the right problem too
late), which argues for smaller, faster looks over waiting for a
complete one.

**The Measurement Inversion**: across many real decision analyses,
the variables an organization has historically spent the most
effort tracking are routinely the ones with close to zero remaining
value to investigate further, while the variables with the highest
actual value to a live decision are often ones nobody has measured
at all — sometimes not even named in the original business case
(a chance of outright cancellation, a risk of low adoption). This
happens because organizations gravitate toward measuring what they
already know how to measure, not what the decision actually turns
on, and because a factor already measured repeatedly in the past
has usually already had its uncertainty narrowed — mechanically
lowering its remaining information value regardless of how
important the topic sounds.

Two named quantities operationalize this for a build-vs-experiment
choice: **EVPI** (expected value of perfect information) is the most
you should ever pay for an experiment that would fully resolve the
uncertainty — a ceiling derived from the estimated cost of choosing
wrong and the current confidence in each option; **EVSI** (expected
value of sample/imperfect information) is the corresponding ceiling
for an experiment (a prototype, a pilot) that would only partially
resolve it. A team choosing between a cheaper, well-understood design
and a pricier one it has never built before can use its own estimates
of each option's cost-if-wrong and its confidence in the choice to
bound what a throwaway prototype is worth building — if the
prototype's cost sits comfortably under that ceiling, building it is
justified regardless of gut feeling about whether the team "should
just know" which design is right.

The practical implication for framing a decision document: before
commissioning more analysis on a topic, ask specifically which
uncertain factor the recommended choice is actually sensitive to,
rather than defaulting to whatever has historically been tracked or
whatever is easiest to measure. This is the same discipline
[when-comparative-analysis-is-worth-the-cost](when-comparative-analysis-is-worth-the-cost.md)
and
[zone-of-indifference-vs-zone-of-ignorance](zone-of-indifference-vs-zone-of-ignorance.md)
argue for from a different angle — all three converge on the same
point: analysis effort should track how much a specific finding
could change the decision, not how uncertain or important a topic
feels in the abstract. Establishing whether a given piece of
evidence is itself trustworthy is a separate question belonging to
evidence-verification; this is about which questions are worth
that scrutiny at all before spending it.
