---
type: concept
title: Security-Reliability Intersection
description: >
  Security and reliability are both emergent, invisible-until-broken system
  properties that differ chiefly in the presence of an adversary — and
  measures for one can complicate the other.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 1"
---

# Security-Reliability Intersection

The cautionary parable: Google's internal password manager — built years
earlier for a few sysadmins — was crushed when thousands of employees hit
it after a bus-WiFi password change. Primary and secondary replicas failed
in turn (poor load balancing/shedding — a reliability flaw), and recovery
was then blocked by the system's own *security* measures: restart required
HSM smart cards locked in safes; one safe's combination lived in the
now-offline password manager; a power drill opened it; and the final
delay was a card inserted upside down. Reliability triggered the outage;
security prolonged it. The interplay is subtle and easy to miss.

**The key difference**: reliability risks are mostly nonmalicious — assume
some things *will* go wrong at some point. Security risks come from
adversaries — assume someone may be *trying* to make things go wrong at
any point. This one difference drives divergent design choices, most
visibly in [fail safe versus fail secure](fail-safe-vs-fail-secure.md),
and reframes each [CIA property](cia-triad.md).

**Commonalities that shape practice**:

- **Emergent and un-bolt-on-able.** Both properties arise from whole-system
  design interactions, not from any component; both are very hard to
  retrofit, so weigh them from the earliest design stages and keep testing
  through the lifecycle — an innocuous change to one component can silently
  break either property system-wide.
- **Invisible when working.** Absent an emergency, both look like
  reducible or deferrable cost — until a breach knocks $350M off an
  acquisition price or a power failure cancels 700 flights. Honest,
  concrete communication in good times as well as bad is what builds the
  trust that funds the work.
- **Assessed differently.** Reliability of a composition can be reasoned
  about with error budgets, partly because component failures can be
  assumed independent. Security composes worse: an adversary needs only
  one path, so assurance comes from design/implementation analysis plus
  **adversarial testing** — simulated attacks from a defined adversary's
  perspective — evaluating resistance, detection effectiveness, and
  consequences.
- **Simplicity serves both.** A simpler design shrinks attack surface,
  reduces unanticipated interactions, and is comprehensible under incident
  pressure — see
  [design for understandability](design-for-understandability.md).
- **Both need a failure plan.** Prevention will fail; detection (logging),
  rehearsed crisis response, and reliable
  [recovery mechanisms](design-for-recovery.md) are part of the design,
  not an afterthought.

One security-specific tension to internalize early: reliability incidents
benefit from many perspectives and rich logs, while security incidents are
handled need-to-know so the adversary isn't tipped off — and the logs
themselves can be a target (see
[security-incident operational security](incident-operational-security.md)
and [security log design](security-log-design.md)).

Calibrate everything to the risk profile at hand: a stock exchange or a
dissident communication platform is not an animal-sanctuary website.
Security and privacy are closely related: privacy requires security
(behaving as intended in the presence of an adversary), and most of these
approaches also serve privacy objectives.
