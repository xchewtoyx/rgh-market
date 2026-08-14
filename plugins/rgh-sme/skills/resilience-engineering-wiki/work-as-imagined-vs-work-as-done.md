---
type: concept
title: Work-as-Imagined vs Work-as-Done
description: >
  The inevitable gap between how work is specified in rules and procedures
  and how it must actually be performed under real conditions — the gap where
  both resilience and drift live.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 1"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 7"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 3"
---

Work-as-imagined is the version of work that exists in procedures, rules, and
management's mental model: complete inputs, adequate time, no competing
demands. Work-as-done is what practitioners actually do to make the system
succeed under real conditions — adapting, bridging gaps in the rules,
absorbing [goal conflicts](goal-conflicts-and-production-pressure.md) the
procedures ignore. The gap between them is inevitable, not a compliance
failure: no procedure can anticipate all operating conditions.

Consequences of ignoring the gap:

- **Imposing more rules doesn't close it** — it drives real practice
  underground, so management loses sight of how work is actually done (the
  Old View's second failed countermeasure; see [old view vs new
  view](old-view-vs-new-view-of-human-error.md)).
- **"Violation" findings are usually artefacts**: behaviour is being judged
  against work-as-imagined. Where routine departures have become the local
  norm, that is [normalisation of deviance](normalization-of-deviance.md),
  and the interesting question is why the departure made local sense
  ([local rationality](local-rationality-principle.md)) — as is judging
  culpability against unworkable rules (see [just culture](just-culture.md)).
- **The gap is where safety is made and lost.** The everyday adaptations in
  work-as-done are the performance variability that
  [Safety-II](safety-i-and-safety-ii.md) credits for routine success; the
  same unmonitored gap is where [drift into
  failure](drift-into-failure.md) accumulates.

Two case studies show the gap operating from opposite ends of formality.
Commercial aircraft line maintenance splits sharply along role: supervisors
equate safety with procedure compliance (a signed-off card means the
procedure was followed), while mechanics working under tight turnaround
pressure treat their own ability to adapt, invent, and improvise as what
actually keeps aircraft safe — informal workarounds function as marks of
expertise and professional pride, not as violations, from inside the role
that performs them. International disaster relief work shows the same
pattern at the other end of formality entirely: headquarters mandates
political accountability and strict protocol, while field workers routinely
dissociate from those distant goals and improvise across political and
organisational boundaries based on whatever local experience and access
they actually have.

**When an incident does surface this gap, the common management response
makes it worse.** McDonald's "cycles of stability": an incident triggers
outrage at the discovered violation, and the organisation responds by
reasserting the very rules the incident just showed were not being followed
— rather than updating its model of how the work actually gets done. This
just resets the gap to reopen the same way, and it is the mechanism
underneath [the fallacy of the quick fix](fallacy-of-the-quick-fix.md)'s
"write a new procedure" reflex specifically.

**The gap is not uniformly bad — it has two faces.** A large gap driven by
uncalibrated leadership (management genuinely not knowing what makes
operations succeed or fail) is macro-level brittleness: the organisation is
steering by a model of its own operations that is simply wrong. But part of
the gap at the sharp end is [subversive investment in
slack](subversive-slack-hoarding.md) — practitioners deliberately hiding
reserve capacity from a management view that would otherwise consume it —
which is a genuine resilience buffer, not a defect, even though it looks
identical to "workers not following the rules" from the outside. Closing the
whole gap indiscriminately can destroy this second kind along with the
first.

Practical rule: to know your system's real risks, study work-as-done — go
where the work is, as [chronic unease](chronic-unease.md) prescribes — rather
than auditing conformance to work-as-imagined.

Fujita's commentary names the same gap **front-end versus back-end
mismatch**: front-end personnel (operators, maintenance) are naturally
adaptive, making continuous minor adjustments, but cannot anticipate how
several of their own simultaneous adjustments will interact; back-end
management and regulators hold static, idealised assumptions that the
system operates exactly as written. The gap between the two — dynamic front-end adaptation against static
back-end assumption — is what generates latent hazards that drive drift,
the same mechanism [the law of stretched systems' "evil
chain"](law-of-stretched-systems.md) names for a performance-optimisation-
driven version of the identical gap.
