---
type: concept
title: Selection Bias
description: When the sampled individuals or cases differ systematically from the population a claim is about, with respect to the exact thing being measured.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 6"
---
# Selection Bias

**Selection bias** occurs when the individuals or cases actually sampled differ systematically from the population a claim is about, specifically with respect to the variable being measured. The organizing question for spotting it is: *what you see depends on where you look* — the same underlying reality can appear to say opposite things depending on who or what ended up in the sample.

## The Sample Only Needs to Be Random for the Question Asked
A sample doesn't need to be globally representative to be valid — it needs to be unbiased with respect to the specific question being asked. A sampling method that would be a poor general-population sample can still be perfectly valid for a narrower question, if the thing that makes the sample skewed doesn't correlate with the variable being measured.

## Common Self-Selection Patterns
- **Self-selection into the visible sample**: a claim about "how people talk about X" drawn from one platform can look completely different from the same claim drawn from another platform, not because reality differs, but because different platforms attract self-selected behavior (people boast in one context and vent or seek help in another).
- **Self-selection on the outcome itself**: surveying only the people currently present to be surveyed can bias a measurement of exactly the behavior that determines presence (e.g., asking currently-attending students how often they skip class will understate typical absence, because frequent skippers are systematically less likely to be in the room to answer).
- **Self-selection into an advertised benefit**: a claim that "everyone who does X saves money" can be true for every individual claim in a batch of testimonials while remaining true only because the people who wouldn't benefit never bothered to do X in the first place — the sample of people making the claim is not the full relevant population.
- **A variable that looks predictive but is actually a downstream consequence**: a correlation between two collected fields can arise because one field is only *collected* once the outcome has already occurred, making it look predictive when it's actually a byproduct of the outcome.

## Verification Action
When a draft cites a measurement, ask what determined who or what ended up in the sample, and whether that selection process is independent of the specific thing being measured. If the selection process is *not* independent of the measured variable, the sample cannot be treated as representative of the broader population the claim is about, no matter how large the sample is.

## See Also
- [Sampling and Measurement Bias](sampling-and-measurement-bias.md)
- [Berkson's Paradox](berksons-paradox.md)
- [Size-Biased Sampling](size-biased-sampling.md)
- [Data Censoring](data-censoring.md)
- [Survivorship Bias](survivorship-bias.md)
