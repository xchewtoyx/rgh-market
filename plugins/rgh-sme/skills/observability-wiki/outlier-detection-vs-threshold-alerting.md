---
type: concept
title: Outlier Detection vs. Threshold Alerting
description: Instead of alerting a human against a fixed, hand-defined threshold, outlier detection computes what "normal" looks like across a population of similar nodes/instances right now and flags whichever ones don't fit — useful when a "correct" value can't be specified in advance.
sources:
  - title: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 15"
---

Given a large population of nodes that should behave identically — a thousand-node stateless compute cluster all running the same software — the operational question is often not "does this metric exceed X" but "which of these nodes looks different from the rest of the herd." Outlier detection answers this by computing the population's "current normal" continuously and flagging members that deviate from it, without requiring a human to define a proper-behavior spec up front.

This differs from conventional threshold alerting in an important way: it needs no static threshold at all, and it adapts automatically as the population's baseline shifts over time (traffic growth, a new build rolling out). It's particularly well suited to remediation that doesn't require paging a human — e.g. automatically killing and replacing a node that doesn't fit the population's current normal, then logging/notifying, rather than waking someone up. This connects to [establishing a baseline for normal system behavior](baseline-normal-system-behavior.md) as the general debugging technique this is an automated, continuous version of.
