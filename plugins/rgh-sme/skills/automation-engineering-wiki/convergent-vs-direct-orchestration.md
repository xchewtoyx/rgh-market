---
type: concept
title: Convergent vs. Direct Orchestration
description: >
  Automation that maintains a system's state can either continuously
  reconcile it toward a declared goal, or execute an explicit ordered
  sequence of steps — and the right choice depends on whether the
  procedure has invariants that must hold mid-flight, not just at the end.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 10"
---

# Convergent vs. Direct Orchestration

Two fundamentally different shapes of automation both count as "orchestration,"
and picking the wrong one for the job produces automation that's either
needlessly convoluted or unsafe:

- **Convergent orchestration** — declare the desired end state and let a
  tool continuously drive the system toward it, self-correcting any drift
  (a manual change, an external event like a machine failure) by
  re-converging. Moving to a *new* desired state is just changing the
  declaration; the tool works out the delta and applies only what's needed.
  This is the same shape as [intent-based
  automation](intent-based-automation.md) and the reconciliation loop behind
  [self-healing](self-healing-overload-response.md): it only cares about the
  gap between current and desired state, not the path taken to close it.
  When a convergent loop must have exactly one active driver rather than
  several instances racing each other, that exclusivity itself needs a
  safe mechanism — see [lease-based exclusive
  coordination](lease-based-exclusive-coordination.md).
- **Direct orchestration** — execute an explicit, ordered, multi-step
  process where certain conditions must hold *throughout* execution, not
  just at the finish. A live database migration is the canonical example:
  clients must retain database access at every step, which forces a
  specific sequence (stand up a replica, wait for sync, force clients
  read-only, swap primary/replica roles, release read-only) — collapsing
  this into a single "desired state" declaration and letting a convergent
  tool figure out its own path risks it choosing an ordering that violates
  the mid-flight invariant, even if it reaches the same correct end state.

The deciding question is whether the procedure has invariants that must
hold *during* the transition, not just at its completion. Forcing a
mid-flight-invariant procedure through a convergent tool means encoding an
awkward chain of intermediate "desired states," each waited on before
advancing to the next — technically possible, but fighting the tool's own
model rather than using it naturally. Conversely, using direct
orchestration where convergence would do is more code to write and
maintain for no benefit, and loses convergence's automatic self-healing
against configuration drift between runs.

A harder, mostly unsolved problem is coordinating *multiple concurrent*
direct-orchestration processes that touch overlapping resources — for
example, a database migration running at the same time as a load-balancer
change and a web-server reconfiguration that all affect the same machines.
Where convergent tools can generally be run concurrently against
overlapping scope without special coordination (they're all just driving
toward compatible end states), stacking several stateful, sequenced,
invariant-bearing processes on the same resources at once is the kind of
interaction [safeguards against runaway
automation](safeguards-against-runaway-automation.md) and [interacting
automated control loops](interacting-automated-control-loops.md) are meant
to guard against, and it's still commonly handled manually rather than by
any general-purpose tooling.
