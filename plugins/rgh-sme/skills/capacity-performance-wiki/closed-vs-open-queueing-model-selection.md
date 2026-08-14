---
type: concept
title: Closed vs. Open Queueing Model Selection
description: Whether to model a workload as a closed queueing system (a fixed population of requesters) or an open one (an unbounded external arrival stream) depends on whether the request population is actually finite, and the two model families give different predictions at the same nominal load.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), Appendix F"
---

Queueing models split into two families depending on where new requests come from:

*   **Closed model:** a fixed, finite population of $N$ requesters, each submitting one request, waiting for its response, "thinking" for a time $Z$, then submitting again — the population circulates but never grows. A load-testing rig with a fixed number of virtual users is the canonical closed system: however busy the target gets, no *new* virtual users appear.
*   **Open model:** requests arrive from an effectively unbounded external population at some arrival rate $\lambda$, independent of how quickly the system under test is responding. Real Internet-facing traffic is the canonical open system: a slow response doesn't stop new, unrelated users from arriving.

## Why the Choice Matters

The two families behave differently under overload. In a closed model, once every member of the fixed population is already waiting for a response, the arrival rate to the server *self-limits* — no member can submit a new request until their current one completes, which caps how bad things can get. In an open model, arrivals keep coming at rate $\lambda$ regardless of how backed up the system already is, so an overloaded open system's queue can grow without the built-in throttling a closed system provides. A model built on the wrong family for the workload being represented will systematically mispredict behavior near and past saturation — this is part of why [coordinated omission](coordinated-omission.md) is a problem specifically for closed-loop load generators measuring what is, in production, actually an open system.

**Selection rule:** if the request population is genuinely finite and bounded (a load-test rig, a fixed pool of backend workers making calls to a shared resource), use a closed model. If the population is effectively unbounded (public internet traffic, any workload where new requesters keep arriving independent of current system health), use an open model.

## Converting a Closed-Model Result to an Open-Model Approximation

Load-test measurements are naturally closed-model data (a fixed number of virtual users), but the production system they're meant to predict is usually open. A practical bridging technique: in a closed model, the effective arrival rate approximates $\lambda \approx N/Z$ (population size over think time). Treat think time $Z$ as a free, tunable parameter rather than a fixed measured value, and adjust it so that $N/Z$ stays constant while scaling $N$ upward in the model — at a sufficiently large $N$, the closed and open model predictions converge closely enough to use the closed-model (load-test-derived) result as a reasonable stand-in for open-model (production) behavior. This is a deliberate approximation, not an exact equivalence, and should be checked against real production measurements once available — see [live-traffic capacity validation](live-traffic-capacity-validation.md).
