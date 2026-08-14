---
type: concept
title: Production Behavior Cannot Be Fully Simulated in Staging
description: Even a dedicated test/staging environment structurally can't stand in for production observability, because serving architectures vary too widely to replicate faithfully, dev-time access to a model or service is looser than production allows, and test-time data is never distributed exactly like live traffic.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 9"
---

A recurring argument for why pre-production testing can reduce, but never replace, the need for production [observability](observability-definition.md): staging environments are structurally unable to fully stand in for production, for three separate reasons.

1. **Serving architectures are too varied to replicate faithfully.** Real deployments span model pools, shared library versions, edge devices, and other infrastructure variations that a single staging setup can't reproduce all at once.
2. **Development-time access is looser than production allows.** During development, code typically invokes prediction or business logic directly, with little intervening code, for iteration speed. Production restricts arbitrary manipulation of inputs, logging, and processing paths — which is good for safety, but means a bug that's trivial to reproduce in dev can become genuinely hard to reproduce once the same code is running under production's tighter constraints.
3. **Test-time data is never distributed like production data.** This matters most for ML specifically, where the data distribution itself is part of what determines correctness — but it holds more generally too: synthetic or sampled test traffic reliably fails to reproduce the full shape (skew, rare combinations, adversarial inputs) of what a system sees in the wild.

The practical conclusion is not "testing doesn't matter" — it's that testing and production observability are answering different questions, and neither substitutes for the other: testing verifies behavior against known, chosen scenarios, while production observability is what catches the scenarios nobody chose to test for. This is the same underlying gap that [known-unknowns vs. unknown-unknowns](known-unknowns-vs-unknown-unknowns.md) describes for debugging generally, applied specifically to the dev-vs-prod boundary.
