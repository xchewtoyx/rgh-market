---
type: concept
title: Automation Surprise
description: >
  An operator is caught off guard by what automation just did because their
  mental model of its current mode or state has silently diverged from
  reality, not because they lack skill or attention.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 4"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 6"
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Klein), ch. 6, 13"
---

# Automation Surprise

Automation surprise is the moment an operator watches a system do something
they did not expect and cannot immediately explain, because the automation
is acting correctly on a mode or internal state the operator no longer
has an accurate picture of. It is a design failure, not an attention
failure: the automation offered no way for the operator to keep their
mental model synchronized with what the system was actually doing.

Recurring failure modes that produce it:

- **Mode error** — the operator issues an action that is correct for the
  mode they believe the system is in, but wrong for the mode it is
  actually in.
- **Display architecture disorientation** — the state that would explain
  the automation's behavior exists, but is buried in a sub-menu or screen
  the operator isn't looking at. A documented military instance: the USS
  Vincennes's combat display in 1988 showed an aircraft's altitude only as
  a raw number on a small side panel, with no trend indicator, forcing
  crew to mentally track a fast-changing figure by memory across
  successive glances under time pressure and radio-channel noise — a
  design gap significant enough that a formal investigation recommended
  adding a trend indicator to the main display afterward.
- **Uncoordinated entries** — one operator (or one automated process)
  changes a setting or input without it being cross-checked or visible to
  the others relying on it. The same Vincennes incident had a second,
  distinct instance of this: the tracking system silently recycled a
  retired track number and reassigned it to an unrelated aircraft
  mid-incident; because the reassignment wasn't clearly broadcast, crew
  members querying "that track" by number were unknowingly pulling live
  data for two different physical aircraft, each internally consistent
  and each wrong about the one everyone believed they were discussing.
- **Workload clutter** — the interaction the automation demands peaks at
  exactly the moment the operator has the least attention to spare.
- **Data overload** — the volume of automation-generated readouts and
  alarms exceeds what a human can triage in real time, burying the signal
  that mattered.
- **Noticing non-events** — human perception is tuned to detect change;
  automation that silently fails to act (a drift it should have corrected,
  a step it should have taken) produces no cue at all, so the absence goes
  unnoticed until it compounds.

These are the operational counterpart to [automation
bias](automation-bias.md): automation bias describes the skill an operator
loses from disuse over time, while automation surprise describes the
moment-to-moment gap between what automation is doing and what its
operator believes it is doing. Designing an automated system to expose its
current mode and state clearly — not just what it intends to do, but what
it is actually doing right now — is what keeps that gap from opening in
the first place.

The canonical framing of this gap (Earl Wiener, 1989) is that operators
watching automation behave unexpectedly during a nonroutine event tend to
ask the same three questions they'd ask about an opaque human teammate's
unexplained actions: **"What is it doing? Why is it doing that? What is it
going to do next?"** An automated system whose interface can't answer
those three questions on demand — not full internal telemetry, just enough
to reconstruct current mode, rationale, and near-term trajectory — is
exposed to automation surprise more or less by design, regardless of how
correct the automation's actual logic is. See [silent correction masking a
growing failure](silent-correction-masks-growing-failure.md) for what
happens when the "what is it doing" answer is not just hard to find but
actively withheld until the automation can no longer cope.

Partial automation is especially exposed to this: at Google, a network
line-card repair tool gave technicians a "prep to drain" button with no
feedback on whether a switch had actually finished draining. Technicians —
reasonably, given the interface — treated pressing the button as
equivalent to the drain being complete, and one experienced technician who
parallelized repairs against that assumption caused a network-wide outage.
The lesson generalizes beyond that one incident: an automation surprise
caused by ambiguous state feedback is a defect in the automation's
interface, and it is exactly the kind of failure that tribal, undocumented
operator expertise papers over until the one time it doesn't — automating
the drain fully (removing the ambiguous manual handoff point entirely)
closed the gap for good, rather than training technicians harder on the
same interface.
