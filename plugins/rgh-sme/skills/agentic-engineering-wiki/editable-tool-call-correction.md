---
type: concept
title: Editable Tool-Call Correction
description: >
  Let users edit a shown tool call's arguments and resubmit, regenerating the
  conversation forward from that corrected point.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 8"
---

Once a [tool call is visible](tool-call-transparency-ui.md) in the UI, let
users modify its arguments directly in the revealed webform and resubmit the
corrected call. On resubmission, regenerate the conversation forward from that
point rather than just patching the one call in place — this gives the user a
concrete way to steer the agent back on track when it has misread the
situation, instead of only being able to argue with it in natural language.

This is a user-facing complement to
[plan-validate-execute](plan-validate-execute.md): where plan-validate-execute
uses a validator (heuristic or AI judge) to catch bad tool calls before
execution, editable correction gives the human the same intervention point
after the model has already proposed a call.
