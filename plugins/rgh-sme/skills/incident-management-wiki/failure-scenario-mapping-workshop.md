---
type: concept
title: Failure Scenario Mapping Workshop
description: A structured workshop technique that walks each candidate failure scenario through cause, failure mode, detection, and correction to turn a prioritized risk into a concrete mitigation plan.
sources:
  - title: "Infrastructure as Code"
    resource: "Infrastructure as Code, 2nd Edition (Kief Morris), ch. 21"
---

A **failure scenario mapping workshop** is where a team turns a prioritized
risk — see [disaster risk assessment matrix](disaster-risk-assessment-matrix.md)
— into an actual mitigation plan, by working through four questions for each
candidate scenario:

- **Causes and prevention**: what situations lead to this failure, and what
  makes them less likely? (E.g., a server running out of disk space during a
  usage spike — mitigate by analyzing usage patterns and expanding capacity
  ahead of need.)
- **Failure mode**: what actually happens when the failure occurs, and can
  the consequence be reduced without human intervention? Teams frequently
  discover they don't actually know what happens when a given error occurs
  until they work through it explicitly — a disk filling up might mean an
  application silently accepts transactions it can't record, which is worse
  than refusing them outright.
- **Detection**: how will the failure be noticed, and can it be noticed
  earlier — ideally before user impact, rather than via a support escalation?
- **Correction**: what steps recover the system? Automatic correction
  (destroying and rebuilding an unresponsive instance) is preferable to a
  manual runbook; either way, the deeper question is why the failure
  happened at all, since automatic recovery that masks a recurring
  underlying problem just delays the reckoning.

The output is a prioritized backlog of mitigations — sized by likelihood,
potential damage, and cost to implement — not a single ambitious plan that
tries to gracefully handle every conceivable failure at once. A cheap first
step (alerting before a resource is exhausted) is often worth doing well
before an expensive one (automatically expanding capacity) is affordable.

This mapping exercise is not a one-time document: every incident, including
ones caught in a lower environment, is a prompt to ask whether it reveals a
new failure scenario that belongs in the map. That closes the loop back into
[learning reviews](learning-reviews.md), and the resulting mitigations are
exactly the scenarios worth exercising with
[preparedness drills](preparedness-drills.md) or validating with a
[chaos engineering experiment](chaos-engineering-experiment-design.md).
