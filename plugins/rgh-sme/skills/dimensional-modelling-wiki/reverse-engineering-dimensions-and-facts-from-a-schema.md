---
type: concept
title: Reverse-Engineering Dimensions and Facts from an Existing Schema
description: Heuristics for recovering a candidate conceptual dimensional model from an undocumented physical schema, to anchor a validation conversation with the business.
sources:
  - title: "Data Modeling with Snowflake"
    resource: "Data Modeling with Snowflake (Serge Gershkovich), ch. 7"
---

Real systems accumulate schema complexity over years, often outliving anyone's complete mental model of them. When no conceptual model exists, the [four-step dimensional design process](four-step-dimensional-design-process.md) can be run in reverse against the physical tables to produce a *draft* candidate model — going from "what is" to a best guess at "what ought to be" — which is then used to anchor a validation conversation with the business, rather than treated as authoritative on its own.

## Classifying tables as facts or dimensions

Naming conventions are the first signal:

- **Dimension tables** tend to use singular nouns (`CUSTOMER`, `PRODUCT`, `NATION`) and hold descriptive, non-quantitative attributes.
- **Fact tables** tend to use transitive-verb-derived names (`ORDERS`, `SHIPMENTS`) and hold quantitative measures recorded per transaction.

## Establishing relationships and candidate keys

If primary/foreign key constraints are actually declared, a modeling tool can derive relationships automatically. Absent constraints (common in warehouse schemas, since only `NOT NULL` is enforced by default on many platforms — see the constraint-enforcement caveat under [surrogate key](surrogate-key.md) and [natural key](natural-key.md) usage), infer candidates from naming: a column resembling `<table name> + id/key/code` (e.g. `N_NATIONKEY` inside table `NATION`) strongly suggests it is that table's key.

Validate a key candidate with a duplicate check before relying on it:

```sql
SELECT N_NATIONKEY, COUNT(*) AS CNT FROM NATION
GROUP BY 1
HAVING CNT > 1
```

No rows returned is *supporting* evidence, never proof — the absence of duplicates in current data cannot conclusively establish uniqueness, and only the business can conclusively confirm the true [grain](grain.md) of a dimension. Once a dimension's key candidate is established, search fact and other dimension tables for matching columns to identify likely [conformed dimensions](conformed-dimensions.md) and conformed attributes; consistent column naming across tables makes both this manual search and automated relationship-detection tooling far more reliable.

## Why the draft still needs business validation

Physical constraints alone underdetermine conceptual cardinality and optionality — the same physical relationship can support multiple valid business interpretations, and data can only hint at which one is correct. The reverse-engineered draft may also reveal that the physical schema has drifted from the true current business model over time (renamed processes, merged or split departments) — validating the draft with the business can surface changes that need to flow back into the physical model, not just corrections to the draft. This is also the point at which it may become clear that a single fact table actually serves more than one [business process](business-process.md), something the data alone cannot disambiguate.
