---
type: concept
title: Surrogate Keys vs. Business Keys
description: >
  Why a warehouse pipeline generates its own meaningless identity column
  instead of relying directly on the natural key a source system uses.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Gershkovich), ch. 5"
---

A **business key** is an identifier whose value is meaningful within the
organization — an order number, a product code, a national ID — and it's
what an OLTP source system typically uses as its primary key, since it's
also how the system's own users and other systems recognize the record.

A **surrogate key** is an identifier with no intrinsic business meaning:
a sequential integer, a hash, or a generated random value. In a pipeline
loading a warehouse, the surrogate key becomes the primary key of the
target table instead of the source's business key, and the business key is
kept as a secondary, still-unique attribute.

This isn't stylistic — it solves concrete problems a warehouse pipeline
runs into that an OLTP source doesn't: a warehouse conforms data from
*multiple* source systems that may reuse the same business key for
different real entities, or represent the same entity with different key
values across systems, so relying on the business key directly would corrupt
joins the moment a second source enters the picture. A surrogate key also
collapses an awkward multi-column composite business key into one column
with a standard, stable format, which matters for
[table load patterns](table-load-patterns.md) like upsert/merge that key off
a single join column. It's also what makes
[slowly-changing-dimension processing](insert-only-history-pattern.md)
tractable: a business key identifies the same real-world entity across every
version of it, while a fresh surrogate key on each new version row is what
lets those versions coexist as distinct, individually addressable rows in
the same table.

A business key is also assumed to be a stable identifier for its entity;
when that assumption doesn't hold, a [durable key](durable-key.md) fills
the gap as a third, separately-maintained identifier alongside the natural
and surrogate keys.

Generating surrogate keys is itself a pipeline mechanic, typically via a
database sequence or an autoincrement/identity column, and it needs the same
discipline as any other [idempotent](idempotent-and-replayable-jobs.md) load
step — a job that's re-run after a partial failure must not mint duplicate
surrogate keys for rows it already loaded.

Two generation methods to avoid: assigning keys via a **database trigger**,
which turns key generation into a per-row performance bottleneck under load
(prefer the pipeline calling a sequence generator directly, or letting the
pipeline tool itself generate and track keys); and **concatenating the
source's natural key with a date/time stamp** to manufacture uniqueness,
which doesn't scale and reintroduces exactly the natural-key fragility a
surrogate key exists to avoid. See [the surrogate key
pipeline](surrogate-key-pipeline.md) for how these keys get substituted into
fact rows once generated.

An alternative to a sequence is **deterministic hashing**: derive the
surrogate key directly from the business key plus whatever else makes a row
version unique, for example `MD5(customer_id || from_date)` in a
[validity-interval](insert-only-history-pattern.md) design. Unlike a
sequence, a hashed surrogate key is reproducible from its inputs alone —
reloading the same source row always yields the same surrogate key without
needing to look up what was assigned last time, which is valuable
specifically when a fact table needs to embed the dimension's surrogate key
directly at load time without a round trip to check what key a matching
dimension row already has.
