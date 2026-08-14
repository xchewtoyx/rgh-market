---
type: concept
title: Cell-Based Isolation (Failure Domains)
description: >
  Partitioning a system into multiple independent, equivalent copies (cells)
  so a single event's blast radius is bounded to one copy instead of the
  whole fleet.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 8"
---

# Cell-Based Isolation (Failure Domains)

A **failure domain** (also called a **cell**) is a blast-radius control that
works by functional isolation rather than by structural separation: instead
of dividing a system by role, location, or time, split it into several
complete, equivalent, and independent copies of the whole system, each
holding only a fraction of total capacity and data. A cell looks like the
entire system to its clients — any cell can take over the work of a failed
one — but a single fault (bad config push, corrupted data, resource
exhaustion) that stays confined to one cell only removes that cell's slice of
capacity, not the whole fleet's. This is the same shape as [cloud regions and
availability zones](cloud-regions-and-availability-zones.md), generalized:
zones buy isolation from *physical* infrastructure faults, while cells buy
isolation from *logical* faults — a bad deploy, a poison-pill request, a data
corruption bug — that physical separation alone does nothing to contain. It
is the concrete answer to the blast-radius question that
[cascading failures](cascading-failures.md) raises but leaves unresolved:
architecture, not just per-service circuit breaking, decides how far a
failure can spread.

## Data isolation is what makes a cell actually independent

A cell is only as independent as its data. Each cell needs its own data copy
so that bad data — corrupted input, a buggy write, an admin mistake — stays
confined the same way a code fault does. Two complementary techniques:

- **Gate what enters a cell.** Validate every data update before it's
  accepted, rate-limit how fast global changes can roll out across cells,
  and reserve unchecked writes for an explicit emergency-override path
  (a *breakglass* mechanism) rather than ordinary operation. This is the
  same instinct behind never letting a single [control-plane
  action](control-plane-vs-data-plane.md) touch every cell at once — a
  fleet-wide automated push is exactly the kind of correlated fault a cell
  boundary is supposed to stop, so it has to be deliberately throttled or
  staged across cells rather than applied atomically.
- **Keep the last known good state on hand.** A cell that caches its most
  recent valid configuration/data locally can keep serving it if the source
  of new data becomes unreachable or starts serving corrupted data —
  trading staleness for availability, the same tradeoff [follower
  reads](follower-reads.md) make deliberately.

## What cells buy beyond fault containment

- **Cheap, real canarying.** With two or more cells and a policy that never
  updates all of them simultaneously, one cell serves as a live canary: push
  a change to it first, compare behavior against the others, and only then
  roll forward. This is the same rollout discipline behind [rolling upgrade
  compatibility](rolling-upgrade-compatibility.md), applied at the
  whole-cell granularity instead of per-node.
- **Version diversity as a fault-tolerance lever.** Running different
  software versions across cells means a single new bug can't break every
  cell at once — a cell boundary is a natural place to stop a bad rollout
  before it reaches 100% of traffic.
- **A unit for targeted chaos and load experiments.** Because a cell has a
  fraction of total capacity, driving it toward its limits (to validate load
  shedding or throttling behavior) takes far less injected load than
  attacking the whole system, and the other cells' healthy metrics give an
  immediate baseline for how much damage the experiment actually caused.

## The recurring cost

None of this is free, and the cost recurs for the life of the system, not
just at design time:

- Every cell needs its own copy of configuration, keyed by cell identity,
  which must be kept mutually consistent without letting a single
  distribution mechanism become the very fleet-wide dependency cells exist
  to avoid.
- The split has to stay invisible to clients — callers should not
  accidentally couple to a specific cell — which pushes the cell-selection
  decision into [request routing](request-routing.md).
- Dependencies need partitioning too: a shared downstream dependency that
  isn't itself cellularized reintroduces a single point of correlated
  failure underneath cells that otherwise look independent.
- A cell can still fail completely on its own — cellularization only bounds
  *how many* copies a fault can reach, it doesn't make any individual copy
  more reliable. The system's overall resilience still depends on each
  cell's own component reliability, and increases only as more, smaller
  cells are added — a return that trades off against the operational cost
  above.
