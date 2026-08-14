---
type: concept
title: SLO Evolution Triggers
description: >
  SLOs work best when deliberately let change as usage, dependencies,
  functionality, and user expectations shift — a checklist of situations
  that should prompt revisiting a target.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 14"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 7"
---

An SLO is a target, not a permanent contract — see
[Service Level Objective](service-level-objective.md). Triggers worth
watching for:

- **Usage changes** — rising traffic can overwhelm a service (revisit based
  on real user impact) or, through low-frequency-metric dilution, actually
  allow a *more* stringent target as traffic grows. Declining/retiring
  services get noisier measurements and are often left over-provisioned,
  masking true capability — revisit before a provisioning cut breaks a stale
  target.
- **Functional changes** — reliability-improving feature work may leave
  surplus budget worth spending or worth tightening the target over;
  reliability-degrading feature work may blow the SLO outright, or more
  subtly leave too little headroom to absorb future incidents even while
  nominally still meeting target. Don't wait for a gross miss — small shifts
  warrant a look too.
- **Dependency changes** — a service can never be more reliable than a hard
  dependency's *stated* SLO, not its historically-better actual performance;
  assume dependencies will only run as reliable as promised. When a
  dependency's SLO changes, either tentatively absorb it into slack or
  update the target in lockstep. See
  [dependency reliability composition](dependency-reliability-composition.md).
- **Failure-induced changes** — every budget-burning incident is a chance to
  ask if the target still makes sense, but not every incident warrants a
  change (a large-scale externally-caused outage is often not worth
  architecting around) — the discussion itself, not necessarily a resulting
  number change, is one of the most valuable outputs.
- **User expectation/requirement changes** — sustained overperformance trains
  users to expect the higher bar (see
  [too reliable is a cost](too-reliable-is-a-cost.md)); competitor products
  raising the bar should push a target up too, even at the cost of budget;
  business-driven SLA changes cascade down into the SLO.
- **Security and regulatory shifts** — Upgrading security posture (e.g., migrating to HTTPS/TLS or enforcing multi-factor authentication) introduces cryptographic overhead, latency, or new credential-checking steps. These shifts require re-evaluating latency and availability targets.
- **Tooling changes** — new metrics systems, changed scrape intervals or
  retention, or a new error-budget calculation pipeline all warrant a
  revisit even if the data is expected to "look the same."
- **Intuition-based changes** — no trigger list is ever complete; proactively
  tighten targets ahead of known high-stakes periods.

See also [identifying a miscalibrated SLO](identifying-a-miscalibrated-slo.md)
for the diagnostic signs that a target is currently wrong, as distinct from
this list of situations that should prompt checking. A revisit prompted by
one of these triggers should end in an explicit, justified decision — a
target that quietly loosens itself in response to its own recent misses
without going through that deliberate process is exhibiting [SLO target
erosion](slo-target-erosion.md), not evolution.
