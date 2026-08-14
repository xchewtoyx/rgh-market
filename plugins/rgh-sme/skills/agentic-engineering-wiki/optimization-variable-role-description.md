---
type: concept
title: Optimization Variable Role Description
description: >
  A short role string on each optimizable variable steers what textual-gradient
  descent is allowed to rewrite — answer-only vs reasoning-plus-answer, and more.
sources:
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), Appendix A.1"
---

In TextGrad, each graph **variable** carries a **role description** — free-form
text naming what the variable is for (e.g. “system prompt reused across
queries”, “final numerical answer”, “reasoning + final prediction”). Empirically
this is a primary steering channel: the same
[textual gradient descent](textual-gradient-descent.md) step updates a
number-only variable to a number, but keeps chain-of-thought text when the role
says reasoning is in scope.

Treat role strings as harness config next to
[system prompt architecture](system-prompt-architecture.md) and
[instance vs prompt optimization](instance-vs-prompt-optimization.md). Wrong
roles silently change the optimization surface (stripping useful reasoning, or
letting the optimizer rewrite frozen fields). Combine with `requires_grad`-style
flags so predecessors that must not change never receive
[textual gradients](textual-gradients.md).
