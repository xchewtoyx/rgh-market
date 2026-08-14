---
type: concept
title: Testing Infrastructure in Production
description: Why pre-production testing has diminishing returns as systems scale, and how observability, zero-downtime deployment, and chaos engineering make deliberately testing in production a rational complement rather than a recklessness.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 8"
---

As systems grow in complexity and scale, the share of real-world risk you can practically check for before production shrinks: production has data, users, traffic, and concurrency that simply can't be replicated outside it — a week-long soak test is trivial next to a year of real production traffic. Treating pre-release testing as if it can comprehensively cover every risk leads to over-investing in it past the point of diminishing returns, while under-investing in testing production itself.

Pre-production testing still answers real, valuable questions — the *known unknowns*: does the code run, does it fail in predictable ways, does it fail the way it's failed before. Testing in production addresses the complementary *unknown unknowns* that can only surface under real conditions. This isn't a substitute for [progressive testing](progressive-testing-for-infrastructure.md) beforehand; it's the next layer once that testing's marginal value has dropped off.

Testing in production safely depends on several supporting capabilities: monitoring and observability to detect when a test is causing harm so it can be stopped quickly; zero-downtime and progressive deployment techniques (see [zero downtime infrastructure changes](blue-green-infrastructure-change.md)) so you can expose a change to a controlled subset of traffic before committing fully; careful handling of test data so tests don't corrupt real records or leak sensitive data; and [chaos engineering](continuous-disaster-recovery.md), which deliberately injects known failure types to prove your detection and recovery mechanisms actually work. Ordinary monitoring itself can be thought of as a passive form of testing in production — not taking an action and checking the result, but watching real user activity for undesirable outcomes, which is why it belongs in the overall testing strategy rather than being treated as a separate operational concern.
