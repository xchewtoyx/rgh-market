---
type: concept
title: Provider Selection Guidance
description: >
  Narrow model choice by picking a provider first, then capability tier, then
  model size within that provider's lineup — hosted API or self-hosted.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 7"
---

Once [model selection criteria](model-selection-tradeoffs.md) narrow what's
needed, the usual sequence is: pick a provider based on requirements,
features, and a scrappy-versus-premium preference; narrow further by
capability; then choose model size within that provider's lineup. Providers
differ in emphasis — some lean toward alignment and safety research, some
toward highly efficient open-weight models suited to specialized
configurations, some toward strong retrieval-augmented-generation
performance, some toward ecosystem integration and large-scale
infrastructure, some toward large, highly capable open-access models — and
the field shifts fast enough that any specific ranking goes stale quickly.
Model-comparison sites are a reasonable starting point for prototyping and
narrowing the field without committing early.

**Open-source options** avoid depending on a hosted LLM-as-a-service provider
entirely, at the cost of real hosting effort — platforms that manage
inference infrastructure for you ease this, but self-hosting is only worth it
once an application is large enough to justify the infrastructure investment.
An agile middle path: prototype on an easily accessible hosted API, and only
move to a different platform (self-hosted or otherwise) before going to
production if the economics or requirements demand it by then.

Within a chosen provider, model-size choice trades completion quality against
cost and possibly latency; the default heuristic is to pick the smallest
model that reliably delivers on the task. One counterintuitive tip:
prototype with a slightly larger, pricier model than you think you can
afford. Flagship releases tend to push older models' prices down over time,
so by the time an application reaches public beta a better model may well be
affordable — and having prompt engineering and postprocessing already tuned
against that stronger model pays off immediately once it becomes affordable,
rather than needing a re-tuning pass later.
