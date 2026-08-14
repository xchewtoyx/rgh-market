---
type: concept
title: User Problem Domain Complexity
description: >
  Scope an LLM application by four independent axes — medium, abstraction
  level, context required, and statefulness — before designing the harness.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 4"
---

Before designing an [LLM application loop](llm-application-loop.md), size up
the user's problem domain along four dimensions. Proofreading, IT-support
assistance, and travel planning sit at increasing complexity across all four:

1. **Medium** — text (the most natural fit for LLMs) versus voice versus
   complex website/API interactions the application must mediate.
2. **Level of abstraction** — a concrete, well-defined, small problem versus a
   large abstract problem-and-solution space constrained by documentation
   versus needing to understand subjective tastes and objective constraints to
   coordinate a genuinely complex solution.
3. **Context required** — nothing beyond the user's own text, versus
   searchable technical docs and example transcripts, versus calendars,
   external APIs, news, official recommendations, and general reference
   material.
4. **Statefulness** — none, where every request is a self-contained problem
   statement, versus tracking conversation history and attempted solutions
   within a session, versus tracking interaction across weeks, multiple
   mediums, and abandoned solution branches.

These axes are independent — a problem can be simple on one and complex on
another — and together they indicate how much architecture the application
actually needs: low scores across the board can stay a
[single-iteration loop](llm-application-loop.md), while high scores on context
and statefulness push toward full
[memory management](memory-management.md) and, past a point, toward
[generality-strength tradeoff](generality-strength-tradeoff.md) decisions
about narrowing scope or building a workflow.
