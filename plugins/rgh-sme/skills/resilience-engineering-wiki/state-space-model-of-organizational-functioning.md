---
type: concept
title: State-Space Model of Organizational Functioning
description: >
  Following Ashby's cybernetics, an organisation's operation decomposes into
  a small set of recognisable functional states — from normal functioning
  through disturbed functioning to decay — with transition rules between
  them that are sometimes irreversible or require passing through an
  intermediate state.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 21"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 15"
---

Following Ashby's (1956) cybernetic definition, a **state** is any
well-defined condition or property of a system that can be recognised if it
recurs; the complete set of an organisation's recognisable states, together
with the rules governing transitions between them, forms its **state
space**. State spaces range from simple, one-dimensional models with
adjacent transitions — a threat-level scale running green to red, a
healthy–unhealthy–catastrophic triad — to genuinely multi-directional
networks. A structurally important property in high-hazard industrial
systems: some transitions are **non-reversible**, requiring passage through
an intermediate state rather than a direct return — an emergency state
cannot transition straight back to normal operation, it must pass through an
idle state first, the same way a system cannot un-cross [Rasmussen's safety
boundary](rasmussen-boundary-model.md) by simply reversing whatever step
crossed it.

Beyond the simplified normal/unhealthy/catastrophic triad, a complex service
or sociotechnical organisation actually operates across six distinct
functional states:

1. **Normal functioning** — scheduled, reliable, effective performance
   fulfilling the system's primary goals.
2. **Regular reduced functioning** — a *scheduled* lower-activity state:
   night shifts, weekend or holiday staffing. This is planned reduction, not
   disturbance.
3. **Irregular reduced functioning** — an *unexpected*, temporary loss of
   resource control from an internal disruption (staff illness, equipment
   failure, a labour action), requiring a pre-planned recovery mechanism to
   exit.
4. **Disturbed functioning** — loss of operational control under severe
   internal or external strain. A resilient organisation maintains several
   genuinely distinct operational modes for handling disturbance, rather
   than one generic "emergency" mode meant to cover every kind of
   disturbance equally badly.
5. **State of repair / reconstruction** — the intermediate recovery state a
   severe disturbance requires passing through before the system can revert
   to normal functioning; this is the concrete instance of the
   non-reversible-transition property above.
6. **Decay / cessation** — the terminal state in which organisational
   integrity fails completely, with no further recovery state available.
   **Barings plc's 1995 collapse** is the cited case: a rogue trader in
   Singapore hid mounting losses in an unreported error account while
   London management, lacking derivatives expertise, accepted implausibly
   high reported profits from a "star performer" without verifying the
   underlying data. The firm passed through a latent-vulnerability state
   (a single trader controlling both front-office trading and back-office
   reconciliation, in violation of basic segregation of duties), into
   deteriorating health (ignored balance-sheet anomalies, escalating margin
   calls approved without inquiry) and finally into decay once accumulated
   losses exceeded total capital reserves. Each state transition in this
   sequence tracked a corresponding collapse in [control
   mode](hollnagel-four-control-modes.md), from strategic/tactical through
   opportunistic to fully scrambled.

The practical value of naming these states explicitly, rather than treating
"working" and "not working" as the only two organisational conditions, is
that it turns "how resilient is this organisation" into a much sharper
question: which of these states can it actually recognise itself as being
in, and does it have a distinct, rehearsed transition rule for moving
between each pair of adjacent states — see [four requirements for
state-transition resilience](four-requirements-for-state-transition-resilience.md)
for what happens when an organisation cannot answer that question in real
time.
