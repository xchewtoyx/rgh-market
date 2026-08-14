---
type: concept
title: Text Comments Dimension
description: Storing freeform comment text outside the fact table, in a dedicated dimension referenced by a foreign key, rather than as a textual fact.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 9"
---

Freeform comments should be stored outside the [fact-table](fact-table.md) — in a separate comments dimension, or as attributes in a dimension with one row per transaction if comment cardinality matches the transaction count — referenced via a fact table foreign key, rather than as a textual metric embedded directly in the fact table. This follows from the general fact-vs-dimension-attribute test: true free text is rare and does not participate in calculations, so it belongs in a dimension even though it isn't used for constraining or grouping the way most dimension attributes are. See [fact-table](fact-table.md) for the broader test distinguishing facts from dimension attributes.

Before committing to freeform storage, check whether the comment can instead be parsed into well-behaved, discrete-domain dimension attributes (e.g., classifying it as a compliment versus a complaint) — though the full original text is often still wanted alongside any parsed classification. Comment text should never be treated as "just another [degenerate dimension](degenerate-dimension.md)" placed directly in the fact table — even though it technically has no associated lookup table, freeform text is bulky, and dragging it along on every operation involving the fact table's real performance metrics degrades exactly the queries that matter most.

**Choosing between the two placements**: use a genuine comments dimension (a small table of distinct comment values, referenced by foreign key) when the number of distinct comments is much smaller than the number of transactions — common in practice, since many rows share literally "No Comment." Use a transaction-grained dimension attribute instead when each event's comment is effectively unique, since a shared comments dimension buys nothing when there's no repetition to exploit. Either way, joining a sizeable text dimension into a query is comparatively slow — but by the time users actually want to read comments they've usually already filtered heavily (there's a practical limit to how many freeform comments a person can read at once), so this cost is confined to comment-inclusive queries and doesn't burden the far more common performance-metric analyses that never need to join the comments dimension at all.

A related bulky-content question arises when a business process also captures images rather than text — see [image attribute storage](image-attribute-storage.md) for the filename-reference-versus-blob trade-off.

## Enriching a comment dimension iteratively

A comments dimension is often a reasonable place to start even when the free text represents a genuine [causal dimension](causal-dimension.md) — a salesperson's freeform reason for varying a customer's price, for example — since building parsed, structured attributes for every such reason up front isn't always feasible. The dimension can then be improved incrementally: low-cardinality descriptive tag attributes, derived from keyword extraction ("textmining") applied to the comment text during ETL, add proper report row headers and consistent, filterable groupings on top of the original free text, without requiring the raw comments to be discarded or the fact table's grain to change. This lets a comments dimension start as simple, searchable free text and grow into a more structured causal dimension over successive iterations as the value of doing so becomes clear.
