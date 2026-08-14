---
type: concept
title: Bayesian Estimation of SLI Values from Small Samples
description: The naive point estimate for a success-ratio SLI (successes/total) can be noisy or misleading over a short window; Bayesian estimation with an explicit prior gives a more honest picture, provided the prior itself is not so strong it masks a real outage.
sources:
  - title: "Implementing Service Level Objectives"
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 9"
---

The default way to compute a success-ratio SLI — successes divided by total events — is **maximum likelihood estimation (MLE)**: `p_hat = successes / total`. It is the natural estimator for a Bernoulli/binomial process, and more data produces a sharper, more trustworthy estimate.

MLE has a weak spot over short or low-traffic windows: with few events, `p_hat` swings wildly and a single failure can look catastrophic (or a single early success can look like everything is fine). **Maximum a posteriori (MAP) estimation** addresses this by folding in a prior belief about the system's reliability via Bayes' theorem, so a small number of new observations nudges an existing belief rather than fully defining it from scratch. MLE is the special case of MAP where the prior is uninformative (uniform).

A prior can be injected either by extending the measurement window, or — more explicitly — by adding artificial "prior" success/failure counts to the real data before computing the ratio.

**Pitfall — an overconfident prior can hide a real outage.** Encoding "the system is 99.9% reliable" as a prior of 999 successes + 1 failure barely moves even after a genuine outage starts producing real failures, because the artificial data swamps the real signal. Fix: use a **mixture prior** — a weighted blend of "system healthy" and "system down" beliefs — so the posterior can flip sharply once enough real failures accumulate, instead of being permanently anchored near the prior's assumed reliability.

For judging how much to trust a given SLI value rather than just producing a point estimate, full Bayesian inference computes the entire posterior distribution and reports a **highest density interval (HDI)** — the region containing, e.g., 95% of the posterior probability mass. This is a **credible interval**, not a frequentist confidence interval, and the two have different meanings: a credible interval says "there's a 95% chance the true success rate is in this range," whereas a confidence interval says "95% of intervals built this way would contain the true rate." More data narrows the HDI even when the point estimate itself doesn't move, which is a useful signal for whether an SLI computed over a short window (e.g. a brief alerting lookback) is trustworthy or still too noisy to act on.

**Practical takeaway:** elaborate Bayesian alerting models can themselves become a source of fragility — a simple hardcoded threshold can outperform a poorly-tuned prior until enough real operational data exists to calibrate it properly. Treat Bayesian SLI estimation as a tool for judging estimate confidence over sparse windows, not a default replacement for straightforward ratio math once traffic volume is adequate. When no defensible prior exists at all, [the Rule of Five](rule-of-five-for-small-sample-confidence.md) gives a cheaper, prior-free fallback: it bounds the plausible range of a small sample without needing a stated belief about the system's reliability.
