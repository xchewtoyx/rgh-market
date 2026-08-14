---
type: concept
title: Perpetual Stability Versioning
description: >
  A versioning strategy that folds compatible changes into the current major
  version and batches breaking work into the next numbered release.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 24.3.1"
---

**Perpetual stability** (often adopted accidentally) labels existing functionality
as version N, adds [backward-compatible](backward-compatibility-policy.md) changes
in place, and builds incompatible work into version N+1 until release-worthy, then
optionally deprecates N.

Process loop:

1. Label current production "Version N."
2. Ship compatible changes into N.
3. Accumulate breaking changes in N+1.
4. Release N+1 when enough value accumulates; deprecate N if cost/usage justify.
5. Repeat.

Works when compatible change is the norm and the incompatible bar is high — most
users stay on one stable line. Poor fit for clients that must pin exact behavior
(IoT firmware) because compatible churn still lands in the active version. If the
compatibility bar is set too low, version explosion (v1…v100) follows.

Often seen on large cloud platform APIs. Pairs with explicit compatibility policy,
not a substitute for it — see [semantic versioning for APIs](semantic-versioning-api.md)
and [agile instability versioning](agile-instability-versioning.md) for alternatives.
