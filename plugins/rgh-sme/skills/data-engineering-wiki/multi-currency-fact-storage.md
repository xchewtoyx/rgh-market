---
type: concept
title: Multi-Currency Fact Storage
description: >
  Loading a monetary fact so it's usable in both its original transaction
  currency and a standardized corporate currency, without one column per
  possible currency.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 6"
---

A pipeline ingesting monetary facts from a multinational source can't add
one fact-table column per currency — the column count would grow with the
business rather than staying fixed. The load-time answer is to replace each
monetary fact with a **pair** of facts: the value in its original local
currency, and the same value converted to one standardized corporate
currency (e.g., USD) using a conversion rate applied at load time under an
agreed business rule (rate at moment of capture, end-of-day rate, etc.). A
currency-identifying dimension attribute travels alongside the pair, since
knowing a fact's originating location doesn't reliably tell you what
currency it was captured in.

The standardized-currency fact is fully additive across every dimension,
the same as any other stored derived amount — see [ratio decomposition and
derived-fact materialization](ratio-decomposition-and-derived-fact-materialization.md)
for the general principle of computing a derived amount once at load time
rather than leaving it to each consumer. The local-currency fact, by
contrast, is only additive *within* a single currency — summing local
amounts across rows captured in different currencies produces a
meaningless number, the same trap a non-additive fact presents. Any further
extrapolation between the two (multiplying or dividing by a rate to recover
one from the other) belongs in a view, not left for each report or analyst
to recompute independently.

When more than one target currency or more than one conversion basis is
needed (any manager wanting to view volume in any currency, not just the
one corporate standard), a separate currency-conversion fact table —
dimensioned by currency pairs actually in use, not the full Cartesian
product of all global currencies — supports the more open-ended lookup
without forcing every consumer through the added complexity of navigating
it for the common case.

The same underlying technique — store the base value plus its conversion
factor(s) as facts, expose derived representations via views — applies to
[multiple units of measure](multi-unit-fact-storage.md) on a quantity fact,
independent of currency.
