---
type: concept
title: Durable (Supernatural) Key
description: >
  A pipeline-assigned, permanently stable identifier for a real-world
  entity, used when the source system's own natural key isn't guaranteed
  to stay constant over the entity's lifetime.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 3"
---

Tracking [slowly-changing-dimension](insert-only-history-pattern.md) history
for one real-world entity across multiple version rows requires something
that reliably identifies "this is still the same entity" across every
version — normally the natural key does that job. But a natural key can
itself change unexpectedly: organizational mergers, duplicate-entry cleanup,
or multi-source integration can all invalidate the assumption that a given
natural key value always refers to the same entity.

When a natural key isn't guaranteed stable, the pipeline has to assign its
own **durable identifier** — also called a **supernatural key** — at load
time: a simple sequential integer, controlled entirely by the pipeline,
immutable for the life of the system. It is loaded as a dimension
*attribute*, the same way the natural key is; it does **not** replace the
dimension table's [surrogate primary key](surrogate-vs-business-keys.md).
The three keys serve three different jobs on the same dimension table: the
surrogate key uniquely identifies one *version* row (a new one is minted on
every Type 2 change), the natural key is whatever the source system uses
today, and the durable key is the one column that keeps pointing at the same
real-world entity even if the natural key it started with later changes.

The durable key is also the join column a [dual-key hybrid SCD
design](hybrid-scd-current-value-backfill.md) uses to expose a "current
value" view over Type 2 history without losing point-in-event accuracy.

**Concrete correctness payoff**: counting distinct entities in a Type 2
dimension (e.g., "how many customers") by `COUNT`ing the dimension's own
surrogate key overcounts, since one real-world entity can own several
surrogate-keyed version rows. `COUNT DISTINCT` on the durable key (or the
natural key, where it's reliable enough) gives the correct answer because it
collapses every version back down to one entity — the same role the durable
key plays for a [current-row indicator](hybrid-scd-current-value-backfill.md)
or an as-of point-in-time count filtered on effective/expiration dates.
