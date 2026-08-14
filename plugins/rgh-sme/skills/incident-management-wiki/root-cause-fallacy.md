---
type: concept
title: The Root Cause Fallacy
description: The misconception that complex system failures can be traced back to a single, identifiable root cause.
sources:
  - title: "The Field Guide to Understanding 'Human Error'"
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 3"
---

Complex, well-defended engineering systems do not fail due to a single, isolated fault. Instead, accidents occur through a conjunction of multiple contributing factors that are **individually necessary and only jointly sufficient** to cause the failure. 

The **Root Cause Fallacy** is the belief that searching deep enough will reveal a single "root cause" (often labeled "human error"). In reality:
* A "root cause" is an arbitrary stopping point in an investigation, typically driven by budget, politics, or administrative convenience.
* Systems fail because of component interactions and latent flaws that are normally present but align catastrophically under specific circumstances.

Instead of seeking a singular cause, incident reviews should map the web of contributing factors, as detailed in different [accident models](accident-models.md). Post-incident methodologies like [learning reviews](learning-reviews.md) and [blameless postmortems](blameless-postmortems.md) must focus on identifying systemic vulnerabilities rather than stopping at a simplistic, comforting "root cause."
