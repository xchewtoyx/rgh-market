---
type: concept
title: Swiss Cheese Testing Model
description: >
  Design a pipeline's test stages by asking where each risk gets caught
  across the whole pipeline, not by forcing every stage to fit a fixed
  layer-by-layer formula — any single stage can have gaps as long as no gap
  lines up across every stage.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code, 2nd ed. (Kief Morris), ch. 8"
---

# Swiss Cheese Testing Model

Borrowed from risk management outside software: a single slice of Swiss
cheese has holes, but stack several slices together and — as long as the
holes don't all line up — nothing gets all the way through. Applied to a
[deployment pipeline](deployment-pipeline.md)'s test stages, no individual
stage needs to catch every risk on its own. A stage that only tests one
component in isolation, or only tests against a mocked dependency, has real
gaps — but that's fine as long as some other stage covers exactly what that
gap misses.

This reframes how to design pipeline stages: rather than asking "does this
stage fit the [test pyramid](test-automation-pyramid.md)'s expected
layer," ask "where in the whole pipeline does this specific risk actually
get caught?" Catch it as early as feasible — earlier stages are cheaper to
fail in and give faster feedback — but the binding requirement is that it's
caught *somewhere*, not that every stage individually be comprehensive. This
is a risk-based way to decide how many pipeline stages to have and what each
one should check, as an alternative to mechanically replicating a fixed
testing-layer formula for every codebase regardless of what it actually
needs.
