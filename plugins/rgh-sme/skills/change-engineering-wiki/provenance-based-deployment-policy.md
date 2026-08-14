---
type: concept
title: Provenance-Based Deployment Policy
description: >
  Deployment environments should verify what artifact is being deployed and
  how it was built, not just who initiated the deployment, by evaluating
  machine-checkable build provenance against an explicit policy.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
---

# Provenance-Based Deployment Policy

Verifying *who* triggered a deployment is not sufficient release gating: the
actor may be well-intentioned but wrong (deploying from an unreviewed local
branch) or their credentials may be compromised. A stronger gate verifies
*what* is being deployed — the artifact's build provenance (source
repository, commit, whether it passed CI, which build system produced it) —
against an explicit deployment policy attached to each environment, such as
"only images built by the CI pipeline from the approved source repository
with passing tests may deploy to production."

This generalizes [segregation of duties via pipeline audit trail](segregation-of-duties-via-pipeline-audit-trail.md):
instead of trusting that the pipeline is the only path to production
(architectural enforcement), a provenance-based policy makes that assumption
explicit and machine-checkable at deploy time, so it survives even if some
other path to the environment exists. Enforcement should happen at a single
**deployment choke point** — the one place all deployment requests are
required to flow through (e.g. a Kubernetes admission controller, or a
proxy in front of the production API) — since a policy check anywhere else
can be bypassed by talking to the environment directly.

Because policy decision systems and their dependencies can themselves fail
or be unavailable, deployment gates built this way need the same fail-open
versus fail-closed tradeoff analysis as other [safe configuration change
properties](safe-configuration-change-properties.md), plus an audited
[emergency change breakglass](emergency-change-breakglass.md) path for when
a legitimate deployment must proceed despite the policy engine being down.
