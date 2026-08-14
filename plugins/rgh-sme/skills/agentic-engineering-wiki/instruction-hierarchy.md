---
type: concept
title: Instruction Hierarchy
description: >
  Train and design so conflicting instructions resolve toward higher-privilege
  layers — system over user over model output over tool output.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
---

Many attacks succeed because system and user text are concatenated into one blob
the model cannot prioritize. An instruction hierarchy (Wallace et al., 2024)
orders privilege roughly as: (1) system prompt, (2) user prompt, (3) model
outputs, (4) tool outputs — conflicts resolve upward.

Putting tool outputs lowest specifically blunts
[indirect prompt injection](indirect-prompt-injection.md). Hierarchy is a
model-level defense that [system prompt architecture](system-prompt-architecture.md)
relies on; prompt- and system-level controls remain necessary because no model
perfectly obeys the ranking. Calibrate safety finetuning for borderline requests
too — refuse everything achieves zero violations and a useless product.
