---
type: concept
title: Confounding Variables
description: A third, often unmeasured factor that independently causes both halves of an observed association, making the two look causally linked when they aren't.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 4"
  - title: "Data Science from Scratch, 2nd Edition"
    resource: "Data Science from Scratch, 2nd ed. (Joel Grus), ch. 5"
---
# Confounding Variables

A **confounding variable** (common cause) is a third factor that independently drives both halves of an observed association, so the two observed variables end up correlated with each other even though neither directly causes the other. Diagrammed as two arrows pointing outward from a shared upstream cause, rather than a direct arrow between the two observed variables — see [correlation vs. causation](correlation-vs-causation.md).

## Worked Example: The Marshmallow Test
Early studies found that a child's ability to delay gratification at age four correlated with later academic success, and popular coverage converted this into prescriptive self-help advice about training delayed gratification. A larger, better-controlled replication found only a fraction of the original effect, and identified **parental socioeconomic status** as a common cause driving both the child's ability to delay gratification and the child's later academic outcomes — once that confound was accounted for, the direct link between the two observed variables largely disappeared.

## Worked Example: Aggregate Geography Masks Degree Mix
A higher average friend count on one coast than another looked like a regional effect until users were split by PhD status — within each degree bucket the other coast had more friends, and the aggregate difference was explained by different PhD/non-PhD composition between coasts. This is [Simpson's paradox](simpsons-paradox.md): the confound lived in who populated each group, not in an inherent regional trait.

## Verification Action
When a draft attributes an outcome to a specific factor based on an observed correlation, check whether the study or data controlled for plausible confounders — especially factors known to broadly influence many outcomes at once (socioeconomic status, age, general health, institutional resources). A correlation that survives adjustment for major known confounders is stronger evidence than one that hasn't been checked against them at all.

## See Also
- [Correlation vs. Causation](correlation-vs-causation.md)
- [Experimental vs. Observational Causal Evidence](experimental-vs-observational-causal-evidence.md)
- [Shortcut Learning Verification](shortcut-learning-verification.md)
- [Proxy Variable Leakage](proxy-variable-leakage.md)
