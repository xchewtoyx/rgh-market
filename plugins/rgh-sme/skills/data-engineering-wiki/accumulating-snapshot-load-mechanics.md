---
type: concept
title: Accumulating Snapshot Load Mechanics
description: >
  Why loading an accumulating-snapshot fact table means repeatedly
  destructively updating the same row as a process progresses, and the
  physical-storage cost that comes with it.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

An accumulating-snapshot fact table tracks the evolving status of a
finite-duration process — order placed, shipped, paid, all as separate
date-valued foreign keys on one row per order. Loading it is fundamentally
different from loading a transaction or periodic-snapshot fact table: only
the first milestone date is known when the row is first created, and the
same physical row gets **destructively modified**, repeatedly, as each later
milestone occurs — a date foreign key gets overwritten and dependent facts
get updated, rather than a new row being appended. The first milestone's
value is the one field that conventionally stays inviolate once set.

This repeated in-place modification has a physical cost that transaction and
periodic-snapshot loads don't share: in row-store engines with variable-length
rows, repeated updates that grow a row's stored size can push it out of its
original disk block, degrading residency and read locality over the row's
lifetime. Where this becomes a measurable problem, periodically dropping and
reloading the affected rows restores locality — a maintenance step the other
fact table types don't need, since they're either pure-append or updated at
most in a narrow recent window.

Accumulating snapshots are typically paired with a transaction or
periodic-snapshot fact table covering the same process, rather than used
alone: the accumulating snapshot gives a single current-status row per
process instance, while the paired table retains full event-level or
period-level history. A process with looping paths or many non-standard
routes doesn't fit this model well, since the fixed set of milestone-date
columns assumes a roughly linear, bounded workflow.

**Handling the minority of instances that don't follow the standard
scenario** — a small, occasional fraction of process instances that deviate
from the milestones the snapshot was built around — without abandoning the
accumulating snapshot for the whole process: add a status dimension to the
snapshot and tag any deviating row with a generic status (e.g., "Weird")
rather than trying to force the milestone columns to represent every
possible deviation path. The full story for a tagged row lives in the
paired transaction fact table, which an analyst joins into via the shared
natural key once they've spotted a non-standard row — keeping the
accumulating snapshot's own load logic simple and bounded while still
leaving a path to the detail for the cases that need it.

**Interaction with Type 2 dimensions**: while a process instance is still
active, its accumulating-snapshot row should be kept pointed at the
*current* surrogate key of any [Type 2](insert-only-history-pattern.md)
dimension it references, updated alongside the milestone columns on each
revisit. Once the row reaches its final milestone and stops being revisited,
it's conventionally left referencing whatever key was current at
completion — later Type 2 changes to that dimension don't get back-applied
to a closed-out row.

**Full-refresh vs. status-change-only updates is a load-frequency trade-off
that scales with how many process instances are active at once.** Updating
every active row on every load pass — incrementing each in-flight instance's
elapsed-time-in-stage facts whether or not its status actually changed — is
simple and correct, and stays cheap enough up to roughly the tens-of-
thousands of concurrently active instances. Past that, restrict the load to
only the rows whose status actually changed since the last pass, which is
far cheaper per run but creates a real reporting gap: a report needing an
"as of today" elapsed-time figure for an instance that's still mid-stage
(no status change to trigger its update) won't see today reflected unless
the report computes the in-flight lag itself from the last-known milestone
date rather than trusting the stored lag column.

**Source the accumulating snapshot from the transaction fact table covering
the same process, not from the operational system directly**, whenever both
exist — the same sourcing discipline
[aggregate tables](aggregate-table-load-consistency.md) follow toward their
own base table. This keeps both fact tables consistent with a single point
of extraction from the source, and avoids two independently-written ETL
processes applying subtly different status-interpretation rules to the same
underlying events. Building a transaction star from an accumulating snapshot
instead is unusual and often outright impossible — operational systems
already tend to emit data in transaction/status-change shape, and some
accumulating-snapshot designs are simplified in ways that discard the
per-event detail a transaction star would need.

**When separate operational systems each own a different phase of the same
process** (an intake system for early stages, a different system for later
ones, joined by a shared process ID), the load has to decide which system's
status wins at each stage and how to handle the two systems disagreeing —
this is a genuine integration decision, not a mechanical mapping. Two
resolutions: build one unified transaction star that already reconciles
every phase before the accumulating snapshot ever loads from it, or keep
separate per-subprocess transaction stars and only reconcile them at the
accumulating-snapshot layer itself, accepting that the snapshot's own load
logic now has to do the cross-system reconciliation the transaction layer
didn't.

**Collapsing many operational status codes onto a handful of business
milestones is where an accumulating snapshot's ETL complexity actually
lives, even though the resulting schema looks identical to the simple
case.** A real operational system can carry dozens of granular status
codes that all belong to the same business-meaningful milestone (several
"under review by X" variants all mapping to a single "Reviewed" milestone,
say); getting that mapping table right, and keeping it current as the
operational system's status codes evolve, is where the load's real
maintenance burden sits — the fact table's column list doesn't reveal any
of it.

**A process that loops back to an earlier stage is still loadable as an
accumulating snapshot**, as long as the elapsed-time facts are named after
the *stage* rather than the milestone pair that produced them: when a
status reverts (an application returned from processing back to review for
a missing signature, say), the load simply resumes incrementing that
stage's existing fact rather than needing a new column for the repeat visit.
The harder question this raises — which date to use when a milestone is
achieved more than once (the earliest occurrence, or the latest) — has no
technically correct answer; it has to be a business rule the load
implements, decided by the people who own the process, not a default a
developer picks unilaterally.

**Lag metrics** (the elapsed time between two milestone dates — order-to-
ship, release-to-finished-goods) are usually derived rather than stored:
compute them in a view over the milestone date columns instead of
persisting a physical lag column, since they're cheap to recompute and
storing them just duplicates information already on the row. Two load-side
complications this glosses over: a naive date subtraction overcounts
elapsed time across weekends and holidays, so the load or view needs a
workday-aware calculation wherever the business cares about workday lag
specifically; and a process short and closely monitored enough to need
finer-than-daily precision needs its milestone columns sourced from
operational timestamps rather than the date dimension's day grain.
