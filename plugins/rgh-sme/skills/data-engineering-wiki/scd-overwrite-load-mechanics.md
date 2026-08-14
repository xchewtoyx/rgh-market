---
type: concept
title: SCD Type 1/3 Overwrite Load Mechanics
description: >
  Two load-time consequences of overwriting a dimension attribute in place —
  a performance trap in generic upsert tooling, and mandatory downstream
  aggregate invalidation — that Type 2's append-only load avoids.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

Overwriting an attribute in place — whether across every historical row for
an entity (Type 1) or by populating a new column with the changed value
(Type 3) — has two load-mechanics consequences that a straight
[Type 2 append](scd-type2-load-via-change-stream.md) doesn't share:

- **Generic "upsert" convenience functionality can silently kill load
  performance.** Many ETL tools offer a single UPDATE-else-INSERT operator
  for convenience, but it typically evaluates row-by-row rather than
  set-based, which doesn't scale. For a pure overwrite load, segregate the
  incoming rows into UPDATEs and INSERTs explicitly and run them as separate
  set-based operations — for a large initial or corrective load, also
  consider disabling destination-table logging or using a bulk loader,
  since the goal is a plain in-place overwrite, not the row-level tracking
  a transactional log exists for.
- **Overwriting invalidates any aggregate built on the changed column.**
  Because Type 1 and Type 3 changes rewrite history rather than appending to
  it, any pre-computed aggregate that summarized the old value is now wrong
  and must be dropped and rebuilt — the load has to notify whatever process
  owns downstream aggregates that a rebuild is due. A Type 2 change, by
  contrast, doesn't force an aggregate rebuild as long as the change is
  applied "as of today" rather than backdated: the new row only affects
  facts loaded from this point forward, so existing aggregates over prior
  periods remain correct without touching them. The trap is sharper than
  just "the aggregate is stale": if the dimension load runs before the
  aggregate load in the same pass, the overwrite destroys the old value
  before anything downstream can use it to correct the aggregate's existing
  rows — see [the Type 1 aggregate-corruption
  trap](type1-change-aggregate-corruption-trap.md) for the full mechanics.

This is a concrete reason the SCD type chosen for an attribute — a
dimensional design decision — has real load-cost consequences: Type 2's
higher storage cost buys cheaper incremental loads, while Type 1/3's lower
storage cost is paid for with a mandatory aggregate-rebuild step on every
overwrite.

**A Type 1 overwrite must update every historical row sharing that natural
key, not just the current version.** A dimension with prior Type 2 history
has several surrogate-keyed rows for the same real-world entity; a corrected
attribute value (a fixed typo in a product name, say) needs to land on all
of them, or facts joined to an older version continue showing the
stale/uncorrected value indefinitely.

**A single incoming source record can trigger a Type 1 change and a Type 2
change on the same load pass — check for both, never either/or.** Treating
them as mutually exclusive is a correctness bug: a record can simultaneously
have one attribute that changed in a way the design says to overwrite and
another that changed in a way the design says to version, and a load that
stops checking once it finds one kind of change misses the other.

**Watch for a Type 1 attribute that isn't actually independent of a Type 2
attribute** — for example, a `brand_name` stored as Type 1 but derived from
a `brand_code` that's itself tracked as Type 2. A changed `brand_name` value
doesn't automatically mean "overwrite it everywhere": first check whether
the underlying `brand_code` also changed. If it did, the record has been
reassigned to a genuinely different brand, which calls for a new Type 2 row,
not a Type 1 overwrite of the old one. Where practical, avoid designing a
Type 1 attribute that depends on a Type 2 one in the first place; where
unavoidable, document the dependency explicitly so ETL developers don't
implement a naive overwrite that silently corrupts history. A snowflaked
dimension sidesteps this specific trap, since the dependent attribute then
lives in its own separate table.
