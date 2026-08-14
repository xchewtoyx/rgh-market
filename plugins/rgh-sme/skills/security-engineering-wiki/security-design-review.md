---
type: concept
title: Security Design Review
description: >
  Reviewing security and reliability implications at design-document time —
  quarters before launch — with structured prompts, because emergent
  properties can't be bolted on later.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 4"
---

# Security Design Review

Security and reliability are
[emergent properties](security-reliability-intersection.md): no module
"implements" them, and design choices affecting them are as fundamental as
relational-vs-NoSQL or monolith-vs-microservices. Retrofitting them into a
tangled system takes major refactoring or rewrites — often under incident
time pressure, where hurried invasive changes introduce new flaws. So
review these requirements in the earliest design phase, involving security
and SRE teams, and file a quick security design review once the design doc
is finalized — it heads off systemic issues that would delay or block the
final pre-launch review. Design reviews can precede launch thinking by
quarters.

Google's design-document template prompts (adapt for any design review):

- **Scalability**: how does the system scale with data and traffic? Are
  initial resources realistic (procurement lead times, cost)?
- **Redundancy and reliability**: handling of local data loss and
  transient errors; what's backed up, how it's restored, and what happens
  *between* loss and restore; can you keep serving on partial loss and
  restore only missing portions?
- **Dependency considerations**: behavior when dependencies are down;
  what must be running for startup (including subtle ones — DNS, local
  time); any dependency cycles?
- **Data integrity**: how corruption/loss is *detected*, which sources
  (user error, bugs, storage-platform bugs, replica disasters) are
  covered, time-to-notice for each, and a recovery plan per type.
- **SLA requirements**: how the promised reliability level is audited,
  monitored, and guaranteed.
- **Security and privacy**: "our systems get attacked regularly" — list
  the relevant attacks, worst-case impact, and countermeasures; list
  known vulnerabilities and potentially insecure dependencies. If a
  design genuinely has no security or privacy considerations, say so
  explicitly and why.

When weighing requirements, distinguish *critical* feature requirements
(no viable product without them) from the rest, and consider adjacent
dimensions — development efficiency and deployment velocity — since
choices there feed back into security and reliability (see
[initial versus sustained velocity](initial-vs-sustained-velocity.md)).
Nonfunctional requirements interact with each other and with features in
cascading ways; the
[payment-processing example](offloading-sensitive-data.md) shows how one
mitigation spawns the next tradeoff.

For an existing or in-progress system, assembling a
[security architecture view](security-architecture-view.md) — pulling
the security-relevant pieces out of the module, runtime, and deployment
views into one place — gives the review something concrete to check
against the attacks and countermeasures the design doc lists.
