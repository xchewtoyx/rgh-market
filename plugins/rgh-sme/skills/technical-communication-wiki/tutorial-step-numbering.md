---
type: concept
title: Tutorial Step Numbering
description: >
  Number only steps that require the reader to act, fold system-side
  effects into the step they belong to, and show input and output on
  separate lines so a procedural tutorial reads as a sequence of real
  user interventions.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 12"
---

A tutorial's numbered steps should track **user interventions**, not every event that happens while the user works. When the tutorial follows what the reader does, number only actions the reader must perform — do not give separate numbers to system-side effects the reader does not need to execute. Fold those side effects into the user step they result from instead. Combine atomic operations logically so each numbered step represents one meaningful intervention; a tutorial that numbers invisible setup work alongside user clicks inflates its apparent length and hides how little the reader actually has to do.

State prerequisites explicitly at the start — assume no domain knowledge unless you say otherwise. When the tutorial follows some other actor ("life of a server," "life of a request"), number from that actor's perspective instead, but keep the same rule: numbered steps should mark deliberate transitions in the story, not every internal subroutine. Denote user-visible input and output on separate lines (monospaced, visually distinct from prose) so a reader can verify they are on track. The best time to write or repair a tutorial is while following it yourself — take notes on everything you had to do, then edit down from the mistakes you made; see [choosing documentation types](choosing-documentation-types.md) for how tutorials differ from how-to guides and reference material.
