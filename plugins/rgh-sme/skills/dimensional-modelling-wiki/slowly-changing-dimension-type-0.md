---
type: concept
title: "Slowly Changing Dimension Type 0: Retain Original"
description: An attribute whose value never changes, so facts are always grouped by the original value.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 5"
---

Type 0 is the simplest [slowly changing dimension](slowly-changing-dimension.md) technique: the attribute value never changes, so facts are always grouped by the original value regardless of when the report is run. It is appropriate for any attribute explicitly labeled "original" (e.g., a customer's original credit score) and for most [date dimension](date-dimension.md) attributes, which are inherently immutable once assigned.

[Durable keys](durable-key.md) — and, by convention, a dimension's own [surrogate key](surrogate-key.md) once assigned to a specific historical row — are always treated as type 0: presumed durable and inviolate for the life of the entity they identify.
