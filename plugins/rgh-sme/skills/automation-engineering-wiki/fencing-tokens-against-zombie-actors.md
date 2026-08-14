---
type: concept
title: Fencing Tokens Against Zombie Actors
description: >
  A control-loop instance or leader that was presumed dead and superseded
  can wake up and keep acting on stale authority unless every action it
  takes is tagged with a monotonically increasing token the rest of the
  system can use to reject it.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 6 (Leader and Followers), ch. 7 (HeartBeat)"
---

# Fencing Tokens Against Zombie Actors

Failure detection in automation is never certain — a heartbeat-based check
can only ever conclude "this actor has been silent longer than our
timeout," never "this actor has actually stopped running." A control-loop
instance, cron leader, or reconciliation worker can be marked dead because
of a GC pause, a network partition, or a slow disk write, then resume
exactly where it left off once the pause ends — with no idea that the rest
of the system has already elected a replacement and moved on. If that
"zombie" actor's next action is allowed through, it can silently undo or
race against work the new leader is already doing, and neither instance
finds out until the state has diverged.

The fix is not a better failure detector — no timeout tuning eliminates
false positives, since [confidence decay in unpracticed
safeguards](confidence-decay-in-unpracticed-safeguards.md) and ordinary
process pauses are always possible. Instead, every change of leadership
increments a **fencing token** (also called a generation number or epoch):
a monotonically increasing counter bumped once per election, attached to
every subsequent write or action that actor takes. Whatever the actor is
writing to — a shared datastore, a downstream API, another service's
queue — rejects any action tagged with a token lower than the highest one
it has already seen. A superseded actor's actions are therefore not
merely *ignored by convention*; they are *structurally unable to succeed*,
because the receiving side enforces the ordering, not the sender's own
(possibly stale) belief about whether it's still in charge.

This is the same problem [safeguards against runaway
automation](safeguards-against-runaway-automation.md) address for a single
system acting too fast or too broadly, applied to a different failure
mode — sometimes called **split brain**: two instances of the same
automation both believing they are the one authorized actor, each acting
on that belief without knowing the other exists. It also complements
[idempotency](idempotency-in-automation.md) rather than replacing it —
idempotency makes a *duplicate* action harmless, but a zombie actor's
action is not a duplicate of the new leader's decision, it's a
contradictory one made from stale information, which idempotent retry
logic alone does nothing to stop.

A concrete instance of the same principle: consensus systems (Raft,
Zookeeper's ZAB) bump this token on every leader election and require a
newly-elected leader's log to be at least as up to date as a majority of
the cluster before it can win an election at all — which is what lets a
recovering ex-leader safely discard any of its own uncommitted entries
and re-sync from the current leader instead of trying to reassert them.
The same shape applies to any automation with an exclusive-actor
requirement: attach the current generation to the lease that grants
exclusivity, and make every downstream effect check it.
