---
type: concept
title: Group Change Rule
description: A business rule identifying which combinations of attributes must change together before a type 2 dimension treats the change as history-worthy rather than a correction.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 3"
---

A [type 2 slowly changing dimension](slowly-changing-dimension-type-2.md) attribute needs to distinguish two different reasons its source value might change: a genuine change worth preserving in history (a customer really moves) versus a correction of previously wrong data (a typo in the street address gets fixed) that should simply overwrite in place, the way a [type 1](slowly-changing-dimension-type-1.md) attribute would. Type 0 and type 1 attributes don't face this ambiguity — they treat every incoming value the same way regardless of why it changed — which is what makes this specifically a type 2 problem.

The ideal source is a change-reason code supplied directly by the operational system, but this is rare in practice; proactive dimensional modeling can request that new operational systems be built to capture update reasons explicitly, since retrofitting reason capture after the fact is much harder. Absent a reliable reason code, a **group change rule** defines, purely from the pattern of which attributes change simultaneously, whether a change is a correction or a real change. For example: if `street` changes but `zip_code` doesn't, treat it as a minor correction (overwrite, no new row); if `street` and `zip_code` change together, treat it as a genuine relocation worth a new type 2 row.

Discover group change rules by asking stakeholders directly which attributes change together, or by framing the question around the real-world activity rather than the data: "when a customer really moves — as opposed to just correcting their address — which attributes should change?" This framing also tends to surface attributes the initial discovery pass missed.

## Notation and nesting

Document group membership with numbered short codes on each attribute: an attribute marked **CV, HV1** is type 1 (correction) by default, but becomes historically tracked (type 2) specifically when every other member of group 1 changes at the same time. Groups can nest: a wider group can require an additional attribute (e.g. `country`) on top of a narrower group's members, so that a within-country move (street, zip, city all changing) is tracked as history without requiring country to change too, while country's own history is only tracked when the full, wider group changes together. An attribute that is unconditionally type 2 on its own, but also participates in a group rule governing when a *different* attribute becomes historical, is marked with both codes together (e.g. **HV, HV2**) rather than **CV, HV2** — the unconditional type 2 policy for that attribute takes precedence over the group rule.

Group change rules are a discovery-time refinement of the [type 2](slowly-changing-dimension-type-2.md) decision already made for the attributes involved — see [discovering each attribute's policy](slowly-changing-dimension.md) for the change-story technique that identifies which attributes are type 2 candidates in the first place.
