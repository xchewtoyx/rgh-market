---
type: concept
title: The Design Stamina Hypothesis
description: >
  Investing in internal design increases a codebase's "stamina," letting a
  team go faster for longer, versus the alternative where feature velocity
  decays as the codebase becomes archaeology.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 2"
---

Named argument for why refactoring pays for itself: investing in internal
design increases the "stamina" of a development effort, letting a team ship
features faster for longer, versus the alternative where feature velocity
decays over a project's life as the codebase becomes hard-to-navigate
archaeology. This is the mechanism behind three more specific benefits
refactoring is claimed to produce:

- **Improves design.** Without ongoing refactoring, architecture decays as
  people patch for short-term goals — and the harder the design is to see,
  the faster it decays further, a compounding effect. Poor design usually
  shows up as more code than necessary, largely from
  [duplication](code-duplication-red-flag.md); eliminating duplication is
  central to good design — "the code says everything once and only once."
- **Makes software easier to understand.** The most important reader of code
  is not the compiler but the future human — often the author themselves —
  who must change it later.
- **Helps find bugs.** Understanding code deeply enough to refactor it
  surfaces the assumptions baked into it, which surfaces bugs even for
  someone who isn't naturally good at spotting them by inspection alone.

Refactoring is what lets [design be built and improved
incrementally](continuous-design.md) over a system's life rather than
needing to be entirely right up front — a shift from the older view that
design must precede coding and can only decay afterward. Stated principle:
**"The whole purpose of refactoring is to make us program faster, producing
more value with less effort."** The main real barrier to this in practice is
the perceived slowdown of adding a refactoring step before a feature — even
though refactoring's entire purpose is to increase speed over the run of the
project, not the single next commit. The only legitimate justification for
refactoring is this economic one — it makes the team faster — not a moral or
aesthetic appeal to "clean code" for its own sake.
