---
type: concept
title: Test Fidelity Compounding
description: >
  Combining multiple low-fidelity test doubles in integration tests multiplies
  the probability of missing real defects as dependency count grows.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# Test Fidelity Compounding

Unit tests rely on mocks and fakes; each double approximates real behavior with
some error. In a chain of N dependencies, low-fidelity doubles **compound**:
two doubles each 90% faithful yield roughly 19% chance of a meaningful gap
(1 − 0.9 × 0.9) — before counting unanticipated behaviors (Hyrum's Law).

This is why [large test SUT forms](large-test-sut-forms.md) with higher
production fidelity become more **necessary** as system size grows, even though
they are more expensive to author, run, and debug. The [test automation pyramid](test-automation-pyramid.md)
still applies — many fast small tests, fewer large tests — but "smallest
possible test" at each layer: shrink SUT scope at natural seams, chain pairwise
integration tests via persisted outputs instead of one enormous end-to-end path.

Configuration fidelity matters separately — [deployment configuration testing](deployment-configuration-testing.md)
addresses outages from config pushes that unit tests cannot see.
