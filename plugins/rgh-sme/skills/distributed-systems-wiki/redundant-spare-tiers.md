---
type: concept
title: "Redundant Spare Tiers: Hot, Warm, and Cold"
description: >
  A general availability spectrum — how synchronized a standby is with the
  active node trades recovery speed against the runtime cost of keeping it
  current, from millisecond hot failover to power-on-reset cold failover.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 4"
---

# Redundant Spare Tiers: Hot, Warm, and Cold

Any design that keeps a standby ready to take over from a failed component
sits somewhere on one spectrum: how closely does the standby's state track
the active node's state right now? That single dial determines both failover
time and steady-state cost, and it recurs across replication, load
balancing, and network-link protection under different names.

- **Hot spare (active redundancy).** All nodes in the protection group — one
  or more active plus spares — process identical inputs in parallel, so the
  spare's state is always synchronously current. Failover takes
  milliseconds because there's nothing left to catch up. This is the same
  shape as [synchronous replication](synchronous-vs-asynchronous-replication.md):
  every write is confirmed on the standby before it's confirmed to the
  client, at the cost that the standby's health gates the active node's
  responsiveness.
- **Warm spare (passive redundancy).** Only the active node processes
  traffic; it periodically pushes state updates to the spare, so the
  spare's state is only as fresh as the last update. This is
  [asynchronous replication](synchronous-vs-asynchronous-replication.md)'s
  shape: the active node stays fully responsive regardless of the spare's
  health, but [failover](leader-failover.md) can lose whatever changed since
  the last push — the size of that loss window is a direct function of the
  update period.
- **Cold spare.** The spare stays powered off or entirely out of service
  until failover, then must complete a full power-on/reinitialization
  before it can take over. Worst mean-time-to-repair of the three, and
  unsuited to any availability target that can't absorb a multi-minute (or
  longer) gap.

The three converge to the same mechanism once a component is stateless —
with nothing to synchronize, "hot" and "cold" differ only in whether the
spare is already running, not in what state it holds. For stateful
components the tradeoff is unavoidable: hot costs the most to run
continuously and recovers fastest; cold costs the least and recovers
slowest. Choosing a tier is really choosing a point on this curve to match
a [recovery time objective](leader-failover.md), not a one-size answer —
the same logic that picks fully synchronous vs. semi-synchronous vs.
asynchronous replication for a database leader applies equally to load
balancer pairs, network link protection, and any other component with a
standby.
