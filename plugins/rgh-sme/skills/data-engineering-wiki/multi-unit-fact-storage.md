---
type: concept
title: Multi-Unit-of-Measure Fact Storage
description: >
  Storing a quantity fact once plus its conversion factors, instead of one
  column per unit of measure different consumer groups want to view it in.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 6"
---

Different functional groups routinely want the same quantity fact in
different units — manufacturing in shipping cases, sales in scan units,
finance in equivalized consumer units. Storing one column per unit (10 base
facts × 5 units → 50 stored facts) doesn't scale, and burying the conversion
factor in a dimension table forces every consumer to multiply or divide it
themselves — error-prone on its own, and worse once conversion factors
change over time, since a consumer then also has to pick the factor that
was valid at the fact's own point in time rather than whatever's current.

The load-time answer, the same underlying technique as [multi-currency fact
storage](multi-currency-fact-storage.md): store the base quantity facts plus
their conversion factors *as facts on the same row* (10 base facts + 4
conversion factors, needing only n−1 factors for n units since one unit is
already the stored base), and expose the full or partial set of derived,
converted facts to users through one or more views rather than every
consumer recomputing the multiplication independently. Packaging the
factors directly on the fact row is what guarantees they're always applied
using the value that was actually in effect for that row, rather than
whatever the dimension table happens to say today.

A secondary payoff specific to this pattern: keeping conversion factors as
row-level facts instead of dimension attributes means a factor that changes
routinely doesn't force a new [Type 2](insert-only-history-pattern.md)
dimension row every time it moves — a conversion factor behaves more like a
fact than a slowly-changing descriptive attribute, and storing it as one
avoids treating routine factor drift as a dimensional change event.
