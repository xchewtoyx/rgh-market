---
type: concept
title: Design for a Changing Landscape
description: >
  Vulnerabilities, user expectations, and regulation shift constantly;
  security changes follow normal release discipline but at speeds set by
  severity, dependencies, sensitivity, and deadlines.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 7"
---

# Design for a Changing Landscape

New vulnerabilities appear continuously while user and regulatory
expectations rise; responding requires changing infrastructure frequently
and quickly *while* staying reliable. Security changes come in flavors —
incident response, newly discovered vulnerabilities, product changes,
proactive posture improvements, regulatory requirements — but all are
subject to normal release-engineering discipline. Every change should be:

- **Incremental** — small and standalone; don't bundle refactoring.
- **Documented** — how *and why*, with scope, rationale, and contacts, so
  others can judge urgency and pick up the work.
- **Tested** — unit/integration tests plus peer review.
- **Isolated** — behind feature flags; the binary behaves identically
  with the flag off.
- **Qualified** — through the normal binary release process and its
  qualification stages.
- **Staged** — gradual, canaried, with instrumentation showing behavior
  before vs. after.

"Slow and steady" is the conscious default: a broken security change can
cause the very downtime or data loss it was meant to prevent.

**What sets the speed** of a given change: *severity* (critical + actively
exploited + applicable to you = as fast as possible — best served by a
patch that can ship *independently* of in-flight rollouts); *dependent
systems and teams* (vendor patches, client-before-server ordering);
*sensitivity* (a posture improvement can wait out a holiday change
freeze); and *deadlines* (regulatory dates, disclosure embargoes — under
embargo you cannot patch broadly before the announcement, so negotiate
announcement dates that suit rollout processes). Time horizons range from
same-day [zero-day response](zero-day-vulnerability-response.md), through
gradual [posture-improvement rollouts](security-change-rollout.md), to
multi-year ecosystem changes.

**Plans will change.** Accelerate when an exploit goes public — but
prefer re-ordering the rollout toward higher-risk systems, rate-limiting
operations, or taking a critical system offline over blind speed-up. Slow
down or roll back when error rates spike. Have an action plan for a
broken embargo at every stage; know whether you're actually severely
impacted before rushing; and accept that third-party patch availability
may set your start date regardless of intent.

The architecture that makes any of this cheap — current dependencies,
frequent rebuilds, containers, microservices — is its own concept:
[architecture for change](architecture-for-change.md). And speed of
change is a two-edged capability governed by
[rollout-speed-vs-policy](decouple-rollout-speed-from-policy.md).

**The slowest-moving instance of this pattern**: the
[quantum threat to cryptography](quantum-threat-to-cryptography.md) is a
landscape change whose direction is already certain, whose timing is not
— exactly the case where cryptographic agility must be built and proven
well before the deadline arrives, because the deadline may already be in
the past for long-lived confidential data.
