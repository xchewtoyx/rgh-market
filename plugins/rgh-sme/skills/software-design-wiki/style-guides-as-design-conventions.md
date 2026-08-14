---
type: concept
title: Style Guides as Design Conventions
description: >
  Organization-wide style guides encode design-relevant conventions — not just
  formatting — so engineers focus on what code says rather than how it is
  written, at the cost of restricted local choice.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 10"
---

Google maintains per-language **style guides** defining mandatory **rules**
(universally enforceable laws) and optional **guidance** (recommendations with
variance — "musts" versus "shoulds"). Despite the name, guides cover far more
than formatting — they are the full set of conventions governing code.

The key question when adding a rule is not "what goes in?" but **"what goal
are we trying to advance?"** At scale (tens of thousands of engineers, billions
of lines, decades-long lifetimes), rules manage complexity so the codebase stays
maintainable while engineers stay productive — accepting restricted choice for
[consistency](consistency-as-a-design-tool.md) and reduced conflict.

Five guiding principles:

1. **Rules must pull their weight** — every rule has nonzero cost (learning,
   remembering, onboarding, maintenance). Omit self-evident behavior; absence of
   a rule does not imply permission.
2. **Optimize for the reader**, not the author — code is read far more than
   written. Require explicit evidence of intended behavior (e.g. `override`
   keyword even when inferable). Comment rules serve the same "in-place
   evidence" goal. Example: prefer `std::unique_ptr` over raw pointers so
   ownership transfer is visible at every call site, enabling **local
   reasoning** without chasing callees.
3. **Be consistent** — enables expert chunking (recognize familiar patterns
   quickly), tooling scale (one auto-import fixer everywhere), people scale
   (engineers ramp faster across projects), and resilience to time. Hierarchy:
   local file > team > project > overall codebase. Perfect consistency may be
   abandoned at extreme scale when retrofit cost exceeds value. For small
   efforts internal consistency dominates; for code that scales or interacts
   externally, matching community standards pays off long-term.
4. **Avoid error-prone and surprising constructs** — complex language features
   have non-obvious pitfalls; rules exist so all engineers (including SREs
   debugging outages in unfamiliar languages) can operate in the codebase, not
   just experts.
5. **Concede to practicalities** — exceptions for performance and
   interoperability (e.g. generated code exempt from rules).

Three rule categories: **avoiding danger** (language features with technical
pros/cons documented), **enforcing best practices** (comments, naming,
structure, limiting new features until usage patterns are understood), and
**building consistency** (picking one answer among equivalent options — the
value is having chosen, not which choice).

Deliberately **not codified**: fundamental engineering advice ("don't be clever,"
"don't reinvent the wheel") — guides aren't meant to take novices to mastery.

See [ensuring consistency across a team](ensuring-consistency.md) and
[style guide rule process and enforcement](style-guide-rule-process-and-enforcement.md).
