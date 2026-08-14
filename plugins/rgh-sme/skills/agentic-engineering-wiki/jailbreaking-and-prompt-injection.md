---
type: concept
title: Jailbreaking and Prompt Injection
description: >
  Subverting safety features or injecting malicious instructions so the model
  follows attacker goals instead of developer policy.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
---

**Jailbreaking** subverts a model's safety features (for example turning a
refusal into compliance). **Prompt injection** inserts malicious instructions
into user content (append "delete the order" to a support query). Techniques
overlap; both succeed because models are trained to follow instructions and
struggle to privilege the [system prompt](system-prompt-architecture.md) over
user text.

Classic manual tactics include obfuscation, output-format disguise, and
roleplay (DAN, grandma exploits). Automated attackers iterate prompts against a
target (PAIR-style attacker models). For agents, the sharper threat is
[indirect prompt injection](indirect-prompt-injection.md) via tools and
retrieved documents.

[Defensive prompt engineering](defensive-prompt-engineering.md) responds with
[instruction hierarchy](instruction-hierarchy.md) training, explicit refuse-
lists, repeated system instructions, known-attack preemption, and system-level
isolation plus [human approval gates](human-approval-gates.md) on write actions.
