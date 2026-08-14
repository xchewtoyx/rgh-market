---
type: concept
title: Surrogate Key Pipeline (Fact Load Key Substitution)
description: >
  Replacing a fact row's natural keys with the dimension's surrogate keys at
  load time, and the ordering and integrity rules that make the substitution
  safe.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

A fact row arrives from its source carrying natural/business keys, but a
warehouse fact table should store only
[surrogate keys](surrogate-vs-business-keys.md) as its foreign keys. The
surrogate key pipeline is the load step that performs this substitution, and
it carries the pipeline's referential-integrity guarantee: every fact foreign
key must resolve to a matching dimension row, or a sale can silently vanish
from a business user's query with no visible error.

Rules that make the substitution correct and safe:

- **Always finish updating every dimension table before loading the fact
  table.** Dimensions are the authoritative source of valid keys; loading
  facts against a dimension that isn't yet current guarantees lookups miss
  rows that should have matched.
- **Resolve historical context, not just current state.** The direct
  approach looks up every dimension row matching a fact's natural key, then
  selects the surrogate key aligned to the fact's actual point in time — via
  a current-row indicator for current facts, or by finding the row whose
  effective begin/end dates bracket the fact's transaction date for
  reloaded history or [late-arriving facts](late-arriving-data.md). Mapping
  every fact to today's *current* surrogate key regardless of when the fact
  actually happened silently corrupts historical reporting.
- **Keep the lookup tables in memory when the dimension set allows it.**
  Modern hardware generally makes pinning all the dimension tables a fact
  load needs for random-access lookup practical, which is far cheaper than a
  join-based database lookup per row at fact-table volumes.
- **Never retain the natural key in the loaded fact row** — only the
  resolved surrogate key. Keeping both invites downstream code to
  accidentally join on the natural key and reintroduce the exact
  multi-source ambiguity surrogate keys exist to prevent.
- **Don't persist input data to disk until every fact row has passed every
  processing step.** Staging a partially-processed batch risks a restart
  reprocessing rows that already got some transformations applied and not
  others.
- **Treat an unresolved lookup as a data-quality event, not a silent drop.**
  A fact whose natural key matches no dimension row, or that collides with
  an already-loaded row, is a [quality screen](quality-screens.md) failure —
  feed it back to the responsible pipeline process and record it in the
  [error event schema](error-event-schema.md) via halt, suspense, or tag,
  the same as any other quality violation, rather than quietly excluding the
  row. Ranked roughly by preference: halting is rarely useful for an
  automated incremental load; discarding the row outright is fine only when
  a missing dimension match genuinely signals business irrelevance; a
  suspense file works poorly whenever every row must eventually load (e.g.
  financial data); and assigning the row a fresh dimension key on the fly —
  the [inferred member pattern](inferred-member-pattern.md) — is generally
  the most attractive option, since it's the only one that needs no later
  destructive fix to the fact row itself.

**Disambiguating which dimension version to resolve to**, when a natural key
matches more than one dimension row because of Type 2 history, has three
concrete mechanisms, in increasing order of precision — and none of them can
be "pick the highest surrogate key value." A sequentially-assigned surrogate
key reflects *load order*, not *effective-date order*: a
[late-arriving](late-arriving-data.md) correction to an old historical
version gets a numerically higher surrogate key than the row that's actually
current today, simply because it was loaded more recently. Any lookup logic
that assumes "highest key = current version" will silently resolve facts to
the wrong dimension row the first time a late correction lands out of
sequence. The three real mechanisms: a `current_version`
flag (works whenever it's refreshed on the same schedule as the fact load
itself); an effective/expiration date range compared against the fact's own
transaction date (needed once a single natural key can undergo more than one
Type 2 change between load cycles, or when loading historical data where
"current as of today" isn't precise enough); or, lacking either, extracting
every Type 2 attribute alongside the source transaction and matching on the
full attribute set directly.

**For a historic (backfill) load against a mix of Type 1 and Type 2
dimensions**, the lookup has to resolve which *version* of a dimension row
was in effect at the fact's original transaction date, not just which
dimension member it belongs to — a `BETWEEN` join on the dimension's
effective begin/end dates, keyed on the fact's actual date rather than the
load date. At moderate volume, a single relational join from the fact
staging table to each dimension table (indexed on natural key plus effective
dates) resolves every dimension in one pass; at very large historic volumes,
that same join becomes the single most expensive part of the load, so it's
often worth splitting the (usually many, small) pure-Type-1 dimensions into
one relational-join pass and handling the (usually fewer) Type 2 dimensions
separately, or falling back to the pipeline tool's own lookup operator
instead of a database join.
