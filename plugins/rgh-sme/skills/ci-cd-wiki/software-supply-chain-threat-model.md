---
type: concept
title: Software Supply Chain Threat Model
description: >
  Modeling the pipeline itself as an attack surface — enumerating benign
  insiders, malicious insiders, and external attackers, and the specific ways
  each could subvert source, build, test, or deployment — before choosing
  which pipeline controls to invest in.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
---

# Software Supply Chain Threat Model

The software supply chain is the whole process of writing, building, testing,
and deploying — everything a [deployment pipeline](deployment-pipeline.md)
does end to end. Treating it as a security-relevant attack surface starts
with naming the adversaries a specific system needs to defend against:

- **Benign insiders** who may make honest mistakes (e.g. building from a
  locally modified, unreviewed copy of the code).
- **Malicious insiders** trying to gain more access or effect than their role
  allows.
- **External attackers** who compromise the machine or account of an insider
  and then act with that insider's privileges.

For each, enumerate concrete ways they could subvert the pipeline: submitting
a change that introduces a vulnerability (accidentally or deliberately);
deploying a binary with harmful configuration; deploying an old, known-
vulnerable version; a misconfigured CI system that will build from an
arbitrary source repository; a compromised build script that exfiltrates a
signing key; a backdoored compiler or build tool.

## Using the model

Once threats are listed, map each to whatever mitigation already exists, and
be explicit about that mitigation's limitations — a mitigation that "mostly"
covers a threat still leaves a residual gap worth naming. Threats with no
mitigation, or only a weak one, are where to prioritize pipeline hardening
next: see [mandatory code review](mandatory-code-review.md),
[verify artifacts, not just people](verify-artifacts-not-just-people.md), and
[binary provenance](binary-provenance.md) for the concrete controls this
threat model motivates.
