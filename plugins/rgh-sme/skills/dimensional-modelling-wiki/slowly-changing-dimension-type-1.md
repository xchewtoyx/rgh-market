---
type: concept
title: "Slowly Changing Dimension Type 1: Overwrite"
description: Overwriting a dimension attribute in place with its new value, losing all history of the change.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 5"
---

Type 1 overwrites the old attribute value with the current value in place; the attribute always reflects the most recent assignment, and no dimension or fact table keys change as a result of the update. For example, if a product moves from one department to another, the existing dimension row is simply updated — no new [surrogate key](surrogate-key.md) is issued.

- It is the simplest [slowly changing dimension](slowly-changing-dimension.md) technique to implement, and leaves the fact table completely untouched.
- It **loses all history** of the attribute's prior values — historical and recent facts both appear as if the current value had always applied. The same BI report can produce different results depending on whether it's run before or after a type 1 change, which is a common source of confusing, hard-to-explain discrepancies.
- It's appropriate for insignificant corrections, or where there is no analytic value in retaining the old description — but it is frequently overused as a lazy default, which becomes hard to walk back once history has already been lost.
- **Catch**: any preexisting aggregations based on the changed attribute must be rebuilt so summary data continues to tie to atomic data. If deployed via an [olap-cube](olap-cube.md) and the type 1 attribute is a hierarchical rollup attribute, the cube likely needs reprocessing.

Type 1 is one of the components combined in [type 6](slowly-changing-dimension-type-6.md) (applied to subsequent changes on top of a type 2 row) and [type 5](slowly-changing-dimension-type-5.md) (applied to a mini-dimension reference).
