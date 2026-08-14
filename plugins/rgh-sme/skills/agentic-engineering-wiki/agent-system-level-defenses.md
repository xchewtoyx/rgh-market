---
type: concept
title: Agent System-Level Defenses
description: >
  Isolation, approval gates, scope filters, and input/output guardrails that
  contain damage when prompt defenses fail on a tool-using agent.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 106–118 (Appendix E)"
---

When an [LLM agent](llm-agent.md) can execute code or call write tools, prompt
defenses alone are insufficient. System-level controls include:

- **Isolation** — run generated code in a separate VM/sandbox, not the host.
  Prefer **ephemeral containers** for inference and evaluation so accidental
  destructive commands (`rm -rf …`) stay off the host. Namespace isolation is
  weaker than full hardware virtualization; treat it as sufficient for ordinary
  agent mistakes, not for deliberately container-escape-engineered malware.
- **[Human approval gates](human-approval-gates.md)** before impactful SQL or
  irreversible actions.
- **Out-of-scope topic filters** — phrase blocklists or intent models over the
  whole conversation, routing unsafe topics to humans.
- **Input and output guardrails** — known-attack patterns, suspicious-request
  detectors, and checks for PII or toxicity in outputs (harmless inputs can
  still yield harmful outputs).
- **Usage-pattern detection** — many similar probes in a short window signal
  bypass hunting, not one-off mistakes.
- **Trusted evaluation channels** — unofficial third-party harnesses or datasets
  can inject malicious issue text (e.g. “build a keylogger”); pin official
  repos/data stores and prefer upstream contributions over opaque forks.
- **Capability-scaled burden of proof** — how much scrutiny a new autonomous
  capability (e.g. live web access, write tools) needs before granting it
  should rise with the underlying model's capability, not stay fixed at
  whatever bar the first, weakest version cleared. A tool graph that was
  provably low-risk for a limited model (can only search and follow links, no
  edit forms) is not automatically still low-risk once the model gets more
  capable at finding indirect paths to the same effect. Pair with **tripwire
  tests** — deliberately plant an easy, low-stakes opportunity to exploit a
  gap (an editable-looking form, an unattended credential) inside the
  eval/staging environment and check whether the agent takes it — as an early
  warning for emerging exploitative behavior before it shows up against real
  targets.

These are harness blast-radius limits for model-generated actions, complementing
[defensive prompt engineering](defensive-prompt-engineering.md) and
[indirect prompt injection](indirect-prompt-injection.md) mitigations. Open
agent codebases also make it easier for others to study and impose sound
capability constraints — design the sandbox and approval surface so those
constraints are enforceable, not only documented.
