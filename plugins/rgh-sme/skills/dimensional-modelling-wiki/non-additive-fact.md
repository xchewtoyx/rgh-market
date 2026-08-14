---
type: concept
title: Non-Additive Fact
description: A numeric fact, such as a ratio or unit price, that cannot be validly summed across any dimension and must be recomputed from its additive components.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
---

A non-additive fact cannot be summed across any dimension. Ratios and percentages are the clearest examples — gross margin (gross profit ÷ extended sales revenue) cannot be summed along any dimension; correctly aggregating it requires summing the numerator and the denominator separately across the rows in scope, then dividing ("ratio of the sums, not sum of the ratios"). Unit price is another example: summing per-unit prices across rows produces a meaningless number (1 widget at $1.00 plus 4 widgets at $0.50 does not sum to "$1.50 total," nor does it simply average to 75 cents — the correct weighted average is total sales ($3.00) divided by total quantity (5) = $0.60).

The recommended handling is to store the fully [additive fact](additive-fact.md) components (e.g., extended sales and extended cost) in the [fact-table](fact-table.md), and compute the non-additive ratio at query time or in the BI layer, rather than storing the ratio itself — an [olap-cube](olap-cube.md) handles this kind of query-time computation well. Whether to physically store a non-additive fact at all is debatable given its limited value outside direct filtering or report printing; some fundamentally non-additive facts (e.g., a temperature reading) supplied directly by a source system may still be carefully averaged if business analysts agree the average is meaningful.

Contrast with fully [additive fact](additive-fact.md)s and [semi-additive fact](semi-additive-fact.md)s.
