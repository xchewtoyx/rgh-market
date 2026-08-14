---
type: concept
title: Deduplication and Survivorship
description: >
  Matching the same real-world entity across source systems and merging the
  matched records into one row using a priority rule per column, when
  identical keys alone can't be trusted to find every duplicate.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

Deduplication comes up whenever a dimension — customer is the canonical
example — is assembled from more than one source system or line of business.
Matching two records as "the same entity" may be as simple as an identical
key column, but often needs fuzzy criteria (near-matching names or
addresses), and different sources frequently disagree on other attributes
even once they're confirmed to be the same entity.

**Survivorship** is the process that resolves that disagreement: combining
matched records into a single unified row using business rules that define,
per attribute, a priority order across the contributing source systems for
which one's value "wins." When a dimension is fed from multiple systems, keep
a separate back-reference column (the natural key) to each contributing
source rather than discarding them once merged — without it, there's no way
to trace a survived attribute value back to which source actually supplied
it, or to re-run survivorship if the priority rules change later.

This is the mechanical predecessor to
[conformed dimensions](warehouse-layering-source-staging-presentation.md):
survivorship is what makes a dimension structurally identical, deduplicated,
and standardized in the first place, before it can be conformed across
processes. It's also the pipeline-level manifestation of
[master data management](master-data-management.md) — MDM sets the
organizational priority rules and golden-record policy; deduplication and
survivorship is how a load actually applies them. For genuinely difficult
matching (large volumes, weak keys, ambiguous fuzzy matches), purpose-built
data integration and standardization tools generally outperform hand-rolled
matching logic.
