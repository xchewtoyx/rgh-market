---
type: concept
title: Expand-Contract Schema Migration
description: >
  Splitting a shared-schema change into add-then-dual-write-then-remove
  phases so a rolling deploy never requires old and new application code to
  agree on a single instantaneous cutover.
sources:
  - title: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation"
    resource: "Continuous Delivery (Humble, Farley), ch. 12"
---

# Expand-Contract Schema Migration

A database schema is shared mutable state that every version of the
application talks to at once during a
[rolling upgrade](rolling-upgrade-compatibility.md) — old-code and new-code
instances run side by side for the whole rollout window, so a schema change
that only one of those versions can read breaks the other half of the
fleet. The expand-contract pattern (also called parallel change) splits a
single risky rewrite into phases that are each individually safe for both
versions to run against concurrently:

1. **Expand.** Add the new schema element (a new column, table, or index)
   alongside the old one. Nothing existing changes shape, so both old and
   new application code keep working unmodified.
2. **Transition.** Deploy application code that writes to *both* the old
   and new structures, and reads from the new one falling back to the old
   when absent. A background job backfills history from old to new. Because
   this step targets a single logical field/relationship at a time, it
   composes with normal [rolling upgrade](rolling-upgrade-compatibility.md)
   deploys rather than needing a coordinated stop-the-world cutover.
3. **Contract.** Once every instance is confirmed running the
   dual-write/dual-read code and the backfill is complete, deploy code that
   uses only the new structure, then drop the old one.

The pattern is the schema-migration analogue of the compatibility
discipline in [rolling upgrade compatibility](rolling-upgrade-compatibility.md):
instead of relying on a wire format that tolerates old and new readers
simultaneously, it manufactures that tolerance at the schema level by never
letting a single deploy step require both versions to agree on a new,
incompatible shape at the same instant. Each phase is independently
reversible — a bad transition step can be rolled back to the previous
phase without data loss, since the old structure is still being
maintained until contract.
