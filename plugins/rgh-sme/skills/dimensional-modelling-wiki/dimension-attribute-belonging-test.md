---
type: concept
title: Dimension Attribute Belonging Test (Moment-in-Time Test)
description: A discovery-time test for whether a candidate attribute belongs to a dimension — asking whether the dimension's subject can have more than one value of it at a single moment in time.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 3"
---

When discovering attributes for a [dimension-table](dimension-table.md), a candidate attribute belongs on that dimension only if it is single-valued for the dimension's subject at any one moment in time — the same "one value per row" discipline [grain](grain.md) applies to a fact table's dimensions, applied instead to an individual dimension's own attributes.

The test is phrased so **"no" is the desired answer**: "Can a [dimension] have more than one [attribute] at any one moment in time, ignoring history?" A confident **no** (e.g., "can a customer have more than one customer type?") means the attribute has a 1:1 or many:1 relationship with the subject and belongs directly on the dimension. A confident **yes** usually means the attribute doesn't belong to *this* dimension at all — testing PRODUCT TYPE against CUSTOMER fails, since a customer can use several products of different types at once, which is really a sign that the attribute belongs on a different, already-identified dimension (PRODUCT).

An ambiguous "yes" needs refinement before it can be classified. "Can a customer have more than one address?" is genuinely ambiguous:

- If stakeholders mean there's a single primary address that should drive geographic analysis, refine the question to "Is there a single primary address that should be used for reporting?" — if so, a qualified attribute ("billing address") belongs on the dimension after all.
- If stakeholders mean a customer can legitimately have many addresses at once (delivery addresses for gifts, multiple corporate locations), that's a genuine many:many relationship — evidence of a missing event detail (a **where** detail the event modeling missed) that should become its own dimension, not an attribute squeezed onto an existing one. Alternatively, it can mean the dimension's own [grain](grain.md) needs adjusting (e.g., redefining CUSTOMER as customer-per-location with a composite [natural key](natural-key.md)), if stakeholders genuinely treat each location as a distinct customer.

A composite address further decomposes into its own hierarchy of attributes (street, city, region, postal code, country) that should be modeled individually once well understood, rather than left as one opaque field.

## An earlier, faster cousin: the position-sensitivity test

During event discovery, before any dimension is being modeled in its own right, the [position-sensitivity test](position-sensitivity-test.md) catches the same underlying mistake — a candidate detail that really belongs to an existing subject or object rather than to the event as a whole — using a quick sentence-reordering check instead of the moment-in-time question. The two tests generally agree; the position-sensitivity test is the practical shortcut for triaging a detail as it surfaces mid-conversation, while this test is the systematic pass applied once a dimension's full attribute set is being discovered.
