---
type: concept
title: Record Replay Dependency Isolation
description: >
  Record real dependency traffic on post-submit, replay it hermetically on
  presubmit to test against external services without live calls or shared
  staging.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# Record Replay Dependency Isolation

Third-party and upstream dependencies are natural seams to shrink the SUT:
automated tests generally should not hit real third-party APIs (cost, quota,
lack of shared test environments). Consumer-driven contract testing is one
external pattern; Google's approach uses **record mode** and **replay mode**:

- **Record mode** — a larger test runs continuously on post-submit, sending
  real traffic to external services and recording requests/responses (must
  pass for logs to generate).
- **Replay mode** — a smaller test used in development and presubmit plays
  back recorded traffic hermetically.

Because of nondeterminism, replay matches requests with matchers (like mock
argument matching) to select a response. If client behavior changes so no
recorded request matches, replay fails and the engineer must rerun record
mode to regenerate traffic — so record-mode tests must stay easy, fast, and
stable.

This complements [capture-and-replay validation](capture-and-replay-validation.md)
(record once, replay many for offline validation) and supports [SUT
hermeticity vs fidelity](sut-hermeticity-vs-fidelity.md): replay shrinks the
SUT onto one machine while preserving realistic dependency interaction
shapes for [presubmit vs postsubmit test gating](presubmit-vs-postsubmit-test-gating.md).
