---
type: concept
title: Resilience State Transitions
description: >
  Requirements for shifting operating mode during an acute disruption —
  recognition, transition rules, readiness, and eventual return to
  sustainable normal functioning.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson, Eds.), Chapter 21 (Hollnagel & Sundström)"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson, Eds.), Chapter 5 (Westrum)"
---

A resilient response is not a single heroic act but a **state transition**:
moving from one well-defined mode of operation to another, acting
competently in the new mode, and eventually returning to durable normal
functioning. Hollnagel and Sundström model this as a state space; Westrum
adds a time axis (foresee, cope, recover). Together they define the
incident-response lifecycle beyond [operational mode
envelopes](operational-mode-envelopes.md).

**Four requirements for transition:**

1. **Recognition** — ability to detect that conditions have changed and a
   response is needed. Reactive recognition always carries a lag; resilient
   systems minimise it. Proactive recognition reduces lag but risks acting
   on wrong cues. Organisational, psychological, and social factors
   (ignorance, bias, vested interest) and simple data gaps all work against
   recognition.

2. **Transition rules** — procedures and routines to shift modes. Key
   questions: do people know what to do; are command lines defined; do
   normal roles change; is there a script, scenario, or guideline set?

3. **Readiness of the receiving state** — backup organisation, facilities,
   supplies, experienced people, and exercised roles ready when the new mode
   activates. Without readiness, recognition and rules produce delay or
   hollow announcements.

4. **Maintaining parallel normal operations** (organisation-dependent) —
   some entities must keep ordinary functions running during emergency
   (e.g. a foreign ministry); others may suspend normal work entirely for
   the duration (e.g. a travel company during a destination disaster).

**Return to normal** is its own transition. It requires detecting that the
abnormal condition has ended (not prematurely), procedures for reverting
or establishing a revised normal, and capacity to absorb resources released
from emergency mode. Where emergency and normal ran in parallel, return is
simpler; otherwise the normal state must absorb idle emergency capacity.

**Reversibility** varies: some disturbances allow direct recovery; severe
ones require a repair or reconstruction phase first. Delays in transition
often trace to fossilised structures or policies that route decisions up
and back down through bureaucratic layers.

Westrum's time dimension separates **foresee and avoid**, **cope with
ongoing trouble**, and **repair after catastrophe** — three capabilities
that do not necessarily imply one another. An organisation strong at
recovery may be weak at early recognition; see [Westrum threat situation
types](westrum-threat-situation-types.md) for how threat familiarity
shapes which capability matters most. Post-incident work is covered in
[post-incident recovery](post-incident-recovery.md).
