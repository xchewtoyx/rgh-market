---
type: concept
title: The Information Paradox of High-Safety Systems
description: >
  A safety programme that succeeds at driving accidents toward zero destroys
  its own traditional source of safety information in the process, and must
  build a deliberate alternative before that happens.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 17"
---

Systematic safety management has, in domains like aviation, railways, and
nuclear power, drastically reduced serious accidents — and that success
creates a genuine paradox: a high-performing, near-zero-accident system has
largely eliminated its own traditional source of safety information, because
accidents were always that information's original source. The safer a
system becomes by the old measure, the less that measure has left to tell
it.

Incident reporting systems exist specifically to resolve this paradox —
substituting continuous learning from front-line reports of near-misses and
deviations for the accident data that used to arrive on its own. This is not
a free substitution: whether reactive incident reporting can actually
deliver the intelligence accidents used to provide depends on structural
features of the domain, not just on installing a reporting programme (see
[five structural dimensions of incident reporting
viability](five-structural-dimensions-of-incident-reporting-viability.md)).

**A successful incident reporting programme runs into a second-order version
of the same paradox.** [Meta-control of risk](meta-control-of-risk.md)
already documents this for mature reporting systems like ASRS: report volume
can grow past the point where recombining and cross-referencing it yields
actionable intelligence, so even a well-designed alternative source of
information eventually needs its own successor. The information paradox is
therefore not a one-time transition from accidents to incidents — it recurs
every time a system's existing learning mechanism succeeds well enough to
run out of the kind of signal it was built to use.
