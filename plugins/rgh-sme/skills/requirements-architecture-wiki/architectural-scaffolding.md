---
type: concept
title: Architectural Scaffolding
description: >
  Temporary, throwaway-or-reusable structure built specifically to bridge
  toward a future architectural state, judged solely by whether it lets
  the system keep shipping in the meantime.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 20"
---

Scaffolding is software built not to satisfy a requirement directly, but
to bridge the gap between the current architecture and a future one
without stopping delivery in between — a mocked API standing in for a
third-party integration that isn't ready yet, or seeded test data letting
partners test independently before the real data pipeline exists. It may
be thrown away once the target state is reached, or it may turn out
useful enough to keep; which of those happens is not decided up front.

The only criterion scaffolding has to meet is "does no harm": it exists
purely to keep a [large architectural change](large-scale-architecture-refactor-cases.md)
incremental rather than forcing a system-wide pause, so its own quality
bar is "good enough to not block or corrupt the rest of the system while
in place," not the same durability bar as a permanent piece of
architecture. Treating scaffolding as if it needed to meet the same
standard as the thing it bridges to is a common overinvestment mistake —
the entire point is that it's disposable infrastructure paying for a
lower-risk path to Case A of the refactor cases, not a deliverable in its
own right.
