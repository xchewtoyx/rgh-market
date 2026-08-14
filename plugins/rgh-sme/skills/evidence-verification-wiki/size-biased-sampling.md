---
type: concept
title: Size-Biased Sampling
description: When a quantity is measured by counting units (classes, groups, hosts) instead of the members within them, small units are structurally over-represented relative to what most members actually experience.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 6"
---
# Size-Biased Sampling

Averaging over *units* (families, classes, servers, groups) versus averaging over the *members* of those units (children, students, requests, individuals) can produce sharply different — and both individually correct — answers to what looks like the same question, because larger units contain proportionally more members.

## Worked Example: Class-Size Paradox
The mean class size, weighted by number of *classes*, can be much smaller than the "experienced" mean class size, weighted by number of *students* — because a few large classes disproportionately affect more students than their count as "one class" suggests. A ranking system that rewards the fraction of small classes (rather than the experienced mean class size most students actually sit in) creates a [Goodhart's Law](goodharts-law.md)-style incentive: an institution can improve its score by packing more students into fewer, larger classes while keeping a technically-high count of small classes, making the typical student's actual experience worse even as the reported metric improves.

## Named Instance: The Friendship Paradox
On average, most people have fewer friends (or followers, or connections) than their friends do — because highly-connected individuals appear disproportionately often in *other people's* friend lists, inflating the observed average from any one person's point of view. This is the same size-biased mechanism applied to a social network: a person's friend list is a sample biased toward well-connected people, not a random sample of the population.

## Verification Action
When a draft reports an average computed over units (classes, servers, teams, releases), check whether the claim is actually about the units themselves or about the experience of the members within them. If it's about member experience, recompute the average weighted by member count, not unit count — the two can diverge substantially whenever unit sizes vary widely.

## See Also
- [Selection Bias](selection-bias.md)
- [Goodhart's Law](goodharts-law.md)
- [Mean vs. Median Selection](mean-vs-median-selection.md)
