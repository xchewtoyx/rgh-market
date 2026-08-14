---
type: concept
title: "Slowly Changing Dimension Type 4: Add Mini-Dimension"
description: Splitting frequently changing, frequently analyzed attributes into a separate mini-dimension keyed by the combination of values, rather than by parent entity.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 5"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 6"
---

Type 4 addresses two problems that arise in large, frequently changing dimensions (multimillion rows): browsing and query-filtering performance, and the unappealing prospect of [type 2](slowly-changing-dimension-type-2.md)-style row explosion if every rapid change were tracked with a new full dimension row. The solution is to break the frequently analyzed, frequently changing attributes out into a separate **mini-dimension**, with one row per unique *combination* of attribute values actually encountered — not one row per parent-dimension member. A customer demographic mini-dimension of age, purchase-frequency score, and income level is a typical example. Continuously variable attributes (like income) are converted to banded ranges to keep the combination count small; band definitions are hard to change later without reprocessing.

Every [fact-table](fact-table.md) row carries two customer-related foreign keys under this scheme: the customer dimension key and the mini-dimension demographics key in effect at event time. This lets the fact table itself track demographic profile changes over time — for example, a monthly [periodic snapshot fact table](periodic-snapshot-fact-table.md) picks up the customer's current age-band key at each load, without altering earlier rows.

- If users need access to a specific raw value (e.g., a monthly-updated credit bureau score) in addition to its band, include it directly in the fact table as well as banding it in the mini-dimension.
- Query performance benefits from this split: queries needing only demographic attributes can enter through the smaller mini-dimension without touching the much larger customer dimension.
- Row-count guidance: 5 demographic attributes × 10 values each ≈ 100,000 rows if every combination is prebuilt — treated as a reasonable upper bound; an alternate ETL approach builds only the combinations that actually occur. Beyond this, multiple mini-dimensions per fact table may be needed.
- If demographic profile changes can occur outside a business event (with no accompanying transaction) and point-in-time accuracy matters, a supplemental [factless fact table](factless-fact-table.md) with effective/expiration dates can capture every customer-to-demographics relationship change directly.
- Terminology: the demographics key is called a "mini-dimension" when it's part of the fact table's composite key. If instead the key sits as a foreign key on the customer dimension, it's called an [outrigger dimension](outrigger-dimension.md) — see [type 5](slowly-changing-dimension-type-5.md).

[Olap-cube](olap-cube.md)s readily accommodate type 4 mini-dimensions.

Type 4 is one of the real fixes for an overly wide, fast-changing dimension table — see [splitting wide dimension tables](splitting-wide-dimension-tables.md) for why merely splitting such a table's columns in half does not solve the same problem.

## Picking mini-dimension candidates: watch for attributes that are really derivable or really facts

Not every attribute stakeholders ask to track historically is actually a good [type 2](slowly-changing-dimension-type-2.md) or mini-dimension candidate. Age is the classic trap: tracking age itself as a historic-value attribute forces a new row (or mini-dimension member) every single year for every member, for no analytic benefit — the fix is to store date of birth as a [type 0](slowly-changing-dimension-type-0.md) attribute instead, and compute historically correct age at query time in the BI layer. If an attribute like age genuinely needs to be captured and analyzed at the same grain as ordinary transactions (medical data recording age at each visit, for instance), that's a sign it isn't a dimension attribute at all — model it as a non-additive fact on the relevant fact table instead. More generally, an attribute with no real historical significance belongs as an ordinary [type 1 (current value)](slowly-changing-dimension-type-1.md) attribute, not folded into the mini-dimension's combination-of-values key, since every additional high-cardinality attribute in the combination multiplies the mini-dimension's own row count — see the row-count guidance above.
