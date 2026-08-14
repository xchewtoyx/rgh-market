---
type: concept
title: Correlation vs. Causation in Debugging
description: Two events starting at the same time or sharing similar symptoms don't necessarily share a root cause; investigating correlations is valuable for narrowing the search, but treating a correlation as proof of causation can send an investigation down the wrong path entirely.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 15"
---

Debuggers sometimes assume that two problems starting at the same time, or exhibiting similar symptoms, share a root cause — but mundane, unrelated problems can coincide. Some correlations are trivial and expected (rising latency causing a drop in request volume simply because users are now waiting longer) — if a team repeatedly rediscovers correlations that are trivial in hindsight, that's itself a sign of a gap in the team's understanding of how the system is supposed to work.

Despite the risk, investigating correlations — especially ones that occur at the start of an outage — is genuinely useful: thinking "X is broken, Y is broken, Z is broken, what's the common element" is a productive way to narrow a large hypothesis space. Automated correlation tooling (e.g. correlating machine-level problems with the specific tasks running on that machine) can produce faster, statistically stronger correlations than human pattern-matching alone.

The most important trap: **a deployment correlated with an outage is not automatically its cause**. In one worked example, old code performed so much worse than new code that it accidentally throttled the rest of the system; when the new, faster code deployed, other parts of the system became overloaded instead — the outage was correlated with the new deployment timing, but the deployment itself wasn't the root cause. See [change correlation in debugging](change-correlation-in-debugging.md) for the related (and usually correct) heuristic that recent changes are a good first hypothesis — this note is the caution that a correlated change still needs to be verified as causal, not just assumed.

There is an equal and opposite trap worth naming: dismissing a correlation outright with a reflexive "correlation isn't causation" throws away real evidence. A correlation between two signals that also has an independently plausible causal story (the deployment happened right before the error rate rose, *and* the deploy diff touches the exact code path that's erroring) should raise confidence in that hypothesis even before it's confirmed — it just shouldn't be treated as confirmation on its own. The two failure modes are symmetric: over-trusting a coincidental correlation, and under-trusting a genuinely informative one.
