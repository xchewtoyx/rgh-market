---
type: concept
title: Grain
description: The precise business-level definition of what a single fact table row represents, declared before choosing dimensions or facts.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 8"
---

Declaring the grain is the second step of the [four-step dimensional design process](four-step-dimensional-design-process.md), and the single most important decision in a dimensional design. The grain statement specifies, in business terms, exactly what a single [fact-table](fact-table.md) row represents — not as a list of dimensions or primary-key columns, but as a sentence such as "one row per individual product scanned on a point-of-sale transaction" or "one row per bank account per month."

Once declared, the grain becomes a binding contract: every candidate [dimension-table](dimension-table.md) and every candidate fact must be evaluated for consistency with it, and all rows in the fact table must sit at the same grain. Different grains must never be mixed in one physical table — each grain gets its own fact table. Failing to declare the grain explicitly before naming dimensions and facts is the most frequent error in dimensional designs; it leaves the whole design "resting on quicksand," producing circular dimension discussions and facts that don't belong.

## Atomic grain

The recommended practice is to declare the **atomic grain** — the lowest level of detail captured by the business process — rather than a pre-summarized grain. Atomic data is inherently the most dimensional: the more detailed the measurement, the more things are known for certain about it, and those become candidate dimensions. A fact table built at a rolled-up grain limits which dimensions can attach (an additional dimension is only valid if it takes a single value at the declared grain) and leaves users hitting an "analytic wall" when they try to drill below it — summary data can always be produced from atomic data, but atomic detail can never be reconstructed from a summary.

Premature summarization also blocks future schema extension: a dimension added years later can only be retrofitted onto historical fact rows if the original grain was atomic; a fact table that was pre-summarized before that dimension existed has nowhere to attach the new foreign key. See [dimensional model extensibility](dimensional-model-extensibility.md).

Rolled-up, summary grains have a legitimate place as [aggregate fact tables](aggregate-fact-table.md) built purely for query performance, but only as a supplement to — never a replacement for — an atomic-grain base table.

### Deliberately coarser-than-atomic primary grain

A narrow exception exists where declaring the fully atomic grain as the *primary* table would be impractical rather than merely unwieldy — for example, a web clickstream where the atomic grain is the individual page event, but a session-grained fact table (one row per completed visit, aggregating perhaps 5 page events into 1 row) is built as the main analytic table because it directly answers the most common questions at a fraction of the row count. This differs from an [aggregate fact table](aggregate-fact-table.md) in that it isn't a supplemental performance layer sitting alongside an atomic base table for the same purpose — it's the primary table for its own set of questions, deliberately trading away some information (which individual pages were visited, in what order) for practicality. This trade-off is only sound when a companion fact table at the true atomic grain still exists separately to answer the questions the coarser table can't — the coarser table should never be the *only* table for a process whose atomic grain is significantly finer.

## Choosing dimensions and facts against the grain

During collaborative requirements gathering, the **repeat story** — one of the five [event story themes](event-story-themes.md) — is the practical technique for discovering the grain interactively with stakeholders rather than declaring it in the abstract: ask "can this happen again, with everything else the same?" and keep extending the story with each newly discovered detail until stakeholders confirm two stories can no longer collide, at which point the combination of details that finally forced uniqueness *is* the grain.

Once the grain is fixed, identifying dimensions becomes an exercise in asking whether each candidate dimension takes exactly one value for a given grain-row; if it could produce more than one value, either the dimension is disqualified or the grain statement itself was wrong and the design must return to declaring the grain. Likewise, a candidate fact only belongs in the table if it is true to the grain — a measurement that summarizes a different level of detail (e.g., a store manager's salary on a per-transaction row, or a total over an extended timespan or wide geography added onto rows at a finer grain) does not belong, however "helpful" it might seem, because it will be silently overcounted by an automatic SUM across the mismatched dimension, producing incorrect results with no obvious error. Every dimensional design falls into one of three grain categories: [transaction fact table](transaction-fact-table.md), [periodic snapshot fact table](periodic-snapshot-fact-table.md), or [accumulating snapshot fact table](accumulating-snapshot-fact-table.md). Failing to declare and comply with the grain is considered the most damaging dimensional modeling mistake there is.

Designing a fact table directly from an intended report, rather than from the grain of the underlying measurement process, is a related and equally serious mistake — see the [designing from reports antipattern](designing-from-reports-antipattern.md).

### Never borrow a measure fact across related events

When modeling one event that is clearly related to an already-modeled one — shipments following orders, say — it's safe and encouraged to borrow the earlier event's *dimensions* (its [conformed](conformed-dimensions.md) who/what/where/why context) directly, without re-interviewing stakeholders about well-understood detail. It is never safe to borrow the earlier event's **how-many** (measure) details the same way. Doing so silently violates the grain: if a single order for 10 units is fulfilled by two partial shipments, and each shipment row is stamped with the *original order quantity* of 10 rather than the quantity actually shipped on that row, summing either quantity or its derived revenue across the two shipments doubles the true total. Order-level measures belong in the order event's own fact table at the order's true grain; a shipment fact table needs its own shipped-quantity measure, captured true to the shipment's own grain, not copied from a related but differently-grained event.

## Documenting grain as an explicit column list

Beyond the business-language grain sentence, it's useful to document grain mechanically too: mark every column that participates in the fact table's composite uniqueness with a granularity-dimension code, so the exact set of columns that together identify one row is visible directly on the table definition rather than left implicit in prose. A [degenerate dimension](degenerate-dimension.md) transaction identifier is often sufficient on its own for this (one row per call reference number, say); documenting a second, more query-friendly equivalent set of columns alongside it (e.g. customer plus date plus time, if a customer can only be on one call at a time) helps readers who think in dimensional terms rather than operational identifiers. For an [accumulating snapshot fact table](accumulating-snapshot-fact-table.md) or any snapshot updated in place rather than only appended to, this same column set doubles as the index ETL needs to find and update the correct existing row.
