---
type: concept
title: Black-Box Claim Verification
description: Verifying a claim produced by an opaque method (statistical model, algorithm, or specialized apparatus) by checking its input data and output plausibility rather than its internal workings.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 3"
---
# Black-Box Claim Verification

A **black box**, in this sense, is any method — a statistical model, a machine-learning algorithm, specialized lab apparatus — that takes in data and produces a result while its internal workings stay opaque to non-specialist readers. Authors can build a claim's apparent authority not by being correct but by wrapping it in a black box: citing allied authors ("if you question me, you have to question the whole field"), deploying exclusionary jargon, or invoking technical apparatus so specialized that questioning it feels like "scientific heresy." A trivially dismissible claim (e.g., "cat people earn higher salaries than dog people") becomes much harder to challenge once wrapped in a plausible-sounding causal mechanism and dressed in genuine-looking statistical jargon, even though nothing about the underlying claim changed.

## The Central Method: You Don't Need to Open the Box
A reviewer rarely needs to understand a black box's internal machinery to verify what it produces. Most bullshit built on a black box comes from flawed **input data** or an unsupported leap to the **output claim** — not from the technical machinery itself, which is comparatively rare to need auditing and is the part non-specialists are least equipped to check anyway. This licenses a non-specialist reviewer to interrogate two tractable things instead:
1. **Input data**: where it came from, how it was collected or labeled, whether it's representative — see [training data provenance check](training-data-provenance-check.md).
2. **Output plausibility**: whether the result passes basic sanity checks, and whether the stated conclusion is actually the simplest explanation that fits the output — see [numeric sanity checking](numeric-sanity-checking.md) and [alternative hypothesis consideration](alternative-hypothesis-consideration.md).

## Verification Action
When a claim is defended by appeal to a specialized method, technical jargon, or "the whole field agrees" rather than by making its evidence checkable:
- Do not treat difficulty understanding the internal machinery as a reason to stop verifying — redirect scrutiny to the input data and the output claim instead.
- Be specifically wary of jargon or technical framing that seems designed to make a claim feel too authoritative to question, rather than to convey information precisely — see [mathiness detection](mathiness-detection.md) for the equivalent pattern in decorative formulas.
- Treat "no bias, no subjectivity" claims made about an automated or algorithmic method with extra skepticism — an opaque method inherits every bias present in its input data and framing, and asserting otherwise is itself a claim requiring evidence, not a property that follows automatically from being automated.

## See Also
- [Training Data Provenance Check](training-data-provenance-check.md)
- [Numeric Sanity Checking](numeric-sanity-checking.md)
- [Alternative Hypothesis Consideration](alternative-hypothesis-consideration.md)
- [Mathiness Detection](mathiness-detection.md)
