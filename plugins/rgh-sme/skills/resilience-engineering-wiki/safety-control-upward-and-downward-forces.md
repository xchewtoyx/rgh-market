---
type: concept
title: Safety as a Control Problem — Upward and Downward Forces
description: >
  Modelling safety as keeping performance variability within an acceptable
  boundary reframes monitoring around two symmetric force sets — what pushes
  variation out of control and what pulls it back — and traditional safety
  practice only ever tracked the first.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 17"
---

Safety, on this model, is a control problem: organisational performance has
to be kept within acceptable boundaries of variation. An **accident**
happens when operational variability escapes the system's control
mechanisms altogether; **incidents** are near-misses close to that boundary,
which is why reactive incident reporting works at all — it uses events near
the edge as a retrospective window onto the forces that pushed variation
toward it (see [structural requisites for incident
reporting](five-structural-dimensions-of-incident-reporting-viability.md)
for when this retrospective window actually functions as designed, and when
it doesn't).

**Traditional safety practice tracks only half of this picture.** It
monitors the *upward* forces — the drivers pushing variation toward and past
the control boundary — through mechanisms like Tripod's basic risk factors
(see [Tripod basic risk factors](tripod-basic-risk-factors.md)). Resilience
engineering adds the symmetric *downward* forces: the capabilities that
actively pull variation back under control — staff and organisational
capacity to anticipate, recognise, and adapt to variability as it happens.
Monitoring only the upward forces treats safety as purely defensive,
measuring how close the system is to falling; monitoring the downward
forces as well measures whether the system's own capacity to catch itself is
intact, which is a different question with a different answer.

**This is where routine monitoring meets [FRAM](functional-resonance-analysis-method.md).**
Resilience-oriented risk monitoring is explicitly framed as detecting
**near-resonance conditions**: situations where disruptions and normal
functional variability are approaching or exceeding the system's baseline
adaptive mechanisms — its "designed-for-uncertainties" envelope (Woods). This
is the proactive-monitoring answer to the question functional resonance
raises: if catastrophic outcomes emerge from several functions' ordinary
variability combining rather than from any one function breaking, then the
thing worth monitoring continuously is not any single function's health but
whether the *combination* is drifting toward resonance — the downward forces
(adaptive capacity) losing ground against the upward ones (variability
accumulating), before the outcome actually escapes control.

The same idea appears at the individual-episode scale in [the boundary of
potential variability](boundary-of-potential-variability.md) — recognising
that a specific unfolding situation has left its anticipated envelope. This
note is the organisational-monitoring analogue: instead of one practitioner
recognising one situation crossing its own envelope in real time, it is the
organisation tracking, on a continuous basis, whether its aggregate adaptive
capacity is keeping pace with its aggregate exposure to variability.
