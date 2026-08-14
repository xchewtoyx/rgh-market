---
type: concept
title: Dark Launch
description: >
  Run a new code path against real production traffic and discard or hide
  its output well before customers ever see it, so scale and correctness
  problems surface long before the feature is exposed.
sources:
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 12"
---

# Dark Launch

A dark launch deploys the full implementation of a feature to production —
often weeks ahead of any customer-facing release — while keeping its output
invisible: the code path executes for real requests, but results are
logged or discarded instead of shown to the user. Exposure to real load is
then ramped deliberately (e.g. invisibly calling the new path for 1% of
sessions, then a larger share) before anyone can see it fail.

This is [decoupling deployment from release](decoupling-deployment-from-release.md)
taken to its most aggressive form: not just "deployed but gated off," but
"deployed, live, and exercised" without being observable. It answers a
question canary metrics on synthetic load can't: does this hold up under
*real* production-scale traffic and data, including the state and
concurrency patterns a load test can't reproduce? It's a form of [testing
in production](canary-measurement-validity.md) that carries none of the
user-facing risk normal production testing does, because nothing about the
result is ever shown.

It's related to but distinct from [traffic teeing](traffic-teeing.md):
teeing duplicates requests to a *separate* system, while a dark launch runs
the new path inline, in the same production instance, alongside the real
one — so it also validates integration and resource contention with the
rest of the live system in a way an external tee cannot. When the feature
is finally ready, turning it on is just flipping visibility (typically a
[feature flag](feature-flag-blast-radius-isolation.md)), not a deploy — the
riskiest part of the change already happened, invisibly, long before launch
day.
