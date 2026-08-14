---
type: concept
title: Migration Based vs. State Based Database Delivery
description: >
  Migration-based delivery keeps explicit versioned migration scripts as the
  source of truth; state-based delivery diffs a model schema against production
  and auto-generates upgrades.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Vladimir Khorikov), ch. 10"
---

# Migration Based vs. State Based Database Delivery

Two ways to evolve relational schema in delivery pipelines:

**State-based** — a model database (or SQL scripts representing desired state)
is authoritative; a comparison tool diffs production vs. model and generates
upgrade scripts. Migrations are implicit. Easier merge conflict handling on
schema files; weak at **data motion** (transforming existing rows to fit a new
shape) because tools cannot infer domain-specific transformation rules.

**Migration-based** — explicit hand-written migrations in source control
(Flyway, Liquibase, FluentMigrator `Up()`/`Down()`) transition version N → N+1.
Final state is implicit (replay all migrations). Strong at data motion; merge
conflicts on migration ordering require human resolution.

**Prefer migration-based** once production has data you cannot discard — data
motion dominates long-term cost. State-based is tolerable pre-production when
seed data can be recreated on every schema change. A comparison tool can still
**detect** undocumented production drift under migration-based delivery.

Apply every schema and reference-data change through migrations; never edit a
committed migration — write a new one unless editing avoids data loss. See
[version-controlled database migration scripts](database-migration-scripts.md)
and [backward-compatible schema migration](backward-compatible-schema-migration.md)
for zero-downtime promotion through the pipeline.

Reference data (lookup tables the app cannot mutate) belongs in source control
as SQL inserts alongside DDL — part of schema, not regular application data.
Keep a [database sandbox](database-sandbox.md) per developer so migrations and
tests do not interfere across the team.
