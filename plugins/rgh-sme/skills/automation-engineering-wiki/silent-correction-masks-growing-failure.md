---
type: concept
title: Silent Correction Masks a Growing Failure
description: >
  Automation that quietly absorbs small deviations without surfacing them
  removes the early warning signs an operator would otherwise notice,
  letting a slowly growing problem go undetected until it fails all at once.
sources:
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Klein), ch. 13, 16"
---

# Silent Correction Masks a Growing Failure

Layering automated defenses on top of a system — warnings, safeguards,
automatic correction of small deviations — reduces how often an error
actually reaches a human. But it comes with a specific, underappreciated
cost: when a failure eventually does slip past all the accumulated
defenses, the person diagnosing it now has to untangle the original
problem *and* the effects and interactions of every defensive layer that
tried to compensate for it along the way, simultaneously. One documented
aviation case did exactly this: someone accidentally kicked a shielded
rudder-control switch out of sight behind a pedestal, deflecting the
rudder to an extreme position. The aircraft's flight management system
silently compensated using other flight controls to hold level flight,
giving the crew no indication anything was wrong. When the compensation
finally exceeded what the system could absorb, it disengaged without
warning and handed control back to a crew with zero context, already
out of tolerance — the aircraft immediately stalled, and the crew initially
misdiagnosed it as an engine problem, taking corrective actions that made
things worse before eventually recovering and finding the real cause. As
Klein summarized it: "a unit designed to reduce small errors helped create
a large one."

This is a sharper, more specific version of the general blind spot in
[self-healing systems](self-healing-overload-response.md): it isn't just
that a silently-recovering system produces no page and no signal (which
[exception collection](exception-collection-as-automation-health-signal.md)
addresses for crash-restart specifically) — it's that continuous, gradual
self-correction can keep a genuinely worsening trend looking perfectly
healthy for an extended period, right up until it isn't. The failure isn't
sudden; it was always there, growing, just invisible to anyone watching
only the corrected output rather than the correction effort itself.

The design response is to make the correction *visible* rather than only
making the output correct: expose how much deviation the automation is
currently absorbing (not just whether it's currently succeeding), the same
way [self-healing overload response](self-healing-overload-response.md)
calls for recording the level of degradation a component is running at.
An automated safeguard that's silently working overtime is exactly the
kind of drift that should surface on a dashboard or trigger an alert on
its own — trusting operators to notice and diagnose a growing correction
burden, rather than trusting the automation's designers to have made the
correction mechanism robust enough that it never needs to be watched.
