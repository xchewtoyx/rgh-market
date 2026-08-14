---
type: concept
title: Defensive Prompt Engineering
description: >
  Design system prompts and input handling so untrusted user content cannot
  override developer instructions or exfiltrate privileged context.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
---

Once an application is live it faces intended users and attackers. Three attack
families matter for harness design:

1. [Prompt extraction](prompt-extraction.md) — stealing system prompts or
   privileged context.
2. [Jailbreaking and prompt injection](jailbreaking-and-prompt-injection.md) —
   getting the model to violate policy or follow attacker instructions.
3. Information extraction — eliciting training data or sensitive context.

Impact includes remote tool/code execution, data leaks, social harm,
misinformation, service subversion, and brand damage. Risk grows with
capability: better instruction-following also means better malicious-instruction
following, and models struggle to distinguish privileged
[system prompts](system-prompt-architecture.md) from user text once concatenated.

Defense is layered — model ([instruction hierarchy](instruction-hierarchy.md)),
prompt, and system (isolation, [human approval gates](human-approval-gates.md),
input/output guardrails). ChatML-style reserved delimiters help only if
untrusted content stays out of the system role
([system prompt architecture](system-prompt-architecture.md)). Prompt-hack risk
cannot be fully eliminated while the system retains impactful capabilities;
measure both attack success and false refusals when tightening defenses.
