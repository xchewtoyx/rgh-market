---
type: concept
title: System Prompt Architecture
description: >
  Split developer instructions into a privileged system prompt and user content
  into a user prompt, then render them through the model's chat template.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
---

Many APIs split input into a **system prompt** (developer task description,
persona, policies) and a **user prompt** (the concrete task and user content).
Under the hood they are concatenated, but models are often post-trained to
prioritize the system prompt (instruction hierarchy), and leading placement
itself can help. Roles assigned in the system prompt also help maintain
character across turns.

The combined strings must follow the model's **chat template** — special tokens
and headers defined by the model developer. That is distinct from an
application's prompt template that hydrates variables with data. Using the wrong
chat template causes silent quality loss: outputs still look plausible. Always
print the final rendered prompt and verify third-party construction tools.

System-prompt privilege is also the foundation for
[defensive prompt engineering](defensive-prompt-engineering.md) against user
attempts to override developer instructions. Chat templates such as ChatML
use reserved role delimiters users cannot emit through the API, which
structurally confines callers to the user role — but **never inject user or
retrieved content into the system message**, or you defeat that boundary and
invite injection. Put “rules of the road” and persona in system; keep untrusted
text in user (or tool) turns. The harness that assembles those turns is the
[prompt engineer as playwright](prompt-engineer-as-playwright.md).
