---
type: concept
title: Artifact Integrity Verification
description: >
  Every binary artifact should get a cryptographic hash at build time that is
  re-checked at deploy time, so tampering or accidental corruption between
  build and deploy is detected rather than silently deployed.
sources:
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 9"
---

# Artifact Integrity Verification

Publishing an artifact to the [artifact repository](artifact-repository.md)
isn't enough by itself to guarantee that what gets deployed to production is
exactly what the [commit stage](commit-stage.md) built and tested. A
cryptographic hash (checksum) computed at build time, stored alongside the
artifact, and re-verified immediately before deployment closes that gap: if
the artifact was tampered with, corrupted in transit, or accidentally
substituted for a different build, the hash mismatch catches it before it
reaches a running environment rather than after.

This is a direct extension of
[build once, deploy everywhere](build-once-deploy-everywhere.md)'s guarantee
— "the exact binary that passed every gate is what gets deployed" is only
actually true if there's a mechanism verifying the artifact wasn't swapped
somewhere in between. It also supports
[compliance through pipeline automation](compliance-through-pipeline-automation.md):
a verified checksum is part of the automated, tamper-evident audit trail
linking a production deployment back to the exact commit and test run that
produced it.
