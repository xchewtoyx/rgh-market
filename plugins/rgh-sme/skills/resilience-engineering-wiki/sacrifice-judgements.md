---
type: concept
title: Sacrifice Judgements and the True Test of Safety Culture
description: >
  Explicit decisions to relax production pressure to stay clear of a safety
  boundary; the real test of a safety culture is how it treats a sacrifice
  that, in hindsight, turned out not to have been necessary.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 2"
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 12"
---

A sacrifice judgement is a deliberate decision to temporarily relax an acute
production or efficiency goal in order to protect a chronic safety goal:
converting a laparoscopic surgery to an open procedure on suspicion of a
problem, breaking off an approach for possible windshear, a technician
delaying a departure over a subtle suspected defect, or a local production
slowdown with no confirmed fault yet. Each trades a certain, visible,
immediate cost against an uncertain, invisible, future one — the opposite
direction from the usual [efficiency–thoroughness
trade-off](efficiency-thoroughness-trade-off.md), which is why it takes a
deliberate act rather than happening by default.

The organisational-scale version of this same trap is [the safety
paradox](strongly-emergent-resilience-and-self-defeating-prophecy.md): a
functioning safety culture works precisely by preventing the disaster it
warns of, which makes its success look, after the fact, exactly like the
warning was never needed.

**The true test of a safety culture is not how it treats the sacrifice that
was vindicated.** Every organisation tells itself flattering stories about
rewarding the operator who stopped the line and was later proven right. The
real test is the much more common case: the operator sacrifices production,
and the subsequent check finds nothing wrong. If leadership or peers treat
that "unnecessary" sacrifice as wasted time, second-guess it, or quietly
penalise the operator's throughput numbers, the organisation is teaching
everyone — implicitly, without ever issuing an instruction — to accept a
higher level of unrecognised risk before sacrificing production next time.
This is the same mechanism [hindsight bias](hindsight-bias.md) runs on:
retrospection judges the sacrifice by the outcome it produced (nothing found)
rather than by the uncertainty that was actually present at the time the
decision was made, and warning signs that were genuinely ambiguous in the
moment look "obvious" once the outcome is known either way.

**Double binds defeat sacrifice judgements structurally**, independent of any
individual's willingness to make one. Aircraft de-icing holdover time is
fixed at the moment of treatment, but it keeps eroding while the aircraft
waits in a takeoff queue; if the organisation's schedule pressure makes
accepting the queue delay the default and there is no clean, costless way to
re-enter the de-icing process, ice can accumulate past the safe margin during
a wait nobody treated as a decision point at all. The sacrifice judgement
never gets made because the situation never presents itself as one — this is
the accountability structure itself, not operator judgement, failing to
protect the chronic goal.

The organisational stakes run in both directions: an organisation that fails
to actively *support* workers in making sacrifice judgements does not stay
neutral by default — it drifts toward operating at a higher level of risk
than it intended, because every unsupported sacrifice judgement an operator
declines to make is production pressure winning by default rather than by
decision.

Sacrifice judgements are distinct from [sacrificing decisions under
crisis](sacrificing-decisions-under-crisis.md), despite the shared
vocabulary: a sacrifice judgement is proactive, made with time still
available, to stay clear of trouble before it starts; a sacrificing decision
is reactive, made once a crisis is already underway, choosing between bad
options purely to bound the worst case.

Making a sacrifice judgement at all requires first having [traversed the
goal-means hierarchy](traversing-the-goal-means-hierarchy.md) far enough to
see the higher-level goal the sacrifice actually protects — a practitioner
reasoning only at the concrete, low-level goal has nothing to weigh the
sacrifice against.

At the managerial level specifically, whether a sacrifice judgement survives
contact with power above the manager making it is what determines whether
[middle managers actually function as a safety
buffer](middle-managers-as-safety-buffer.md) against executive production
pressure, or fail to.

Because these decisions are made under uncertainty and are easy to punish
retrospectively regardless of which way they go, resilience engineering
treats supporting them as a design problem: decision support and dynamic
criteria that keep the current distance to the [safety
boundary](rasmussen-boundary-model.md) visible, rather than relying on
individual nerve exercised against organisational headwind.
