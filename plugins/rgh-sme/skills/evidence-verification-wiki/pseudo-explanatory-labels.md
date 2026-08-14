---
type: concept
title: Pseudo-Explanatory Labels
description: A technical-sounding label that merely redescribes the outcome it's meant to explain, creating an illusion of explanation through circular reasoning.
sources:
  - title: "The Field Guide to Understanding 'Human Error'"
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 4"
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power (Gary Klein), ch. 6"
---
# Pseudo-Explanatory Labels

A **pseudo-explanatory label** is a technical-sounding term applied to an outcome that, on inspection, is defined entirely in terms of that same outcome — so attaching the label feels like an explanation but adds no actual information about *why* the outcome happened. The giveaway is a circular chain: *why did the failure happen? Because of [label]. How do we know [label] applied? Because the failure happened.* Two well-documented examples from incident investigation: "loss of situation awareness" (defined as an operator's understanding falling short of some external reference the investigator holds with the benefit of hindsight and outcome knowledge — so the label is really just a restatement of the gap between what the operator knew and what the investigator now knows, not a cause of that gap) and "complacency" (which requires an objectively defined optimal level of vigilance or checking to be meaningful — a standard that in practice is never actually specified, making the accusation unfalsifiable).

## Why This Matters Beyond Safety Investigations
Any domain that explains outcomes by naming a plausible-sounding construct is vulnerable to this pattern: a business failure attributed to "poor execution," a model's error attributed to "insufficient generalization," a project delay attributed to "scope creep" — each can be a pseudo-explanation if the label's only evidence is the very outcome it's supposed to explain, with no independent, checkable definition of the labeled condition. This is a specific, checkable version of the broader failure covered by [hindsight bias in review](hindsight-bias-in-review.md): a pseudo-explanatory label frequently smuggles hindsight in by defining the labeled deficiency relative to what's obvious only after the outcome is known.

## The "No One Can Win" Diagnostic for Unfalsifiable Bias Attribution
A specific version of this pattern targets *decision-making itself* after a bad outcome: a post-hoc investigation labels the decision maker's error as a named cognitive bias — "scenario fulfillment," "expectancy bias" — without independently establishing that a bias-driven distortion actually occurred, rather than a traceable factual or instrumentation error. A documented military case: investigators attributed a crew's mistaken belief that a plane was descending (it was, in fact, continuously climbing) to unconscious "scenario fulfillment" bias — but a later technical reanalysis found a mundane, traceable cause instead: a recycled tracking-system ID number had been silently reassigned to a different aircraft that genuinely was descending, and different crew members querying the same ID were unknowingly retrieving data on two different real aircraft. The bias-attribution explanation, unlike the traceable systems error, offered no way to have been wrong — a version of this label is available whichever way the incident had gone: acting on an expectation that turns out false is "expectancy bias," while ignoring the same expectation and being wrong the other way would just as easily have been labeled "ignoring the base rate." A framework flexible enough to explain literally any outcome after the fact explains nothing about this specific one.

## Verification Action
- When a document attributes an outcome to a named condition or construct, check whether that condition has an independent, checkable definition and evidence trail — established *before or apart from* the outcome — or whether the only evidence offered for the condition is the outcome it's meant to explain.
- Apply a specific circularity test: restate the explanation as "why X? because Y. How do we know Y? because X." If the chain closes on itself this way, the label is not doing explanatory work and the document needs to say what actually happened at a level of detail that doesn't depend on already knowing the outcome.
- Prefer and look for explanations that could, in principle, have been stated *before* the outcome was known — a genuine causal factor is one whose presence could have been assessed independent of hindsight.

## See Also
- [Hindsight Bias in Review](hindsight-bias-in-review.md)
- [Root Cause Fallacy](root-cause-fallacy.md)
- [Necessary, Sufficient, and Probabilistic Cause](necessary-sufficient-probabilistic-cause.md)
