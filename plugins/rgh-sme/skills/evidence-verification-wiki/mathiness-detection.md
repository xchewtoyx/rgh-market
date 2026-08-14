---
type: concept
title: Mathiness Detection
description: Identifying formulas that look mathematically rigorous while the specific arithmetic operations they use aren't actually justified by anything.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 5"
---
# Mathiness Detection

**Mathiness** is a formula or equation that looks and feels mathematically rigorous while disregarding logical coherence — an analogue to "truthiness" applied to quantitative claims. A formula can combine real, meaningful variables using an arithmetic structure (which terms are added vs. multiplied, what's in the numerator vs. the denominator) that isn't actually justified by anything beyond looking formula-shaped.

## Two Diagnostic Tests
1. **Dimensional analysis**: do the units make sense? Quantities in different units can't be validly added or subtracted, and exponents on a dimensioned quantity must themselves be dimensionless. A formula that subtracts "debt" from "weather," or raises "time since a date" to a power, fails this test outright.
2. **Functional-form justification**: is the specific structure (sum vs. product, which variable is in the numerator, which is in the denominator) actually derived from or justified by anything, or could an entirely different formula equally represent the same qualitative "more of X leads to more of Y" relationship? A formula that only conveys sign-of-relationship information is often better expressed as a simple table of directional effects than as a spurious equation. Test the formula against an extreme or edge-case input (e.g., what does the formula predict as one term approaches zero?) — an absurd result at the edge case is a sign the functional form has no real justification.

## Verification Action
When a draft presents a claim backed by a named formula or equation combining several factors, apply both tests before accepting the formula's implied precision: check the units, and check whether the specific arithmetic structure is justified rather than arbitrary. A formula failing either test should be treated as decorative rather than as quantitative evidence, regardless of how confidently it's presented.

## See Also
- [Numeric Sanity Checking](numeric-sanity-checking.md)
- [Claim Scope Calibration](claim-scope-calibration.md)
