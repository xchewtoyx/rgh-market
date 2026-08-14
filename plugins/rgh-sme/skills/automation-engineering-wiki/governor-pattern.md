---
type: concept
title: Governor Pattern
description: >
  A programmable throttle that caps the maximum rate of an automated
  operation — batch processing, automated deploys, mass sends — so a bug
  or misconfiguration can't run away to its full damage before anyone can
  intervene.
sources:
  - title: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 5"
  - title: "Building Secure and Reliable Systems"
    resource: "Building Secure and Reliable Systems (Google), ch. 9"
---

# Governor Pattern

A governor is an administrative rate cap placed directly on an automated
operation: a batch job, an automated deployment, a mass email send. Instead
of trusting the automation's own logic to behave, the governor imposes an
external ceiling on how much it can do per unit time, independent of
whatever triggered the run.

The value of a governor is that it doesn't need to know *why* an automated
run might misbehave — it just guarantees that even a completely broken run
can only do damage at a bounded rate, buying time for a human or a
higher-level safety check to notice and stop it. This makes it one concrete,
implementable instance of the more general principle of
[safeguards against runaway automation](safeguards-against-runaway-automation.md).

Build the governor as its own small, independent service rather than logic
embedded inside the automation it's throttling. Keeping it simple, single
purpose, and separately testable is what makes it trustworthy — a rate
limiter tangled into the automation it constrains is much harder to verify
in isolation, and it's easy for engineers under pressure to route around
embedded checks that share the same failure domain as the thing failing.
A standalone governor can issue a short-lived approval token per action
(proof it reviewed and permitted a specific change at a specific time) and
double as the audit log for every change actuated through it. It should
also be sized independently from how fast the automation it governs
*could* run: build the automation to move as fast as is technically
possible, and use the governor to constrain it down to whatever the
current risk policy allows — so tightening or loosening the policy is a
governor configuration change, not a rewrite of the automation itself.
