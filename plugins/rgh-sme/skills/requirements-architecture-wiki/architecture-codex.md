---
type: concept
title: Architecture Codex
description: >
  An architecture codex records how architectural decisions get made —
  the process, not just the decisions themselves — and pairs with
  mechanisms that check whether the code still matches stated intent.
sources:
  - title: Living Documentation
    resource: "Living Documentation: Continuous Knowledge Sharing by Design (Cyrille Martraire), ch. 12"
---

Most architecture documentation records *what* was decided and *why* (see
[architectural decision capture](architectural-decision-capture.md)). An
architecture codex records something one level up: *how* decisions get
made in a given organization or system — the process and governance of
decision-making itself, not any individual decision's content. **Transparent
architecture** is the companion idea: relevant architectural information
should be accessible to whoever needs it, rather than living in the heads
of whoever made the original decision.

The practical payoff of writing this down explicitly is an **architectural
reality check**: architectural annotations that connect stated intent to
actual code make it possible to verify, mechanically or by inspection,
whether the code still matches what the architecture claims about it. This
is what turns architecture documentation from a static description into
something that can be checked against reality on an ongoing basis, rather
than trusted purely on faith that nobody has quietly drifted from it. A
lighter-weight, conversational counterpart that costs nothing but talking
is [telling the story of the
system](telling-the-story-of-the-system.md): checking whether the team can
still narrate the architecture consistently with what the code actually
does.

Good architecture documentation should open with the problem, the stakes, and
the [quality attributes](non-functional-requirement.md) and assumptions
in play — not lead with a solution diagram that has no stated reason to
exist.
