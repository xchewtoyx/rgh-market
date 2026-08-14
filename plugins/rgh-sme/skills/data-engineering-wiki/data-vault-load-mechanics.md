---
type: concept
title: Data Vault Load Mechanics (Hubs, Links, Satellites)
description: >
  How Data Vault's insert-only Hub/Link/Satellite structure gets loaded so
  that raw facts stay permanently auditable and separate from any business
  interpretation applied downstream.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Gershkovich), ch. 17"
---

Data Vault's core philosophy is auditability: once a source system is
updated or decommissioned, the warehouse becomes the only remaining record,
so if the base layer ever modifies data in place, traceability back to what
the source actually said is permanently lost. The fix is a strict
**insert-only discipline** at the base ("Raw Vault") layer — no updates, no
cleansing, no business rules — captured in the practitioner mantra "Data
Vault is a source of facts, not a source of truth," since "truth" depends on
whose business rules get applied, while the raw facts underneath don't
change. This is the same principle behind keeping a
[warehouse's source layer](warehouse-layering-source-staging-presentation.md)
unaltered, taken further: even conformed history stays insert-only, with
interpretation pushed all the way downstream into marts.

Three object types, and how each actually gets loaded:

- **Hubs** hold every unique business key ever seen for one entity, keyed by
  a hash of that business key (not a meaningless sequence — the hash is
  deterministic so any system re-encountering the same business key computes
  the same key independently, without a round trip). A hub load only inserts
  a business key **the first time it's ever seen** — a later load of the
  same key, even from a different source system, is neither inserted nor
  updated.
- **Links** hold nothing but the hashed keys of two or more related hubs —
  effectively an [associative table](reconciliation-with-set-operators.md)
  for the relationship itself, regardless of whether that relationship is
  actually many-to-many today. This is deliberate: a link stores a
  one-to-many relationship the same way it would store a many-to-many one,
  so if the business rule later changes (a single order becomes shareable
  across multiple customers, say), the structure absorbs it with no
  redesign. Like hubs, a link only inserts a relationship the first time
  it's observed.
- **Satellites** carry the attributes and their change history, functionally
  similar to [Type 2 SCD tracking](insert-only-history-pattern.md) but still
  strictly insert-only. A satellite compares an incoming record's
  [hash of all its attributes](hash-based-change-detection.md) against the
  latest stored hash for that hub/link key, and inserts a new timestamped row
  only when the hash actually differs — the same technique as any other
  hash-based change detection, just applied at the attribute-history layer
  specifically.

Because every one of these load steps is a strict first-seen-only or
changed-only insert, re-running an already-processed batch against a Data
Vault produces zero new inserts — the insert-only discipline gives the load
[idempotency](idempotent-and-replayable-jobs.md) as a direct structural
consequence, not something bolted on separately.
