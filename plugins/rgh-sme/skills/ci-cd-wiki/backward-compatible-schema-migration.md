---
type: concept
title: Backward-Compatible Schema Migration (Expand-Contract)
description: >
  Splitting a database schema change into expand, transition, and contract
  phases so old and new application versions can both run correctly against
  the database at once, enabling zero-downtime deploys and safe rollback.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 12"
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd ed. (Nygard), ch. 13"
---

# Backward-Compatible Schema Migration (Expand-Contract)

Also called the parallel-change pattern. A schema change deployed atomically
with the application code that depends on it breaks
[zero-downtime deployment](rolling-deployment.md) and
[rollback](rollback-and-roll-forward.md): during a rolling or canary rollout,
old and new application code run simultaneously against the same database, so
the schema has to satisfy both versions at once. The fix is to split the
change into three phases, deployed as separate steps:

1. **Expand**: add the new schema structure (e.g. a new column) while leaving
   the old structure intact. The old application version keeps working
   unmodified.
2. **Transition**: deploy an application version that reads from the old
   structure as a fallback but writes to both old and new; then run a
   background data-migration script to backfill historical data into the new
   structure; then deploy a further version that reads and writes exclusively
   to the new structure.
3. **Contract**: once no running application version depends on the old
   structure, remove it via a final migration script.

## Worked example: renaming `phone` to `mobile_number`

1. Expand: migration adds `mobile_number`, `phone` untouched.
2. Transition A: deploy app version that reads `phone` if `mobile_number` is
   null, but writes to both columns.
3. Backfill: background script copies historical `phone` values into
   `mobile_number`.
4. Transition B: deploy app version that reads/writes only `mobile_number`.
5. Contract: migration drops `phone`.

Because each step is independently deployable and the schema is always valid
for whichever application versions might be running, this pattern is what
makes [rollback](rollback-and-roll-forward.md) safe even when a release
includes a schema change: rolling the application back mid-transition doesn't
break, because the transition phase was designed to support both versions
concurrently.

## Schemaless data stores

NoSQL and document databases defer schema enforcement to the application
rather than the database engine, so there's no migration script to run in
the first place — but the same underlying problem still exists: different
documents in the same collection may have been written by different code
versions and so have different effective shapes. Application code reading
this data needs to tolerate multiple concurrent shapes rather than assuming
the latest one, the same discipline the
[tolerant reader pattern](tolerant-reader-pattern.md) describes for API
consumers, applied here to a database read path instead of an API call.
