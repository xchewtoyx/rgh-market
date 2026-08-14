---
type: concept
title: Compliance-Driven Bitemporal Fact Versioning
description: >
  Why a strict chain-of-custody compliance requirement rules out overwriting
  fact rows at all, and the five extra columns that turn any overwrite into
  a fully reconstructable version history instead.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

Compliance, in the chain-of-custody sense (analogous to police evidence
handling), means being able to show exactly what data looked like at any
point while it was under the pipeline's control, plus who touched it. Taken
seriously, this has one blunt practical consequence for fact table design:
**it rules out both Type 1 overwrite and Type 3 add-attribute changes
outright** — every change has to become an insert, never a delete or an
in-place update, because either of those destroys the very history
compliance exists to preserve. See [SCD Type 1/3 overwrite load
mechanics](scd-overwrite-load-mechanics.md) for what a compliance-driven
table gives up by forbidding this.

The mechanical fix is five extra columns added to an otherwise normal fact
table:

- A **fact table surrogate key** — a unique integer per *original,
  unmodified* row, shared across every subsequent version of that row.
- **Begin version date/time** — the instant this specific row version was
  created.
- **End version date/time** — a far-future placeholder until the row is
  superseded, then set to the exact instant it was.
- A **change reference** — `"original"` initially, later an explanation of
  why a new version was created.
- A **source reference** — the operational source initially, later the
  source of whatever revised the columns.

Under this scheme, an "overwrite" becomes: insert a new row that shares the
original row's fact table surrogate key, carries the updated column values
and a fresh begin-version timestamp, and set the *prior* row's end-version
timestamp to that same instant. Reconstructing history is then two simple
queries: date-constrain the table to see its state at any specific moment,
or constrain on one fact table surrogate key and sort by begin-version date
to see a specific row's complete revision history. If the compliance-enabled
table exists purely to satisfy an audit requirement, it can run alongside a
normal, unmodified operational fact table and skip BI-oriented indexing
entirely, since it's never meant to serve interactive queries.

This scheme depends on the same supporting capabilities as any other
compliance program: full [lineage](data-lineage.md) and rerun capability for
every transform, dependency analysis showing everywhere an original source
element was ever used, version control over which ETL logic produced a given
row, and tamper-evident backups — commonly implemented by hash-coding
archived data and storing the hash separately with a trusted third party, so
a later restore can be verified against that hash rather than trusted on
faith. The [audit dimension](audit-dimension.md) is the piece that ties
runtime load context to a specific fact row at the moment it was created,
which is exactly the context a compliance investigation needs alongside the
row's version history. Get the specific retention and reconstruction
requirements from whoever owns compliance in the organization before
building any of this — it's expensive enough that over-building it "just in
case" wastes real engineering effort.
