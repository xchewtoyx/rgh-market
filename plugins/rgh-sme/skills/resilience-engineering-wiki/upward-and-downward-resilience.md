---
type: concept
title: Upward and Downward Resilience
description: >
  Resilience is a cross-scale process — macro-level goal-setting and intent
  ("downward") meeting frontline craftsmanship and improvisation ("upward")
  — and it fails when either direction is missing, not just when one is.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 12"
---

Resilience to goal conflict runs in two directions between organisational
levels, and both must work for the system to stay clear of its [safety
boundary](rasmussen-boundary-model.md).

**Downward resilience** is what macro-level structures give the sharp end to
work with: policy, infrastructure, and explicit procedures that prepare the
system for handling trade-offs, plus something procedures alone cannot
supply — communicated *intent*. When supervisors and regulators make the
strategic reasoning behind a goal or rule explicit, not just the rule itself,
frontline operators can extend that reasoning correctly to novel situations
the rule never anticipated. Explicit safety goals also function as a
diagnostic yardstick: a deviation from them is a legible signal to management
that operations are encroaching on the safety boundary, in a way a raw
production number cannot be. When downward guidance is absent, ambiguous, or
internally contradictory, operators have no basis for judging whether their
local rule adaptations remain safe — deviations go unmonitored, accumulate,
and this is the raw material of [normalisation of
deviance](normalization-of-deviance.md) and [drift into
failure](drift-into-failure.md).

**Upward resilience** is what the sharp end feeds back: domain experience,
problem-solving flexibility, and professional craftsmanship applied to the
"hidden grey zones" between static written procedures and the actual demands
of the moment — the same territory [procedures as resources for
action](procedures-as-resources-for-action.md) describes. This is the
generative side of adaptation, the reason variability produces success far
more often than failure ([Safety-II](safety-i-and-safety-ii.md)). Its
characteristic failure mode is not laziness or carelessness but frontline
actors becoming fixated within a single problem frame and failing to
re-evaluate as new information arrives — [cognitive
fixation](cognitive-fixation.md) operating at the point where an operator's
adaptation is supposed to be flowing information back up, not just holding
the line locally.

A field study of Norwegian aircraft line maintenance shows upward resilience
inventing its own tools when downward guidance is missing. Technicians
facing intense conflict between scheduled departure times and unresolved
technical defects would log an ad-hoc, invented category — "delay due to
technical reasons" — specifically to artificially manufacture the time
buffer a repair actually needed, a self-authored [action
rule](goal-process-action-rules.md) built to compensate for a [goal rule
that regulators above them had never made explicit](goal-process-action-rules.md).
The same study names the systemic risk of leaning on upward resilience this
heavily and this consistently: sustained reliance on individual
professional judgement, uncorrected by any goal-level guidance from above,
can itself tip into overconfidence — operators taking on risk they no
longer register as risk, or bypassing formal rules as a matter of routine
rather than considered judgement, precisely because upward resilience has
had to substitute for downward resilience for so long that the substitution
stops feeling like one.

**Anticipation itself is not evenly distributed across the two directions.**
The global system level anticipates remote, low-probability catastrophes an
individual sharp-end operator would rarely contemplate locally (an airliner
losing both engines simultaneously); local operators anticipate fine-grained,
contextual variation invisible from the design level. Defence-in-depth
against a known hazard class — minimising strike frequency, engineering
tolerance into hardware, then providing a procedure for the worst case —
works because each layer is aimed at the kind of anticipation its level is
actually positioned to do; it fails when a global-level layer tries to
substitute for local, contextual anticipation it cannot see, or vice versa.

Deliberately **contrasting** the two perspectives — putting the sharp end's
operational view and the blunt end's management view side by side on
purpose — is itself an anticipation practice, not just a post-hoc
reconciliation. Latent vulnerabilities in highly interdependent processes
are often invisible from either vantage point alone and only show up in the
juxtaposition: what looks like margin from the blunt end's aggregate metrics
can be visibly gone from the sharp end's local view, and vice versa.

Neither direction substitutes for the other. Downward guidance without
upward craftsmanship produces brittle, over-specified procedures that cannot
cover real variability; upward craftsmanship without downward intent produces
locally sensible improvisation with no organisational visibility into how far
it has drifted from what leadership believes is happening — the standing gap
[work-as-imagined versus work-as-done](work-as-imagined-vs-work-as-done.md)
describes at organisational scale. How the two directions are supposed to
connect through an organisation's rule structure is addressed in [goal,
process, and action rules](goal-process-action-rules.md).
