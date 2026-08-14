---
type: concept
title: Listening to the Documentation
description: >
  Difficulty explaining a system's shape, language, or rationale is
  itself design feedback — it exposes a decision that was never actually
  made deliberately, not just a documentation gap.
sources:
  - title: Living Documentation
    resource: "Living Documentation: Continuous Knowledge Sharing by Design (Cyrille Martraire), ch. 11"
---

When explaining a system's vocabulary, its shape, its behavior, or the
reasoning behind a decision turns out to be difficult, that difficulty is
itself useful information about the design — not just a gap in the
documentation. Struggling to write down *why* something is the way it is
often exposes "programming by coincidence": a decision that accreted
rather than one anyone actually, deliberately made. Documentation, read
this way, functions like a code review — it asks whether a decision can be
stated at all, and whether the rationale behind it, once stated, actually
deserves confidence.

This motivates **documentation-driven development**: writing the
explanation of an intended result before or during building it, using the
act of explaining to keep the design honest, rather than writing the
explanation only after the fact to describe whatever got built. The output
of doing this doesn't need to be permanent — see [deprecating design
documentation](deprecating-design-documentation.md) — the value is in the
exercise of explaining, not necessarily in the artifact it produces. This
is a design-validation technique closely related to [requirement
rationale](requirement-rationale.md) and [architectural decision
capture](architectural-decision-capture.md): both ask you to state the
"why," and both are liable to expose that no real "why" exists yet if the
underlying decision was never actually made.
