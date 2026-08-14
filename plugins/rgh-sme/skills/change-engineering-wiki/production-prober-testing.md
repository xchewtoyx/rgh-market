---
type: concept
title: Production Prober Testing
description: >
  Continuously run the same test suite against live production to verify
  both that production works and that the tests still detect real failures.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# Production Prober Testing

Beyond [canary release](canary-release.md) and staged rollouts, the same
suite of tests (sometimes called **probers**) can run **continuously against
production itself**. **Probers** are functional tests with encoded assertions
against production — typically well-known deterministic **read-only** actions
(e.g., query a service and assert *something* returns, without asserting
full content). They are production smoke tests giving early detection of
major issues.

**Canary analysis** applies the same assertions during staged rollout:
run probers against the canary population and compare canary vs baseline
health metrics for divergence — structurally similar to other large tests
but aimed at the release decision. Probers should exist in any live system;
canary analysis whenever rollout includes a canary phase.

Limitation: failures here may already affect end users. **Mutable (write)
prober actions** risk nondeterminism, future write failures, or user-visible
side effects — prefer read-only probes in production. Consider discovery risk
if test data is user-visible (public test channels, uploaded artifacts).

This serves two purposes at once:

1. Verify the **working state of production** according to the tests —
   catching regressions that no pre-production stage modeled.
2. Verify the **relevance of the tests** — if production behavior drifts
   but tests still pass, the suite has gone stale.

This is layered **defense in depth** alongside [presubmit vs postsubmit
test gating](presubmit-vs-postsubmit-test-gating.md), [release candidate
regression testing](release-candidate-regression-testing.md), and
[pre-production fidelity limits](pre-production-fidelity-limits.md): no
single stage alone carries full quality assurance. Probers are a form of
[testing in production](canary-release.md) with ongoing, synthetic traffic
rather than a one-time rollout gate.

Presubmit system-under-test composition should generally **not** talk to
real production backends (security and quota risk); staging often can.
Production probers close the loop only after deploy.

Running the **same suite** against both post-submit CI (new binaries, live
backends) and production is a cheap way to **isolate failures**: if a test
already fails in production, a CI failure may be unrelated to the team's
recent change; if it passes in prod but fails in CI, the regression likely
lies in the candidate build. Manual comparison is expensive at scale —
hermetic record/replay in CI is one path to stabilize the post-submit side.
