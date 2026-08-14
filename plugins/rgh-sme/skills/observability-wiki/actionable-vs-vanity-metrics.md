---
type: concept
title: Actionable Metrics vs. Vanity Metrics
description: A metric belongs on a dashboard or behind an alert only if someone would change behavior based on it moving; metrics that are merely interesting to look at should be stored, not displayed or alerted on.
sources:
  - title: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 14"
---

Metrics should be **actionable**: a metric worth displaying prominently or alerting on is one where a specific change in its value would cause someone to do something differently. A metric that's merely interesting — often called a **vanity metric** — should still be stored (it may become useful later, or feed an aggregate that is actionable), but shouldn't clutter a dashboard or trigger a notification, because doing so just adds noise that trains viewers to skim past the dashboard rather than act on it.

Note that whether a given metric is actionable can be domain-dependent, not universal — e.g. time-on-site is a good thing to maximize for an e-commerce site (more browsing tends to mean more sales) but a *bad* thing to maximize for a search engine (a long session may mean the user is struggling to find results). A metric that's a clear positive signal in one product context can be a negative signal in another, so "actionable" has to be evaluated against what the metric implies for *this* product, not assumed to generalize.

This is a dashboard-design principle distinct from [self-service telemetry access](self-service-telemetry-access.md) (which is about who can reach telemetry) — this is about which telemetry deserves prominent, always-visible placement once people can reach it.
