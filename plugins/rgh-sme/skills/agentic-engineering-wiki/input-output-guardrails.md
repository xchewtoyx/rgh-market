---
type: concept
title: Input Output Guardrails
description: >
  Harness checks on prompts and generations that block leaks, attacks, and bad
  outputs — with explicit policies per failure mode and false-refusal awareness.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 10"
---

Guardrails sit wherever risk appears. **Input guardrails** address leaking
private data to external APIs and executing malicious prompts
([defensive prompt engineering](defensive-prompt-engineering.md)). Mitigations
include sensitive-data detectors and mask/unmask PII reverse-maps before and
after the model call.

**Output guardrails** catch failures and attach a policy per mode: empty
responses, malformed JSON, hallucinations, toxicity, leaked secrets, tool
execution triggers, brand-risk text. Retries (sequential or parallel) and
human handoff after N turns or anger/phrase triggers are common policies.
Track false refusal rate with security blocks — over-refusal is also failure.

Tradeoffs: latency cost, streaming (unsafe tokens may reach users before a
check), and provider versus app-owned layers. Scorers are often smaller/faster
models. Pair with [agent system-level defenses](agent-system-level-defenses.md)
when tools can write.
