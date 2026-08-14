---
type: concept
title: Conditional Probability Inversion
description: The reasoning error of treating the probability of evidence given a hypothesis as if it were the probability of the hypothesis given the evidence.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 9"
---
# Conditional Probability Inversion

A recurring statistical reasoning error is confusing **P(evidence | hypothesis)** — the probability of seeing this data if the hypothesis is true — with **P(hypothesis | evidence)** — the probability the hypothesis is actually true given the data. These are not the same number, and the gap between them depends on the *prior* plausibility of the hypothesis, which the evidence's own error rate cannot supply.

## Worked Example: The Prosecutor's Fallacy
A fingerprint-match test has a tiny false-positive rate (1 in 10 million). A prosecutor argues this means a matched defendant is almost certainly guilty. But if the fingerprint was searched against a 50-million-person database, roughly 5 innocent people are expected to match purely by chance, against perhaps 1 true guilty match — so a random match actually carries close to a 5-in-6 chance of pointing at an innocent person. The test's own accuracy (P(match | innocent) is tiny) says nothing on its own about P(innocent | match), which depends on how large the population searched was.

## Verification Action
When a document cites a test's error rate, a match probability, or a p-value as if it directly states the probability that a claim/hypothesis is true, check whether the actual quantity being reported is really the *reverse* conditional. Ask what population or hypothesis space was searched, and whether the document accounts for it — a small stated error rate can still mean the reported match or result is very likely a false positive once that context is included.

## See Also
- [P-Value Misinterpretation](p-value-misinterpretation.md)
- [Base Rate Fallacy](base-rate-fallacy.md)
