---
type: concept
title: Unknown Unknowns (Software Design)
description: >
  Unknown unknowns is the complexity symptom where it isn't obvious which
  code must change, or what information is needed, to complete a task
  safely — the worst of the three complexity symptoms because it makes the
  outcome of a change unpredictable rather than merely costly.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 2"
---

Extend the banner-color example from [change amplification](change-amplification.md):
a shared `bannerBg` variable looks easy to change safely, but if some pages
independently hardcode a "darker shade for emphasis" derived from that color,
changing the shared variable silently breaks those pages' visual consistency
— and there is no way to know which pages depend on the emphasis color without
searching all of them by hand.

This is what makes unknown unknowns worse than
[change amplification](change-amplification.md) or
[cognitive load](cognitive-load.md): with those two symptoms, once you know
what needs to change the outcome is predictable and can be gotten right. With
unknown unknowns, you can't even tell whether a proposed fix will work. The
only certain remedy — reading every line of the system — is infeasible at
scale, and even that can miss an undocumented design decision.

Unknown unknowns are produced primarily by
[obscurity](obscurity.md): information that matters for a change isn't
visible from the code you're looking at. Reducing them is what makes a system
[obvious](code-obviousness.md) rather than merely fast to read.
