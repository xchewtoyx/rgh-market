---
type: concept
title: Provenance-Based Deployment Policy
description: >
  Gating deployment on explicit, per-environment rules evaluated against an
  artifact's binary provenance — e.g. "built by the official pipeline from an
  approved repository, with tests passing" — rather than on a single
  all-or-nothing signature.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
---

# Provenance-Based Deployment Policy

A pure signature check ("does this artifact have any valid signature from our
build system?") answers only one question. A deployment policy checked
against [binary provenance](binary-provenance.md) can answer much richer,
environment-specific questions with a single signing key per build step
rather than a separate key per environment: which source repository the
build came from, whether it passed the required tests, whether a recent
vulnerability scan came back clean, whether the artifact is explicitly
approved for *this* environment (e.g. rejecting a "test" build in
production).

Example rules:

- Source was submitted to version control and peer reviewed.
- Source came from a specific, approved repository and build target.
- Build ran through the official pipeline (see
  [verifiable builds](verifiable-builds.md)).
- The required test gates passed.
- The artifact is explicitly allowed for this deployment environment.
- The code or build is recent enough, and free of known vulnerabilities per a
  sufficiently recent scan.

## Evaluating a policy

Checking a deployment against a policy has three distinct steps: verify the
provenance itself is authentic (correctly signed); verify the provenance
actually applies to *this* artifact (its recorded hash matches); verify the
provenance satisfies every policy rule. Skipping any one of the three leaves
a gap — a valid signature on provenance that doesn't match the artifact in
hand is as useless as no signature at all.

## Practical design lessons

- **Keep the policy unambiguous**: design the system so exactly one policy
  applies to any given deployment, rather than needing to resolve what
  happens when two policies could apply. A global requirement can still be
  expressed as a meta-policy that every individual policy must satisfy.
- **Give actionable rejections**: a rejected deployment should say
  specifically what failed and how to fix it (e.g. "source URI was X, policy
  requires Y") rather than a bare "does not meet policy" — a policy language
  that can't produce specific failure messages is a warning sign worth
  catching early in the design, not living with.
- **Verify after deployment too, not only at deployment time**: policies
  change and need re-evaluating against artifacts already deployed under an
  older policy; a decision service might have failed open during an outage;
  someone may have used an emergency breakglass; and investigators may need
  the record later for forensics. This means the enforcement point must log
  enough detail — the full request plus any state the policy depended on —
  to re-evaluate the decision after the fact.

See [emergency fixes follow the same pipeline](hotfix-through-pipeline.md)
for how a deliberate, audited breakglass exception fits into a system that
otherwise enforces this policy strictly.
