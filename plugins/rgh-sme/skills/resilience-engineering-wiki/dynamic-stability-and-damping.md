---
type: concept
title: Dynamic Stability, Damping, and Confined Recovery
description: >
  Resilience redefined for a systemic accident model — not resisting
  disturbance but reacting early enough that recovery stays local, because
  damping caught the deviation before it grew large enough to spread.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 1"
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 3"
---

Under a [systems-theoretic](systems-theoretic-accident-model.md) view, safe
operation is not a fixed, static condition — it is **dynamic stability**: a
system continuously perturbed by [performance
variability](safety-i-and-safety-ii.md) that stays safe because deviations
are damped rather than amplified. **Damping** is the progressive reduction
of an oscillation or deviation over time; a system that damps well converts
routine disturbance into routine correction, and a system that doesn't
converts the same disturbance into escalating instability.

The size of an eventual correction is not fixed by the size of the original
disturbance — it depends on how early the system detects and reacts. Catching
a deviation early keeps the required adjustment small and the recovery
**confined** to the local subsystem where the deviation started. Miss the
early window and the same deviation propagates before anything responds,
forcing a larger, more disruptive correction across more of the system —
this is why margin, once eroded past a certain point, cannot be recovered
proportionally: the cost of correction rises faster than the size of the
thing being corrected. This gives resilience a sharper, more operational
definition than "coping with disruption" in general: **the ability of a
system or organisation to react to and recover from disturbances at an early
stage, with minimal effect on its own dynamic stability.**

A system moving through decreasing dynamic stability passes through
recognisably different **operational modes**, not a smooth continuum: normal
functioning, reduced/irregular functioning, and disturbed functioning. A
resilient system's job is not only to stay in normal functioning as long as
possible but to actively detect which mode it is currently in and sustain
required operation *within* that mode once a transition has happened, rather
than continuing to act as though nothing has changed — misreading a reduced
or disturbed mode as still-normal is what lets a deviation go undamped long
enough to reach [decompensation](decompensation.md).

**The substitution myth** is the standing obstacle to acting on this
definition: the assumption that introducing an artefact or intervention into
a system produces only its intended, local effect, with no side effects
elsewhere. In reality every intervention triggers broader system changes —
new load on adjacent processes, new failure paths, new [complexity from the
relationships it adds](redundancy-can-increase-complexity-risk.md) — so an
intervention chosen to fix one thing is itself a fresh disturbance the system
now has to damp. Believing the myth is what makes early detection hard to
prioritise: if a fix is assumed to have no side effects, there is no reason
to watch for the side effects that damping actually depends on catching
early.

Because dynamic stability is a systemic, moment-to-moment property rather
than a structural one, it cannot be assessed by inspecting components or
tracing fixed causal chains — see [the structural limits of tree-based risk
assessment](structural-limits-of-tree-based-risk-assessment.md) for why the
standard risk-analysis toolkit is built for the wrong kind of model.
