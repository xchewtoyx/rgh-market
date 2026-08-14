---
type: concept
title: Reconciliation with Set Operators
description: >
  Using EXCEPT/MINUS and INTERSECT to check two datasets against each other
  as a lightweight data-quality reconciliation technique.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Gershkovich), ch. 12"
---

Set operators combine whole result sets rather than joining on columns, and
two of them are specifically useful as [data quality](data-quality-dimensions.md)
reconciliation tools rather than just query-composition tools:

- **EXCEPT / MINUS** returns rows present in one result set but not the
  other (with deduplication) — pointed at a source extract and its loaded
  target, it surfaces exactly which rows failed to make it through a load,
  or which rows exist in a target that shouldn't be there. Run in both
  directions (source minus target, then target minus source), it's a cheap
  completeness check that doesn't require row-by-row comparison logic.
- **INTERSECT** returns only rows present in both result sets — useful for
  confirming that two independently derived datasets that are expected to
  agree (a value recomputed after a pipeline change, say, against the
  pre-change baseline) actually still agree on their genuinely shared rows,
  which is a fast way to scope down to exactly the rows that changed instead
  of diffing every row of both datasets.

Both require the two queries to share the same column count, compatible
types, and matching column order, same as any set operator. They're a
lightweight complement to the
[binary vs. statistical validation gates](data-quality-validation-tests.md)
a pipeline already runs — cheap to write, and well suited specifically to
the reconciliation-against-source-systems half of data quality engineering,
as opposed to the distributional checks statistical testing covers.
