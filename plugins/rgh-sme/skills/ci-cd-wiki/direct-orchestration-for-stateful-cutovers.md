---
type: concept
title: Direct Orchestration for Stateful Cutovers
description: >
  An explicit, ordered multi-step deployment process used when intermediate
  states must satisfy invariants throughout — unlike convergent
  configuration management, which only guarantees the final declared state.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 10"
---

# Direct Orchestration for Stateful Cutovers

[Idempotent provisioning](idempotent-provisioning.md) and convergent
configuration management (Puppet, Chef, Ansible-style tools) work by
declaring a desired end state and letting the tool drive the system toward
it, self-correcting drift along the way. That model is a poor fit whenever a
process has invariants that must hold at every intermediate step, not just
at the end — a live database migration is the canonical case: clients must
retain access throughout, so the process can't simply declare "database is
now on host B" and let a convergence engine figure out the path.

## The pattern

Direct orchestration instead executes a fixed, ordered sequence of steps,
each one a precondition for the next. A database host migration under this
model looks like:

1. Configure the new host as a replica of the current primary.
2. Wait for replication to catch up.
3. Put clients into temporary read-only mode.
4. Swap roles: the new host becomes primary, the old one becomes replica.
5. Take clients out of read-only mode, now pointed at the new primary.

Forcing this through a purely convergent tool would require encoding each of
these as its own separate "desired state," waiting for convergence before
declaring the next state — an awkward, easy-to-get-wrong workaround for what
is naturally a linear procedure with a mid-flight invariant (clients must
never see the database as simultaneously writable in two places, or fully
inaccessible for longer than the read-only window).

## When to reach for it

Use direct orchestration specifically when a [rollout](rolling-deployment.md)
or migration has a state that is only safe to pass through briefly (read-only
mode, dual-write mode, a drained-but-not-yet-decommissioned node) rather than
one that's equally valid to sit in indefinitely. Ordinary application
deployment — where each host's end state is independent and self-contained —
is exactly the case convergent tooling handles well; reach for an explicit
step sequence only when the invariant genuinely spans multiple steps.

## The unsolved edge: concurrent direct-orchestration processes

Coordinating two direct-orchestration processes that touch overlapping
resources at the same time (e.g. a database migration running concurrently
with a load-balancer change touching the same hosts) is still largely a
manual, error-prone problem — there's no standard tooling equivalent to a
distributed lock across arbitrary orchestration procedures. Treat "is another
orchestrated change touching these hosts right now" as a question a human
has to answer before kicking off a stateful cutover, not one automation
currently answers for you.
