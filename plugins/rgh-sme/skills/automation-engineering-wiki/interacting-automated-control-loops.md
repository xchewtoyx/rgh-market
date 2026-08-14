---
type: concept
title: Interacting Automated Control Loops
description: >
  Two automated systems that are each individually correct can still drive
  each other into a runaway feedback loop if they were built and tuned
  without a shared view of how their signals affect one another.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 11"
  - title: "Thinking in Systems: A Primer"
    resource: "Thinking in Systems: A Primer (Meadows), ch. 2"
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Dekker), ch. 3"
---

# Interacting Automated Control Loops

Autoscaling, load balancing, and load shedding are usually built and tuned
by different engineers at different times, each one reacting to its own
observed signal. Treated as independent systems, each can be individually
correct — and still combine into a feedback loop that none of them, in
isolation, was buggy enough to cause.

One documented case: a load balancer measured per-request CPU cost to
decide where to route traffic. One region hit its load-shedding threshold
first and began rejecting a large share of requests — but a *rejected*
request is cheap to serve, so that region's average measured cost dropped,
making it look more efficient than the others. The load balancer responded
by routing it *more* traffic, which pushed it to shed even more, which made
it look even more "efficient" — a positive feedback loop that concentrated
load onto the one region already failing, while healthier regions sat
under-used.

The fix wasn't tuning any one system harder; it was making load shedding
and load balancing share a consistent view of cost — counting a shed or
errored request as effectively over 100% capacity used, so an overloaded
region reads as full rather than efficient. More generally, wherever
several automated systems each drive on their own signal but touch the
same underlying resource, the interaction between them needs to be
designed and monitored as its own thing:

- Coordinate emergency shutdown/kill triggers across all of them, not just
  each one individually — see [safeguards against runaway
  automation](safeguards-against-runaway-automation.md).
- Add monitoring specifically for the feedback path between systems, not
  just for each system's own health.
- Sequence them deliberately — e.g. tune autoscaling to trigger before load
  shedding kicks in, not after, so the systems escalate in the intended
  order rather than fighting for the same signal at the same time.
- Set a floor (a minimum instance count, a minimum traffic share) under any
  location, to stop a "route toward apparent efficiency" loop from
  collapsing all load onto one increasingly overloaded target.

This is the systemic version of what a single [governor
pattern](governor-pattern.md) or [autoscaling safety
practice](autoscaling-safety-practices.md) bounds for one automated system
on its own — the same discipline of explicit limits and monitored feedback
applies across the boundary between systems, not just within each one.

This is also why adding safeguards is not a free way to buy safety: every
additional automated control loop, governor, or safety check is itself a
new component with its own relationships to the rest of the system, and
each such addition multiplies the number of ways components can interact
unexpectedly. A system layered with enough individually-reasonable
automated safeguards can become more complex — and therefore harder to
fully reason about — than the risk any single safeguard was added to
address, which is part of why bounding *interactions between* safeguards
matters as much as strengthening each one individually.

A general reason these interactions oscillate rather than settle: any
control loop that corrects a stock based on a delayed reading of that stock
is prone to overshoot, because it keeps correcting for a state that no
longer reflects reality by the time the correction lands. Autoscaling
reacting to a lagging load metric, or a load balancer redistributing traffic
based on a cost measurement one polling interval stale, are both this
pattern. The fix is rarely "make it react faster" — a control loop that is
already overreacting to noise gets *worse*, not better, when its reaction
delay is shortened, because it starts correcting before the previous
correction has even taken effect. Where the loop's reaction is the thing
overshooting, the more effective (and less intuitive) fix is often to slow
it down: widen the sampling window, react to a smaller fraction of the
perceived gap per cycle, or otherwise damp the correction — the same lever
[autoscaling safety practices](autoscaling-safety-practices.md) uses when it
asks for scale-up and scale-down to move at different speeds rather than
symmetrically.
