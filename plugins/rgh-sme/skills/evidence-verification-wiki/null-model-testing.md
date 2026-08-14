---
type: concept
title: Null Model Testing
description: Building a deliberately boring simulation with no real effect to check whether an observed pattern could arise without the mechanism being claimed.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 11"
---
# Null Model Testing

A **null model** is a simplified, deliberately "nothing interesting is happening" simulation used to check whether an observed pattern in data could plausibly arise *without* the causal mechanism a claim attributes it to. The null model does not need to be realistic — its only job is to show that a competing, boring explanation produces the same observed pattern, which is enough to strip the original claim of its evidentiary force.

## Worked Example
A chart of world-record running speeds by age of record-holder shows a downward slope with age, apparently illustrating age-related physical decline. But a purely statistical alternative explanation exists: far more people compete in their 20s–30s than in their 70s–80s, and the fastest time within a larger sample is expected to be faster than the fastest time within a smaller sample, regardless of any true underlying age effect (this specifically affects extremes/records, not simple averages, where sample size wouldn't matter). Simulating a world where age has *no* effect on speed, and only the sample size per age group varies to match the real competition data, reproduced the same downward-sloping pattern. The original graph, while still consistent with a real decline effect, provides no actual evidence for one, since an null-of-effect world produces an identical-looking chart.

## Verification Action
When a draft attributes an observed pattern to a specific mechanism, check whether a simpler statistical or structural explanation — sampling artifacts, selection effects, or pure chance — could produce the same pattern with no real effect present. Where feasible, simulate that boring alternative explicitly rather than asserting it's implausible; a null model that reproduces the pattern is strong grounds to treat the original claim as unsupported, not just unconfirmed.

## See Also
- [Spurious Correlation Detection](spurious-correlation-detection.md)
- [Base Rate Fallacy](base-rate-fallacy.md)
