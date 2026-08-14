---
type: concept
title: "Code Smell: Shotgun Surgery"
description: >
  A single conceptual change requires many small edits scattered across many
  different classes, making changes easy to miss — the mirror image of
  Divergent Change.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Shotgun Surgery is the mirror-image of [Divergent
Change](divergent-change.md): instead of one module absorbing many kinds of
change, one kind of change requires many small edits scattered across many
different classes — every scattered edit is a place the change can be
missed. This is [change amplification](change-amplification.md) in its most
literal form, and it's [high coupling](coupling.md) made visible: the
scattered modules turn out to have a high probability of needing to change
together.

Cures: [Move Function](move-function.md) or [Move Field](move-field.md)
consolidate the scattered edits into one module; [Combine Functions into
Class](combine-functions-into-class.md) groups functions that share similar
data; [Combine Functions into Transform](combine-functions-into-transform.md)
groups functions that all enrich the same data structure; [Split
Phase](split-phase.md) applies when scattered functions' outputs all feed one
consuming phase. At the scale of whole top-level modules, the same smell
shows up as [organizing modules by technical layer instead of business
concept](organize-modules-by-business-concept.md). A useful tactical
permission here: it's fine to first [Inline Function](inline-function.md) or
[Inline Class](inline-class.md) to smash the scattered pieces together —
temporarily creating an oversized Long Function or Large Class —
and only then re-extract along better lines. Accepting a worse intermediate
state deliberately, in service of a cleaner endpoint, is a legitimate part
of the [refactoring rhythm](rhythm-of-refactoring.md).
