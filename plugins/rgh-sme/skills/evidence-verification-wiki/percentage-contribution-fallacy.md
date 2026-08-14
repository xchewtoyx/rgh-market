---
type: concept
title: Percentage Contribution Fallacy
description: "\"Percent of total change\" claims can exceed 100% or go negative when the components being summed have mixed signs, producing numbers that look meaningful but aren't."
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 5"
---
# Percentage Contribution Fallacy

A claim of the form "X accounted for N% of the total change" only behaves sensibly when every component contributing to the total is moving in the same direction. When some components rise while others fall, the arithmetic can produce a contribution figure exceeding 100%, or a negative contribution, from figures that are individually correct.

## Worked Example
If one category's usage grew substantially while a competing category's usage *declined* over the same period, the growing category's raw growth alone can mathematically "explain" **more than 100%** of the total net growth — because the declining category's negative contribution had to be offset. A claim like "Wisconsin created 50 percent of the nation's job growth" can be true purely because national net job growth was tiny (many states lost jobs while others gained), making one state's modest net gain look enormous as a fraction of a near-zero total — the percentage says more about how small the denominator was than about the state's actual performance.

## Related Trap: Compounding With Mixed Signs
A value that rises 10% and then falls 10% does **not** return to its starting point — it ends up below where it started, because the second percentage is applied to a larger base than the first. Order of compounding doesn't change the final result, but naively assuming symmetric percentage changes cancel out is a common arithmetic error.

## Verification Action
Before accepting a "percent of total change" or "accounted for X%" claim, check whether every component contributing to that total moved in the same direction. If some components rose while others fell, or if the total itself was near zero, treat any single component's percentage-of-total claim as potentially misleading regardless of its arithmetic correctness, and look at the absolute figures instead.

## See Also
- [Percentage Base Ambiguity](percentage-base-ambiguity.md)
- [Numeric Sanity Checking](numeric-sanity-checking.md)
