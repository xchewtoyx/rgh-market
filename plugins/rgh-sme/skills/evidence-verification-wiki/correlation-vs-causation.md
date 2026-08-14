---
type: concept
title: Correlation vs. Causation
description: Why an observed association between two variables does not by itself establish which one causes the other, or that either causes anything at all.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 4"
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd ed. (Douglas W. Hubbard), ch. 9"
  - title: "Data Science from Scratch, 2nd Edition"
    resource: "Data Science from Scratch, 2nd ed. (Joel Grus), ch. 5"
---
# Correlation vs. Causation

An **association** between two variables X and Y (knowing one tells you something about the other) is compatible with at least four distinct explanations, and the data alone cannot distinguish between them without further evidence:
1. X causes Y.
2. Y causes X.
3. A third factor causes both (see [confounding variables](confounding-variables.md)).
4. The association is coincidental or an artifact of the data (see [spurious correlation detection](spurious-correlation-detection.md)).

Multiple concrete causal stories can fit the same correlation — e.g., more friends causing more time on site, more time on site causing more friends, or a shared passion driving both independently. [Randomized trials](experimental-vs-observational-causal-evidence.md) are one way to break the tie: randomly assign different experiences to comparable groups and attribute outcome differences to the assigned change rather than pre-existing differences.

A document that observes an association and reports it as if only one of these four explanations were true, without ruling out the others, is making an unsupported causal leap.

## One Hard Constraint
**Causation flows only forward in time**: if A precedes B, B cannot be the cause of A. This constraint can rule out one of the four explanations above, but it never proves causation on its own — it only eliminates reverse causation as a candidate.

## Named Fallacy: Post Hoc Ergo Propter Hoc
"After this, therefore because of it" — assuming that because event A preceded event B, A caused B. Temporal sequence is *necessary* for causation but nowhere near *sufficient*: two unrelated events that happen to occur in sequence look identical, from a pure timeline reading, to a real cause-and-effect pair. Even eminent researchers have proposed physiologically serious but ultimately wrong reverse-causal stories (e.g., disease symptoms causing a habit, rather than the habit causing the disease) — illustrating that ruling out reverse causation from first principles, without further evidence, is genuinely hard even for experts.

## The Opposite Error: Dismissing Correlation Entirely
The reflexive rejoinder "correlation isn't causation," used to wave away an association with no further analysis, is itself a distinct error — described by one source as arguably the more common of the two biggest mistakes in interpreting correlation. Correlation is not proof of causation, but it *is* legitimate Bayesian evidence for it once combined with an independently plausible causal mechanism: the absence of any correlation makes a causal claim less likely, and the presence of correlation, alongside a plausible mechanism, should genuinely raise confidence even though it doesn't settle the question. Treating "correlation isn't causation" as a complete rebuttal throws away real evidentiary weight exactly as readily as the opposite error (treating correlation as proof) manufactures evidentiary weight that isn't there.

## Verification Action
When a draft reports an association, check explicitly which of the four explanations the underlying evidence actually supports. When a draft (or a reviewer) instead dismisses a correlation outright with no further discussion, check whether an independently plausible causal mechanism is also present — if so, the correlation should be weighed as partial supporting evidence, not discarded. If the evidence is observational (not from a controlled manipulation — see [experimental vs. observational causal evidence](experimental-vs-observational-causal-evidence.md)), the document should not assert a single causal direction without either ruling out the alternatives or hedging the claim to match — see [causal language calibration](causal-language-calibration.md).

## See Also
- [Confounding Variables](confounding-variables.md)
- [Spurious Correlation Detection](spurious-correlation-detection.md)
- [Causal Language Calibration](causal-language-calibration.md)
- [Experimental vs. Observational Causal Evidence](experimental-vs-observational-causal-evidence.md)
- [Necessary, Sufficient, and Probabilistic Cause](necessary-sufficient-probabilistic-cause.md)
