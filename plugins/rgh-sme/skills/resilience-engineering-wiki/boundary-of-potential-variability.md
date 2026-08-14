---
type: concept
title: The Boundary of Potential Variability
description: >
  Situations anticipated in advance, however unlikely, stay inside a
  system's envelope of potential variability; situations no one envisaged at
  all are qualitatively different, and resilience depends on recognising
  which kind is currently underway.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 1"
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 3"
---

Cuvelier and Falzon's distinction separates two categories of demanding
situation that feel similar from inside but call for opposite responses:

- **Potential situations** — events envisaged before the fact, however rare
  or severe, and managed within an expected envelope of variability. A
  scripted emergency procedure, an engineered tolerance, a rehearsed crisis
  plan all exist because someone already put the situation inside this
  envelope.
- **Unthought-of or unprecedented situations** — genuinely out-of-bounds
  events, typically produced by compounding failures (an equipment fault
  interacting with an inter-team breakdown) that no one, at any level,
  foresaw together.

The core resilience mechanism this distinction demands is **detecting and
accepting that the boundary has been crossed** — that the situation now in
progress is the second kind, not the first, so a predefined response no
longer applies and improvisation is required instead of harder execution of
the plan. Accidents recur from the failure of exactly this step: operators
persist with a de-adapted strategy — one tuned to the anticipated envelope —
well past the point the actual situation left it, because nothing marks the
crossing as an event. This is the same mechanism as [plan-continuation
bias](plan-continuation-bias.md) and the same absorption dynamic as
[ambiguous threats](ambiguous-threats.md): the cues that would signal the
boundary has been crossed are exactly the weak, late, ambiguous cues that
lose to strong early ones.

One observable **transition indicator** is the decision to request external
assistance — an anaesthetist calling in a colleague, a crew declaring an
emergency to air traffic control. The act of asking for help is itself a
recognition, made externally visible, that the situation has moved from
controlled operation to crisis management; it is worth treating as a
deliberately protected, non-punished option for exactly this reason (the
same logic behind [permission stories](permission-stories.md) and
non-punitive go-around policies). A study of 22 near-accident anaesthesia
cases found calling for help was not a reflex triggered automatically once
resources ran out — it was itself a multi-criteria trade-off decision,
weighing colleague availability, time of day, the specific task at hand, and
the practitioner's own self-assessment of capability, made under the same
severe time pressure as everything else in the crisis.

**Classification of an event as "potential" or "unthought-of" is
subjective, not objective.** What determines the category is not an
independent measure of the event's complexity or severity but "the
astonishment of the perceiver" — whether *this* practitioner, with their
specific training and experience, had the event inside their own envelope of
anticipation. The same clinical event can be a routine potential situation
for one practitioner and a genuine unthought-of situation for another,
which is why building the anticipated envelope is itself a distinct,
practice-improvable skill rather than a fixed property of the event
catalogue: it draws on formal training, personal memory of past close calls,
and tacit, barely-articulable perceptual cues ("bad feelings") built from
experience. Three levers follow directly from decomposing the envelope this
way: reduce the objective uncertainty of the event itself (research,
incident modelling that codifies warning signs); train the anticipatory
skill directly (reflective practice, debriefing that surfaces tacit
knowledge); and align the envelope across roles, since a surgeon,
anaesthetist, and hospital administrator working from different unstated
envelopes of what counts as "expected" is itself a source of the
[cross-purposes](working-at-cross-purposes.md) that turns a locally
manageable event into a coordination failure.
