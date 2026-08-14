---
type: concept
title: Pre-Canary Artifact Smoke Test
description: >
  Before exposing any real load to a newly deployed artifact, confirm it
  is the intended version, that it loads in an exact copy of the
  production environment, and that it can serve a single minimal request
  without crashing — catching catastrophic failures at near-zero cost
  before spending canary population or time on them.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Chen, Murphy, Parisa, Sculley, Underwood), ch. 5"
---

# Pre-Canary Artifact Smoke Test

A [canary](canary-release.md) is not free — it consumes real user
requests and a slice of the release's time budget (see [canary population
and duration selection](canary-population-and-duration-selection.md)).
Whether the artifact being deployed will crash outright, or fail to load
at all, is knowable *before* any live traffic is ever sent to it, so
checking it first is strictly cheaper than discovering it in canary. Three
checks, run as a single gate immediately before the smallest canary stage:

1. **Is it the right artifact?** Verify automatically, not by manual
   process, that the version about to serve is the version actually
   intended — e.g. by checking version or build identity metadata embedded
   in the artifact itself at load time. This is easy to get wrong silently
   (a stale cached copy, a wrong path) and hard to detect any other way;
   see [deployment pipeline traceability](deployment-pipeline-traceability.md)
   and [provenance-based deployment policy](provenance-based-deployment-policy.md)
   for the pipeline-side version of the same guarantee — this check is its
   runtime counterpart, confirming what actually got loaded matches what
   the pipeline promoted.
2. **Does it load in a true copy of the production environment?** Format
   incompatibilities, missing dependencies, and size-vs-available-memory
   problems are all things a non-representative environment can hide; see
   [pre-production fidelity limits](pre-production-fidelity-limits.md) for
   why environment parity, not just "some staging environment," is what
   makes this check meaningful.
3. **Does it serve a single minimal request without crashing?** Test with
   one deliberately trivial request before sending any real volume, not a
   full battery of test cases — this isolates "does the serving path work
   at all" from "is the output correct under load," and keeps the blast
   radius and debugging surface as small as possible if it fails.

This gate is deliberately narrower than [canary measurement
validity](canary-measurement-validity.md): it asks only whether the
artifact is structurally safe to run, not whether its behavior is good —
that's what the canary stage that follows is for.
