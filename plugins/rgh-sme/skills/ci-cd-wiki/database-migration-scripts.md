---
type: concept
title: Version-Controlled Database Migration Scripts
description: >
  Schema and reference-data changes are applied only through sequentially
  numbered, version-controlled delta scripts run by an automated migration
  tool, never through manual edits in a database GUI.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 12"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 8"
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Vladimir Khorikov), ch. 10"
---

# Version-Controlled Database Migration Scripts

Database schema, DDL, stored procedures, views, triggers, and static
reference data all fall under
[version-control everything the pipeline depends on](version-control-everything.md).
The mechanism that applies these changes automatically is a **migration
script** (delta script): an explicit, version-controlled script that
transforms the database from schema version N to N+1.

Anti-pattern: a dedicated "model database" that accumulates manual schema
changes and is diffed at deploy time — no history, competing sources of truth
with Git. Prefer [migration-based vs. state-based database delivery](migration-based-vs-state-based-database-delivery.md):
explicit migrations as the artifact of record, especially once production data
exists and **data motion** scripts are required.

## Discipline

- **Never edit schemas manually.** Manual tweaks via a DB admin GUI are
  forbidden — every schema change happens through a migration script, for the
  same reason a [snowflake server](snowflake-server.md) is forbidden: an
  unrecorded change makes the schema's actual state untraceable.
- **Automated migration tooling** (Liquibase, Flyway, dbdeploy) tracks which
  deltas have already been applied via an internal `schema_version` table,
  and applies only the deltas a given database hasn't seen yet — during
  deployment, this runs unattended as part of the
  [deployment script](deployment-script-design.md).
- **Strict sequential naming** (`V001__create_users.sql`,
  `V002__add_email_column.sql`) keeps ordering unambiguous.
- Scripts should be deterministic, and specify both a forward (`UP`) and,
  where feasible, a backward (`DOWN`) path.

## Testing a migration before it reaches production

A migration script needs its own test cycle, distinct from testing the
application code that depends on it, because the risk it carries is
different: applying it, not just the resulting schema, can itself degrade a
live system. A standard cycle: apply the changeset, run a quick integration
test pass, apply the rollback, run the same quick tests again to confirm the
rollback genuinely restores the prior state, re-apply the changeset, run the
quick tests once more, then subject the change to longer periodic testing
(full-dataset and load testing) before it's trusted for production. Never
roll back a migration by simply dropping the objects it created — rename
them instead, so any data already written under the new structure isn't
destroyed if the rollback needs to be reverted again.

## Rules-based gating for risky migrations

Not every migration carries the same risk, and a pipeline gate can
distinguish them automatically before a human ever needs to look: flag any
migration matching known risky patterns — updates or deletes with no `WHERE`
clause, an alter on a table above some row-count threshold, a new column
with a non-null default (which can lock the whole table on some engines),
a risky datatype (e.g. a new `BLOB` column) in a `CREATE`/`ALTER`, a foreign
key with no supporting index, or any operation touching a table flagged as
sensitive. A flagged migration routes to manual review instead of
proceeding automatically; anything that doesn't match a known risky pattern
proceeds through the ordinary automated path. This is the database-specific
instance of [risk-based test gating](swiss-cheese-testing-model.md): route
review effort at the specific operations known to be dangerous rather than
requiring the same manual scrutiny for every migration regardless of risk.

Four categories of production risk to check a migration against before it
ships: object locking duration (measured against the same latency/
availability SLOs the rest of the pipeline gates on), resource saturation
from the migration's own I/O load, transitional data-integrity issues
(relaxed or deferred constraints letting data land in an unexpected
intermediate state), and replication lag or stalls the extra write volume
might induce on replicas.

## Earning migration automation incrementally

Fully automated, push-button migration deployment is worth building toward,
but it's earned rather than assumed: start with migrations reviewed and run
by hand, build a track record of tested, reliable rollback and recovery, and
only automate once that track record and engineer familiarity with the
process are established — the same incremental-trust progression that
applies to [compliance through pipeline automation](compliance-through-pipeline-automation.md)'s
standard-change reclassification, applied here to the migration pipeline
itself.

## Relationship to zero-downtime deployment

A migration script by itself doesn't guarantee the application stays
available while it runs — see
[backward-compatible schema migration](backward-compatible-schema-migration.md)
for the pattern that decouples schema change from application deployment so
neither one requires downtime.
