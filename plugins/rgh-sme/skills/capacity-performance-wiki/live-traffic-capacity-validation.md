---
type: concept
title: Live-Traffic Capacity Validation
description: Validating that new code or infrastructure holds up under real production load — via dark launches or staged traffic ramps — rather than relying solely on synthetic pre-launch load testing, trading test-harness fidelity risk for the operational risk of testing against a live system.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 27"
---

Pre-launch [capacity testing](capacity-test-types.md) validates a system against synthetic load, which is only ever an approximation of real traffic — see [benchmarking pitfalls](benchmarking-pitfalls.md) for how easily that approximation goes wrong, and [load generator bottlenecks](load-generator-bottlenecks.md) for how the test harness itself can cap what a synthetic test can even reveal. **Live-traffic capacity validation** sidesteps both problems by exercising a new code path or piece of capacity with genuine production traffic, at controlled and increasing exposure, before it takes on the full launch load.

## Two Techniques

*   **Dark launches:** real production requests are routed to the new backend code path and processed at full scale, but the results are discarded rather than shown to the user (the user instead sees the response from the existing, already-validated path). This validates the new path's actual capacity and correctness behavior under real traffic patterns and volume, entirely decoupled from user-facing risk — a dark launch that fails or performs badly has no visible impact, because nothing it produces reaches a user.
*   **Gradual / staged rollouts:** traffic to the new path is ramped up in stages (e.g., 1% → 5% → 25% → 100%) over days or weeks using feature flags, with results now visible to the users in that stage. Each stage is a real, live capacity test at that traffic level — if the system holds up at 5%, the next stage raises exposure; if it doesn't, the flag is dialed back before the failure reaches more users.

## Why This Complements, Not Replaces, Synthetic Testing

Live-traffic validation only ever exercises the traffic pattern that's actually arriving — it cannot proactively probe a target load the system hasn't reached yet, the way [stress or breakpoint testing](capacity-test-types.md) deliberately does. It answers "does this hold up at the load we're seeing right now," not "where exactly does this break." The two are sequenced together in a launch process: synthetic testing (including stress testing to find the breaking point) validates capacity before any real traffic is at risk, and live-traffic validation confirms that the synthetic test's conclusions actually hold once real traffic — with its real skew, real request mix, and real failure modes — is the thing being served.

## Operational Requirement

Both techniques depend on being able to cut exposure back quickly if the new path shows trouble — a staged rollout is only safe if the feature flag controlling traffic percentage can be adjusted (including an immediate kill-switch back to 0%) without a binary redeploy, since a rollout that can only be reversed by a slow deploy pipeline has already done its damage by the time the reversal takes effect.
