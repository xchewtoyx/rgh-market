---
type: concept
title: Iteration Zero
description: >
  Running a few architecture-design iterations before regular feature
  sprints begin, to settle the patterns and structures that are expensive
  to change later, without reverting to a full up-front design phase.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 24"
---

How much architecture work belongs up front is a real spectrum, not a
binary "agile vs. waterfall" choice. At one end, **Big Design Up Front**
does full design before any coding starts; at the other, **emergent
design** does no deliberate design at all and lets architecture fall out
of incremental coding — workable for small, simple, easily-refactorable
systems, but not for large or quality-attribute-heavy ones, because
quality attributes like security or performance can't be bolted on after
the fact once enough code already assumes their absence.

**Iteration zero** is the middle position: run a small number of
[Attribute-Driven Design](attribute-driven-design.md) iterations before
regular feature-delivery sprints begin, aimed specifically at settling the
major patterns, reference architecture, frameworks, and components the
rest of the project will build on. It gives early structure to team
formation and work assignment, and lets the hardest [quality attribute
requirements](quality-attribute-scenario.md) get addressed first, while
still leaving the bulk of detailed design to happen incrementally as
regular iterations reach each part of the system.

When a requirement surfaces later that genuinely threatens an
already-settled architectural decision, an **architecture spike** — the
same [spike](spike-story.md) technique used for ordinary requirements
uncertainty, applied to a technical question — investigates it in a
separate, throwaway-oriented branch, merged into the mainline only if it
pans out. This lets emergent, unanticipated requirements be absorbed
without treating every one of them as grounds to redo iteration zero's
foundational decisions.
