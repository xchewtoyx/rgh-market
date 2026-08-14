---
type: concept
title: Failure Scenario Mapping
description: >
  A structured workshop for brainstorming specific failure modes and mapping each one across causes, blast-radius behavior, detection, and correction, before spending effort building mitigations.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code, 2nd Edition (Morris), ch. 21"
---

**Failure scenario mapping** is a workshop technique for turning "failures
are inevitable" into a concrete, prioritized backlog of resilience work,
rather than either ignoring the risk or trying to build unlimited
protection against everything. A team brainstorms specific ways the system
could fail, then works through each candidate scenario along four
dimensions:

1. **Causes and prevention** — what situations lead to this failure, and
   what would make it less likely? (E.g. a disk filling up under a usage
   spike — addressed by capacity monitoring, or automatic expansion.)
2. **Failure mode** — what actually happens when it occurs, and can the
   consequence be reduced without human intervention? The ideal failure
   mode keeps the system operating in a reduced capacity rather than
   failing outright — this is where [graceful
   degradation](graceful-degradation.md) and [load
   shedding](load-shedding.md) get selected as the specific mitigation for
   a specific scenario, rather than applied generically.
3. **Detection** — how will the team know the failure occurred, and can
   detection happen earlier (ideally before user impact, not after)?
4. **Correction** — what has to happen to recover, and can it be automated
   rather than requiring a person to remember and execute a sequence of
   manual steps under pressure?

Each mapped scenario is then rated by likelihood and impact and turned into
prioritized backlog work — an incremental set of measures, not an
all-at-once demand for the system to gracefully handle every conceivable
failure (no team has the time or resources to build that). A cheap first
step (e.g., alerting before a resource is exhausted) is worth shipping
even when the more ambitious fix (e.g., fully automatic remediation) isn't
affordable yet.

Once a failure scenario and its intended mitigation are defined, the
mitigation should be verified with an automated test or a live [chaos
experiment](chaos-engineering.md) — a belief about what the system does
under a given failure is not the same as evidence that it actually does
that. Failure scenario mapping is the planning and prioritization layer
that decides *which* failure to inject and *what correct behavior looks
like*; chaos engineering and [game day exercises](game-day-exercises.md)
are how that belief gets tested against reality. Failure planning is also
naturally recurring: every real incident (including ones caught safely in
a non-production environment) is a prompt to ask whether it represents a
new scenario worth mapping.
