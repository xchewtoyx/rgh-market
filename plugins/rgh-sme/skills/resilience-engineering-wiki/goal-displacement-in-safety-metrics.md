---
type: concept
title: Goal Displacement in Safety Metrics
description: >
  A feedback loop faithfully optimises whatever it is actually told to
  optimise; a safety metric that is easy to measure but is not the same
  thing as safety produces exactly that metric, not safety.
sources:
  - title: "Thinking in Systems: A Primer"
    resource: "Thinking in Systems (Meadows), ch. 5-6"
---

Meadows states the mechanism plainly: "systems... have a terrible tendency
to produce exactly and only what you ask them to produce." A goal is a
system's direction-setter — whatever a balancing loop is built to correct
discrepancies against is what the system will reliably deliver, regardless
of whether that target actually tracks the underlying property anyone
cared about. Two distinct failure shapes follow from the same root cause:

- **Seeking the wrong goal**: the system obediently, transparently pursues
  its stated metric, and that is exactly the problem — an early Indian
  family-planning programme that measured success by number of IUDs
  implanted produced more IUDs implanted, including without patient
  consent; a program tracking "number of security incidents opened" can be
  satisfied by opening fewer tickets rather than by anything getting safer.
  This is **confusing effort (or throughput) with result**.
- **Rule beating**: the actors evade the *intent* of a target while
  technically satisfying its letter — filing incidents just under whatever
  threshold triggers a formal review, closing tickets to hit a queue-depth
  number rather than resolving the underlying condition. Rule beating is a
  self-organising response to a rule perceived as unworkable, and escalating
  enforcement of the same rule typically produces *more* distortion, not
  less; the more durable fix is redesigning the rule so that satisfying it
  and achieving its purpose are the same act.

Both failure modes explain why a metrics-driven safety programme can show
steadily improving numbers while the underlying hazard is unchanged or
worsening — the classic case is a falling *count* of reported incidents that
actually reflects [reporting being suppressed by
blame](blame-suppresses-reporting.md) or a shrunken definition of what
counts as reportable, not a safer system. This is the general systems-theory
version of a critique already made narrowly against human-error
bookkeeping: see [why counting and targeting 'human error'
misleads](why-error-counting-misleads.md), which lists "produces flawed
statistics" and "reifies error as a countable category" as two of seven
reasons error-rate KPIs and zero-error targets fail to measure or manage
anything real — goal displacement is the general mechanism that specific
critique is an instance of.

The practical implication for anyone setting a safety target: because a
feedback loop optimises its literal target rather than its intended
referent, the design question is never "what number should we report" but
"does hitting this number, by the cheapest available means, actually leave
us safer" — and if the honest answer is no, the metric itself is the thing
that needs fixing, not the people being measured against it.
