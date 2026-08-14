---
type: concept
title: Emergency Fixes Follow the Same Pipeline
description: >
  Even during an outage, a hotfix must go through version control, the commit
  stage, and automated acceptance tests via the normal deployment pipeline —
  never patched directly onto a production server.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 10"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
  - title: Infrastructure as Code
    resource: "Infrastructure as Code, 2nd ed. (Kief Morris), ch. 20"
---

# Emergency Fixes Follow the Same Pipeline

The instinct under outage pressure is to patch the running production server
directly to save time. This is exactly the
[snowflake server](snowflake-server.md) anti-pattern under time pressure, and
it's more dangerous during an incident, not less: there's no automated test
run to catch a mistake in the fix, and the change now exists nowhere except on
that one server, invisible to version control and to whatever gets deployed
next.

The rule: push the hotfix to version control, let it run the
[commit stage](commit-stage.md), run automated acceptance tests, and deploy it
through the same automated [deployment pipeline](deployment-pipeline.md) as
any routine change. Skipping the pipeline to save minutes risks introducing a
second, worse regression on top of the first — the pipeline's job is
precisely to catch the mistakes people make when they're moving fast under
pressure.

## A separate emergency process is itself a diagnostic signal

A maintained, separate "fast path" for emergency changes (sometimes called
the dual value streams antipattern) is usually a sign the normal pipeline
itself needs work, not evidence that emergencies genuinely require different
handling. An emergency process only speeds things up by skipping steps —
either steps that were never actually necessary, in which case they should
be cut from the normal process too, or steps that are necessary but slow,
in which case the fix is to make that step fast enough to survive in the
normal path (better automation, better tooling) rather than to make an
unsafe shortcut around it exclusively for emergencies.

## When a true breakglass is warranted

In systems that enforce
[provenance-based deployment policy](provenance-based-deployment-policy.md)
at a [deployment choke point](deployment-choke-point.md), there can be
genuine emergencies where even the normal pipeline is too slow — for example,
diverting traffic away from a failing backend right now, where the
config-as-code change would normally take minutes to clear every gate.
For these, a deliberate breakglass mechanism that bypasses the policy is
more honest than an ad hoc manual workaround, provided it comes with strict
conditions: every use must raise an alarm and get audited quickly, and
because adversaries could exploit the same mechanism, breakglass events need
to stay rare enough that a real audit can actually distinguish legitimate
emergency use from abuse. A breakglass that's used routinely has stopped
being an emergency exception and has become a second, unaudited deployment
path — which defeats the point of having a
[choke point](deployment-choke-point.md) at all.
