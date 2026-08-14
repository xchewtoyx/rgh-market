---
type: concept
title: Operational Mode Envelopes
description: >
  Three operating regions — normal, abnormal, and emergency — each with
  different procedures, decision styles, and acceptable improvisation when
  an acute situation is already underway.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel et al., Eds.), Chapter 2 (Pariès, Hudson Ditching)"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson, Eds.), Chapter 21 (Hollnagel & Sundström)"
---

Once prevention has failed or was never enough, the first runbook step is
recognising which operating envelope you are in. Aviation frames three
regions that generalise cleanly to personal acute response:

1. **Normal envelope** — events follow expected tracks, parameters stay
   within design limits, variation is absorbed by ordinary flexibility.
   Procedures are detailed and accurate.

2. **Abnormal envelope** — departure from normal but mainly in anticipated
   ways: a component fails, a parameter exceeds limits, a known risk
   materialises. Response uses specific procedures, redundancy, and
   reconfiguration. The system must re-adapt through predefined active
   steps.

3. **Emergency (open) region** — extreme, possibly unanticipated
   departure. Procedures shift from detailed protocols toward generic
   frameworks; the operator must supply sense-making, improvisation, and
   [sacrificing decisions](sacrificing-decisions.md). Creativity and
   ultimate backups matter; control may be partial but consequences can
   still be mitigated if capabilities stretch quickly.

Hollnagel and Sundström's organisational state space adds parallel labels:
**normal functioning**, **regular reduced functioning** (scheduled, e.g.
holidays), **irregular reduced functioning** (unexpected resource loss,
usually anticipated with recovery functions), and **disturbed functioning**
(loss of control, possibly several distinct disturbed modes). A resilient
organisation may have multiple disturbed modes available; transition into
disturbed functioning is itself a detection event. Severe disturbance may
require return via a **repair** state rather than direct recovery.

Misclassifying the envelope is a common failure mode: staying in "regular
reduced functioning" (holiday staffing, business as usual) while continuous
news and escalating scope signal disturbed functioning — as when a foreign
ministry received disaster information at dawn but did not shift modes
until the next day. Detection thresholds and [resilience state
transitions](resilience-state-transitions.md) cover the recognition and
shift steps once the envelope is correctly named.
