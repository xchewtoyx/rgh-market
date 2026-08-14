---
type: concept
title: Four Monitoring Cadence Modes
description: >
  A proactive monitoring architecture needs more than one cadence — routine
  continuous tracking, time-bound probes, change-triggered checks, and
  indicator-triggered deep dives each catch a different kind of risk shift.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 6"
---

Once an organisation has moved [the sensor upstream of the outcome
stage](proactive-monitoring-control-model.md), it still faces a design
question the sensor placement alone doesn't answer: on what cadence does
monitoring actually run? A mature monitoring architecture (drawn here from
aviation fatigue risk management, but the shape generalises to any proactive
safety-indicator system) combines four distinct modes rather than relying on
one:

1. **Continuous mode** — an always-on feedback loop, routinely updating the
   organisation's picture of risk from data streams that already exist
   (incident reports, operational telemetry). This is the baseline; the
   other three modes exist because continuous monitoring alone has blind
   spots continuous monitoring cannot see into on its own.
2. **Probe mode** — a deliberately time-bound period of focused, deeper
   monitoring (days to weeks) aimed at auditing one specific segment of
   operation more closely than the continuous baseline affords, then
   standing back down.
3. **Proactive mode** — focused monitoring triggered *before* a known
   operational change takes effect (a new route, a new schedule structure,
   a new procedure), so the change's actual effect on risk is measured
   deliberately rather than inferred later from whatever the continuous
   baseline happens to pick up.
4. **Reactive mode** — focused monitoring triggered *by* a spike in the
   continuous indicators themselves, deployed to understand a signal the
   baseline has already flagged rather than to originate a new one.

The pattern across all three focused modes (probe, proactive, reactive) is
that they exist to answer a specific question at a specific moment, and then
retract — sustained, universal deep monitoring of everything is neither
affordable nor, past a certain point, informative; see [criteria for
selecting safety indicators](criteria-for-selecting-safety-indicators.md)
for why a candidate indicator has to earn its place in the continuous
baseline rather than being added indiscriminately. What distinguishes this
from [pinging](pinging-proactive-risk-probing.md) is scope and initiation:
pinging is a specific *organisational-design* answer to who should be doing
proactive detection (people embedded in the work, not off-site
specialists); these four modes describe *when* and *why* monitoring
activity intensifies, a question that applies regardless of who is doing
the watching.
