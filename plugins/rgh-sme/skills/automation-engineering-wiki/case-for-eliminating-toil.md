---
type: concept
title: The Case for Eliminating Toil
description: >
  Eliminating toil prevents operator burnout, keeps headcount growth
  sublinear as the system it supports scales, and removes the manual-error
  risk that comes from doing operational tasks by hand.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 5"
---

# The Case for Eliminating Toil

Three distinct benefits justify spending engineering time to eliminate
[toil](toil.md) rather than just tolerating it:

- **Preventing burnout**: mind-numbing repetitive work damages morale and
  retention over time, independent of whether the team can technically keep
  up with the volume.
- **Scaling without headcount**: toil scales O(N) with the system, but if
  it's eliminated by [automation](value-of-automation.md) instead of
  absorbed by hiring, headcount only needs to grow O(log N) — a small team
  can keep operating a system that's grown far larger than the team has.
- **Reducing human error**: manual execution of operational tasks — typing
  in configuration, running commands by hand — is where typos and operator
  mistakes get introduced; automating the task removes that failure mode
  along with the toil itself.

These benefits are the reason toil elimination gets treated as a first-class
engineering priority rather than something to fit in around other work —
see the [toil budget](toil-budget.md) for the concrete mechanism that
protects time for it. Where the toil comes from an expensive, hard-to-touch
legacy system rather than a simple repetitive task, eliminating it usually
can't happen in one step — see the [legacy system automation
pathway](legacy-system-automation-pathway.md).
