---
type: concept
title: Multiple Currency Facts
description: Storing each financial fact in both its transaction currency and a standard currency, using a currency dimension to identify the true transaction currency.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
---

A [fact-table](fact-table.md) recording multi-currency financial transactions should carry a pair of columns per financial fact: one holding the value in the transaction's true currency, and one holding the value converted to a standard currency via an approved ETL business rule. This requires a currency dimension identifying the transaction's true currency on each row, so users can report in either the local or standard currency without ambiguity about which conversion, if any, has already been applied. This pattern can extend to a third metric set (e.g. a regional roll-up currency) or to metric pairs for other currency-bearing roles on the same row (such as ship-to versus bill-to currency); in every case, the fact table holds one full metric set per role plus its conversion rate(s), and any further extrapolation between them should happen in a view rather than being left to users to compute themselves.

## Currency conversion fact table for arbitrary reporting currency

The paired local/standard columns above only satisfy the two currencies actually stored. When any manager needs to view volume converted into *any* currency they choose, supplement the main fact table with a separate currency conversion fact table whose dimensions are the currencies themselves (a currency-to-country mapping isn't one-to-one, so country is not a suitable dimension here). Local sales reps and HQ management typically query the main fact table directly using its built-in pair of currencies; the currency conversion table serves the less predictable requirement of converting to an arbitrary third currency, at the cost of a more complex query to navigate. The conversion table should hold only the currency pairs that realistically occur, not the full Cartesian product of all traded currencies — with roughly 100 global currencies, a full product would produce about 10,000 daily rows, most of them for pairs that aren't a meaningful market. It may also need to carry multiple defined rates per pair (e.g. end-of-month or end-of-quarter close rates alongside the daily rate), including rates determined well after the underlying transactions were already loaded.
