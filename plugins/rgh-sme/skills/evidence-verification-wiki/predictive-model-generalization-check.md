---
type: concept
title: Predictive Model Generalization Check
description: Verifying that a data-driven predictive model's demonstrated accuracy reflects durable causal structure rather than incidental correlations that will decay or self-undermine over time.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 8"
  - title: "Thinking in Systems: A Primer"
    resource: "Thinking in Systems: A Primer (Donella H. Meadows), ch. 4"
---
# Predictive Model Generalization Check

A predictive model can demonstrate strong accuracy during development and still be built on correlations that don't generalize — either because the correlations were never causally grounded, or because the very system the model depends on changes after the model is built.

## Named Case: Google Flu Trends
A 2009 paper claimed search-query patterns could "nowcast" flu outbreaks faster and more cheaply than CDC epidemiological tracking, and was held up as proof that at sufficient data scale the numbers "speak for themselves" without need for underlying theory. The method worked for roughly two years, then began missing by about 2x and continuing to worsen, until it was shut down. Two compounding root causes:
- **No causal theory behind predictor selection**: some of the search terms used were correlated with flu purely by seasonal coincidence (e.g., "high school basketball," since both peak in winter) rather than any real connection to influenza — see [curse of dimensionality overfitting risk](curse-of-dimensionality-overfitting-risk.md) for why a large pool of candidate search terms makes this likely.
- **Feedback loop / concept drift**: the search platform's own product changes (introducing search-suggest/autocomplete mid-study) altered user search behavior in ways the frozen model couldn't adapt to — the system generating the input data changed after the model was fit, and the model's own popularity likely fed back into which terms got searched at all.

## Why Fitted Correlations Are Structurally Fragile
A statistical model fit to two co-varying quantities can be a real, non-coincidental, historically robust pattern and still be a poor basis for prediction or intervention, because the two quantities may only correlate as a byproduct of both being driven by a shared underlying structure (a common stock or state variable) rather than one directly causing the other. A thermostat's heat-in and heat-out flows correlate reliably enough over time to fit an equation predicting near-term room temperature — but the fitted relationship is useless the moment someone opens a window or retunes the furnace, because the equation captured the *historical output* of the system's structure, not the structure itself. This is a distinct failure mode from an outright [spurious correlation](spurious-correlation-detection.md) found by chance: the correlation here is real and was genuinely produced by the system, but it remains valid only for as long as the system's internal structure stays constant — exactly the assumption an intervention (a policy change, a new feature, a regulatory shift) is liable to violate.

## Verification Action
When a draft cites a data-driven model's track record as evidence it will keep working going forward:
- Check whether the predictor variables have an independently plausible causal connection to the outcome, not just a historical correlation with it — see [alternative hypothesis consideration](alternative-hypothesis-consideration.md).
- Check how much time has elapsed, and what could plausibly have changed, between when the model was fit and the period the claim is being applied to — a model is evidence about the conditions it was built under, not a permanent law.
- Ask whether the model's own outputs or existence could feed back into the process generating its input data (e.g., a widely-used tool changing the behavior it measures) — a static model trained before deployment can't adapt to a feedback loop it helped create.

## See Also
- [Curse of Dimensionality Overfitting Risk](curse-of-dimensionality-overfitting-risk.md)
- [Alternative Hypothesis Consideration](alternative-hypothesis-consideration.md)
- [Correlation vs. Causation](correlation-vs-causation.md)
