---
type: concept
title: Expand-and-Contract Schema Migration
description: >
  Decouple a relational schema change from the application code deployment
  that depends on it by splitting the migration into an expand phase, a
  dual-write phase, and a contract phase across successive releases.
sources:
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 13"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 8"
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 11"
---

# Expand-and-Contract Schema Migration

Also called the parallel-change pattern, or the **McHenry Technique**
(after Stephen McHenry) in older operations literature. A schema change
and the code that
depends on it are the most common way a deployment breaks
[zero-downtime deployment](zero-downtime-deployment.md) and
[independent deployability](independent-deployability.md), because a naive
migration forces schema and code to change atomically together — which is
incompatible with rolling out code gradually (see
[rolling deployment](rolling-deployment.md), [canary release](canary-release.md))
or keeping an instant [blue-green](blue-green-deployment.md) rollback path
open. Expand-and-contract avoids this by spreading the change across three
phases, each shippable and rollback-safe on its own:

1. **Expand**: add new columns or tables (nullable, or with defaults)
   alongside the old structures. Code version N keeps using the old
   structures unchanged — this phase is purely additive and safe to deploy
   and roll back on its own.
2. **Dual-write**: deploy code version N+1, which writes to *both* old and
   new structures while a background job backfills historical data into
   the new structures. Reads can still come from the old structures, so
   this phase is also safe to roll back to N.
3. **Contract**: deploy code version N+2, which reads exclusively from the
   new structures. Once verified, run a migration script to drop the
   obsolete old columns or tables.

Because each phase is independently deployable and independently
revertible, the whole migration never requires a single high-risk,
all-at-once cutover — see [schema migration production risk categories](schema-migration-production-risk-categories.md)
for the specific risks each phase is designed to contain, and
[versioned incremental migrations](versioned-incremental-migrations.md) for
how the phases are tracked and applied.

Schemaless (NoSQL/document) databases push the equivalent problem into
application code instead of DDL: the application must tolerate reading
multiple concurrent schema versions of a document (a "tolerant reader" at
the data layer — see the API-level [tolerant reader pattern](tolerant-reader-pattern.md)
for the same idea applied to service contracts). The same tolerance is
needed transiently even in a relational schema during the expand phase:
once new columns exist but before every reader has migrated, code must not
break on the presence of columns it doesn't yet know about — in practice
this is rarely an issue for well-written SQL that names its columns
explicitly rather than relying on positional or `SELECT *` assumptions.
