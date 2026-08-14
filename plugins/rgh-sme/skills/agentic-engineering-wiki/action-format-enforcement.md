---
type: concept
title: Action Format Enforcement
description: >
  Require one thought and one action per turn, repair or strip malformed
  replies, and stop the episode after repeated format failures.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 31–45"
---

Interactive agents that emit free-form shell or tool text need hard format
rules in the harness, not only in the prompt. SWE-agent expects one DISCUSSION
plus a single markdown code-block command per turn (JSON `thought`/`action` or
XML delimiters are alternatives — pick one style per episode). Malformed
output triggers an error template restating the exact shape; after a fixed
streak of consecutive failures (three in the paper), terminate early rather
than burning budget on unparseable turns.

Context hygiene: if a malformed turn is followed by a valid one, remove the
malformed action/response from history so noise does not linger. Each
well-formatted reply then becomes an in-context demonstration of correct
interaction — useful “momentum” when the transcript is already long under
[collapsed observations](collapsed-observations.md). This is
[tool definition design](tool-definition-design.md) meets
[agent control flow](agent-control-flow.md): the parser is part of the
interface, and format errors are first-class observations in the
[ReAct loop](react-loop.md).
