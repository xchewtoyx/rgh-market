---
type: concept
title: Failure Domain Amplification in Automation
description: >
  Automation running at scale can apply a destructive bug to an entire
  fleet almost instantaneously, turning a small coding error into a
  global outage in the time it takes the automation to run.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 7"
  - title: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 10"
---

# Failure Domain Amplification in Automation

A human operator making the same mistake on every machine in a fleet would
take hours or days, and would likely notice and stop partway through.
Automation removes that natural circuit breaker: a bug in a script that
touches every machine it's pointed at can apply the same destructive change
to the entire fleet before anyone notices anything is wrong — for example,
an automated wipe or config push that was meant to target one cluster but
matched everything.

This is the central risk that grows as automation moves up the [automation
maturity spectrum](automation-maturity-spectrum.md): the same
consolidation that gives automation its speed and scale also means the
failure domain of a single bug is no longer bounded by how fast a human can
type. It's the direct motivation for
[safeguards against runaway automation](safeguards-against-runaway-automation.md)
— rate limits, safety checks, and a way to stop a run in progress — and for
making sure the automation is [idempotent](idempotency-in-automation.md) so
a bad run doesn't compound itself on retry.
