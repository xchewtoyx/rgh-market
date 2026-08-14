---
type: concept
title: Slowly Changing Dimension
description: The family of techniques (types 0-7) for handling a dimension attribute's value changing over time.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 5"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 3"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 3"
---

Dimension attributes are relatively static but not fixed forever — product hierarchies get restructured, customers move. A slowly changing dimension (SCD) technique is the deliberate strategy chosen for how a [dimension-table](dimension-table.md) responds when a real-world attribute value changes. It's common for a single dimension table to combine different SCD techniques across its different attributes — there is no single correct technique for an entire table.

Dimensional designers must proactively work with business [data governance](data-governance-for-conformed-dimensions.md) representatives to decide the appropriate change-handling strategy for each attribute; this decision should not be made by IT alone, and the topic going unmentioned during requirements gathering doesn't mean the business doesn't care about it. Putting every changing attribute directly into the fact table, on the false assumption that dimensions are static, is unacceptable — dedicated per-attribute strategies within the dimension table are needed instead.

## The techniques

- [Type 0: Retain Original](slowly-changing-dimension-type-0.md) — the attribute never changes.
- [Type 1: Overwrite](slowly-changing-dimension-type-1.md) — the old value is replaced, destroying history.
- [Type 2: Add New Row](slowly-changing-dimension-type-2.md) — a new dimension row captures the change, preserving history exactly.
- [Type 3: Add New Attribute](slowly-changing-dimension-type-3.md) — a new column preserves the prior value alongside the current one.
- [Type 4: Add Mini-Dimension](slowly-changing-dimension-type-4.md) — fast-changing attributes are split into a separate, smaller dimension.
- [Type 5: Mini-Dimension and Type 1 Outrigger](slowly-changing-dimension-type-5.md) — type 4 plus a current-value reference on the base dimension.
- [Type 6: Add Type 1 Attributes to a Type 2 Dimension](slowly-changing-dimension-type-6.md) — combines types 1, 2, and 3 in one dimension table.
- [Type 7: Dual Type 1 and Type 2 Dimensions](slowly-changing-dimension-type-7.md) — carries both a durable key and a type 2 surrogate key on the fact table.

An apparent attribute that should never change once set (e.g. "age at signing") usually isn't a new response type at all — see [frozen attribute](frozen-attribute.md).

Type 2 is the safest default when the business isn't certain what rule an attribute should follow — it's the only technique that preserves full history, and later can be layered with a type 6- or type 7-style "current value" view on top; reverting from a type 1 choice back to type 2 retroactively requires significant rework (new rows, fact table rekeying), whereas a type 2 dimension deployed too cautiously never loses information that later analysis needs.

The response type is chosen and documented per attribute, not per dimension table or per change event — shorthand like "state is a type 2 attribute" really means "for a given natural key, if the source value of this attribute changes, apply type 2." Some source systems log the *reason* for a change, which can legitimately drive different response types for the same attribute depending on that reason — e.g. marital status changed via an "error correction" reason gets handled as type 1, while the same attribute changed via an actual life-event reason gets handled as type 2.

## Discovering each attribute's policy: change stories

During requirements gathering, an attribute's SCD policy is discovered one attribute at a time by asking two questions in sequence, never conflated into one:

1. "Can the [attribute] of a [dimension] change?" A confident **no** settles the attribute as [type 0](slowly-changing-dimension-type-0.md) (fixed value) — document it by copying its example value unchanged, and move to the next attribute.
2. If yes: "If [attribute] changes, will you need its historic values for grouping and filtering your reports?" — never ask "do you want current or historic values," since the answer to that framing is trivially always "current" and settles nothing; it also wrongly implies an either/or choice, when a type 2 attribute's current value is still exactly what's shown for the most recent events. A **no** here settles the attribute as [type 1](slowly-changing-dimension-type-1.md) (current value only, "as is" reporting) — but before accepting it, confirm stakeholders understand what they're giving up: a misstated history and reports that silently produce different results if rerun after a later change. A **yes** settles the attribute as [type 2](slowly-changing-dimension-type-2.md) (historic value, "as was" reporting).

Treat a type 1 ("current value") answer as a *reporting* default, not a *storage* mandate — for most attributes it's entirely feasible to store full type 2 history while still defaulting reports to current-value behavior, satisfying stakeholders who asked for "current" without destroying the underlying history a later requirement might need. A type 2 attribute can likewise be **recast** back to a current-value ("as is") view, or to a specific fixed date ("as at," e.g. a financial year-end), without needing to store the data any differently — see [current-value view over a type 2 dimension](current-value-view-over-type-2-dimension.md) for the self-join technique this relies on. This flexibility is also what lets stakeholders change their mind about current-vs-historic reporting later without a warehouse reload.

Documenting this discovery directly on each dimension's worked examples — writing the "before" and "after" value into two rows and asking whether both rows should show the same value (type 1) or genuinely different values (type 2) — makes the consequence of each choice visible to stakeholders before it's finalized, rather than settling it as an abstract policy question. A [natural key](natural-key.md) itself should generally be treated as type 0: if it's known to actually change, that calls for dedicated ETL to detect and handle the change, not an ordinary attribute-level SCD policy. See [group change rule](group-change-rule.md) for distinguishing a genuine change from a same-attribute correction once type 2 is chosen, and [profile changes as SCD attributes vs. fact events](profile-changes-as-scd-vs-fact-events.md) for when a change is frequent or detailed enough that it should become its own fact table instead of a dimension attribute.
