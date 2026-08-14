---
type: concept
title: User Behavior Adaptation as a Metric Drift Cause
description: Users learn to adapt their inputs to get better results from a system over time, causing a gradual, real metric drift that has no corresponding internal cause — a debugging trap because the instinct is to look for what changed in the system rather than in how people are using it.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 10"
---

As users interact with a system repeatedly, they adapt their behavior to get better results from it — the same dynamic as Google Search SEO, or documented cases of people learning to "bully" self-driving cars into yielding right of way (Liu et al. 2020). In an LLM application, users may learn over time to phrase requests more concisely to get faster or better responses, producing a gradual downward drift in average input/output length that isn't explained by anything in the system itself.

This is a distinct trap from [silent model version drift](silent-model-version-drift.md): both produce an unexplained metric shift with nothing to find via [change correlation](change-correlation-in-debugging.md), but the model-drift case has an external technical cause to eventually locate, while user-behavior drift has no "bug" at all — the system is behaving exactly as before, and the population of inputs it receives has simply changed. Root-causing this kind of drift means correlating the metric shift against usage-pattern changes (e.g. average input tokens, phrasing patterns) rather than searching for a code or infrastructure change that was never made.
