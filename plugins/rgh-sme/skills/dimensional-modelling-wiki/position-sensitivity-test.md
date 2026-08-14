---
type: concept
title: Position-Sensitivity Test (Detail About Detail)
description: A discovery-time sentence test for whether a newly surfaced detail belongs to the event itself or is really an attribute of an existing subject/object detail.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 2"
---

While working through the [7Ws](seven-ws-framework.md) to discover an event's details, a newly surfaced "detail" can turn out to be **detail about detail** — a characteristic of an *existing* detail rather than a genuine detail of the event as a whole. This risk is greatest from open-ended *what* questions: asked "with what?" a stakeholder may answer "PRODUCT TYPE," which sounds like a new event detail but is really an attribute of the PRODUCT already on the table.

The test: mentally swap the candidate detail into a different position within the event's main clause and read the sentence both ways.

- "CUSTOMER orders PRODUCT with PRODUCT TYPE" reads fine.
- "CUSTOMER **with PRODUCT TYPE** orders PRODUCT" does not.

Because the sentence only makes sense with PRODUCT TYPE positioned next to PRODUCT, the detail is **position-sensitive** — it belongs to PRODUCT, not to the event as a whole. Rather than being discarded, it is placed in a scratchpad space (reserved above the relevant subject/object column on a BEAM✲ table) for later use when that dimension's own attributes are modeled.

By contrast, a genuine event detail passes the test in any position: "from SALESPERSON, CUSTOMER orders PRODUCT" reads just as naturally as "CUSTOMER orders PRODUCT from SALESPERSON," confirming SALESPERSON is a detail of the event itself, not of CUSTOMER or PRODUCT.

## Relationship to the moment-in-time test

This is an earlier, faster-to-apply cousin of the [dimension attribute belonging test](dimension-attribute-belonging-test.md) (the "can this subject have more than one value of this attribute at a moment in time?" question asked later, once a dimension is being modeled in its own right). The position-sensitivity test is applied *during* event-story discovery, before any dimension has its own dedicated modeling session, to quickly triage a detail as it surfaces rather than let it get recorded as an event-level column by default. The moment-in-time test is applied once a dimension is being modeled properly and needs every one of its attributes discovered and validated systematically — the two tests generally agree, but the position-sensitivity test is the practical shortcut for catching an obvious case in the middle of a live event-modeling conversation.

## When several details fail the test

If several candidate event details all turn out to be position-sensitive to the same subject or object, reconsider whether the event stories being told are actually different enough that they belong in separate event tables — an event whose "details" keep collapsing into attributes of one subject is a sign of an over-generalized event that has stopped being meaningful to stakeholders as a single story.

After finishing a round of questions for one W-type, scan back through the earlier Ws — a detail newly recognized as position-sensitive (and thus reclassified into a dimension) can jog loose further details that belong to *that* dimension, worth capturing in the scratchpad before moving on.
