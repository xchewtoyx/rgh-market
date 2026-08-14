---
type: concept
title: Self-Serve Staging Load Test
description: >
  When local profiling stops predicting production performance, build a
  production-representative, self-serve load-testing capability in
  staging so a performance regression is caught before it consumes canary
  rollout budget on repeated deploy-and-rollback cycles.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Chen, Murphy, Parisa, Sculley, Underwood), ch. 15"
---

# Self-Serve Staging Load Test

[Pre-production fidelity limits](pre-production-fidelity-limits.md) can
bite performance specifically: local profiling against sampled inputs can
be predictive for a lighter workload and simply stop being predictive once
a change crosses some complexity threshold (e.g. moving from a lightweight
model to a much heavier one) — the mismatch shows up only once the change
reaches [canary](canary-release.md), by which point every failed
prediction costs a real deploy-and-rollback cycle, wasted engineering
time, and growing hesitancy to ship the next iteration.

The fix is not more sophisticated local profiling — it's giving the
people iterating on the change direct, repeated access to a
production-representative load test, so the fidelity gap is closed before
canary rather than discovered inside it. Building one well means:

- **Production-representative test data** — the input mix should reflect
  real production characteristics (e.g. a realistic distribution of input
  lengths, weighted toward the longer/heavier end that best approximates
  stress conditions), not a convenient synthetic sample.
- **Guarantee the code path under test is actually exercised** — a
  request that gets short-circuited by caching or an optimization fast
  path produces a misleadingly low latency reading; the test must force
  the real inference/serving path to run.
- **Self-serve, not routed through another team** — making the tool
  directly usable by the people making the change (rather than requiring
  a request to a separate operations team for every iteration) is what
  makes it actually get used on every iteration instead of only
  occasionally; this is what turns the load test from an occasional gate
  into a routine part of the development loop.

A useful design choice is offering more than one test mode: an
end-to-end mode that replays realistic full request traces for broad
coverage (related to, but distinct from, [capture-and-replay
validation](capture-and-replay-validation.md) — it need not be an exact
recording of past production traffic), and a narrower mode that targets
one component directly so the person iterating can hand-pick the hardest,
most stress-inducing inputs for the specific piece they're changing.

This closes the performance-fidelity gap; it doesn't replace canary. A
change still needs to pass an actual [canary](canary-release.md) in
production afterward — the staging load test's job is to make that canary
much more likely to succeed on the first attempt, by checking the same
kind of signal [canary metric selection](canary-metric-selection.md) would
already track (e.g. p95 latency against an absolute budget) earlier, and
at zero cost to real traffic.
