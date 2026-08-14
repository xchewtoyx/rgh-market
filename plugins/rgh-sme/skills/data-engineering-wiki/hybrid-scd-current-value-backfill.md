---
type: concept
title: Hybrid SCD Current-Value Backfill (Type 6 / Type 7)
description: >
  The load-time work needed to expose a "what's true today" attribute on
  top of Type-2 history, without losing the point-in-event accuracy Type 2
  exists to preserve.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 5"
---

[Type 2 history](insert-only-history-pattern.md) alone can't answer "roll up
all historical facts under this entity's *current* attribute value" without
an expensive query that resolves every fact's dimension row and then joins
again to the entity's latest version. Hybrid designs solve this at load
time by carrying a current-value view alongside the type-2 history, at the
cost of extra load steps most Type-2-only pipelines don't need:

- **Column-pair approach**: every dimension row gets both a `historic_X`
  column (set once, fixed for that row, same as ordinary Type 2) and a
  `current_X` column. The load-time obligation this creates: whenever a
  Type 2 change occurs, the new `current_X` value must be **backfilled onto
  every existing row sharing that entity's durable key**, not just the
  freshly inserted row — the same historical-rewrite step [Type 1/3
  overwrite load mechanics](scd-overwrite-load-mechanics.md) requires, run
  as an extra pass immediately after every Type 2 insert rather than as
  the whole load. Skipping this backfill leaves older rows' `current_X`
  stale, silently breaking any "roll up by current value" query.
- **Dual-key approach**: the fact table carries two foreign keys — the
  ordinary type-2 surrogate key for point-in-event accuracy, and the
  entity's [durable key](durable-key.md) for current-value access. A second
  table or **view, filtered to only current rows of the type-2 dimension**,
  is what the durable key joins against for "current" queries. Because it's
  a view over existing rows rather than a maintained column, this approach
  needs no backfill pass at all on ordinary Type 2 changes — the trade-off
  is one extra fact-table column (the durable key) and, if a physical
  filtered table is used instead of a view, an extra table to keep in sync
  on every load pass.
- **"As of" reporting** is the dual-key approach's added capability: because
  the fact table already carries the durable key, historical facts can be
  rolled up by the attribute profile in effect on *any* specific past date,
  not just current or event-time — filter the type-2 dimension's
  effective/expiration dates to the target date to collapse it to one row
  per durable key, then join on the durable key. Skipping the
  effective/expiration filter and joining directly on the durable key
  multiplies every fact row by however many type-2 versions that entity has
  accumulated — a correctness bug that's easy to introduce by treating the
  durable key as if it were unique per dimension row.

Both approaches are strictly more load work than plain Type 2, and both
depend on Type 2 processing already being correct underneath — pick one
only once the business has confirmed it actually needs current-value
rollups, rather than defaulting to it for anticipated future flexibility.
