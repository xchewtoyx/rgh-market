---
type: concept
title: Conformed Dimensions
description: Dimension tables that share identical column names, definitions, and domain values across fact tables, enabling integration across business processes.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 4"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 5"
---

Dimension tables conform when attributes in separate dimension tables share the same column names and domain contents. Conformed dimensions (also called common, master, reference, or shared dimensions) mean exactly the same thing wherever they're joined: consistent keys, consistent attribute column names, consistent definitions, and consistent values. A dimension is not conformed if it is merely labeled differently (Month vs. Month Name) or valued differently ("July" vs. "JULY") across the tables that use it.

## Why non-conformance breaks drilling across

[Drilling across](drilling-across.md) two fact tables runs a separate query against each, then merges the results on shared dimension attributes — a **structural** mismatch breaks the first (aggregation) phase, and a **content** mismatch breaks the second (merge) phase, even when structure matches:

- Structural: one table has a column the other lacks, or columns holding the same information are named differently (`product` vs. `prod_name`). Some structural gaps can be worked around with developer-specific knowledge (matching on natural key, applying column-equivalence rules), but the workaround has to be repeated in every affected query, defeats automated drill-across generation in BI tools, and risks inconsistent results — the same "boiling the frog" problem as forcing mismatched facts into one table (see [single vs. multiple fact tables](single-vs-multiple-fact-tables.md)). Deeper structural gaps — different definitions of what the entity *is*, or collection periods that share no common grain — cannot be worked around at all.
- Content: the same logical value formatted differently across tables (mixed case vs. all-caps), a natural key renamed via a [type 1 change](slowly-changing-dimension-type-1.md) in one star but left alone in the other, a natural key that's a single row in one star but multiple [type 2](slowly-changing-dimension-type-2.md) rows in the other (skewing comparisons toward the more recent value), or the same natural key assigned different surrogate key values across stars. Workarounds (case/punctuation normalization before joining) degrade query performance, don't cover every case, still require a skilled developer, and leave users unsure which version of a value is "correct."

The fix is for the two dimension tables involved to actually satisfy one of the conformance types below, rather than being patched around at query time.

Conforming dimensions is described as the single most important technique in the dimensional modeling arsenal, and the essence of integration in an enterprise DW/BI system. It lets information from separate [fact-table](fact-table.md)s be combined in one report by using the conformed attributes as the grouping/row-header columns, so results align correctly — this technique is called [drilling across](drilling-across.md). Conformed dimensions are defined once, with business [data governance](data-governance-for-conformed-dimensions.md), and reused everywhere they apply — delivering analytic consistency and reducing future development cost, because new work increasingly focuses on facts alone once the dimensions are "already sitting on the shelf."

Conformed dimensions are the mechanism by which separate business-process fact tables plug into the [enterprise data warehouse bus architecture](enterprise-data-warehouse-bus-architecture.md); without them, a dimensional model becomes an isolated "stovepipe" that can't be combined with others, regardless of whether the underlying model is dimensional or normalized.

## Shared dimension tables

The most direct form of conformance: two stars literally share the same logical dimension table — either the same physical table, or two-or-more identical replica tables (same structure, same content). A shared dimension table supports drilling across on any of its attributes, not just a designated subset.

When implemented as separate physical replicas rather than one shared physical table, a single ETL process should own updating the shared dimension — either by updating a master table and replicating outward, or, for large tables where full replication is impractical, by identifying new/changed rows once, doing key management once, and applying the changes to each replica. Separately built replicas make it hard to guarantee identical results, since each would need to apply identical attribute-construction rules and identical slow-change rules, produce the same row set, and use the same key values — relaxing any of this risks silently wrong analysis.

## Shrunken dimensions

A [shrunken dimension](shrunken-dimension.md) is a conformed dimension that is a subset of the rows and/or columns of a base dimension — required whenever a fact table captures data at a higher grain than the atomic base dimension.

## Degenerate dimensions can conform too

A [degenerate dimension](degenerate-dimension.md) — an attribute (typically a transaction/document identifier) stored directly in the fact table rather than in a separate dimension table — can conform under the same structure/content rule as any other dimension, anchoring drill-across between fact tables that share it (e.g. `order_id`/`order_line_num` present in both an orders fact table and a shipments fact table). One requirement is relaxed here versus shared dimensions and rollups: the same distinct combination of values need **not** appear in both fact tables. Enforcing that would force a sparsity violation — requiring every `order_id` to also appear in the shipments fact table would mean inserting zero-valued shipment rows for every order not yet shipped, cluttering reports the same way forcing mismatched-grain facts into one table does (see [single vs. multiple fact tables](single-vs-multiple-fact-tables.md)).

## Overlapping dimensions

Occasionally two dimension tables share some attributes without either being a subset of the other — an intersection rather than a [shrunken-dimension](shrunken-dimension.md) subset relationship. For example, a salesperson dimension and a customer dimension might both carry a region attribute (assigned region vs. located-in region), while each also has attributes the other lacks. Drilling across on the overlapping attribute is possible if that attribute shares structure and content between the two tables (e.g. comparing customer-support-call profitability to salesperson-compensation profitability, both rolled up by region).

This form of conformance is riskier and less broadly accepted than shared tables or rollups: the two dimensions are usually maintained by separate ETL processes, so the shared attribute can drift out of sync over time, and overlapping dimensions tend to defeat BI tools' automated drill-across features, which typically expect rollup-style conformance instead. Designers generally prefer to eliminate the overlap by extracting the shared attributes into a new third dimension table (e.g. a standalone `territory` table) — at the cost of no longer being able to browse the territory attribute alongside the rest of either original dimension's attributes directly. Two variants preserve more of that lost capability, at additional cost: adding factless fact tables that track how each original dimension's relationship to the third table changes over time (if that history matters), or turning the third table into an [outrigger dimension](outrigger-dimension.md) — giving it its own surrogate key referenced as a foreign key from both original dimensions, so each can still join directly to it for browsing, though this may defeat RDBMS star-join optimization. The choice hinges on whether cross-browsing the shared attribute alongside each dimension's other attributes is a real analytic requirement.

## Supplemental, non-conforming attributes

Attributes relevant only to one business process (for example, inventory-only product or store attributes) don't conform and can't be used for drill-across reporting — they simply live alongside the conformed attributes in the same physical dimension table without being part of the conformance contract.

## Partial conformity across many similar dimensions

A large enterprise can easily have dozens of internal customer-facing systems and dozens more external data sources, each with its own version of what is conceptually the same dimension, at wildly varying granularity and consistency, with no shared high-quality key and no organizational control over the sources. Building one single, fully comprehensive, top-to-bottom conformed dimension across all of them is often simply impossible. The lighter-weight alternative is to recognize that dimensions only need to conform on the specific attributes they actually share — same column name, same domain values, for those attributes — not identically across their entire structure; nothing requires two conformed dimensions to have matching grain or an otherwise identical attribute set.

This relaxation enables an incremental, agile path to conformance: pick one attribute of enterprise-wide significance (a high-level "customer category," for example), methodically plant it with consistent naming and values across every relevant dimension without changing any target dimension's grain or breaking the applications already built against it, and then [drill across](drilling-across.md) on the dimensions where that attribute has been added so far. Repeating this with additional attributes over time (geographic attributes such as city, county, state, and country are typically an easier next target) steadily expands the scope of cross-source analysis, with each newly conformed attribute standing on its own as a small, deliverable increment rather than waiting on a single big-bang integration effort.

## Limited conformity

For a conglomerate of unrelated subsidiaries with no cross-selling interest, enterprise-wide conformance may have little business value — it can be better to build separate, self-contained warehouses per subsidiary, accepting that "enterprise performance" questions spanning them won't be answerable. Where some integration goal does exist, it's better to start down the path with a least-common-denominator set of conformed attributes (even just a product description, category, or line-of-business) than to abandon conformance entirely.

## Governance

Reaching agreement on what a conformed dimension actually contains is a business-led process — see [data governance for conformed dimensions](data-governance-for-conformed-dimensions.md).
