---
type: concept
title: Getting Stuck in Outdated Behaviours
description: >
  A system-level failure of adaptation — strategies that succeeded
  repeatedly become rigid and keep being applied even as accumulating
  evidence shows the environment has shifted past their design assumptions.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 10"
---

The third of three basic patterns by which adaptive systems fail (alongside
[decompensation](decompensation.md) and [working at
cross-purposes](working-at-cross-purposes.md)): a strategy that worked
reliably in the past stops being re-evaluated and simply gets executed
again, even once operating conditions have moved outside the assumptions it
was built for. Military tactics that stop matching a shifted battlefield and
nuclear-plant mishaps driven by rote rule-following are both instances of
the same organisational-level rigidity — this is a failure of the *system's*
learning, not any one operator's diagnosis, which is what distinguishes it
from the individual-level mechanisms in [plan-continuation
bias](plan-continuation-bias.md) and [cognitive
fixation](cognitive-fixation.md); an organisation can institutionalise this
pattern in its standard procedures long after the individuals who wrote them
are gone.

Recurring sub-patterns:

- **Oversimplification** — a strategy's success gets attributed to a
  simplified account of why it worked, and that simplified account is what
  gets reapplied, stripped of the conditions that actually made it valid.
- **Failing to revise the current assessment as new evidence arrives** —
  each new data point is fit to the existing read of the situation instead
  of being allowed to update it.
- **Failing to revise plans in progress when disruptions or opportunities
  arise** — the plan, not the situation, becomes the fixed reference point.
- **Discounting discrepant evidence** — the Columbia accident's foam-strike
  warnings are the canonical case: each new piece of contrary evidence gets
  explained away individually rather than accumulating into a revised risk
  picture (see [ambiguous threats](ambiguous-threats.md)).
- **Literal-mindedness** — especially in automated systems, executing a
  rule exactly as specified in a situation the rule's authors did not
  anticipate, because the system has no way to recognise its own
  assumptions have stopped applying.
- **Distancing through differencing** — dismissing another organisation's
  disaster as inapplicable because of surface differences, rather than
  updating on the generic failure mechanism underneath (fuller treatment in
  [armor strategies against drift](armor-strategies-against-drift.md)).
- **Cook's cycle of error** — a narrow explanation of one accident becomes
  the basis for a narrow intervention, which addresses the named cause
  without touching the systemic conditions that produced it, so the next
  accident recurs by a different specific path and receives its own equally
  narrow explanation, in a self-reinforcing loop that never widens the
  frame.

The common thread is a system that keeps confirming an old model instead of
testing whether the model still applies — the organisational-scale version
of choosing [assimilation over
accommodation](adapted-vs-adaptive-trade-off.md), and, read forward, the
mechanism inside Mitroff's [error of the third
kind](resilience-as-adaptive-capacity.md): solving the wrong problem well
rather than noticing the problem itself has changed.
