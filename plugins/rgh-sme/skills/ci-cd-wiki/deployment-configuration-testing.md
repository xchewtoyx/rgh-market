---
type: concept
title: Deployment Configuration Testing
description: >
  Presubmit smoke tests that each deployment configuration starts healthy in an
  isolated sandbox, catching flag and config incompatibilities before deploy.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Deployment Configuration Testing

When one codebase deploys as many **configured instances** (different flags,
quotas, ACLs, feature sets), unit tests alone miss failures where servers fail
to start under a specific configuration or flags for one instance break another.

**Deployment configuration testing** spins up sandboxed mini-environments per
instance on presubmit and asserts healthy startup — essentially a
[smoke test](smoke-test.md) scoped to configuration matrices. Moving these
checks from nightly deploy to presubmit can eliminate most broken-server deploys
and cut deployment failures sharply.

End-to-end tests across instances may still run postsubmit on a slower cadence
(when security constraints forbid presubmit test accounts). Reuse the same
sandbox fixtures extended into scheduled postsubmit environments pulling
[green head](continuous-build-and-green-head.md) into a release candidate.

Treat static configuration as part of the
[release candidate](release-candidate.md) promoted with code — see
[version-control everything](version-control-everything.md). At Google,
**configuration changes are the number one cause of major outages** — faster
config rollout cycles than binaries make this gap especially dangerous without
presubmit config smoke tests.
