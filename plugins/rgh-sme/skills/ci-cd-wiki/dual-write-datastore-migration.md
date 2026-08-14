---
type: concept
title: Dual-Write Datastore Migration
description: >
  Migrating a stateful service to a new database, queue, or storage instance
  by writing to both the old and new instance simultaneously before cutting
  reads and then writes over, so the migration itself never requires downtime
  or an unrecoverable data cutover moment.
sources:
  - title: "Infrastructure as Code: Patterns and Practices"
    resource: "Infrastructure as Code: Patterns and Practices (Rosemary Wang), ch. 9"
---

# Dual-Write Datastore Migration

[Blue-green deployment](blue-green-deployment.md) and [backward-compatible
schema migration](backward-compatible-schema-migration.md) both assume the
same underlying database instance stays in place while the application
changes around it. Some changes don't fit that assumption — replacing the
database engine itself, moving to a different cluster topology, or
migrating a queue or object store to new infrastructure — because there's no
single schema to expand and contract; the whole stateful instance is being
replaced.

The pattern for this case is a staged cutover with a period of genuine dual
operation, not a single switchover moment:

1. **Provision the new (green) stateful instance** alongside the existing
   (blue) one, using the updated infrastructure code.
2. **Replicate existing state** from blue to green with an idempotent,
   out-of-band migration/sync pipeline, so green starts caught up.
3. **Dual-write**: change the application to write every state change to
   both blue and green simultaneously, so green stays caught up going
   forward while still verified as correct against blue's known-good state.
4. **Cut reads over** to green once its data is trusted, while writes still
   go to both — this is the point where a problem with green is cheapest to
   detect and revert, since blue is still receiving every write and remains
   the fallback.
5. **Cut writes over**, stopping writes to blue entirely.
6. **Decommission blue** once green has run as the sole source of truth for
   long enough to be confident, retaining a final blue snapshot as an
   emergency reference rather than deleting it immediately.

The dual-write window is what makes this safer than a one-shot data
migration with a maintenance-window cutover: at every step there's a known
good fallback still receiving live writes, so a problem discovered at the
read-cutover or write-cutover step is a same-instant rollback rather than a
data-recovery exercise. The cost is added application complexity (writing to
two targets, reconciling any divergence during the dual-write window) that
only pays for itself when the datastore's downtime or data-loss risk during
a single-shot cutover would be unacceptable.
