---
type: concept
title: Bubble Context for Legacy Architecture
description: >
  A bubble context is a protected area where a team can design and
  document a target architecture without being immediately constrained by
  a legacy system's actual structure, with the relationship back to the
  old code made explicit rather than assumed.
sources:
  - title: Living Documentation
    resource: "Living Documentation: Continuous Knowledge Sharing by Design (Cyrille Martraire), ch. 14"
---

When a legacy system's actual structure no longer matches anyone's mental
model of it (see [deprecating design
documentation](deprecating-design-documentation.md) for the "documentation
bankruptcy" state this often follows from), designing a replacement
directly against that structure tends to just replicate its problems. A
**bubble context** is a deliberately protected area — conceptual or
literal — in which a team develops the desired target model or structure
without being immediately bound by the legacy system's real shape.

The bubble only stays useful if its relationship to the old system is
documented explicitly rather than left implicit. **Superimposed
structure** is the technique of explicitly relating the target structure
back to the existing legacy code; **highlighted structure** is making that
mapping visible so anyone reading either side can see the correspondence.
Without this, a bubble context risks becoming an aspirational document
disconnected from what's actually being migrated — a target architecture
diagram nobody can trace to the code it's meant to replace.

This is a documentation technique for [constraints and trade-offs
capture](documenting-trade-offs.md) applied specifically to systems that
are mid-transition: the target architecture is a real design decision
worth capturing with its own rationale, but it has to stay honestly linked
to the current, messier reality it's migrating away from. The [strangler
pattern](strangler-pattern-for-legacy-migration.md) is the incremental
execution technique a bubble context's target model is usually built
toward — the bubble documents the destination, the strangler pattern is
how a team actually gets there without a big-bang rewrite.

The legacy state a bubble context is designed against is often what Brian
Foote and Joseph Yoder named a **Big Ball of Mud**: a system with no
consistently enforced boundaries, where structure was never well-defined
or has eroded past the point of being trustworthy. Recognizing that a
system has reached this state — rather than continuing to document it as
if it had the clean boundaries its diagrams claim — is what makes starting
a bubble context the right move instead of attempting an in-place fix.
Decomposing a Big Ball of Mud usually means discovering [bounded
contexts](bounded-context.md) inside it that were never made explicit, and
protecting the new boundaries with the same [context
map](context-map.md) patterns (an Anticorruption Layer especially) used to
protect any bounded context from a poorly-designed upstream.
