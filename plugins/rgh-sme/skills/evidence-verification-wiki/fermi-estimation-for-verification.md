---
type: concept
title: Fermi Estimation for Verification
description: Deriving an independent order-of-magnitude estimate from roughly-known factors to test whether a stated figure is even plausible.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 10"
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd ed. (Douglas W. Hubbard), ch. 2"
---
# Fermi Estimation for Verification

**Fermi estimation** (named for physicist Enrico Fermi's back-of-envelope reasoning) decomposes an unfamiliar quantity into a chain of factors that are each roughly known, estimated to the nearest power of ten, and multiplied together. Accepting roughly 10x margin of error is "good enough" to catch a claim that is wrong by orders of magnitude, without needing exact data.

## When to Reach for It
Use Fermi estimation whenever a claim states a large aggregate quantity (total waste produced, total people with some name, total dollars in a program) and no primary source is immediately available — it produces an independent sanity-check estimate to compare the claim against.

## Worked Examples
- A claim of "9 billion tons of plastic waste entering the ocean every year" is implausible on its face once compared against total human plastic production across *all of history* (~8 billion tons) — the true figure was 9 *million* tons/year, a thousandfold unit error.
- Estimating "how many men in a country are named John Smith": population × fraction named John × fraction of Johns surnamed Smith, chaining three roughly-known factors, lands within the right order of magnitude and is sufficient to debunk a claim inflated by more than an order of magnitude.
- A claimed causal mechanism (e.g., a specific geological event materially raising sea level) can be tested by estimating the physical volumes and areas involved and computing the resulting order of magnitude — a result many orders of magnitude too small refutes the premise without needing to argue mechanism at all.

## Reframe: "What Do You Already Know?"
Fermi's classroom exercise (estimating the number of piano tuners in a city from population, household size, ownership rate, tuning frequency, and tuner throughput) is explicitly **not itself a measurement** — no new observation is made. It is an inventory of what you already know, useful for two things beyond ballparking the answer: it counters the "we can't even begin to guess" paralysis response to an uncertain figure, and it reveals *which* sub-estimate is driving the overall range — i.e., where a real measurement would pay off most if one were commissioned. Treat a wide disagreement between a stated claim and a Fermi decomposition as a signal about where to dig, not only as a pass/fail plausibility test.

## Verification Action
Before accepting a large aggregate figure, especially one used to support an argument's conclusion, build an independent estimate from a short chain of roughly-known factors. If the estimate and the claim disagree by more than about an order of magnitude, treat the claim as suspect until traced to its primary source. See [numeric sanity checking](numeric-sanity-checking.md) for adjacent single-number plausibility checks.

## See Also
- [Numeric Sanity Checking](numeric-sanity-checking.md)
