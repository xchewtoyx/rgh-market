---
type: concept
title: Standard Change Pre-Approval
description: >
  Earn a pre-approved, no-manual-gate category for a class of changes by
  building a track record of automated testing and low change failure
  rate, instead of routing every change through the same approval process.
sources:
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 23"
---

# Standard Change Pre-Approval

ITIL distinguishes three change categories, and the distinction is a lever
a change process can use deliberately rather than routing everything
through the same gate:

- **Standard changes** — well-understood, low-risk, following an
  established and already-approved process. No approval is needed before
  each individual deployment; they're logged for traceability, not
  gatekept.
- **Normal changes** — higher-risk, require case-by-case review from an
  agreed authority before deployment.
- **Urgent changes** — must deploy immediately (an active incident, a
  critical security patch); approval and documentation can follow the
  deployment rather than precede it.

The lever: a class of changes doesn't have to stay "normal" forever. A
pipeline that has built a track record — automated test coverage, a low
[change failure rate](change-failure-rate.md), fast [mean time to
restore](mean-time-to-restore.md) — is evidence a reviewing authority can
use to reclassify that pipeline's changes as standard, moving them out of
manual review permanently rather than one exception at a time. This gives
teams a direct incentive to invest in automated verification: better
pipeline evidence is what earns the exit from case-by-case gating, not
negotiation or appeals to urgency.

This is a durable, structural alternative to [change approval board
pathology](change-approval-board-pathology.md): instead of arguing that
CABs don't work in general, it takes the volume of changes a CAB would
otherwise review down to the genuinely novel or risky ones, where human
judgment has an actual chance of adding signal.
