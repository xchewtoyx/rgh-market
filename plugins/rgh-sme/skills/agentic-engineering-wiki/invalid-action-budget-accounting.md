---
type: concept
title: Invalid Action Budget Accounting
description: >
  Count malformed or unknown commands against the episode action budget even
  when they are ignored, so format failure cannot be free.
sources:
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT (Nakano et al.), §2"
---

When an agent emits text that is not a valid command, WebGPT **ignores** the
action for environment effect but still charges it against the maximum action
budget. Combined with
[action format enforcement](action-format-enforcement.md) (error templates and
early exit on streaks), this prevents infinite free retries that never move
state.

Use the same rule in any discrete-action ACI
([browser tool action inventory](browser-tool-action-inventory.md),
shell/tool enums): invalid turns are expensive observations, not no-ops. Report
invalid-action rate next to
[agent episode termination modes](agent-episode-termination-modes.md) — rising
invalid spend is a harness health signal before resolve rate collapses.
