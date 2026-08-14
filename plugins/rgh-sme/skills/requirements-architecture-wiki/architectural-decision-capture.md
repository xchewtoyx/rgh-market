---
type: concept
title: Architectural Decision Capture
description: >
  Capturing an architectural decision as a durable record — issue,
  decision, status, rationale, alternatives, and consequences — is what
  lets a design be understood and revisited without reconstructing
  context from scratch.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), ch. 6"
  - title: Living Documentation
    resource: "Living Documentation: Continuous Knowledge Sharing by Design (Cyrille Martraire), ch. 4, ch. 12"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 20"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 3"
---

An architectural decision record captures a single [architecturally
significant decision](architecturally-significant-decision.md) as a
structured artifact rather than as a fact only visible in the current
state of the code. The recurring structure across sources is: the
**issue** or **context** (what problem or question forced a decision),
the **decision** actually made, its **status** (proposed, accepted,
superseded), the **assumptions** it depends on, the **rationale** (why
this option, in this context), the **alternatives** considered and why
they were rejected, the **consequences** (what this decision now commits
the system to), and which architecture views are affected by it.

One compact **why-statement** template (from Zdun, popularized via
Nygard's ADR form) captures context, choice, rejected options, benefit,
and accepted downside in a single paragraph: "In the context of
[feature/component], wanting to/facing the need for [requirement/quality
goal], we decided to [option chosen] and neglected [alternatives] to
achieve [benefit], accepting that [negative consequences]." Use it as the
narrative spine of a fuller record; the structured fields above still
matter when alternatives or consequences need to be inspected item by
item.

The point of recording alternatives and rationale, not just the decision,
is that the rationale is usually the knowledge that goes missing first —
the decision itself is visible in the code, but the reasoning behind it,
the options that were rejected, and the assumptions it depended on are
not. Established patterns or well-known practices can serve as
pre-documented rationale (citing a known pattern substitutes for
re-explaining the reasoning from scratch), but record real rationale
deliberately rather than speculation.

A decision record only stays useful if it is genuinely maintained as a
log, not a one-off document: keep it change-friendly and structured
enough to add new entries over time, since architecture is fractal — large
systems contain systems, and decisions accumulate at every level. Target's
`recommend_tech` is a concrete example: a version-controlled repository
listing technology choices by domain, each tagged with a status
(recommended / limited-use / do-not-use), its rationale, and a "half-life"
after which it should be reconsidered, with changes proposed and discussed
via pull request so the full decision history stays in the repository
itself rather than in a separate, easily-stale wiki. See also [code as
architecture documentation](code-as-architecture-documentation.md) for
keeping decision records next to the code they govern, and [documenting
trade-offs](documenting-trade-offs.md) for how to lay out the alternatives
themselves before a decision is made.

Which decisions are worth this overhead is governed by [architecturally
significant decision](architecturally-significant-decision.md); when in
the project's life they tend to get made, and why that makes rationale
capture more urgent rather than less, is covered in [timing of
architectural decisions](timing-of-architectural-decisions.md).
