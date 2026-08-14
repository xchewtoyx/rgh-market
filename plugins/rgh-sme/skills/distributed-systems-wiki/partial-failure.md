---
type: concept
title: Partial Failure
description: >
  The defining hazard of distributed systems: some components fail
  nondeterministically while the rest keep working, so the system is never
  simply "up" or "down".
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 8"
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 1"
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 1, Why Distribute?"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 7"
---

# Partial Failure

A single computer is close to deterministic: hardware faults typically cause a
total crash, and an operation either works or it doesn't. A distributed system
has no such binary state — some nodes, links, or processes fail while others
work normally, and which ones are failing is **nondeterministic and often
unknowable** from any single vantage point. A request may even have succeeded
without the requester ever learning it (see [unreliable
networks](unreliable-networks.md)).

Vocabulary that keeps the reasoning straight: a **fault** is one component
deviating from spec; a **failure** is the system as a whole ceasing to
provide service. Faults can't be reduced to zero — fault *tolerance* means
preventing faults from escalating into failures. Note also that fault types
differ in correlation: hardware faults are mostly independent (in 10,000
disks, roughly one dies per day — routine), while software faults are
*correlated* — the same bug or leap-second edge case fires on every node at
once, which is why systematic software faults cause the larger outages and
why redundant hardware alone is insufficient. The arithmetic of independent
faults still bites at scale: if a single disk fails on any given day with
probability 1/1000, that's negligible for one disk, but across 1,000 disks
the probability that *some* disk fails that day is effectively 1 — a fleet
turns a rare per-unit event into a routine, expected condition, which is
exactly why partial failure has to be designed for rather than treated as an
edge case. Software fault tolerance is
also what makes rolling upgrades possible — patching nodes one at a time
while the service runs.

Two engineering traditions respond differently:

- **Supercomputers/HPC** escalate partial failure to total failure: checkpoint
  the job, crash the whole cluster, restart from the checkpoint. Acceptable
  for batch jobs; useless for services.
- **Cloud/internet systems** accept partial failure as the normal operating
  condition and build fault tolerance into software, so the service keeps
  running through node deaths and rolling upgrades. It is reasonable to assume
  in a large cluster *something* is always broken.

The constructive principle: **build reliable abstractions from unreliable
parts** — error-correcting codes give reliable data over noisy channels, TCP
gives an ordered reliable stream over an IP layer that drops and reorders
packets. Fault-tolerant distributed algorithms
([consensus](consensus.md), [total order broadcast](total-order-broadcast.md))
do the same one level up. The reliable layer is never absolute — it removes a
class of faults from your concern, not all of them.

Because partial failure is nondeterministic and rare interactions of faults
matter, deliberately triggering faults in testing (e.g. killing processes at
random) is one of the few ways to gain confidence the tolerance actually
works.

## Replication tolerates node failure, not data corruption

[Replication](single-leader-replication.md) is fault tolerance for *node*
failure specifically: lose a node and the data survives elsewhere. It is not
fault tolerance for bad data — a user error (wrong `WHERE` clause), an
application bug, or silent storage corruption on the leader replicates
faithfully to every follower, because replication's whole job is to
propagate writes accurately, and it cannot distinguish a correct write from
a mistaken one. This is the correlated-fault problem from above recast at
the data layer: just as a software bug fires identically on every replica
running the same code, a bad write fires identically on every replica that
faithfully applies it. Recovering from *this* class of fault needs a
different mechanism — point-in-time backups and a tested restore path —
because by the time corruption is noticed, every live replica may already
agree on the wrong answer.
