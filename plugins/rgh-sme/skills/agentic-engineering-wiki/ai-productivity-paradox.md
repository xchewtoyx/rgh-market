---
type: concept
title: AI Productivity Paradox
description: >
  Responsible AI use costs verification time, but perceived productivity rewards
  skipping scrutiny — design harness gates that keep review mandatory.
sources:
  - title: Taking Testing Seriously
    resource: "Taking Testing Seriously (Bach & Bolton), ch. 7"
---

Bach & Bolton’s productivity paradox: responsible AI use takes considerable
time and effort to verify, yet “productive” AI must save time — so organizations
are rewarded for using AI **irresponsibly**. Management pressure to believe the
tool works shrinks tolerance for nuanced, hard-to-reproduce failure reports.
Refuting fluent wrong output is often an order of magnitude harder than
producing it.

For agent harness design: do not optimize only for fewer human minutes per
task. Budget mandatory review paths
([human approval gates](human-approval-gates.md),
[genai use safety modes](genai-use-safety-modes.md)) and automated
[offline prompt evaluation](offline-prompt-evaluation.md) so “faster” cannot
silently delete oracles. Prefer
[me-first prompt collaboration](me-first-prompt-collaboration.md) when humans
steer agents, to resist anchoring on the first fluent draft.
