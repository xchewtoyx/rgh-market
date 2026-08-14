---
type: concept
title: Migration Rollback Testing Cycle
description: >
  Every schema migration change needs its rollback path re-tested as part
  of the same test cycle as the forward change, and rollback should rename
  rather than drop objects so written data is never destroyed.
sources:
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 8"
---

# Migration Rollback Testing Cycle

[Roll back vs. roll forward](rollback-vs-roll-forward.md) only works for
schema migrations if the rollback path is actually tested, not just
assumed. Any change to a migration's implementation must be re-integrated
and re-tested before deployment, including in production, using the
standard cycle:

    apply changeset → quick integration tests
    → apply rollback → quick tests
    → re-apply changeset → quick tests
    → longer periodic testing

The rule that makes this safe in practice: **never simply drop objects to
roll back a migration** — rename them instead, to preserve any data that
was already written to them. A dropped table's data is gone; a renamed
one's data can still be recovered or reconciled if the rollback decision
turns out to be wrong, or if some other component wrote to it during the
window before rollback happened.

Migration automation should be earned incrementally rather than adopted
immediately: don't rush to fully automated, push-button migration
deployment until the rollback path has a track record of tested,
reliable fallback and the team has practiced the recovery process, not just
designed it on paper.
