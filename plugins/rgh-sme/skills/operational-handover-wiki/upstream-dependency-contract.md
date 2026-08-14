---
type: concept
title: Upstream Dependency Contract
description: A written agreement documenting what an external data or system dependency actually provides, how, and who to contact, so a new maintainer isn't left reverse-engineering someone else's system under pressure.
sources:
  - title: "Fundamentals of Data Engineering"
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 5"
---

A system that depends on another team's source system, API, or feed is exposed to that upstream owner's decisions — schema changes, outages, deprecated fields — with no automatic warning. The fix is an explicit, written contract with the upstream owner, agreed before it's needed rather than reconstructed during an incident.

## What Belongs in the Contract

- **What is being provided**: the specific data, fields, or capability the dependency covers.
- **How it's provided**: the access method and whether it's a full refresh or incremental/delta.
- **How often**: the expected delivery or refresh cadence.
- **Who to contact**: named owners on both the upstream and downstream sides — not just a team name, since a team name doesn't tell a new maintainer who actually answers at 2am.

Layered on top of this, an explicit SLA (what's promised — e.g. "99% uptime, data available by 6am") paired with an SLO (what's actually measured against that promise) turns a vague mutual understanding into something a new maintainer can check against reality rather than take on faith. Even where a fully formal contract is impractical, at minimum verbally establish and write down these expectations so the upstream owner knows what's actually being relied upon.

## Why This Matters for Handover

An upstream dependency that was never formally documented is exactly the kind of "non-obvious dependency" a new maintainer discovers the hard way — usually during an outage, when they have no idea who owns the failing system or what was ever promised about it. Store the contract somewhere discoverable (alongside other system documentation, not buried in an email thread or a departed engineer's memory) so it survives the transition. This is the same underlying instinct as [Playbook Required Content Elements](playbook-required-content-elements.md)'s "who to notify" element, applied one level further upstream: to the external teams and systems a maintainer depends on rather than the teams they must inform when running a procedure.
