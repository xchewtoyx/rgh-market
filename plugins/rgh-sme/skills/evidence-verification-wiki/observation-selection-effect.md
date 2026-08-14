---
type: concept
title: Observation Selection Effect
description: When the act of observing something is itself correlated with the state being measured, making a routine or unbiased process feel systematically unlucky.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 6"
---
# Observation Selection Effect

An **observation selection effect** occurs when the moment or method of observation is itself statistically correlated with the quantity being measured, so a genuinely unbiased or evenly-distributed process produces a systematically skewed experience for the observer.

## Worked Examples
- **Irregular-interval waiting time**: if arrivals happen on average every N minutes but at irregular intervals, an observer arriving at a random moment is more likely to land inside one of the longer gaps than one of the shorter ones — so the *average experienced wait* is longer than half the average interval, even though the process's true average interval hasn't changed. This isn't bad luck; it's a structural consequence of random arrival landing more often in longer intervals.
- **Density-weighted lane/queue occupancy**: when parallel channels process at different effective rates, the slower channel is typically more densely packed (items follow more closely together) than the faster one, so at any given instant a larger fraction of total items are physically located in the slower channel — producing the common feeling of consistently picking the slower option, even when channel assignment is actually random.

## Verification Action
When a draft or an anecdote reports a pattern that "always" seems to disadvantage the observer (always the slow line, always the long wait, always the smaller share), check whether the observation process itself is structurally more likely to sample the less favorable state, before concluding the underlying process is actually biased or unfair. This failure mode looks like bad luck but is fully explained by sampling mechanics, requiring no unfairness or bias in the underlying system at all.

## See Also
- [Selection Bias](selection-bias.md)
- [Size-Biased Sampling](size-biased-sampling.md)
