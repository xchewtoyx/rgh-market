---
type: concept
title: Verify Artifacts, Not Just People
description: >
  A deployment environment should require cryptographic proof that each
  pipeline step actually ran on a given artifact, rather than only checking
  who is requesting the deployment — because a trusted person can still make
  a mistake or be compromised.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
---

# Verify Artifacts, Not Just People

Controls on source, build, and test infrastructure — [mandatory code
review](mandatory-code-review.md),
[commit stage](commit-stage.md) tests, [automated acceptance
testing](automated-acceptance-testing.md) — only mean anything if a
deployment can't bypass them by deploying an artifact that never actually
went through those stages. Checking *who* is initiating a deployment isn't
enough, because even a fully trusted person can make a mistake, or their
credentials can be compromised and used by someone else. The deployment
environment should instead verify *what* is being deployed: proof that the
specific artifact in hand actually passed through the required pipeline
steps.

## What this requires

- Every automated pipeline step needs to produce evidence that it ran, tied
  to the specific artifact it ran against — see
  [binary provenance](binary-provenance.md).
- The deployment target must actually check that evidence before accepting
  an artifact, and this check must happen somewhere an attacker can't route
  around — see [deployment choke points](deployment-choke-point.md).
- Humans should not be able to bypass the automated verification, except
  through a deliberately narrow, audited exception — see
  [emergency fixes follow the same pipeline](hotfix-through-pipeline.md)'s
  breakglass discussion.

This is a stronger claim than [artifact integrity
verification](artifact-integrity-verification.md)'s tamper-detection checksum:
a checksum proves the artifact wasn't altered after being produced, but says
nothing about whether it was produced by the trusted pipeline in the first
place. Verifying artifacts closes that second gap.
