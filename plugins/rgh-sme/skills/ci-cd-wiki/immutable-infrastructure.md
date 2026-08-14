---
type: concept
title: Immutable Infrastructure
description: >
  Disallowing manual changes to running infrastructure entirely — the only
  path to a production change is a version-controlled rebuild — which
  eliminates configuration drift structurally rather than by policing it.
sources:
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 9"
---

# Immutable Infrastructure

A [phoenix server](phoenix-server.md) *can* be rebuilt from scratch on
demand; immutable infrastructure goes further and insists it always *is* —
manual production changes are not just discouraged, they're structurally
disallowed. Any config change, patch, or upgrade happens by building a new
instance from version control and replacing the old one, never by logging
into a running server and changing it in place.

The metaphor (Bill Baker, Microsoft): servers used to be pets — named,
individually nursed back to health when something went wrong. Under immutable
infrastructure they're cattle — numbered, and replaced rather than treated
when something's wrong with one.

## Enforcement

- Disable remote login to production servers outright, or restrict it to
  emergency-only access with console activity logged and reported
  automatically.
- Routinely kill and replace running instances even when nothing is known to
  be wrong with them, so any drift that crept in despite the above gets
  purged on a schedule rather than accumulating indefinitely (Netflix
  reportedly keeps average instance age around three weeks this way).

## Why it matters more than just "can rebuild"

A system that's merely *capable* of automated rebuild but still permits
manual hotfixes under pressure will accumulate
[environment drift](environment-drift.md) anyway, because the manual path
stays available and gets used exactly when discipline is weakest — during an
incident. Immutable infrastructure removes that path rather than relying on
the team to avoid it. This is the infrastructure-level version of the same
argument behind
[emergency fixes follow the same pipeline](hotfix-through-pipeline.md): the
automated path has to be the *only* path, not just the preferred one, or it
gets bypassed exactly when the stakes are highest.
