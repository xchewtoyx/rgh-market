---
type: concept
title: Versioned Incremental Migrations
description: >
  Apply schema changes as a sequence of small, sequentially-numbered
  migrations rather than as full schema diffs, so deployment tooling can
  always tell exactly what's been applied and what hasn't.
sources:
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 8"
---

# Versioned Incremental Migrations

Schema changes should be packaged as sequentially-numbered incremental
migrations rather than as full schema diffs computed at deploy time. Every
changeset gets an incrementing numeric version stored in the database
itself; deployment tooling compares the target version against the
database's current version to know exactly which changesets still need to
be applied.

This is what [working in small batches](working-in-small-batches.md) looks
like applied to schema changes specifically, and it's the versioning
substrate that [expand-and-contract migrations](expand-and-contract-schema-migration.md)
and the [migration rollback testing cycle](migration-rollback-testing-cycle.md)
both depend on: without a reliable, explicit record of exactly which
migration version is live, there's no reliable way to know what "rollback"
should revert to.

The trade-off: the incremental/agile approach produces fast, small, visible
changes, but requires the engineers writing migrations to understand what
makes a migration safe, and understand the risk of two concurrent
migrations touching the same object at once.
