---
type: concept
title: Decision Tables for Branching Diagnostics
description: Enumerating every combination of diagnostic conditions as an explicit table or tree forces complete coverage that nested prose conditionals silently omit.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements (Leffingwell), ch. 18"
---

A troubleshooting guide written as nested "if this symptom, and that condition, then check this" prose quickly becomes tangled once more than one or two conditions interact. Two problems follow: a reader unfamiliar with the system can't easily confirm they've correctly followed the logic, and the author can't be sure every combination of conditions was actually considered — some combinations simply get forgotten because prose doesn't force you to enumerate them.

## The technique

Lay out every relevant condition as a **decision table** (conditions as columns, one column per combination, the resulting action in the last row) or an equivalent **decision tree** (the same logic as branches). With *n* boolean conditions, a decision table has 2^n columns — small enough to be tractable for the handful of conditions a real diagnostic procedure usually turns on, and large enough that writing it out is what surfaces the combinations the author hadn't consciously thought about (for example, "what if the primary check passes but the secondary indicator is already in its failure state" — a combination that's easy to skip when just narrating the common cases).

Use whichever form reads more naturally for the audience: a table suits diagnostics with many largely-independent binary conditions; a tree suits diagnostics that are more naturally sequential (each answer determines which question is asked next).

## When to reach for this

Not every runbook step needs this treatment — most procedures are a straight sequence with no real branching. Reach for a decision table or tree specifically when a troubleshooting step has to account for more than one or two independent conditions at once, since that's exactly the point where prose stops reliably conveying "have we covered every case." Once written, the table itself becomes the artifact to check against when a genuinely new failure combination shows up in production: does it correspond to an existing column, or is it a case the diagnostic never accounted for?

This is a complementary tool to [System Baseline for Troubleshooting](system-baseline-for-troubleshooting.md): the baseline tells an operator what normal looks like so they can recognize a deviation exists, while a decision table tells them, once a deviation is confirmed, how to navigate the space of possible causes without missing a branch.
