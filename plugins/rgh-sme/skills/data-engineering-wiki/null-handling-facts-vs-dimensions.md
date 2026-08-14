---
type: concept
title: NULL Handling Differs for Facts vs. Dimensions
description: >
  Why a load should replace sentinel values with true NULL in fact measures
  but replace NULLs with crafted defaults in dimension attributes — the
  opposite convention in each direction.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 20"
---

Source systems frequently encode "no value" as a sentinel — `-1`, `0`,
an empty string — rather than a true database NULL, and a load has to
normalize that, but the correct normalization runs in opposite directions
for facts and dimensions:

- **Fact measures**: convert sentinels to true NULL. NULL behaves correctly
  in `SUM` and `AVG` — it's excluded from the calculation rather than
  silently corrupting it the way a `-1` sentinel would if left in place and
  summed as if it were a real value.
- **Dimension attributes**: convert NULL (and other missing-value
  indicators) to a crafted default value instead — leaving NULL in a
  dimension attribute causes real problems for anyone querying or filtering
  on it directly, and for BI tools that don't handle NULL groupings
  gracefully.

One column type gets the opposite treatment from both: **fact table foreign
keys that reference dimension tables should always be `NOT NULL`.** A null
foreign key on a fact row is a [referential-integrity
failure](surrogate-key-pipeline.md) to resolve at load time — via the
[inferred member pattern](inferred-member-pattern.md) or another quality
response — never a value to load through as-is.
