---
type: concept
title: Toil Budget (the 50% Rule)
description: >
  Capping toil and on-call at half of operational time, with a mechanism to
  push the surplus back to development teams when the cap is exceeded,
  protects the other half as guaranteed time for the engineering work that
  removes toil permanently.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 5"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 18"
---

# Toil Budget (the 50% Rule)

Stating "we should minimize toil" as a value isn't enough to actually
protect engineering time from being consumed by it — operational work
tends to expand to fill whatever time is available, because it's reactive
and each individual ticket feels urgent. The concrete mechanism is a hard
cap: [toil](toil.md) plus on-call work must not exceed 50% of operational
time, which guarantees the remaining 50% (minimum) for
[engineering work](engineering-work-vs-toil.md) — building the software,
tooling, and automation that removes toil instead of just doing it.

The cap needs an enforcement path to be real. When toil exceeds the 50%
threshold, the surplus tickets and alerts get assigned back to the
development team that owns the underlying system, rather than absorbed
by the operations team. This isn't just load-shedding — it's a deliberate
incentive: the team that has to eat the pain of unaddressed toil is also
the team with the ability to fix the architecture that's generating it.

This budget is what makes [the case for eliminating
toil](case-for-eliminating-toil.md) actionable rather than aspirational,
and it's the same discipline that protects time for [treating operational
tooling as production software](software-engineering-rigor-for-ops-tooling.md)
— that work only happens if toil isn't allowed to consume the time it needs.
