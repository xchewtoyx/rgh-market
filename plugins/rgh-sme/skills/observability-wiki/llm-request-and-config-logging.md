---
type: concept
title: LLM Request and Configuration Logging
description: For an LLM or agent application, log the full request configuration, the assembled prompt, all intermediate and tool-call outputs, and component lifecycle events, because a probabilistic system makes it impossible to predict in advance which of these will explain the next failure.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 10"
---

The general [structured logging](structured-logging.md) rule — log everything, since you don't know in advance what you'll need — applies with extra force to LLM/agent applications: because model behavior is probabilistic rather than deterministic, the same code path can fail on one run and succeed on the next, so the log has to carry enough context to reconstruct *why this particular run* went the way it did, not just that it failed.

For each request, capture:

- **Full configuration**: model API endpoint, model name/version, sampling settings (temperature, top-p, top-k, stopping condition), and the prompt template used.
- **The user query** and the **final assembled prompt** actually sent to the model — these can diverge significantly once retrieval and templating are involved, and only the final prompt explains what the model actually saw.
- **Output and intermediate outputs** — not just the final response, for multi-step (chain-of-thought, agentic) flows.
- **Tool calls and their outputs** — the call the model generated and what the invoked tool actually returned.
- **Component lifecycle events** (start, end, crash) for each step in the pipeline.

Tag or ID every log entry so its origin in the system is traceable — the same request/trace-ID discipline as [context propagation](context-propagation.md). This log volume grows fast enough that many log-analysis and anomaly-detection tools operating on it are themselves AI-powered; see [the wide event attribute checklist](wide-event-attribute-checklist.md) for the equivalent capture discipline in non-LLM services, and [LLM token and cost metrics](llm-token-and-cost-metrics.md) for the aggregate telemetry this logging feeds.
