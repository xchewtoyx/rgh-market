---
type: concept
title: Configuration Startup Presubmit Test
description: >
  Sandbox per-deployment-instance configuration on presubmit and verify
  every server starts healthy before merge, catching config incompatibilities
  unit tests miss.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# Configuration Startup Presubmit Test

When one binary serves many customized instances — shared code, different
flags, quotas, auth, and ACL rules — configuration complexity causes
failures unit tests miss: a flag for one instance breaks another, or
servers fail to start under an incompatible config combination. Engineers
may only discover this at deploy time if each instance isn't exercised
before merge.

This is the **deployment configuration testing** pattern in large-test
catalogs: SUT hermetic or cloud-isolated, no seeded traffic data,
verification by assertion that the process starts successfully against its
config files — a smoke test at the configuration layer.

**Temporary sandboxed mini-environments per instance**, run on presubmit,
that assert all servers are healthy on startup, catch the majority of
broken configuration before it reaches shared environments. In the Google
Takeout case, this cut broken servers from bad configuration by ~95% and
nightly deployment failures by ~50%.

End-to-end tests that need production-like accounts or backends may still
belong on post-submit on a faster cadence (e.g., every two hours from
[green head](green-head-vs-true-head.md)) rather than presubmit — see
[pre-production fidelity limits](pre-production-fidelity-limits.md). Pair
startup checks with [safe configuration change
properties](safe-configuration-change-properties.md) and promoting config
in the [release candidate](build-once-promote-artifact.md).
