---
type: concept
title: Systemic vs. Random Error in Telemetry
description: A metric can be wrong in two distinct ways — systemic error (a consistent, predictable-direction bias) or random error (unpredictable per-observation noise) — and only random error is fixed by averaging more samples; a biased metric stays biased no matter how much data you collect.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything (Douglas W. Hubbard), ch. 8"
---

Two distinct error properties matter when judging whether a telemetry source can be trusted:

- **Accuracy** (low systemic error / low bias) — the measurement isn't consistently skewed in one direction. A latency metric that always undercounts by a fixed offset (say, because it excludes TLS handshake time) is inaccurate but can still be precise.
- **Precision** (low random error) — repeated measurements of the same underlying value cluster tightly together, even if that cluster sits in the wrong place. A metric with high sampling variance but no directional bias is imprecise but can still be accurate on average.

The distinction matters operationally because the two error types respond to completely different fixes. **Random error shrinks as you collect more samples** — averaging over a longer window or a larger population cancels out unpredictable per-observation noise, which is exactly why [percentile metrics need a minimum sample count](latency-percentiles-not-averages.md) before they're trustworthy. **Systemic error does not shrink with more samples at all** — a metric that's biased low by a fixed mechanism stays biased low however long you collect it, or however many instances you aggregate across; more data just gives you a more precisely wrong number. This is the direct telemetry analog of a bathroom scale that always reads eight pounds heavy: taking the reading a thousand times and averaging doesn't fix the offset, because the error isn't random, it's structural.

The practical implication is diagnostic: when a metric looks wrong, the first question is whether the discrepancy is consistent in direction and magnitude (systemic — look for a measurement-pipeline bug, an excluded code path, a unit mismatch, a known instrumentation gap) or whether it varies unpredictably around the true value (random — look at sample size, sampling rate, or aggregation window instead). Conflating the two leads to the wrong fix: throwing more volume at a systemically biased metric wastes effort, and trying to "correct" genuinely random noise with a fixed offset just introduces a new bias. A metric with known, *quantified* systemic bias can still be useful for tracking relative change over time even if its absolute value is off — the same way a scale that's always eight pounds heavy still correctly shows an eight-pound weight gain — but this only holds if the bias is actually stable and known, not merely assumed to be.
