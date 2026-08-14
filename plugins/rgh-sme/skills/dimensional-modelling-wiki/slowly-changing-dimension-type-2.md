---
type: concept
title: "Slowly Changing Dimension Type 2: Add New Row"
description: Inserting a new dimension row with a new surrogate key to capture a changed attribute value, leaving prior fact rows pointing at the old row.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 5"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 8"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 6"
---

Type 2 is the predominant technique for correctly representing history in a [dimension-table](dimension-table.md), and the **safest default** [slowly changing dimension](slowly-changing-dimension.md) choice when the business hasn't yet decided on a rule for an attribute. On a change, a new dimension row is inserted with a new [surrogate key](surrogate-key.md) holding the new attribute values; the [fact-table](fact-table.md) is left completely untouched — old keys are never back-updated. New fact rows reference the new surrogate key; historical fact rows keep referencing the old one. This "perfectly partitions" history: a report covering a period before the change produces identical results whether it's run before or after the change happens.

Because type 2 requires multiple rows to describe one real-world entity over time, a [durable key](durable-key.md) is needed to identify the entity across all its versions — the natural or durable key is "the glue that holds the separate type 2 rows for a single entity together," and should be used (not the surrogate key) for distinct-count questions like "how many products." Constraining on the changed attribute differentiates profiles by version; constraining on a stable descriptor instead fetches all versions and joins to the full fact history automatically.

No aggregation tables or [olap-cube](olap-cube.md)s need to be rebuilt for a type 2 change, unlike [type 1](slowly-changing-dimension-type-1.md) — the new row simply starts accumulating new facts under its own key.

## Effective and expiration dates

Type 2 rows carry administrative **effective** and **expiration** date/timestamp columns marking when the row's attribute values are valid — this specific technique (sometimes called "effective dating," or a **transaction tracking dimension**) is what lets a single type 2 change be localized to a particular point in time. ETL uses these to determine which surrogate key applies when loading a historical fact row — see [late arriving facts](late-arriving-facts.md). Newly loaded rows get an expiration date of 12/31/9999 (avoiding nulls, and enabling reliable `BETWEEN` queries — see [null handling in dimensional models](null-handling-in-dimensional-models.md)). Convention: the old row's expiration date is set just prior to the new row's effective date, leaving no gap — the granularity of "just prior" depends on the grain at which changes are tracked (day vs. timestamp). An alternative convention sets the old row's expiration exactly equal to the new row's effective date, requiring `>= effective AND < expiration` logic instead of `BETWEEN`. A current-row indicator flag is a useful complement for quickly constraining to only-current profiles.

Without effective/expiration dates, plain type 2 versioning alone can only answer "what did this dimension member look like at the time of a given fact?" — it cannot answer a point-in-time question independent of any fact (e.g. "how many policy holders were married on March 1st") unless a fact row happens to exist for that exact date, since there is otherwise no way to place a version's boundaries in calendar time. A naive alternative — a separate change-tracking [factless fact table](factless-fact-table.md), one row per dimension change, with its own effective/expiration date columns — works but ends up with the same row count as the dimension table itself, which is a sign that the effective/expiration columns belong directly on the dimension instead.

**Multiple changes on the same day**: if same-day changes are common enough that they must be distinguished, add `effective_time`/`expiration_time` columns alongside the date columns, at whatever granularity (hours, minutes, seconds) is needed, kept non-overlapping and gap-free the same way the date columns are. This means a date-only query predicate can now return more than one version of the same entity for a single day — for clean end-of-day status, add a `last_change_of_day` flag (e.g. "Final" on the day's last version) and filter on it explicitly.

**ETL payoff**: without effective/expiration columns, determining which surrogate key an incoming transaction should reference requires comparing the transaction's full set of type 2 attribute values against dimension history. With them, ETL only needs the entity's natural key and the transaction's date, compared against `effective_date`/`expiration_date` to find the matching row — this is especially valuable when a new fact table is added later against an already-established dimension, since the new source only needs to supply natural key plus date, not a full attribute snapshot, to identify the historically correct row. Time-stamping like this is most worth the extra ETL maintenance for core, widely conformed dimensions; simple reference/lookup dimensions usually don't need it.

## Hybrid attributes

A dimension attribute that is additive when the dimension table is queried standalone (no fact table join) is called a hybrid attribute — usable as either a dimension or a fact depending on the query. For example, `SELECT state, SUM(covered_parties) FROM policy ... GROUP BY state` sums `covered_parties`, an ordinary dimension column, exactly as if it were a fact. This is a common phenomenon specifically in dimensions carrying effective/expiration dates, since each row already represents a bounded span of time over which the attribute's value held, making it meaningful to aggregate directly.

Type 2 requires surrogate keys — a natural key is insufficient on its own, and appending version digits or effective dates onto the natural key is also inadvisable; the surrogate key alone should establish the fact-to-dimension linkage. See [surrogate key](surrogate-key.md).

## Change reason tracking

A type 2 row can carry a change-reason attribute recording why it was created — a short code or a legible label such as "Last Name" or "Address Change" — embedding ETL lineage metadata alongside the data itself. Because several attributes can legitimately change at once within a single new row, the change reason is inherently multivalued: handle it either as a single delimited text string or via a multivalued [bridge table](bridge-table.md), the same technique used for other multivalued dimension attributes. Also see [profile changes as SCD attributes vs. fact events](profile-changes-as-scd-vs-fact-events.md) for the related question of when a stream of profile-change transactions should become type 2 dimension rows at all, versus its own fact table.

## Micro-level vs. macro-level change

Not every type 2 change costs the same. A **micro-level** change affects one dimension member at a time for its own reasons — one customer's category changes because that customer's behavior changed — and produces the ordinary one-row-expired, one-row-inserted pattern type 2 is built for; this is usually easy to justify against the row growth it causes. A **macro-level** change instead comes from redefining the *concept* itself — renaming every "Great Customer" to "Wonderful Customer," say — and type 2's row-per-change mechanics apply it member by member regardless, expiring and reinserting a row for every affected member at once (potentially millions of rows for a single relabeling). This is much harder to justify purely as history: the dimension gains a huge number of "historical" versions that don't reflect any change in the underlying member, only a change in how the category is labeled. A macro-level change is usually better handled as a deliberate one-time correction (closer to [type 1](slowly-changing-dimension-type-1.md) in intent, even if it must be executed as type 2 rows for mechanical reasons) than processed through the same pipeline as ordinary micro-level history.

## Type 1 corrections within a type 2 dimension

A type 1-style correction (for example, fixing an erroneous product introduction date) may need to be applied to *all* existing versions and rows of that entity, not just the current one — this is a distinct ETL business rule that data stewards must define explicitly, separate from how the dimension normally tracks type 2 changes.

## Type 2 under other names in modern tooling

The same technique recurs under different names once analytics-engineering tools and alternative modeling methodologies enter the picture — recognizing this matters because it means type 2's rules (durable key, effective/expiration dating, surrogate keys, never mutating history) still apply even when the surface vocabulary is unfamiliar. The dbt "snapshot" feature builds new-row-with-new-key change history on a source table, which is a type 2 implementation under the hood. In Data Vault modeling, a "satellite" table capturing an entity's changing descriptive attributes over time is likewise functionally a type 2 dimension — see [Data Vault versus dimensional modeling](data-vault-versus-dimensional-modeling.md). Neither tool nor methodology eliminates the need to understand type 2's underlying rules — they automate its mechanics, not its design decisions.
