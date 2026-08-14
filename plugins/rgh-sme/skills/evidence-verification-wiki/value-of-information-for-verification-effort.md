---
type: concept
title: Value of Information for Verification Effort
description: Bounding how much a verification activity is worth spending on by computing the expected value of the information it would produce, before deciding whether to run it.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Len Bass, Paul Clements, Rick Kazman), ch. 20"
---

# Value of Information for Verification Effort

Verification activities — prototyping, benchmarking, a spike, a load test — cost time and money, and it is possible to either under-invest (proceeding on an untested assumption that turns out expensive to get wrong) or over-invest (spending more on an experiment than the decision it informs could ever be worth). **Value of information (VoI)** analysis makes this an explicit calculation rather than a gut call, by estimating what the answer is worth before deciding whether to go get it.

## The core quantities

- **Expected Value of Perfect Information (EVPI)**: the most a fully definitive experiment could ever be worth — computed from your current uncertainty between the candidate options, the estimated cost of discovering later that you picked wrong, and the probability of that happening. EVPI is a hard ceiling: no experiment, however good, is worth spending more than this on, because even a perfect answer cannot save you more than the cost of the wrong choice it would have prevented.
- **Expected Value of Sample Information (EVSI)**: the realistic value of an experiment that is merely informative rather than perfect (a small benchmark, a limited prototype) — discounts EVPI by the experiment's own accuracy, since an imperfect test can itself mislead.

## Applying it to a verification decision

1. Estimate the cost of being wrong under each option under consideration (e.g., the cost to refactor away from an architecture choice that turns out unsuitable).
2. Estimate your current confidence in each option, and the accuracy you'd expect from the proposed verification activity.
3. Compute EVPI as an upper bound, then EVSI for the specific, realistically-imperfect activity being considered.
4. Compare EVSI against the activity's actual cost. Only proceed if the expected value of what you'd learn exceeds what learning it costs.

## Why this matters beyond one decision

This reframes "should we verify this before committing?" from an intuition call into a structured comparison of stakes, uncertainty, and cost — directly complementing [partial verification over unexecuted completeness](partial-verification-over-unexecuted-completeness.md): that note argues for not letting perfectionism block verification from happening at all; this technique argues for not over-spending on verification whose payoff, in expectation, is smaller than its cost. Both point at the same discipline — verification effort should be sized to the decision it serves, not maximized or skipped by default.
