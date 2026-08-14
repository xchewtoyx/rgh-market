---
type: concept
title: Harness Drift Awareness
description: >
  Prompt templates, user behaviour, and silent provider model swaps all change
  agent behaviour without code diffs — version and detect them as first-class
  maintenance risks.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 10"
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 16–30"
---

Agent systems drift even when application code is unchanged:

- **System prompt / template changes** — intentional updates or silent typos;
  catch with diffs in the [prompt catalog](prompt-catalog.md).
- **User behaviour adaptation** — users learn phrasing that changes length and
  tool use over time.
- **Underlying model swaps** — same API name, different weights; quality can
  move without a deploy.

Maintenance practice: version prompts and harness config with the
[prompt catalog](prompt-catalog.md), pin models when possible, and treat
provider updates as deliberate upgrades. For computer-use agents, also version
the [configurable ACI harness](configurable-aci-harness.md) YAML (templates,
command files, parsers, history processors) — those are interface changes that
shift behaviour as much as model swaps. Runtime detection and metric design for
drift belong to observability; the design obligation here is to make prompts,
models, and tool inventories identifiable artifacts you can bisect when
behaviour shifts. Score those shifts at
[episode scale, not request-APM latency](episode-scale-evaluation-vs-request-apm.md).
