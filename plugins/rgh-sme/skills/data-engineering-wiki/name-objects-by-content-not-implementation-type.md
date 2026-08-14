---
type: concept
title: Name Objects by Content, Not Implementation Type
description: >
  Why a transformation's output should be named for what it contains rather
  than whether it's currently a table, view, or materialized view, so its
  implementation can change without breaking every downstream reference.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Gershkovich), ch. 12"
---

A transformation's output can reasonably start as a plain table, later get
promoted to a [materialized view](copy-on-write-load-cost.md) for
performance, or drop back to a view once query volume no longer justifies
storing the result — the underlying transformational logic doesn't change
across any of these, only how the platform executes and stores it. A naming
convention that encodes the current implementation choice into the object's
name (a `_v` suffix for views, `_mv` for materialized views) turns that
purely internal decision into a breaking change for every downstream query
that references the object by name, every time the implementation is
revisited.

Naming an object after what it *contains* (`customer`, `daily_active_users`)
rather than what it *currently is* (`customer_v`) means switching its
`CREATE TABLE` to a `CREATE VIEW`, or vice versa, requires touching exactly
one definition with no downstream reference needing to change at all. This
is the same interface-stability principle behind
[pipelines as code](pipelines-as-code.md) and
[table load patterns](table-load-patterns.md) — consumers should depend on a
stable name and contract, not on an implementation detail that's expected to
change as query volume and cost trade-offs shift over a system's life.
