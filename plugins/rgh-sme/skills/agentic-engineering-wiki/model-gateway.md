---
type: concept
title: Model Gateway
description: >
  A unified interface to self-hosted and commercial models that centralizes
  access control, fallbacks, logging hooks, and API-change maintenance.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 10"
---

A model gateway sits between applications and model providers. Benefits for
harness design:

- One place to update when a provider API changes.
- Central token distribution and per-user/per-app access rules (avoid handing
  org keys to every caller).
- Fallback policies on rate limits or failures — alternate models, retry, or
  degrade.
- Natural chokepoint for load balancing, logging hooks, caching, and sometimes
  [input and output guardrails](input-output-guardrails.md).

In [progressive agent architecture](progressive-agent-architecture.md) the
gateway replaces a bare Model API box. A similar "tool gateway" is conceivable
but uncommon. Keep orchestration concerns in
[AI pipeline orchestration](ai-pipeline-orchestration.md); the gateway's job is
uniform model access, not the full agent loop.
