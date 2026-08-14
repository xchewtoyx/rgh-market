---
type: concept
title: Proxy Variable Leakage
description: Removing a sensitive or protected variable from a model or comparison does not eliminate its influence if other, correlated variables still leak the same signal.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 8"
---
# Proxy Variable Leakage

A claim that bias or influence from a specific variable has been eliminated "by removing it" from a model or dataset should not be accepted at face value. If other variables in the data are correlated with the removed one, they can **proxy** for it and reintroduce the same effect through a different route.

## Worked Example
An automated hiring tool was found to preferentially select men, and *persisted* in doing so even after the candidate's name and gender field were removed as inputs — because other résumé features (e.g., attendance at a women's college, membership in gender-associated organizations or hobbies) still statistically leaked the protected attribute the removal was meant to neutralize.

## Verification Action
When a draft claims a source of bias was eliminated by removing or controlling for a specific variable:
- Ask what other variables in the data are plausibly correlated with the removed one, and whether the analysis checked for their residual influence — removal of the named variable alone is not sufficient evidence of removal of its effect.
- Treat "we removed X" as a claim requiring the same evidence as any other causal claim: did outcomes actually change after removal, or only the presence of the named input?
- This is a specific case of an unaddressed [confounding variable](confounding-variables.md): the proxy plays the same role a confound would, standing in for the variable the analysis intended to control away.

## See Also
- [Confounding Variables](confounding-variables.md)
- [Shortcut Learning Verification](shortcut-learning-verification.md)
- [Construct Validity Through Multi-Item Measurement](construct-validity-through-multi-item-measurement.md)
